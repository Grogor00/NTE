# Corpus path lock (2026-09-26) - Cursor Main

Greg correction: **OneDrive is not used for this project.**
Canonical root is only: `G:\My Drive\NTE_ZENODO_CLEAN`.

## Applied
- `Resolve-NteRoots.ps1` hard-locks to Drive; no OneDrive/Desktop corpus candidates.
- `auto.ps1` / `cursor_autonomous_toggle.ps1` launch workers from `G:\...\Workflow` only.
- Poll workers restarted with G: paths on the command line.
- Cursor rule `nte-canonical-corpus-path.mdc` updated: do not use/repair OneDrive for NTE.

Prior note about "repairing OneDrive junctions" is superseded - do not pursue OneDrive fixes.

- Cursor Main, 2026-09-26.