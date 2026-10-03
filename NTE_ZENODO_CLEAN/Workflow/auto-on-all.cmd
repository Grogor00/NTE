@echo off
cd /d "%~dp0"
start "NTE poll main" /MIN powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_poll.ps1" -Stream main
start "NTE poll ac_jammer" /MIN powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_poll.ps1" -Stream ac_jammer
start "NTE poll pc_scratch" /MIN powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_poll.ps1" -Stream pc_scratch
start "NTE supervisor" /MIN powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_supervisor_poll.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%~dp0.cursor_autonomous_toggle.json'; $t=if(Test-Path $p){Get-Content $p -Raw|ConvertFrom-Json}else{[pscustomobject]@{enabled=$true;streams=@{}}}; $t.enabled=$true; foreach($s in 'main','ac_jammer','pc_scratch','supervisor'){ if(-not $t.streams.$s){$t.streams|Add-Member -NotePropertyName $s -NotePropertyValue ([pscustomobject]@{enabled=$true;tick_minutes=3}) -Force}; $t.streams.$s.enabled=$true; if($s -eq 'ac_jammer'){$t.streams.$s.tick_minutes=5}; if($s -eq 'pc_scratch'){$t.streams.$s.tick_minutes=7}; if($s -eq 'main'){$t.streams.$s.tick_minutes=3}; if($s -eq 'supervisor'){$t.streams.$s.tick_minutes=60} }; [IO.File]::WriteAllText($p, ($t|ConvertTo-Json -Depth 5))"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_execute_tick.ps1" -Stream main
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_execute_tick.ps1" -Stream ac_jammer
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_execute_tick.ps1" -Stream pc_scratch
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0cursor_autonomous_supervisor_tick.ps1"
echo All poll workers + hourly supervisor started (minimized windows). Agent chain via .cursor/hooks.json stop hook.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0auto.ps1" status
