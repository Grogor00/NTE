# Start all enabled NTE Cursor autonomous streams
& (Join-Path $PSScriptRoot 'cursor_autonomous_toggle.ps1') -Stream all -On
