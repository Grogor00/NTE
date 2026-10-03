. "$PSScriptRoot\cursor_autonomous_inbound.ps1"
$l = Get-LedgerFromDisk
$ids = @('P5-TWOBRANCH-KEYWORDS-FIX','CONSOLIDATED-CLEAN-BUILD-V02-TRIO','CONSOLIDATED-DISPOSITION-BCD')
foreach ($id in $ids) {
  $hits = @($l.tasks | Where-Object { $_.id -eq $id })
  Write-Output "$id count=$($hits.Count) states=$($hits.state -join ',') done=$(Test-LedgerTaskDone $l $id)"
}
$cons = 'CONSOLIDATED_BUILD_DISPOSITION_QUEUE_AC_to_Cursor_Main_v0_2_Papers_Octonion_HeatKernel_P4_Kappa_Trilogy_P5_Build_Demote_v0_1_S2_OldCorpus_Fold_F1_To_Pedagogical_Populate_Folder_Supersedes_Piecemeal_StallNote_20260623.md'
Write-Output "consolidated_fulfilled=$(Test-InboundHandoffFulfilled $l $cons)"
$p = Scan-AndPromoteMandatoryInbounds -Stream main
Write-Output "scan1 promoted=$($p -join ',')"
$p2 = Scan-AndPromoteMandatoryInbounds -Stream main
Write-Output "scan2 promoted=$($p2 -join ',')"
