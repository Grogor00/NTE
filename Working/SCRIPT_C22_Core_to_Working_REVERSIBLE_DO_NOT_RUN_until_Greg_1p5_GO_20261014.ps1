# REVERSIBLE C22 Core -> Working move
# DO NOT RUN until Greg Stage 1.5 GO (AC DISPATCH 2026-10-14 answer #5).
# Usage after GO: powershell -File this_script.ps1

$ErrorActionPreference = 'Stop'
$root = Split-Path (Split-Path $PSScriptRoot -Parent) -ErrorAction SilentlyContinue
if (-not $root) { $root = 'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN' }
$src = Join-Path $root 'Core_Papers\Companion_22_Dark_Sector_Geometric_CDM_Investigation_v10_19_0.md'
$dstDir = Join-Path $root 'Working'
$dst = Join-Path $dstDir 'Companion_22_Dark_Sector_Geometric_CDM_Investigation_v10_19_0_RESEARCH_LOG_from_Core_20261014.md'
$bak = Join-Path $root 'Core_Papers\_HOLD_Companion_22_MOVED_TO_WORKING_pointer_20261014.md'

if (-not (Test-Path $src)) { throw "Source missing: $src" }
if (Test-Path $dst) { throw "Destination already exists: $dst" }

Copy-Item -LiteralPath $src -Destination $dst
Remove-Item -LiteralPath $src
@"
# Companion 22 removed from Core (Stage 1.5)

**Moved to:** ``Working/Companion_22_Dark_Sector_Geometric_CDM_Investigation_v10_19_0_RESEARCH_LOG_from_Core_20261014.md``

**Authority:** Greg Stage 1.5 GO (fill date when run).

To reverse: move the Working file back to ``Core_Papers/Companion_22_Dark_Sector_Geometric_CDM_Investigation_v10_19_0.md`` and delete this pointer.
"@ | Set-Content -LiteralPath $bak -Encoding UTF8

Write-Host "C22 moved Core -> Working. Pointer left in Core_Papers."
