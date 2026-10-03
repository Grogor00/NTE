# Handoff — Cursor Main → AC: **C15 C15-1…C15-9 applied** (Joint-use continuation held); **§5 continuation verbatim**; **C8 `N_e` inventory**; **C8/C17 flagged sentences**.

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**GO:** `Handoffs\Handoff_AC_to_Cursor_GO_Companion15_All_Nine_Plus_Next_Four_Companions_20260928.md` (Greg ratified 19:44 NZDT).
**Registers:** C15 base + ADDENDUM C15-6…C15-9. C8 register remains **DRAFT — not applied**.

---

## 1. Companion 15 — apply results

**Target:** `Core_Papers\Companion_15_EPhi_Farnsworth_Spectral_Data_v10_19_0.md`

| Patch | Result |
|-------|--------|
| **C15-1** subtitle | **MATCH → APPLIED** |
| **C15-2** Door B banner insert | **APPLIED** (after corpus line) |
| **C15-3** §3.3(A) heading + prose | **MATCH → APPLIED** (both blocks) |
| **C15-4** §6.2 Companion 17 clause | **MATCH → APPLIED** |
| **C15-5** §7 Companion 9 row | **MATCH → APPLIED** |
| **C15-6** §6.4 item 1 closing | **MATCH → APPLIED** |
| **C15-7** abstract ¶1 + ¶3 | **MATCH → APPLIED** (K(Φ)-pin clause cut) |
| **C15-8** §1 framing (2) + blurb | **MATCH → APPLIED** |
| **C15-9** Leg 1 heading + Joint-use **opening** | **MATCH → APPLIED** |
| **C15-9** Joint-use **continuation** | **HELD — reported below; not patched** |

**Untouched (per GO):** §6.1, §6.3, §4.

**Render:** `paper-build\pdf-out\Companion_15_EPhi_Farnsworth_Spectral_Data_v10_19_0.pdf` — PASS; md 19:48:53 → pdf 19:49:31 NZDT; 67 903 B. **0 PDFs in `Core_Papers\`.**

---

## 2. §5 “Joint use” continuation — **verbatim (owed locus)**

**Applied opening (now on disk):**

> **Joint use (historical).** For saddle / trajectory analysis the constrained action was Leg 1; under Door B no such constrained saddle exists, and the origin sector is open (Part 3).

**Continuation — unchanged, byte-exact as found (and still on disk after the opening patch):**

> For claiming that $V_{\mathrm{NTE}}$ or $K(\Phi)$ is *derived* from the triple: require Leg 2(B) closed — and that closure must use a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ (§6.1). Confluence with $V_E(x)=\lambda_0 x^4/(1+(\kappa_0^2/12)x^2)^2$ (Companion 8 §8) is structural form-match only until (B) is computed.

**Full §5 Joint-use paragraph as now printed** (opening patched + continuation held):

```
**Joint use (historical).** For saddle / trajectory analysis the constrained action was Leg 1; under Door B no such constrained saddle exists, and the origin sector is open (Part 3). For claiming that $V_{\mathrm{NTE}}$ or $K(\Phi)$ is *derived* from the triple: require Leg 2(B) closed — and that closure must use a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ (§6.1). Confluence with $V_E(x)=\lambda_0 x^4/(1+(\kappa_0^2/12)x^2)^2$ (Companion 8 §8) is structural form-match only until (B) is computed.
```

**Cursor note (not a draft):** the continuation is a conditional on Leg 2(B) / non-metric entry / confluence form-match. It does **not** assert a live constrained Leg-1 saddle. AC to rule survive-as-written vs further edit.

---

## 3. Companion 8 — further `N_e` inventory (register Item 2 request)

**File:** `Core_Papers\Companion_08_VNTE_Trajectory_v10_19_0.md`  
**Status:** report only — C8 register still DRAFT; **nothing patched**.

AC extracted three. **All further live `N_e` hits below** (same 63.4 / HH-sub-phase quantity unless noted):

| # | Locus | Verbatim / context |
|---|-------|-------------------|
| 1 | §2 (AC drafted) | `N_e = −ln(β_NTE·M_Pl) ≈ 63.4` |
| 2 | §2 (AC drafted) | `energy-scale ratio N_e ≈ 63.4` |
| 3 | §6 F4 table header (AC drafted) | `n_s at pivot (N_e ≈ 63.4)` |
| 4 | §6 F4 body | `N = N_e at the Janus point, H → 0` |
| 5 | §6 F4 body | `H(0) ≈ M_Pl and H(N_e) → 0` |
| 6 | §6 F4 table rows | `N/N_e` (P2, P3); `N_e−N` (P4) |
| 7 | §6 F4 finding | `r = 12/N_e² ≈ 0.003` |
| 8 | F5 banner / §1 F5 | `M₁ ≈ M_Pl·e^{−N_e/3}` |
| 9 | §7 F5 body | `M₁ ≈ M_Pl·e^{−N_e/3} ≈ 1.8 × 10⁹ GeV` |
| 10 | §7 F5 table header | `H(N = N_e/3)/M_Pl` ; `matches M_Pl·e^{−N_e/3}?` |
| 11 | §7 F5 table / finding | `e^{−N_e/3}` ; `H(N_e/3)` ; `M_Pl·e^{−N_e/3}` |

**Reading for AC:** every hit above names the **HH energy-scale / sub-phase length** (~63.4), not a separately defined inflationary pivot $N_*$. The table header *“n_s at pivot (N_e ≈ 63.4)”* is the explicit collision. Relabel package should cover **§2 + F4 table/body + F5/§7** consistently as `N_HH` (AC’s three drafts are the seed; items 4–11 still need AC blocks before apply).

**Not applied.** Awaiting C8 GO + AC drafts for the further loci.

---

## 4. Parallel request — C8 / C17 flagged sentences (verbatim)

### C8 — exit (a) presented as selected (five loci; matches AC Item 1)

1. **Banner:** `early acceleration is exit (a) (credited SM Higgs), not \(\Phi_{\mathrm{NTE}}\).`
2. **§1:** `Deriving a dynamical V_NTE … is **not** a live Door B target; early acceleration is exit (a).`
3. **§6 / F4:** `the spectrum register is **imported exit (a)** (Companion 9).`
4. **§9:** `Companion 9 restores GR and withdraws μ / F(Φ)R; exit (a) supplies credited SM Higgs inflation.`
5. **Summary:** `imported exit-(a) Higgs-inflation numbers cover the spectrum register (F4 status amended).`

### C17 — C9 eq. (1) + exit (a) (body still keyed after banner)

1. **Banner / Door B regrade:** `Early-universe spectrum, if any, is imported under **exit (a)** (SM Higgs \(\xi_H\gg1\), credited) — not from this companion.`
2. **§1 heading:** `## 1. Input: Companion 9 eq. (1)`
3. **§1 body opens on the withdrawn action:** `F(\Phi)=M_{\mathrm{Pl}}^{2}+\Phi^{2}/6`, `\xi=1/6`, curvature sector `\tfrac{1}{2} F(\Phi)\,R` — framed as historical in Scope, but §1 still titles it as live “Input.”
4. **§3:** conditional `(n_s,r)` at `N_e=63.4` / `N_e=55` (same symbol collision as C8).
5. **§4 table / Refs:** `Source action eq.~(1)`; `Companion 9 — action (1), saddle addendum.`

C17 banner correctly withdraws the object; the **body still organises around C9 eq. (1) and exit-(a) import** as the spectrum path.

---

## 5. Standing

- **C15:** applied set complete except AC ruling on Joint-use continuation.
- **C8:** register DRAFT; `N_e` inventory above; exit-(a) loci confirmed; **await GO**.
- **Next per AC:** C17 / C12 / C16·C14 registers from reads — no Cursor apply until filed + GO.

— Cursor Main, 2026-09-28.
