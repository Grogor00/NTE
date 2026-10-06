# NTE autonomous toggle — Windows-friendly wrapper
# Usage (from CMD or PowerShell):
#   auto on
#   auto off
#   auto status
#   auto on main
#   auto off ac_jammer
#   auto on pc_scratch
#   auto on all
#
# Bare "auto on/off" uses Workflow\.cursor_autonomous_chat_lane (set by stream bootstrap)
# Canonical corpus: C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN  (see Resolve-NteRoots.ps1)

param(
  [Parameter(Mandatory = $true, Position = 0)]
  [ValidateSet('on', 'off', 'status')]
  [string]$Action,
  [Parameter(Position = 1)]
  [string]$StreamName = ''
)

# Canonical only (Greg: OneDrive unused; Google Drive is the project root)
. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteWorkflowRoot
$lanePath = Join-Path $root '.cursor_autonomous_chat_lane'
$toggle = Join-Path $root 'cursor_autonomous_toggle.ps1'

function Resolve-Stream([string]$Name) {
  if (-not $Name) { return $null }
  $n = $Name.ToLower().Trim()
  switch -Regex ($n) {
    '^(main|m)$' { return 'main' }
    '^(all|a)$' { return 'all' }
    '^(ac_jammer|ac-jammer|acjammer|ac|jammer|aj)$' { return 'ac_jammer' }
    '^(pc_scratch|pc-scratch|pcscratch|pc|scratch|ps)$' { return 'pc_scratch' }
    '^(supervisor|watch|watchdog|wd|sup)$' { return 'supervisor' }
    default { return $null }
  }
}

$stream = Resolve-Stream $StreamName
if (-not $stream -and (Test-Path $lanePath)) {
  $lane = (Get-Content $lanePath -Raw -ErrorAction SilentlyContinue).Trim().ToLower()
  $stream = Resolve-Stream $lane
}
if (-not $stream) { $stream = 'all' }

switch ($Action) {
  'on' {
    if ($stream -eq 'all') {
      & (Join-Path $root 'auto-on-all.cmd')
    } else {
      & $toggle -Stream $stream -On
    }
  }
  'off' { & $toggle -Stream $stream -Off }
  'status' { & $toggle -Status }
}
