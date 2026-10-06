param(
  [string[]]$Only
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path $PSScriptRoot -Parent
$canonicalRoot = Join-Path $repoRoot "Papers"
$workingRoot = Join-Path $repoRoot "Working"
$buildDir = $PSScriptRoot
Set-Location $buildDir

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }

# Tier 1 standalone (technical)
$technical = @(
  "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md",
  "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md",
  "Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md"
)

# Pedagogical-pivot companions (PC v1.0 — see Working/NTE_Pedagogical_Pivot_Companions_Register.md)
$pedRoot = Join-Path $canonicalRoot "Pedagogical_Explanatory_For_Curious_Readers"
$pedagogical = @(
  "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Kappa_AB_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_S1_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_S2_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_OctonionExtension_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_External_Empirical_Surface_Clean_Gates_Pedagogical_Pivot_v1_0_20260530.md"
)

# Technical companions C1–C13 (canonical filenames — see Papers/COMPANION_CANONICAL_INDEX.md)
$companions = @(
  "Companion_1_Entanglement_v10_6.md",
  "Companion_2_BornRule_Hopf_v10_6_v2.md",
  "Companion_3_Quantisation_Compactness_v10_6.md",
  "Companion_4_Hierarchy_Resonance_v10_6.md",
  "Companion_5_StateSpace_Surface_v10_8.md",
  "Companion_6_Gap5_BornRule_GaugeBirth_v10_6_v2.md",
  "Companion_7_Neutrino_v10_17_2.md",
  "Companion_8_VNTE_Trajectory_v10_8.md",
  "Companion_9_VNTE_Stage3_v10_8.md",
  "Companion_10_Gap1_M1_Pathways_v10_17_2.md",
  "Companion_11_Lambda_Unimodular_Closure_v10_17_2.md",
  "Companion_12_Spectral_Chord_Closure_v10_17_2.md",
  "Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md"
)

$papers = $technical + $pedagogical + $companions + @(
  "NTE_v10_18_0_Part1_Foundations.md",
  "NTE_v10_18_0_Part2_Structure.md",
  "NTE_v10_18_0_Part3_Accounting.md",
  "Paper_S6_M_R_Heat_Kernel_v1_0.md",
  "Paper_Popular_v10_8_Full_Edition.md",
  "Paper_External_Empirical_Surface_Clean_Gates_v0_1_20260530.md",
  "Paper_Kappa_AB_v10_17_2.md",
  "Paper_S2_v1_0_Consolidation_20260525.md",
  "Paper_S1_v0_4.md",
  "Paper_OctonionExtension_v10_9.md",
  "Paper_Popular_v10_8_Reader_Edition.md",
  "NTE_Corpus_Papers_Index.md"
)

# Working-folder docs (reader glossary — not in Papers/)
$workingDocs = @(
  "NTE_Reader_Glossary_Companion_v1_0.md"
)

$buildItems = @()
foreach ($name in $papers) {
  $root = $canonicalRoot
  if ($pedagogical -contains $name) { $root = $pedRoot }
  $buildItems += [pscustomobject]@{
    Name = $name
    SourceRoot = $root
    Kind = "paper"
  }
}
foreach ($name in $workingDocs) {
  $buildItems += [pscustomobject]@{
    Name = $name
    SourceRoot = $workingRoot
    Kind = "working"
  }
}

if ($Only -and $Only.Count -gt 0) {
  $buildItems = $buildItems | Where-Object { $Only -contains $_.Name }
}

$scratchDir = Join-Path $env:TEMP "nte-build-scratch"
$outDir = Join-Path $buildDir "pdf-out"
$defaults = Join-Path $buildDir "pdf-defaults.yaml"
$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }
New-Item -ItemType Directory -Force $scratchDir | Out-Null
New-Item -ItemType Directory -Force $outDir | Out-Null

$preparePaper = Join-Path $workingRoot "prepare_paper_pdf.py"
$prepareMaster = Join-Path $workingRoot "prepare_master_pdf.py"
$stripScript = Join-Path $workingRoot "strip_publication_tail.py"

foreach ($item in $buildItems) {
  $name = $item.Name
  $src = Join-Path $item.SourceRoot $name
  if (-not (Test-Path $src)) {
    Write-Warning "Missing source: $src"
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

  if ($item.Kind -eq "paper" -and $name -notlike "NTE_v10_17_Part*.md" -and $name -notlike "NTE_v10_18_0_Part*.md") {
    if (Test-Path $preparePaper) {
      & python $preparePaper $scratch
      if ($LASTEXITCODE -ne 0) { throw "prepare_paper_pdf.py failed for $name" }
    }
  }

  $defaultsFile = $defaults
  if ($name -like "NTE_v10_17_Part*.md" -or $name -like "NTE_v10_18_0_Part*.md") {
    if (Test-Path $prepareMaster) {
      & python $prepareMaster $scratch
      if ($LASTEXITCODE -ne 0) { throw "prepare_master_pdf.py failed for $name" }
    }
    $masterDefaults = Join-Path $buildDir "pdf-defaults-master.yaml"
    if (Test-Path $masterDefaults) { $defaultsFile = $masterDefaults }
  }

  if (Test-Path $stripScript) {
    & python $stripScript $scratch
    if ($LASTEXITCODE -ne 0) { throw "strip_publication_tail.py failed for $name" }
  }

  $out = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
  Write-Host "Building $name -> $out"
  $pandocArgs = @($scratch, "--defaults", $defaultsFile)
  $doclabel = [System.IO.Path]::ChangeExtension($scratch, ".doclabel.tex")
  if (Test-Path $doclabel) { $pandocArgs += @("--include-in-header", $doclabel) }
  $pandocArgs += @("-o", $out)
  & $pandoc @pandocArgs
  if ($LASTEXITCODE -ne 0) {
    throw "Pandoc failed for $name (exit $LASTEXITCODE)"
  }
}

Write-Host "Done. $($buildItems.Count) PDFs in $outDir"
