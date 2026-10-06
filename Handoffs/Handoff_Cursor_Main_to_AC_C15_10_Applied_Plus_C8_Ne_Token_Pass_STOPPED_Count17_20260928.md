# Handoff — Cursor Main → AC: **C15-10 applied**; **C8 N_e token pass STOPPED** (count ≠ 11).

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**Source:** `Handoffs\AC_C15_10_Joint_Use_Survives_Plus_Kappa_Collision_Plus_C8_N_e_Token_Pass_Revised_20260928.md` (Greg: two rulings).
**C8 Item 1 (exit-(a)):** not in this apply set — still DRAFT.

---

## 1. C15-10 — APPLIED

**OLD matched byte-exact → NEW on disk.**

Physics conditional retained; Door B non-liveness note added; confluence denominator now `\kappa_{\mathrm{cfm}}`; explicit κ₀ ≠ κ_cfm note added.

**Render:** `paper-build\pdf-out\Companion_15_EPhi_Farnsworth_Spectral_Data_v10_19_0.pdf` — PASS; md 19:53:20 → pdf 19:53:39 NZDT; 69 357 B. **0 PDFs in `Core_Papers\`.**

### Post-apply κ₀ grep (as requested)

| Hit | Role |
|-----|------|
| §5 Joint-use note (NEW text) | **DM Hopf coupling** $\kappa_0 = 3/\sqrt{4\pi}$ — intentional, correct |
| *(no other)* | — |

**Zero remaining bare `\kappa_0` used as the confluence coefficient.** AC’s single-locus read confirmed. `\kappa_{\mathrm{cfm}}` appears twice in the patched sentence (formula + gloss).

---

## 2. C8 N_e → N_HH token pass — **STOPPED (safety condition 1)**

**Required:** count before = **11**, after = 11, zero remaining `N_e`.

**Observed on disk (pre-pass; file untouched):**

| Metric | Value |
|--------|-------|
| `N_e` **token** count | **17** (≠ 11) |
| Lines containing `N_e` | **13** (≠ 11) |
| `N_*` count | **3** (all on L114 eq. (7) — pivot; must stay) |
| `N_lock` count | **12** (distinct; no substring collision with `N_e`) |

**Nothing replaced.** A partial or force-17 pass without AC updating the checksum would violate condition 1 as written.

**Likely cause:** Cursor’s prior inventory listed **11 loci/rows**, collapsing multi-token lines; AC locked the safety checksum to that undercount. True token inventory is 17.

### Verbatim lines containing `N_e` (before; for AC’s revised pass)

**L34** (1×): `M_Pl·e^{−N_e/3}`

**L64** (2×): `roughly N_e = −ln(β_NTE·M_Pl) ≈ 63.4` … `energy-scale ratio N_e ≈ 63.4`

**L112** (1×): `N = N_e at the Janus point`

**L116** (1×): `H(N_e) → 0`

**L118** (1×): `n_s at pivot (N_e ≈ 63.4)`

**L122** (1×): `N/N_e`

**L123** (1×): `N/N_e`

**L124** (1×): `(N_e−N)`

**L128** (1×): `r = 12/N_e² ≈ 0.003`

**L134** (1×): `M_Pl·e^{−N_e/3}`

**L136** (2×): `H(N = N_e/3)` ; `M_Pl·e^{−N_e/3}`

**L139** (1×): `e^{−N_e/3}`

**L144** (3×): `H(N_e/3)` ; `M_Pl·e^{−N_e/3}` ; `M_Pl·e^{−N_e/3}`

### Pivot / lock intact (pre-pass verification)

**L114 eq. (7) — MUST NOT be touched by any relabel:**
```
  n_s(N_*) − 1 = −2ε_H(N_*) − ε₂(N_*).    (7)
```
`N_lock` occurrences are separate tokens; a literal `N_e`→`N_HH` replace does not collide with them.

### Proposed checksum for AC’s re-issue

```
Count before = 17, count after = 17, zero remaining N_e.
N_* unchanged (= 3 on L114).
N_lock unchanged (= 12).
Then apply the two post-relabel prose blocks (§2 definition; F4 table header).
```

**Post-relabel blocks not applied** (token pass did not run).

---

## 3. Standing

- **C15:** C15-1…C15-10 complete.
- **C8 Item 2:** await AC checksum revision (11 → 17) + GO.
- **C8 Item 1** (exit-(a) five loci): still DRAFT, untouched.

— Cursor Main, 2026-09-28.
