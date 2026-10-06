param(
  [switch]$SkipBuild,
  [ValidateSet("Live", "Full")]
  [string]$Tier = "Live"
)

$ErrorActionPreference = "Stop"

$buildDir = $PSScriptRoot
$pdfOut = Join-Path $buildDir "pdf-out"
$uploadDir = Join-Path $buildDir "zenodo-upload"
$recordId = "19440068"
$recordUrl = "https://zenodo.org/records/$recordId"
$doi = "10.5281/zenodo.19440067"

# Live v2 = files to publish on corpus deposit (Greg upload set)
# Pdf = public filename on Zenodo (Wave 1 link stability where noted)
# SourceMd = canonical markdown to build from
$liveBundle = @(
  @{ SourceMd = "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md"; Pdf = "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.pdf"; Role = "Wave 1 standalone P1" },
  @{ SourceMd = "Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md"; Pdf = "Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.pdf"; Role = "Wave 1 standalone kappa0" },
  @{ SourceMd = "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md"; Pdf = "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.pdf"; Role = "Wave 1 standalone P4" },
  @{ SourceMd = "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md"; Pdf = "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.pdf"; Role = "Wave 1 standalone P5 (CR2 B1; stable v0_2 filename)" },
  @{ SourceMd = "NTE_v10_17_Part1_Foundations.md"; Pdf = "NTE_v10_17_Part1_Foundations.pdf"; Role = "Master corpus Part 1" },
  @{ SourceMd = "NTE_v10_17_Part2_Structure.md"; Pdf = "NTE_v10_17_Part2_Structure.pdf"; Role = "Master corpus Part 2" },
  @{ SourceMd = "NTE_v10_17_Part3_Accounting.md"; Pdf = "NTE_v10_17_Part3_Accounting.pdf"; Role = "Master corpus Part 3" },
  @{ SourceMd = "Paper_Popular_v10_8_Full_Edition.md"; Pdf = "Paper_Popular_v10_8_Full_Edition.pdf"; Role = "Popular Full (corpus deposit)" },
  @{ SourceMd = "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md"; Pdf = "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.pdf"; Role = "P5 explicit version label (optional 9th file)"; Optional = $true }
)

# Full tier = local build archive (not default Zenodo upload)
$fullSources = @(
  "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md",
  "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md",
  "Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md",
  "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_Pedagogical_Pivot_v1_0_20260530.md",
  "NTE_v10_17_Part1_Foundations.md",
  "NTE_v10_17_Part2_Structure.md",
  "NTE_v10_17_Part3_Accounting.md",
  "Paper_S6_M_R_Heat_Kernel_v1_0.md",
  "Paper_Popular_v10_8_Full_Edition.md",
  "Paper_External_Empirical_Surface_Clean_Gates_v0_1_20260530.md",
  "Paper_Kappa_AB_v10_17_2.md",
  "Paper_S2_v1_0_Consolidation_20260525.md",
  "Paper_S1_v0_4.md",
  "Paper_OctonionExtension_v10_9.md",
  "Paper_Popular_v10_8_Reader_Edition.md"
)

if (-not $SkipBuild) {
  Write-Host "Building corpus PDFs (tier: $Tier)..."
  if ($Tier -eq "Full") {
    & (Join-Path $buildDir "build-pdfs.ps1")
  } else {
    $toBuild = $liveBundle | ForEach-Object { $_.SourceMd } | Select-Object -Unique
    & (Join-Path $buildDir "build-pdfs.ps1") -Only $toBuild
  }
}

New-Item -ItemType Directory -Force $uploadDir | Out-Null

$rows = New-Object System.Collections.Generic.List[object]
$missing = @()

if ($Tier -eq "Live") {
  foreach ($entry in $liveBundle) {
    $srcMd = $entry.SourceMd
    $pdfName = $entry.Pdf
    $srcPdf = Join-Path $pdfOut ([System.IO.Path]::GetFileNameWithoutExtension($srcMd) + ".pdf")
    $destPdf = Join-Path $uploadDir $pdfName

    if (-not (Test-Path $srcPdf)) {
      $missing += "$pdfName (from $srcMd)"
      continue
    }

    Copy-Item $srcPdf $destPdf -Force
    $hash = (Get-FileHash $srcPdf -Algorithm MD5).Hash.ToLower()
    $size = (Get-Item $srcPdf).Length
    $url = "$recordUrl/files/$pdfName" + "?download=1"

    $rows.Add([pscustomobject]@{
      Source   = $srcMd
      Pdf      = $pdfName
      Role     = $entry.Role
      Optional = [bool]$entry.Optional
      Bytes    = $size
      Md5      = $hash
      Download = $url
    })
  }

  $keepNames = @($rows | ForEach-Object { $_.Pdf }) + @("MANIFEST.md")
  Get-ChildItem $uploadDir -File | Where-Object { $_.Name -notin $keepNames } | Remove-Item -Force
} else {
  foreach ($src in $fullSources) {
    $pdfName = [System.IO.Path]::GetFileNameWithoutExtension($src) + ".pdf"
    $srcPdf = Join-Path $pdfOut $pdfName
    $destPdf = Join-Path $uploadDir $pdfName

    if (-not (Test-Path $srcPdf)) {
      $missing += $pdfName
      continue
    }

    Copy-Item $srcPdf $destPdf -Force
    $hash = (Get-FileHash $srcPdf -Algorithm MD5).Hash.ToLower()
    $size = (Get-Item $srcPdf).Length
    $url = "$recordUrl/files/$pdfName" + "?download=1"

    $rows.Add([pscustomobject]@{
      Source   = $src
      Pdf      = $pdfName
      Role     = "Full tier local"
      Optional = $false
      Bytes    = $size
      Md5      = $hash
      Download = $url
    })
  }
}

$manifestPath = Join-Path $uploadDir "MANIFEST.md"
$generated = Get-Date -Format "yyyy-MM-dd HH:mm"

$lines = @(
  "# Zenodo corpus upload bundle",
  "",
  "Generated: $generated",
  "Tier: **$Tier**",
  "Record: [$recordUrl]($recordUrl)",
  "DOI: [$doi](https://doi.org/$doi)",
  "",
  "Upload PDFs marked **required** below as a **new version** of the corpus deposit.",
  "See ``NTE v10_6/Zenodo_Corpus_Deposit_Register.md``.",
  ""
)

if ($Tier -eq "Live") {
  $required = @($rows | Where-Object { -not $_.Optional })
  $optional = @($rows | Where-Object { $_.Optional })
  $lines += "**Required on deposit:** $($required.Count) files (8 if you omit optional P5 v0.3 label)."
  $lines += "**Optional 9th file:** P5 v0.3 filename (same content as slot 4; explicit version stamp)."
  $lines += ""
  $lines += "P5 slot 4: PDF filename stays ``..._v0_2_arxiv_...`` for Wave 1 links; built from ``..._v0_3_zenodo_...md`` (CR2 B1 honest scope)."
  $lines += ""
}

if ($missing.Count -gt 0) {
  $lines += "## MISSING (build failed or not run)"
  foreach ($m in $missing) { $lines += "- $m" }
  $lines += ""
}

$lines += "## Files"
$lines += ""
$lines += "| Upload | Source .md | Role | Req | Size | MD5 |"
$lines += "|--------|------------|------|-----|------|-----|"

foreach ($r in $rows) {
  $kb = [math]::Round($r.Bytes / 1024, 1)
  $req = if ($r.Optional) { "opt" } else { "**yes**" }
  $lines += "| $($r.Pdf) | ``$($r.Source)`` | $($r.Role) | $req | ${kb} KB | ``$($r.Md5)`` |"
}

$lines += ""
$lines += "## Version notes (paste into Zenodo)"
$lines += ""
$lines += "- v2 - CR2 honest-scope refresh (2026-06-01): P5 solar-only Tier A; atmospheric ~1.49x open; Lambda numeric 1.05x retired; S2 a4=0 labels in corpus; Part 1-2 F7 disclosure language; Popular CR-H1/H2 sync."
$lines += "- Changelog: ``Working/P5_v0_3_Zenodo_Changelog_20260601.md``"
$lines += ""

if ($Tier -eq "Live") {
  $lines += "## Download URLs (required files)"
  $lines += ""
  foreach ($r in ($rows | Where-Object { -not $_.Optional })) {
    $lines += "- [$($r.Pdf)]($($r.Download))"
  }
  $lines += ""
}

$lines | Set-Content $manifestPath -Encoding UTF8

Write-Host "Bundle: $uploadDir ($($rows.Count) PDFs, tier $Tier)"
Write-Host "Manifest: $manifestPath"

if ($missing.Count -gt 0) {
  Write-Warning "Missing $($missing.Count) PDF(s): $($missing -join ', ')"
  exit 1
}
