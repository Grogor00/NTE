# Shared NTE path resolution for autonomous / auto scripts.
# Dot-source from any Workflow script:
#   . (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
#
# Greg mandate: OneDrive is NOT used for this project.
# Canonical corpus ONLY: C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN
#
# Sets (all always the Drive paths):
#   $NteCorpusRoot / $NteRoot
#   $NteWorkflowRoot

$script:NteCanonicalCorpus = 'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN'
$script:NteCanonicalWorkflow = 'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Workflow'

if (-not (Test-Path (Join-Path $script:NteCanonicalCorpus 'Handoffs'))) {
  throw "NTE canonical corpus missing or incomplete: $($script:NteCanonicalCorpus) (Handoffs not found). OneDrive/Desktop are not valid substitutes."
}
if (-not (Test-Path (Join-Path $script:NteCanonicalCorpus 'Working'))) {
  throw "NTE canonical corpus missing or incomplete: $($script:NteCanonicalCorpus) (Working not found)."
}
if (-not (Test-Path (Join-Path $script:NteCanonicalWorkflow 'Resolve-NteRoots.ps1'))) {
  throw "NTE canonical Workflow missing: $($script:NteCanonicalWorkflow)"
}

$invokeRoot = $PSScriptRoot
if (-not $invokeRoot) {
  $invokeRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
}
if ($invokeRoot -and ($invokeRoot -match '(?i)OneDrive|NTE_historical_archive')) {
  Write-Warning "Ignoring non-canonical invoke path: $invokeRoot - using $($script:NteCanonicalWorkflow)"
}

$NteCorpusRoot = $script:NteCanonicalCorpus
$NteWorkflowRoot = $script:NteCanonicalWorkflow
$NteRoot = $NteCorpusRoot
