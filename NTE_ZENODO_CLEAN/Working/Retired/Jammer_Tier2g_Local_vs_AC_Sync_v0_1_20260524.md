# Jammer: Tier 2g local vs AC sync v0.1

**Date:** 2026-05-24  
**AC source:** `Master_v10_17_1_Tier2g_Patch_Instructions_R6_LB6_C13_S22_1_20260524.md`  
**Local master:** `NTE_v10_17_Part3` header **v10.17.6**

---

## §1. Patch checklist

| Patch | AC T2g | Local v10.17.6 |
|-------|-------|-----------------|
| T2g-1 §17.5.18 Λ + β_NTE-chain | Required | **Done** (long-form merge 2026-05-24) |
| T2g-2 §17.5.20 $m_{\nu_2}$ row | Required | **Done** (in genuine-test row) |
| T2g-3 §17.5.21 R6 row | Required | **Done** |
| T2g-4 §22.1 partial ν₂ | Required | **Done** + ν₁ bracket + **ν₁ zero-param** (Jammer ahead) |
| T2g-5 §17.5.17 M₂ | Required | **Done** |
| T2g-6 Part 1 LB-6 | Required | **Done** (AC also applied) |
| T2g-7 cross-refs | Required | **Partial** — spot-check §22.18–19 if needed |
| Header v10.17.2 | AC label | Local uses **v10.17.6** (Jammer sprint bundle) |

---

## §2. Optional merge — **T2g-1 long prose DONE** (2026-05-24)

- ~~§17.5.18: 2π² boundary unit cell + promotion path~~ → merged in Part3 v10.17.6  
- Inventory pointer in `COMPANION_CANONICAL_INDEX` → v0.3 (still optional)

**Action:** Greg ratify trilogy → AC ratification handoff.

---

## §3. Jammer additions beyond AC Tier 2g (keep)

- Ghost scan v0.2 PASS  
- P0.10 a–c closed  
- $Y_{\nu_1}$ zero-parameter (v0.1c)  
- Charged-lepton attack route (v0.1d)

---

— Jammer Tier 2g sync v0.1, 2026-05-24.
