# DEPRECATED — use cursor_autonomous_start.ps1 (three streams)
# Kept for backward compatibility: launches ac_jammer stream only.

& (Join-Path $PSScriptRoot 'cursor_autonomous_poll.ps1') -Stream ac_jammer
