# Handoff — PC → Cursor: Appendix C v1.4, patch A5 (CLFV)

**From:** PC
**To:** Cursor — apply with the A1–A4 set
**Date:** 2026-09-24
**Base file:** `Book\Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md`
**Target:** `Book\Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md`
**Status:** Greg-ratified 2026-09-24. Apply.

---

## Provenance

The original A5 — updating the (n_s, r) row — was **withdrawn** on 2026-09-24 as redundant: v1.3 already carries 0.9692 and 0.0053 and already frames the open item correctly. Flag F1 was raised in error and is retired. This A5 replaces it, and closes flag F2 instead.

## The finding

C.4's charged-lepton-flavour-violation entry gives the amplitude ratio as tan²θ₂₃. The framework's own zero-parameter prediction is θ₂₃ = π/4, at which tan²θ₂₃ is **exactly 1**. So the appendix currently states, in trigonometric dress, that the two channels have equal amplitude — a sharper and more falsifiable claim than the notation lets the reader see. Stating it plainly costs nothing and gains a real prediction; leaving it in the general form makes the framework look more hedged than it is.

## Patch A5 — §C.4, charged-lepton flavour violation

**OLD**

```
**Charged-lepton flavour violation.** A conditional signature of a distinctive kind: if CLFV is ever observed at all, the framework fixes the amplitude ratio between channels — |A(μ→eγ)|²/|A(τ→eγ)|² = tan²θ₂₃ — even though the framework's own heavy scale makes observation unlikely. An almost-certainly-untestable prediction stated anyway, because stating it costs nothing and a surprise observation would score it.
```

**NEW**

```
**Charged-lepton flavour violation.** A conditional signature of a distinctive kind: if CLFV is ever observed at all, the framework fixes the amplitude ratio between channels — |A(μ→eγ)|²/|A(τ→eγ)|² = tan²θ₂₃ — even though the framework's own heavy scale makes observation unlikely. It is worth writing that ratio out, because the trigonometry disguises how sharp it is. The framework does not leave θ₂₃ free: it predicts exactly π/4, at which tan²θ₂₃ is exactly 1. So the claim is that the two channels come with *equal* amplitude, and any observed inequality between them falsifies either the maximal atmospheric angle or the structure that carries it into the flavour sector. An almost-certainly-untestable prediction, stated plainly rather than in disguise, because stating it costs nothing and a surprise observation would score it.
```

---

## Registration (discipline 10)

Amends the Appendix C v1.4 entry in `NTE_Workflow_Manifest_v10_18.md` §10:

```
- **Book/ Appendix C v1.4 patch set** — A1–A4 (2026-09-24) plus **A5 (CLFV tan²θ₂₃ = 1 stated plainly)**, Greg-ratified 2026-09-24. The originally proposed A5 on the (n_s, r) row was withdrawn as redundant; flag F1 retired as raised in error (v1.3 already current). F2 closed by A5.
```
