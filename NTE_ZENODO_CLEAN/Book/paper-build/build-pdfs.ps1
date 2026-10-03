param(
  [string[]]$Only
)

$ErrorActionPreference = "Stop"

# Canonical book sources: parent Book/ folder (excludes depreciated/)
$canonicalRoot = Split-Path $PSScriptRoot -Parent
$buildDir = $PSScriptRoot
Set-Location $buildDir

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }

$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }

# Canonical chapter list (per NTE_Chapter_State_Ledger; Book/ root only)
$chapters = @(
  "Prelude_The_Forty_Million_Year_Instant_v5.md",
  "Chapter_1_The_Photons_Journey_v7_3.md",
  "Chapter_2_Entanglement_as_Geometry_v6.md",
  "Chapter_3_A_Closed_Universe_v5.md",
  "Chapter_4_Time_as_Expansion_v7_2.md",
  "Chapter_5_The_Eighth_Colour_v6_2.md",
  "Chapter_6_Why_Quantum_Mechanics_is_Geometry_v5_3.md",
  "Chapter_7_The_Gauge_Birth_v3_3.md",
  "Chapter_8_The_Unresolved_Particle_v4.md",
  "Chapter_9_The_Number_That_Could_Have_Failed_v3.md",
  "Chapter_10_The_Silvered_Boundary_v6.md",
  "Chapter_11_What_the_Universe_Sounds_Like_v3_1.md",
  "Chapter_12_The_Chord_v3_1.md",
  "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v5.md",
  "Chapter_14_Strange_Geometries_and_Structural_Rhymes_v1.md",
  "Chapter_15_The_Score_v2.md",
  "Chapter_16_Stranger_and_Stranger_v1_1.md",
  "Chapter_17_The_Working_Bet_v2.md",
  "Appendix_A_NTE_Popular_Paper_Reader_Edition.md",
  "Appendix_B_NTE_Corpus_Links.md"
)

if ($Only -and $Only.Count -gt 0) {
  $chapters = $Only
}

$scratchDir = Join-Path $buildDir "scratch-src"
$outDir = Join-Path $buildDir "pdf-out"
$defaults = Join-Path $buildDir "pdf-defaults.yaml"
New-Item -ItemType Directory -Force $scratchDir | Out-Null
New-Item -ItemType Directory -Force $outDir | Out-Null

$built = 0
foreach ($name in $chapters) {
  $src = Join-Path $canonicalRoot $name
  if (-not (Test-Path $src)) {
    Write-Warning "Missing canonical source: $src"
    continue
  }

  $scratch = Join-Path $scratchDir $name
  Copy-Item $src $scratch -Force

  $t = Get-Content $scratch -Raw -Encoding UTF8
  $t = $t.Replace(([char]0x2713).ToString(), "PASS")
  $t = $t.Replace(([char]0x2714).ToString(), "PASS")
  $t = $t.Replace(([char]0x2611).ToString(), "PASS")
  $t = $t.Replace(([char]0x2612).ToString(), "FAIL")
  $t = $t.Replace([string][char]0x27F9, "=>")   # ⟹
  [System.IO.File]::WriteAllText($scratch, $t, [System.Text.UTF8Encoding]::new($false))

  $prepareBook = Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) "NTE v10_6\Working\prepare_book_pdf.py"
  if (Test-Path $prepareBook) {
    & python $prepareBook $scratch
    if ($LASTEXITCODE -ne 0) { throw "prepare_book_pdf.py failed for $name" }
  }

  $stripScript = Join-Path (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent) "NTE v10_6\Working\strip_publication_tail.py"
  if (Test-Path $stripScript) {
    & python $stripScript $scratch
    if ($LASTEXITCODE -ne 0) { throw "strip_publication_tail.py failed for $name" }
  }

  $out = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
  Write-Host "Building $name -> $out"
  & $pandoc $scratch --defaults $defaults -o $out
  if ($LASTEXITCODE -ne 0) {
    throw "Pandoc failed for $name (exit $LASTEXITCODE)"
  }
  $built++
}

Write-Host "Done. $built PDF(s) in $outDir"
