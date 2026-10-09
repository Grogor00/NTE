<#
.SYNOPSIS
  Render Book_Cursor_Suggested chapter/appendix/prelude markdown to PDF.

.DESCRIPTION
  Copies each source .md to a temp scratch dir, runs Working\strip_corpus_metadata.py,
  applies book-folder process banner / path scrubbing, then pandoc + pdflatex into pdf\.

  Excludes: README*, Chapter_09_The_Number_That_Could_Have_Failed_v6.md (pointer stub).
  Zenodo register is included by default; pass -SkipZenodo to omit it.

.NOTES
  Root .gitignore has **/*.pdf — track outputs with: git add -f Book_Cursor_Suggested/pdf/*.pdf
#>
param(
  [switch]$SkipZenodo,
  [string[]]$Only
)

$ErrorActionPreference = "Stop"

$bookDir = $PSScriptRoot
$repoRoot = Split-Path $bookDir -Parent
$pdfDir = Join-Path $bookDir "pdf"
$defaults = Join-Path $bookDir "pandoc-book.yaml"
$stripScript = Join-Path $repoRoot "Working\strip_corpus_metadata.py"
$pandoc = Join-Path $env:LOCALAPPDATA "Pandoc\pandoc.exe"
if (-not (Test-Path $pandoc)) { $pandoc = "pandoc" }

$miktexBin = Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) {
  $env:Path = "$miktexBin;" + $env:Path
}

if (-not (Test-Path $defaults)) {
  throw "Missing pandoc defaults: $defaults"
}
if (-not (Test-Path $stripScript)) {
  throw "Missing strip script: $stripScript"
}

New-Item -ItemType Directory -Force $pdfDir | Out-Null
# Pandoc resolves include-in-header / resource paths relative to CWD (same pattern as Workflow\zenodo_build_keep_pdfs.ps1)
Set-Location $bookDir
$scratchRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("nte_book_cursor_pdf_" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force $scratchRoot | Out-Null

$excludeExact = @(
  "Chapter_09_The_Number_That_Could_Have_Failed_v6.md"
)

function Test-IsBookSource {
  param([System.IO.FileInfo]$File)
  $name = $File.Name
  if ($name -like "README*") { return $false }
  if ($excludeExact -contains $name) { return $false }
  if ($SkipZenodo -and $name -like "Zenodo*") { return $false }
  if ($Only -and ($Only -notcontains $name)) { return $false }
  $stem = [System.IO.Path]::GetFileNameWithoutExtension($name)
  if ($stem -match '^(Prelude_|Chapter_|Appendix_|Zenodo_)') { return $true }
  return $false
}

function Get-TitleFromHeadings {
  param([string]$Text)
  $titles = @()
  foreach ($line in ($Text -split "`r?`n")) {
    if ($line -match '^#\s+(.+)$') {
      $titles += $Matches[1].Trim()
      if ($titles.Count -ge 2) { break }
    }
  }
  if ($titles.Count -eq 0) { return @{ Title = $null; Subtitle = $null } }
  if ($titles.Count -eq 1) { return @{ Title = $titles[0]; Subtitle = $null } }
  # Convention: "# The Shape of Time" then "# Chapter N — ..."
  return @{ Title = $titles[1]; Subtitle = $titles[0] }
}

function Strip-BookProcessBanners {
  param([string]$Text)
  $lines = $Text -split "`r?`n"
  $kept = New-Object System.Collections.Generic.List[string]
  foreach ($line in $lines) {
    # Drop HTML process comments
    if ($line -match '^\s*<!--.*-->\s*$') { continue }

    $drop = $false
    if ($line -match '(?i)CURSOR\s+SUGGESTED') { $drop = $true }
    elseif ($line -match '(?i)Not for publication') { $drop = $true }
    elseif ($line -match '(?i)Greg\s+ratif') { $drop = $true }
    elseif ($line -match '(?i)PC\s+ship') { $drop = $true }
    elseif ($line -match '(?i)Handoffs/') { $drop = $true }
    elseif ($line -match '(?i)Working/') { $drop = $true }
    # Process end-of-file Cursor banners (keep literary chapter text)
    elseif ($line -match '(?i)^\*End of Cursor-suggested') { $drop = $true }

    if (-not $drop) { $kept.Add($line) }
  }
  $out = ($kept -join "`n")

  # Soft scrub residual path tokens inside remaining lines (do not drop whole literary lines)
  $out = [regex]::Replace($out, '(?i)`(?:Working|Handoffs)/[^`\n]+`', '')
  $out = [regex]::Replace($out, '(?i)\b(?:Working|Handoffs)/[^\s)\]>,;]+', '')
  $out = [regex]::Replace($out, "`n{3,}", "`n`n")
  return $out.TrimEnd() + "`n"
}

function Convert-UnicodeScriptRun {
  param(
    [string]$Run,
    [int]$BaseCode,
    [string]$Wrap  # '_' or '^'
  )
  $digits = New-Object System.Text.StringBuilder
  foreach ($ch in $Run.ToCharArray()) {
    [void]$digits.Append([int][char]$ch - $BaseCode)
  }
  return ('{0}{{{1}}}' -f $Wrap, $digits.ToString())
}

function Fix-PdflatexUnicode {
  param([string]$Text)
  # √ is awkward for newunicodechar; rewrite structured forms, else ASCII word
  $sqrt = [char]0x221A
  $Text = [regex]::Replace($Text, [regex]::Escape($sqrt) + '\(([^)]+)\)', '$\sqrt{$1}$')
  $Text = [regex]::Replace($Text, [regex]::Escape($sqrt) + '([0-9]+)', '$\sqrt{$1}$')
  $Text = $Text.Replace([string]$sqrt, ' sqrt ')

  # Collapse unicode subscript/superscript *runs* so Δm²₂₁ → Δm^{2}_{21} (not double _)
  $Text = [regex]::Replace($Text, '[\u2080-\u2089]+', {
      param($m)
      Convert-UnicodeScriptRun -Run $m.Value -BaseCode 0x2080 -Wrap '_'
    })
  # Superscript digits: ⁰¹²³⁴⁵⁶⁷⁸⁹ (scattered codepoints) — handle common contiguous runs via explicit map
  $supMap = @{
    ([char]0x2070) = '0'; ([char]0x00B9) = '1'; ([char]0x00B2) = '2'; ([char]0x00B3) = '3'
    ([char]0x2074) = '4'; ([char]0x2075) = '5'; ([char]0x2076) = '6'
    ([char]0x2077) = '7'; ([char]0x2078) = '8'; ([char]0x2079) = '9'
  }
  $Text = [regex]::Replace($Text, '[\u2070\u00B9\u00B2\u00B3\u2074-\u2079]+', {
      param($m)
      $digits = New-Object System.Text.StringBuilder
      foreach ($ch in $m.Value.ToCharArray()) {
        if ($supMap.ContainsKey($ch)) { [void]$digits.Append($supMap[$ch]) }
      }
      return ('^{{{0}}}' -f $digits.ToString())
    })

  # Light ASCII normalisations; Greek/ops handled by header-book.tex \newunicodechar
  $pairs = @(
    @([string][char]0x2212, '-'),     # minus → hyphen-minus
    @([string][char]0x00AD, ''),      # soft hyphen
    @([string][char]0x2002, ' '),     # en space
    @([string][char]0x2003, ' '),     # em space
    @([string][char]0x2009, ' '),     # thin space
    @([string][char]0x200A, ' '),     # hair space
    @([string][char]0x200B, ''),      # zero-width space
    @([string][char]0x00A0, ' '),     # nbsp
    @([string][char]0x2713, 'PASS'),
    @([string][char]0x2714, 'PASS'),
    @([string][char]0x2717, 'FAIL'),
    @([string][char]0x2611, 'PASS'),
    @([string][char]0x2612, 'FAIL'),
    @([string][char]0x27F9, '=>')
  )
  foreach ($p in $pairs) {
    $Text = $Text.Replace($p[0], $p[1])
  }
  return $Text
}

function Inject-YamlTitle {
  param(
    [string]$Text,
    [hashtable]$Meta
  )
  if (-not $Meta.Title) { return $Text }
  # If YAML front matter already present, leave it (e.g. Appendix A)
  if ($Text -match '(?s)^---\r?\n.*?\r?\n---\r?\n') { return $Text }

  $esc = {
    param($s)
    if ($null -eq $s) { return $null }
    return ($s -replace '\\', '\\' -replace '"', '\"')
  }
  $title = & $esc $Meta.Title
  $yaml = "---`ntitle: `"$title`"`n"
  if ($Meta.Subtitle) {
    $sub = & $esc $Meta.Subtitle
    $yaml += "subtitle: `"$sub`"`n"
  }
  $yaml += "---`n`n"
  return $yaml + $Text
}

$sources = Get-ChildItem -Path $bookDir -Filter "*.md" -File |
  Where-Object { Test-IsBookSource $_ } |
  Sort-Object Name

if ($sources.Count -eq 0) {
  throw "No source markdown matched inclusion rules under $bookDir"
}

$ok = New-Object System.Collections.Generic.List[string]
$fail = New-Object System.Collections.Generic.List[object]

try {
  foreach ($src in $sources) {
    $name = $src.Name
    $scratch = Join-Path $scratchRoot $name
    $outPdf = Join-Path $pdfDir ([System.IO.Path]::GetFileNameWithoutExtension($name) + ".pdf")
    Write-Host "Building $name -> $outPdf"

    try {
      Copy-Item -LiteralPath $src.FullName -Destination $scratch -Force

      & python $stripScript $scratch
      if ($LASTEXITCODE -ne 0) { throw "strip_corpus_metadata.py exit $LASTEXITCODE" }

      $text = [System.IO.File]::ReadAllText($scratch, [System.Text.UTF8Encoding]::new($false))
      $text = Strip-BookProcessBanners $text
      $text = Fix-PdflatexUnicode $text
      $meta = Get-TitleFromHeadings $text
      $text = Inject-YamlTitle -Text $text -Meta $meta
      [System.IO.File]::WriteAllText($scratch, $text, [System.Text.UTF8Encoding]::new($false))

      $pandocArgs = @(
        $scratch,
        "--defaults", $defaults,
        "--resource-path", $bookDir,
        "-o", $outPdf
      )
      & $pandoc @pandocArgs
      if ($LASTEXITCODE -ne 0) { throw "pandoc exit $LASTEXITCODE" }
      if (-not (Test-Path $outPdf)) { throw "PDF not written" }

      $mdT = (Get-Item -LiteralPath $src.FullName).LastWriteTimeUtc
      $pdfT = (Get-Item -LiteralPath $outPdf).LastWriteTimeUtc
      if ($pdfT -lt $mdT) { throw "PDF older than source md" }

      $ok.Add($name)
    }
    catch {
      $fail.Add([pscustomobject]@{ Name = $name; Error = $_.Exception.Message })
      Write-Warning "FAILED $name : $($_.Exception.Message)"
    }
  }
}
finally {
  if (Test-Path $scratchRoot) {
    Remove-Item -LiteralPath $scratchRoot -Recurse -Force -ErrorAction SilentlyContinue
  }
}

Write-Host ""
Write-Host "OK: $($ok.Count) / $($sources.Count)"
if ($fail.Count -gt 0) {
  Write-Host "FAILURES ($($fail.Count)):"
  $fail | ForEach-Object { Write-Host ("  - {0}: {1}" -f $_.Name, $_.Error) }
  exit 1
}

Write-Host "All PDFs current under $pdfDir"
exit 0
