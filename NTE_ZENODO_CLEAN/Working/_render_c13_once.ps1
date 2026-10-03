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
New-Item -ItemType Directory -Force $scratchDir | Out-Null
New-Item -ItemType Directory -Force $outDir | Out-Null

$name = "Companion_13_Yukawa_Nu2_v10_19_0.md"
$src = Join-Path $repoRoot "Core_Papers\$name"
$scratch = Join-Path $scratchDir $name
$out = Join-Path $outDir ([IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")

Copy-Item $src $scratch -Force
$t = Get-Content $scratch -Raw -Encoding UTF8
$t = $t.Replace([string][char]0x2713, "PASS").Replace([string][char]0x2714, "PASS").Replace([string][char]0x2611, "PASS").Replace([string][char]0x2612, "FAIL").Replace([string][char]0x27F9, "=>")
[IO.File]::WriteAllText($scratch, $t, [Text.UTF8Encoding]::new($false))

& python (Join-Path $workingRoot "prepare_paper_pdf.py") $scratch
if ($LASTEXITCODE -ne 0) { throw "prepare_paper_pdf.py exit $LASTEXITCODE" }
& python (Join-Path $workingRoot "strip_publication_tail.py") $scratch
if ($LASTEXITCODE -ne 0) { throw "strip_publication_tail.py exit $LASTEXITCODE" }

$prevEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$pandocOut = (& $pandoc $scratch --defaults $defaults -o $out 2>&1 | Out-String)
$ErrorActionPreference = $prevEap
if ($LASTEXITCODE -ne 0) {
  Write-Host $pandocOut
  throw "pandoc exit $LASTEXITCODE"
}
if (-not (Test-Path $out)) { throw "PDF not created" }

$md = Get-Item $src
$pdf = Get-Item $out
Write-Host "PASS $name"
Write-Host ("md=" + $md.LastWriteTime.ToString("o") + " pdf=" + $pdf.LastWriteTime.ToString("o") + " size=" + $pdf.Length)
if ($pdf.LastWriteTime -le $md.LastWriteTime) { throw "PDF not newer than md" }
Write-Host "CURRENCY_OK"
