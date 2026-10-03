param(
  [switch]$ReportOnly
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $PSScriptRoot -Parent
$papersRoot = Join-Path $repoRoot "Papers"
$pedRoot = Join-Path $papersRoot "Pedagogical_Explanatory_For_Curious_Readers"
$workingRoot = Join-Path $repoRoot "Working"
$buildDir = Join-Path $repoRoot "paper-build"
Set-Location $buildDir

$miktexBin = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) { $env:Path = "$miktexBin;" + $env:Path }

$keep = @(
  "NTE_v10_18_0_Part1_Foundations.md",
  "NTE_v10_18_0_Part2_Structure.md",
  "NTE_v10_18_0_Part3_Accounting.md",
  "Paper_P5_Neutrino_MassRatio_Flux_TwoBranches_4pi_8pi_v0_5_20260621.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md",
  "Paper_P4D_Antilinear_Theta23_MuTau_Reflection_Character_Identity_With_CPN_Phase_v0_3_20260626.md",
  "Paper_P4_CLFV_Amplitude_Ratio_tan2theta23_R_Matrix_Freezing_Z2_Majorana_Clean_Standalone_v0_2_20260622.md",
  "Paper_HeatKernel_S3xS1_SpectralTriple_a4_Vanishing_kappa0_Confluence_Clean_Standalone_v0_2_20260622.md",
  "Paper_Octonionic_Origin_SM_GaugeGroup_SpeciesCount_Associativity_Transition_Clean_Standalone_v0_2_20260622.md",
  "Paper_Hopf_Kappa0_Bare_Coupling_Clean_Standalone_v0_2_20260622.md",
  "Paper_DM_Ratio_Identification_CrossSector_FixedPoint_TwoOrientation_Cosmology_Clean_Standalone_v0_1_20260622.md",
  "Paper_S1_v0_4.md",
  "Paper_S2_v1_0_Consolidation_20260525.md",
  "Paper_S6_M_R_Heat_Kernel_v1_0.md",
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
  "Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md",
  "Paper_Popular_v10_8_Full_Edition.md",
  "Paper_Popular_v10_8_Reader_Edition.md"
)

$pedKeep = @(
  "Paper_S1_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_OctonionExtension_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_S2_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_External_Empirical_Surface_Clean_Gates_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Kappa_AB_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.md"
)

function Get-CurrencyRows {
  param($Items, $OutDir)
  $rows = @()
  foreach ($item in $Items) {
    $src = Join-Path $item.SourceRoot $item.Name
    $pdf = Join-Path $OutDir ([System.IO.Path]::GetFileNameWithoutExtension($item.Name) + ".pdf")
    $row = [ordered]@{
      md = $item.Name
      md_path = $src
      pdf_path = $pdf
      md_mtime = $null
      pdf_mtime = $null
      status = "MISSING_MD"
    }
    if (Test-Path $src) {
      $row.md_mtime = (Get-Item $src).LastWriteTimeUtc.ToString("o")
      if (Test-Path $pdf) {
        $row.pdf_mtime = (Get-Item $pdf).LastWriteTimeUtc.ToString("o")
        $mdT = (Get-Item $src).LastWriteTimeUtc
        $pdfT = (Get-Item $pdf).LastWriteTimeUtc
        $row.status = if ($pdfT -ge $mdT) { "CURRENT" } else { "STALE" }
      } else {
        $row.status = "NO_PDF"
      }
    }
    $rows += $row
  }
  return $rows
}

$buildItems = @()
foreach ($name in $keep) {
  $buildItems += [pscustomobject]@{ Name = $name; SourceRoot = $papersRoot; Kind = "paper" }
}
foreach ($name in $pedKeep) {
  $buildItems += [pscustomobject]@{ Name = $name; SourceRoot = $pedRoot; Kind = "paper" }
}

$outDir = Join-Path $buildDir "pdf-out"
$currency = Get-CurrencyRows $buildItems $outDir
$reportPath = Join-Path $workingRoot "zenodo_pdf_currency_report.json"
$summary = [ordered]@{
  at = (Get-Date).ToString("o")
  total = $currency.Count
  current = @($currency | Where-Object { $_.status -eq "CURRENT" }).Count
  stale = @($currency | Where-Object { $_.status -eq "STALE" }).Count
  no_pdf = @($currency | Where-Object { $_.status -eq "NO_PDF" }).Count
  missing_md = @($currency | Where-Object { $_.status -eq "MISSING_MD" }).Count
  rows = $currency
}
($summary | ConvertTo-Json -Depth 6) | Set-Content $reportPath -Encoding UTF8

if ($ReportOnly) {
  Write-Host "Currency report: $reportPath"
  $currency | Format-Table md, status -AutoSize
  exit 0
}

$scratchDir = Join-Path $buildDir "scratch-src"
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
  $t = $t.Replace([string][char]0x27F9, "=>")
  [System.IO.File]::WriteAllText($scratch, $t, [System.Text.UTF8Encoding]::new($false))

  if ($name -notlike "NTE_v10_18_0_Part*.md") {
    if (Test-Path $preparePaper) {
      & python $preparePaper $scratch
      if ($LASTEXITCODE -ne 0) { throw "prepare_paper_pdf.py failed for $name" }
    }
  }

  $defaultsFile = $defaults
  if ($name -like "NTE_v10_18_0_Part*.md") {
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

$currency = Get-CurrencyRows $buildItems $outDir
$summary = [ordered]@{
  at = (Get-Date).ToString("o")
  total = $currency.Count
  current = @($currency | Where-Object { $_.status -eq "CURRENT" }).Count
  stale = @($currency | Where-Object { $_.status -eq "STALE" }).Count
  no_pdf = @($currency | Where-Object { $_.status -eq "NO_PDF" }).Count
  missing_md = @($currency | Where-Object { $_.status -eq "MISSING_MD" }).Count
  rows = $currency
}
($summary | ConvertTo-Json -Depth 6) | Set-Content $reportPath -Encoding UTF8
Write-Host "Done. $($buildItems.Count) KEEP PDFs in $outDir"
