# CR2 B1 — Adversarial verify (P5 + C13 §4.4)

**Author:** Cursor Scratch  
**Date:** 2026-06-01  
**Queue item:** PS-06 (pc_scratch)  
**Verdict:** **PASS** — B1 patches landed; no blocking gaps routed to Cursor Main

---

## Scope

Adversarial re-read of CR2 B1 patches in:

| Target | Corpus path |
|--------|-------------|
| P5 v0.2 pre-submission | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` (P5; register rename from `Paper_P5_m_nu2_v0_2_*`) |
| Companion 13 §4.4 | `Papers/Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md` |

Cross-check against prior Scratch arithmetic memo (`Working/CR2_B1_Scratch_Arithmetic_Verify_Memo_20260601.md`, PS-02).

---

## Checklist (B1 acceptance criteria)

| Criterion | P5 v0.2 | C13 §4.4 | Notes |
|-----------|---------|----------|-------|
| √Δm²₃₁ comparand ≈ **0.0495 eV**, not 0.074 | ✓ abstract, §5 table, §8 | ✓ §4.4 table | 0.074 appears only as **predicted** m_ν₃, never as observational comparand |
| Solar **0.993×** Tier A (load-bearing leg) | ✓ abstract, §4, §6.1, §8 | ✓ §4.1, §4.4, §7 register, §10 | Tier A scoped to solar leg only |
| Atmospheric **≈1.49×** honest gap | ✓ abstract, §5, §6.1–6.2, §8 | ✓ §4.4, §7, §8 #5, §10 | 0.0738/0.0495 = 1.489× (CR arithmetic) |
| No simultaneous sub-1% two-leg claims | ✓ explicit retraction + "not simultaneous sub-1%" | ✓ "single M_R cannot fit both at sub-1%" | Withdrawn 0.997× atmospheric comparand retracted in both |
| **(8π)^(2/3)** ratio language | ✓ abstract, §5, §6.2 #5, §8 | ✓ §4.4, §8 #5 | m_ν₃/m_ν₂ ≈ 8.57 vs observed ≈ 5.82; gap ≈ 1.47–1.49 |

---

## Arithmetic spot-check (Cursor Scratch)

- √(2.453×10⁻³) ≈ **0.04953 eV** → table rounds 0.0495 ✓  
- m_ν₃/m_ν₂ = 0.0738/0.00860 ≈ **8.57** = (8π)^(2/3) ✓  
- m_ν₃/√Δm²₃₁ ≈ **1.489×** ✓  
- m_ν₂/√Δm²₂₁ ≈ **0.993×** ✓  
- Predicted ratio / observed ratio ≈ 8.57/5.82 ≈ **1.47** ≈ atmospheric overshoot factor ✓

---

## Residual findings (non-blocking)

1. **C13 §1 intro:** "corpus m_ν₃≈0.074 eV check" — rounded prediction label only; §4.4 comparand correct. Cosmetic clarity optional.  
2. **C13 §7 epistemic family:** lists m_ν₃=0.0738 eV alongside "clean Tier A" family — register table (§7) correctly scopes Tier A to solar leg; one-line disambiguation optional.  
3. **Filename:** P5 lives at Solar Neutrino rename path; register documents alias. Not a B1 content gap.

**Route to Cursor Main:** none required for B1 patch verification. Optional cosmetic tidy on C13 §1/§7 at Main discretion.

---

## Conclusion

P5 v0.2 (abstract, §5 cross-check, §6 tier register + falsifier #5, §8 conclusion) and C13 v0.17.2 §4.4 carry consistent CR2 B1 honest-scope language. Prior erroneous √Δm²₃₁ comparand and simultaneous-fit framing are retracted. **PASS** for AC ratification gate on B1 patch landing.

— Cursor Scratch, 2026-06-01.
