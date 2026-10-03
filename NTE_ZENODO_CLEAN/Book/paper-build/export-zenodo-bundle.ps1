param(
  [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"

$buildDir = $PSScriptRoot
$pdfOut = Join-Path $buildDir "pdf-out"
$uploadDir = Join-Path $buildDir "zenodo-upload"
$recordId = "19535903"
$recordUrl = "https://zenodo.org/records/$recordId"
$doi = "10.5281/zenodo.19535902"

# Same canonical set as build-pdfs.ps1 (basename without .md → .pdf)
$sources = @(
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

if (-not $SkipBuild) {
  Write-Host "Building all book PDFs..."
  & (Join-Path $buildDir "build-pdfs.ps1")
}

New-Item -ItemType Directory -Force $uploadDir | Out-Null

# Drop PDFs not in this export (stale filenames from prior bundles)
$expectedPdfs = $sources | ForEach-Object { [IO.Path]::GetFileNameWithoutExtension($_) + ".pdf" }
Get-ChildItem $uploadDir -Filter "*.pdf" -ErrorAction SilentlyContinue | ForEach-Object {
  if ($expectedPdfs -notcontains $_.Name) {
    Remove-Item $_.FullName -Force
    Write-Host "Removed stale upload: $($_.Name)"
  }
}

$rows = New-Object System.Collections.Generic.List[object]
$missing = @()

foreach ($src in $sources) {
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
    Bytes    = $size
    Md5      = $hash
    Download = $url
  })
}

$manifestPath = Join-Path $uploadDir "MANIFEST.md"
$generated = Get-Date -Format "yyyy-MM-dd HH:mm"

$lines = @(
  "# Zenodo book upload bundle",
  "",
  "Generated: $generated",
  "Record: [$recordUrl]($recordUrl)",
  "DOI: [$doi](https://doi.org/$doi)",
  "",
  "Upload every PDF in this folder as a **new version** of the book deposit.",
  "See ``Book/Zenodo_Book_Deposit_Register.md`` for the maintenance checklist.",
  ""
)

if ($missing.Count -gt 0) {
  $lines += "## MISSING (build failed or not run)"
  foreach ($m in $missing) { $lines += "- $m" }
  $lines += ""
}

$lines += "## Files"
$lines += ""
$lines += "| PDF | Source | Size | MD5 | Download URL |"
$lines += "|-----|--------|------|-----|--------------|"

foreach ($r in $rows) {
  $kb = [math]::Round($r.Bytes / 1024, 1)
  $lines += "| $($r.Pdf) | ``$($r.Source)`` | ${kb} KB | ``$($r.Md5)`` | $($r.Download) |"
}

$lines += ""
$lines += "## v1 obsolete on Zenodo (remove or supersede in next version)"
$lines += ""
$lines += "- ``Chapter_16_The_Working_Bet_v1.pdf`` → replaced by Ch 16 + Ch 17"
$lines += "- ``Appendix_A_NTE_Popular_Paper_v10_8_v7.pdf`` → ``Appendix_A_NTE_Popular_Paper_Reader_Edition.pdf``"
$lines += ""

$lines | Set-Content $manifestPath -Encoding UTF8

Write-Host "Bundle: $uploadDir ($($rows.Count) PDFs)"
Write-Host "Manifest: $manifestPath"

if ($missing.Count -gt 0) {
  Write-Warning "Missing $($missing.Count) PDF(s): $($missing -join ', ')"
  exit 1
}
