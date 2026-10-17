# Cursor Main — standing inbox / monitor protocol

**Date:** 2026-10-18 · **Greg GO:** auto-on-all + monitor for work directed to Cursor Main

## What is monitored

Files under `Handoffs\` whose names or opening lines direct work to **Cursor Main** (patterns: `To:** Cursor`, `→ Cursor Main`, `Cursor Main —`, `apply on GO` with Cursor as apply lane).

## Cadence

Local loop **every 15 minutes** while this chat session is live:
- Scan `Handoffs\` mtimes newer than last scan watermark
- If Cursor-directed → process within fence (Working / apply-only Core on Greg GO)
- Emit tick even if idle (heartbeat)

**Not a 24/7 daemon.** Stops when the chat/loop is stopped. Between sessions, ping “auto on all” or “scan handoffs.”

## Watermark file

`Working/CURSOR_INBOX_LAST_SCAN.txt` — ISO timestamp of last completed scan.

## Fence (unchanged)

- No Core except Greg-ratified apply register  
- Nothing of ours onto foundation map until step 4  
- Refuse “while you’re in there” physics edits  

— Cursor Main
