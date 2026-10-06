$ErrorActionPreference = "Stop"
$buildDir = "C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\paper-build"
$repoRoot = "C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN"
$workingRoot = Join-Path $repoRoot "Working"
Set-Location $buildDir

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }
$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }

$scratchDir = Join-Path $env:TEMP "nte-build-scratch"
$outDir = Join-Path $buildDir "pdf-out"
$defaults = Join-Path $buildDir "pdf-defaults.yaml"
$masterDefaults = Join-Path $buildDir "pdf-defaults-master.yaml"
New-Item -ItemType Directory -Force $scratchDir | Out-Null

$files = @(
  "NTE_v10_19_0_Part3_Accounting.md",
  "Companion_10_M1_Majorana_v10_19_0.md",
  "Companion_13_Yukawa_Nu2_v10_19_0.md"
)

foreach ($name in $files) {
  $src = Join-Path $repoRoot "Core_Papers\$name"
  $scratch = Join-Path $scratchDir $name
  $out = Join-Path $outDir ([IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
  Copy-Item $src $scratch -Force
  $t = Get-Content $scratch -Raw -Encoding UTF8
  $t = $t.Replace([string][char]0x2713, "PASS").Replace([string][char]0x2714, "PASS").Replace([string][char]0x2611, "PASS").Replace([string][char]0x2612, "FAIL").Replace([string][char]0x27F9, "=>")
  [IO.File]::WriteAllText($scratch, $t, [Text.UTF8Encoding]::new($false))

  $isMaster = ($name -like "NTE_v10_*_Part*.md")
  if ($isMaster) {
    & python (Join-Path $workingRoot "prepare_master_pdf.py") $scratch
    if ($LASTEXITCODE -ne 0) { throw "prepare_master_pdf exit $LASTEXITCODE for $name" }
  } else {
    & python (Join-Path $workingRoot "prepare_paper_pdf.py") $scratch
    if ($LASTEXITCODE -ne 0) { throw "prepare_paper_pdf exit $LASTEXITCODE for $name" }
  }
  & python (Join-Path $workingRoot "strip_publication_tail.py") $scratch
  if ($LASTEXITCODE -ne 0) { throw "strip_publication_tail exit $LASTEXITCODE for $name" }
  if ($isMaster) {
    & python (Join-Path $workingRoot "strip_corpus_metadata.py") $scratch
    if ($LASTEXITCODE -ne 0) { throw "strip_corpus_metadata exit $LASTEXITCODE for $name" }
  }

  $defaultsFile = $defaults
  if ($isMaster -and (Test-Path $masterDefaults)) { $defaultsFile = $masterDefaults }

  $prevEap = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  $pandocOut = (& $pandoc $scratch --defaults $defaultsFile -o $out 2>&1 | Out-String)
  $ErrorActionPreference = $prevEap
  if ($LASTEXITCODE -ne 0) { Write-Host $pandocOut; throw "pandoc exit $LASTEXITCODE for $name" }
  if (-not (Test-Path $out)) { throw "PDF not created for $name" }

  $md = Get-Item $src
  $pdf = Get-Item $out
  if ($pdf.LastWriteTime -le $md.LastWriteTime) { throw "PDF not newer than md for $name" }
  Write-Host ("PASS " + $name + " pdf=" + $pdf.LastWriteTime.ToString("o") + " size=" + $pdf.Length)
}
Write-Host "ALL_CURRENCY_OK"
