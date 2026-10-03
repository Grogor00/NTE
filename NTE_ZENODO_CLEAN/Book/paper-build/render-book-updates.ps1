param(
  [switch]$Watch,
  [int]$IntervalSec = 180,
  [string[]]$Only
)

$ErrorActionPreference = "Stop"
$bookRoot = Split-Path $PSScriptRoot -Parent
$buildDir = $PSScriptRoot
$scratchDir = Join-Path $buildDir "scratch-src"
$outDir = Join-Path $buildDir "pdf-out"
$statePath = Join-Path $buildDir "book_render_state.json"
$lockPath = Join-Path $buildDir "book_render.lock"
$defaults = Join-Path $buildDir "pdf-defaults.yaml"

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }
$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }

New-Item -ItemType Directory -Force $scratchDir, $outDir | Out-Null
Set-Location $buildDir

function Get-BookSources {
  param([string[]]$Names)
  $all = Get-ChildItem $bookRoot -Filter "*.md" -File | Sort-Object Name
  if ($Names -and $Names.Count -gt 0) {
    return $all | Where-Object { $Names -contains $_.Name }
  }
  return $all
}

function Load-State {
  if (Test-Path $statePath) {
    try { return Get-Content $statePath -Raw -Encoding UTF8 | ConvertFrom-Json -AsHashtable } catch { }
  }
  return @{}
}

function Save-State([hashtable]$State) {
  ($State | ConvertTo-Json -Depth 4) | Set-Content $statePath -Encoding UTF8
}

function Needs-Render($mdFile, [string]$pdfPath) {
  if (-not (Test-Path -LiteralPath $pdfPath)) { return $true, "new md" }
  $pdfFile = Get-Item -LiteralPath $pdfPath
  if ($mdFile.LastWriteTimeUtc -gt $pdfFile.LastWriteTimeUtc) { return $true, "updated md" }
  return $false, "current"
}

function Render-One($mdFile) {
  $name = $mdFile.Name
  $scratch = Join-Path $scratchDir ("render_" + $PID + "_" + $name)
  $out = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
  $log = Join-Path $buildDir ("renderlog_" + [System.IO.Path]::GetFileNameWithoutExtension($name) + ".txt")

  try {
    $t = [System.IO.File]::ReadAllText($mdFile.FullName, [System.Text.UTF8Encoding]::new($false))
    $t = $t.Replace([string][char]0x2713, "PASS").Replace([string][char]0x2714, "PASS")
    $t = $t.Replace([string][char]0x2611, "PASS").Replace([string][char]0x2612, "FAIL")
    $t = $t.Replace([string][char]0x27F9, "=>")
    [System.IO.File]::WriteAllText($scratch, $t, [System.Text.UTF8Encoding]::new($false))

    $prevEap = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $pandocOut = (& $pandoc $scratch --defaults $defaults -o $out 2>&1 | Out-String)
    $ErrorActionPreference = $prevEap
    [System.IO.File]::WriteAllText($log, $pandocOut, [System.Text.UTF8Encoding]::new($false))
    if ($LASTEXITCODE -ne 0) { throw "pandoc exit $LASTEXITCODE for $name" }
    if (-not (Test-Path $out)) { throw "PDF not created for $name" }
    return $out
  } finally {
    if (Test-Path -LiteralPath $scratch) {
      Remove-Item -LiteralPath $scratch -Force -ErrorAction SilentlyContinue
    }
  }
}

$script:RenderMutex = New-Object System.Threading.Mutex($false, "Global\NTE_Book_Render_$([System.IO.Path]::GetFileName($bookRoot))")

function Invoke-BookRenderPass {
  param([string[]]$Names)
  if (-not $script:RenderMutex.WaitOne(0)) {
    Write-Host "Book render pass skipped: another pass in progress."
    return [ordered]@{ at = (Get-Date).ToString("o"); rendered = 0; skipped = 0; failed = 0; note = "mutex busy" }
  }
  try {
  $state = Load-State
  $sources = Get-BookSources -Names $Names
  $rendered = @()
  $skipped = @()
  $failed = @()

  foreach ($md in $sources) {
    if (-not (Test-Path -LiteralPath $md.FullName)) {
      $skipped += [pscustomobject]@{ md = $md.Name; reason = "source missing" }
      continue
    }
    $pdf = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($md.Name) + ".pdf")
    $need, $reason = Needs-Render $md $pdf
    if (-not $need) {
      $skipped += [pscustomobject]@{ md = $md.Name; reason = $reason }
      continue
    }
    try {
      $out = Render-One $md
      $state[$md.Name] = $md.LastWriteTimeUtc.ToString("o")
      $kb = [math]::Round((Get-Item $out).Length / 1KB, 1)
      $rendered += [pscustomobject]@{ md = $md.Name; pdf = (Split-Path $out -Leaf); kb = $kb; reason = $reason }
      Write-Host "PASS $([math]::Round($kb,1))KB $($md.Name)"
    } catch {
      $failed += [pscustomobject]@{ md = $md.Name; error = $_.Exception.Message }
      Write-Warning "FAIL $($md.Name): $($_.Exception.Message)"
    }
  }

  Save-State $state
  $summary = [ordered]@{
    at = (Get-Date).ToString("o")
    rendered = $rendered.Count
    skipped = $skipped.Count
    failed = $failed.Count
    rendered_rows = $rendered
    skipped_rows = $skipped
    failed_rows = $failed
  }
  ($summary | ConvertTo-Json -Depth 5) | Set-Content (Join-Path $buildDir "book_render_latest.json") -Encoding UTF8
  return $summary
  } finally {
    $null = $script:RenderMutex.ReleaseMutex()
  }
}

if ($Watch) {
  Write-Host "Book render watch: interval ${IntervalSec}s, sources=$bookRoot (new or updated .md only)"
  while ($true) {
    $s = Invoke-BookRenderPass -Names $Only
    if ($s.rendered -gt 0) {
      Write-Host "AGENT_LOOP_TICK_BOOK_RENDER rendered=$($s.rendered) skipped=$($s.skipped) failed=$($s.failed)"
    }
    Start-Sleep -Seconds $IntervalSec
  }
} else {
  $s = Invoke-BookRenderPass -Names $Only
  Write-Host "Done: rendered=$($s.rendered) skipped=$($s.skipped) failed=$($s.failed)"
  if ($s.failed -gt 0) { exit 1 }
}
