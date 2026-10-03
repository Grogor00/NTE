@echo off
REM NTE autonomous poll toggle (Windows CMD)
REM   auto on          — turn ON this chat's stream (see .cursor_autonomous_chat_lane)
REM   auto off         — turn OFF this chat's stream
REM   auto status      — show all streams
REM   auto on main     — explicit: main | ac_jammer | pc_scratch | all
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0auto.ps1" %*
