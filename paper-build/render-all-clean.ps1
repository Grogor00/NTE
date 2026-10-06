param([switch]$ReportOnly)

$ErrorActionPreference = "Stop"
$buildDir = $PSScriptRoot
$repoRoot = Split-Path $buildDir -Parent
$workingRoot = Join-Path $repoRoot "Working"
Set-Location $buildDir

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }
$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }

# Build-local only — must NOT live under the Drive-synced tree (stripped staging copies).
$scratchDir = Join-Path $env:TEMP "nte-build-scratch"
$outDir = Join-Path $buildDir "pdf-out"
$defaults = Join-Path $buildDir "pdf-defaults.yaml"
$masterDefaults = Join-Path $buildDir "pdf-defaults-master.yaml"
New-Item -ItemType Directory -Force $scratchDir | Out-Null
New-Item -ItemType Directory -Force $outDir | Out-Null

$preparePaper = Join-Path $workingRoot "prepare_paper_pdf.py"
$prepareMaster = Join-Path $workingRoot "prepare_master_pdf.py"
$stripScript = Join-Path $workingRoot "strip_publication_tail.py"
$stripCorpus = Join-Path $workingRoot "strip_corpus_metadata.py"

foreach ($req in @($preparePaper, $prepareMaster, $stripScript, $stripCorpus)) {
  if (-not (Test-Path $req)) {
    throw "Missing required strip/prepare script: $req"
  }
}

$folders = @("Core_Papers", "Popular_Editions", "Pedagogical_Notes")
$files = @()
foreach ($f in $folders) {
  $dir = Join-Path $repoRoot $f
  if (Test-Path $dir) {
    Get-ChildItem $dir -Filter "*.md" |
      Where-Object { $_.Name -notlike "_*" -and $_.Name -notlike "*copy_probe*" } |
      Sort-Object Name |
      ForEach-Object { $files += $_ }
  }
}

$rows = @()
foreach ($file in $files) {
  $name = $file.Name
  $out = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
  $row = [ordered]@{ md = $name; pdf = $out; exists = $false; status = "FAIL"; error = $null }

  if ($ReportOnly) {
    $row.exists = (Test-Path $out)
    $row.status = if ($row.exists) { "PASS" } else { "MISSING" }
    $rows += [pscustomobject]$row
    continue
  }

  try {
    $scratch = Join-Path $scratchDir $name
    Copy-Item $file.FullName $scratch -Force
    $t = Get-Content $scratch -Raw -Encoding UTF8
    $t = $t.Replace([string][char]0x2713, "PASS").Replace([string][char]0x2714, "PASS").Replace([string][char]0x2611, "PASS").Replace([string][char]0x2612, "FAIL").Replace([string][char]0x27F9, "=>")
    [System.IO.File]::WriteAllText($scratch, $t, [System.Text.UTF8Encoding]::new($false))

    $isMaster = ($name -like "NTE_v10_*_Part*.md")
    if ($isMaster) {
      & python $prepareMaster $scratch
      if ($LASTEXITCODE -ne 0) { throw "prepare_master_pdf.py exit $LASTEXITCODE" }
    } else {
      & python $preparePaper $scratch
      if ($LASTEXITCODE -ne 0) { throw "prepare_paper_pdf.py exit $LASTEXITCODE" }
    }

    # Belt-and-braces: masters already strip inside prepare; papers too.
    # Re-run strip_publication_tail for any residual editorial markers.
    & python $stripScript $scratch
    if ($LASTEXITCODE -ne 0) { throw "strip_publication_tail.py exit $LASTEXITCODE" }
    if ($isMaster) {
      & python $stripCorpus $scratch
      if ($LASTEXITCODE -ne 0) { throw "strip_corpus_metadata.py exit $LASTEXITCODE" }
    }

    # Silent-omission guard: strip must not delete bare prose "see" (ORPHAN_SEE class).
    $srcBody = [regex]::Replace($t, '(?s)^---.*?---\s*', '')
    $scrBody = [regex]::Replace((Get-Content $scratch -Raw -Encoding UTF8), '(?s)^---.*?---\s*', '')
    $srcSee = ([regex]::Matches($srcBody, '(?i)\bsee\b')).Count
    $scrSee = ([regex]::Matches($scrBody, '(?i)\bsee\b')).Count
    if ($srcSee -ge 2 -and $scrSee -lt [Math]::Max(1, [int]($srcSee * 0.5))) {
      throw "silent 'see' omission: source had $srcSee, stripped scratch has $scrSee"
    }
    foreach ($canary in @('cannot see', '(see below)')) {
      if ($srcBody -match [regex]::Escape($canary) -and $scrBody -notmatch [regex]::Escape($canary)) {
        throw "silent omission canary missing from scratch: $canary"
      }
    }

    $defaultsFile = $defaults
    if ($isMaster -and (Test-Path $masterDefaults)) { $defaultsFile = $masterDefaults }

    $logFile = Join-Path $scratchDir ("renderlog_" + [System.IO.Path]::GetFileNameWithoutExtension($name) + ".txt")
    $prevEap = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $pandocOut = (& $pandoc $scratch --defaults $defaultsFile -o $out 2>&1 | Out-String)
    $ErrorActionPreference = $prevEap
    [System.IO.File]::WriteAllText($logFile, $pandocOut, [System.Text.UTF8Encoding]::new($false))
    if ($LASTEXITCODE -ne 0) { throw "pandoc exit $LASTEXITCODE" }
    if (-not (Test-Path $out)) { throw "PDF not created" }
    $row.exists = $true
    $row.status = "PASS"
    Write-Host "PASS $name"
  } catch {
    $row.error = $_.Exception.Message
    Write-Warning "FAIL $name : $($row.error)"
  }
  $rows += [pscustomobject]$row
}

$produced = @($rows | Where-Object { $_.exists }).Count
Write-Host "Done: $produced/$($rows.Count) PDFs in $outDir"
$summary = [ordered]@{
  at = (Get-Date).ToString("o")
  out_dir = $outDir
  expected = $rows.Count
  produced = $produced
  all_pass = ($produced -eq $rows.Count)
  rows = $rows
}
($summary | ConvertTo-Json -Depth 5) | Set-Content (Join-Path $buildDir "render_all_clean_report.json") -Encoding UTF8
if (-not $summary.all_pass) { exit 1 }
