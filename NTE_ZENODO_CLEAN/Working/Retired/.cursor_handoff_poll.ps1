$stateFile = "C:\Users\gregw\Desktop\NTE_ZENODO_CLEAN\Working\.cursor_handoff_watch_state.json"
$handoffs = "C:\Users\gregw\Desktop\NTE_ZENODO_CLEAN\Handoffs"
$working = "C:\Users\gregw\Desktop\NTE_ZENODO_CLEAN\Working"
while ($true) {
  Start-Sleep -Seconds 300
  $new = @()
  foreach ($dir in @($handoffs, $working)) {
    Get-ChildItem $dir -Filter "*.md" -ErrorAction SilentlyContinue | ForEach-Object {
      if ($_.Name -notlike "WITHDRAWN_*") { $new += "$($_.Name)|$($_.LastWriteTime.ToString('o'))" }
    }
  }
  $payload = ($new | Sort-Object) -join ";"
  Write-Output "AGENT_LOOP_TICK_handoffs {`"prompt`":`"AFK poll: check Handoffs/ and Working/ for new or updated .md since last pass. Read AC-to-Cursor handoffs first. Update .cursor_handoff_watch_state.json. File completion handoffs to Handoffs/.`",`"inventory`":`"$payload`"}"
}
