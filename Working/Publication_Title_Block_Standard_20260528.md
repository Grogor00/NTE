# Publication Title Block Standard (corpus-wide)

**Date:** 2026-05-28  
**Authority:** Greg directive — center-justified titles for all publications

## Standard

All `Papers/Paper_*.md` publication manuscripts use Pandoc YAML frontmatter:

```yaml
---
title: "Reader-facing title"
author: "G. White"
date: "YYYY-MM-DD (version label only)"
---
```

## Rules

- **Author** is always `G. White` in metadata (not stream names).
- **Date** is reader-facing only (draft/version), e.g. `2026-05-26 (v0.2 pre-submission draft)`.
- **Do not** put internal workflow notes in `date` (no CR-7, ratification, handoff, or cross-paper alignment notes).
- Internal process history belongs in handoffs/working docs, not PDF front matter.

## Applied (2026-05-28)

Tier-1 standalones + major `Papers/Paper_*.md` publication docs normalized to YAML title blocks.

Cursor rule: `.cursor/rules/publication-title-blocks.mdc` (always apply).
