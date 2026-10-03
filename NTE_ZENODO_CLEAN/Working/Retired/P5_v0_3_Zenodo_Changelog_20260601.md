# P5 v0.3 — Zenodo changelog (CR2 B1)

**Author:** Cursor PC  
**Date:** 2026-06-01  
**Queue item:** PS-07 (pc_scratch)  
**Zenodo file:** `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md`  
**Prior:** `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` (2026-05-26 arxiv pre-submission draft)  
**Upload:** **Greg only** — Cursor did not upload to Zenodo.

---

## Summary

v0.3 is a **release snapshot** for Greg's Zenodo deposit. Substantive neutrino-honesty edits were applied during CR2 Wave 1 (B1) and adversarial-verified in PS-06 (`Working/CR2_B1_Cursor_Scratch_Verify_Memo_20260601.md`, **PASS**). v0.3 packages that corpus state under an explicit version stamp and this changelog.

---

## CR2 B1 patches (content delta vs pre-B1 standalone wording)

### 1. √Δm²₃₁ comparand correction

| Item | Before (retracted) | After (v0.3) |
|------|-------------------|--------------|
| Atmospheric observational scale | Mis-cited ≈ **0.074 eV** (conflated with Σm_ν / predicted m_ν₃ label) | **√Δm²₃₁ ≈ 0.0495 eV** (PDG 2024 Δm²₃₁ = 2.453×10⁻³ eV²; NuFIT 5.3 NO) |
| Locations | — | Abstract; §5 table; §8 conclusion |

**Source:** `Working/CR2_B1_PMNS_MR_Seesaw_Convention_Verdict_Claude_Jammer_20260601.md` §1.2–1.3; Scratch arithmetic memo PS-02.

### 2. Solar leg — Tier A (0.993×)

- **Prediction:** m_ν₂ = 0.00860 eV from (8π)^(−2/3) v²/M_R.  
- **Comparand:** √Δm²₂₁ = 0.00866 eV → **0.993×** (load-bearing Tier A test).  
- **Scope:** Not fitted to Δm²₂₁; no β_NTE-chain input in solar derivation.  
- **Locations:** Abstract; §4; §6.1; §8.

### 3. Atmospheric leg — honest gap (≈1.49×)

- **Same single M_R:** m_ν₃ = 0.0738 eV vs √Δm²₃₁ ≈ 0.0495 eV → **≈1.49×** (master corpus §19.2 “within factor 1.5”).  
- **Retracted:** Prior **0.997×** atmospheric match (artifact of wrong comparand).  
- **Explicit:** **Not** simultaneous sub-1% two-leg fit.  
- **Locations:** Abstract; §5; §6.1–6.2; §8.

### 4. Structural mass-ratio — (8π)^(2/3)

- **Predicted:** m_ν₃/m_ν₂ = (8π)^(2/3) ≈ **8.57**.  
- **Observed ratio:** √(Δm²₃₁/Δm²₂₁) ≈ **5.82** (≈5.72–5.82 in memos).  
- **Implication:** Single M_R anchors solar at 0.993× but forces atmospheric off by ≈8.57/5.82 ≈ **1.47–1.49**.  
- **Locations:** Abstract; §5; §6.2 falsifier #5; §8.

### 5. Falsifier / tier-register updates

| Change | Detail |
|--------|--------|
| Tier A scope | **Solar leg only**; atmospheric leg open, not Tier A simultaneous-fit |
| Falsifier #5 | Replaces withdrawn simultaneous sub-1% claim → **mass-ratio coherence** test |
| §6.2 #5 | Precision data on √(Δm²₃₁/Δm²₂₁) vs (8π)^(2/3) while holding solar prediction |
| Honest-scope tag | **CR2 / B1, 2026-06-01** in abstract and cross-check sections |

---

## Files touched (PS-07)

| Action | Path |
|--------|------|
| Created | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` |
| Changelog | `Working/P5_v0_3_Zenodo_Changelog_20260601.md` (this file) |
| Unchanged baseline | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` (arxiv-era filename retained) |

---

## Greg Zenodo checklist (handoff)

1. Deposit **`Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md`** (or rendered PDF from same source).  
2. Attach or cite this changelog in Zenodo version notes.  
3. Register alias: P5 / Programme S solar Yukawa duality paper (see `NTE_Standalone_Papers_Register`).  
4. Companion C13 §4.4 is corpus-aligned (PS-06 PASS); optional cosmetic on C13 §1/§7 not blocking upload.

— Cursor PC, 2026-06-01.
