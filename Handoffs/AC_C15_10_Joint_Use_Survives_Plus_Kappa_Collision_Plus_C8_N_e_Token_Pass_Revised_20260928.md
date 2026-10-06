# AC → Greg: **C15-10** (§5 continuation — survives, with a κ₀ symbol collision) + **C8 N_e relabel revised to a token pass**

**From:** AC (Claude) · **To:** Greg (ratification) · **Cc:** Cursor Main, PC, Scratch, Jammer · **Date:** 2026-09-28
**Responds to:** `Handoffs\Handoff_Cursor_Main_to_AC_C15_Applied_Plus_Joint_Use_Continuation_Plus_C8_Ne_Inventory_20260928.md`
**Status: DRAFT. Nothing patched.**

**C15-1…C15-9 applied, currency OK — acknowledged.** The Door A action no longer reads as load-bearing anywhere in that file.

---

## 1. **C15-10 — the §5 "Joint use" continuation. RULING: the physics survives; one symbol must change.**

**AC's ruling on the conditional itself: it is TRUE and stays.** *"For claiming that V_NTE or K(Φ) is derived from the triple: require Leg 2(B) closed — and that closure must use a non-metric entry of Φ_NTE into D_A (§6.1)"* is a consequence of §6.1's theorem, which survives Door B intact. **AC was right to hold it rather than patch it blind.**

**But two things need saying in it.**

**(a) A symbol collision C8 explicitly warns against.** The text writes the confluence denominator as **κ₀²/12**. **Companion 8 §8 uses κ_cfm for that coefficient and states: *"κ_cfm here is the confluence coefficient — not the dark-matter Hopf coupling κ₀ = 3/√(4π) (Companion 7)."*** C15 §5 commits exactly the conflation C8 flags — **and κ₀ is one of the framework's three empirical handles.** This is a genuine defect independent of Door B.

**(b) The antecedent is no longer a live target.** Under Door B, C8 F3 states that pinning a dynamical off-trajectory V_NTE **is not required**, and frame-level K(Φ) is withdrawn (C15-6). The conditional remains true, but as written it implies these are current objectives.

```
OLD: For claiming that $V_{\mathrm{NTE}}$ or $K(\Phi)$ is *derived* from the triple: require Leg 2(B) closed — and that closure must use a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ (§6.1). Confluence with $V_E(x)=\lambda_0 x^4/(1+(\kappa_0^2/12)x^2)^2$ (Companion 8 §8) is structural form-match only until (B) is computed.
NEW: For claiming that $V_{\mathrm{NTE}}$ or $K(\Phi)$ is *derived* from the triple: require Leg 2(B) closed — and that closure must use a **non-metric** entry of $\Phi_{\mathrm{NTE}}$ into $D_A$ (§6.1). **That requirement stands on §6.1's theorem and is unaffected by Door B; the targets themselves, however, are not live — off-trajectory $V_{\mathrm{NTE}}$ is not required under the identity reading (Companion 8 F3), and frame-level $K(\Phi)$ is withdrawn (§6.4).** Confluence with $V_E(x)=\lambda_0 x^4/(1+(\kappa_{\mathrm{cfm}}^2/12)x^2)^2$ (Companion 8 §8) is structural form-match only, and **historical/audit under Door B**. **Note the symbol: $\kappa_{\mathrm{cfm}}=\sqrt{2}/M_{\mathrm{Pl}}$ is the confluence coefficient, not the dark-matter Hopf coupling $\kappa_0 = 3/\sqrt{4\pi}$ (Companion 7); the two must not be conflated.**
```

**Cursor: after applying, grep C15 for any further bare `\kappa_0` that denotes the confluence coefficient rather than the DM coupling, and report.** AC has read C15 in full and found only this one, but the symbol appears in both roles across the corpus.

---

## 2. **C8 — the three drafted blocks are WITHDRAWN. Replace with a token pass.**

**Eleven hits, all the same quantity, is a relabel — not eight more OLD/NEW blocks.** Drafting eight blocks against LaTeX-dense lines (`N/N_e`, `N_e−N`, `12/N_e²`, `e^{−N_e/3}`) is where byte-exact matching fails, and a partial application would leave the file using **two symbols for one quantity** — worse than the collision it fixes.

**Revised instruction — supersedes item 2 of `AC_Patch_Register_Companion8_Exit_a_Presented_As_Selected_Plus_N_HH_Label_Collision_20260928.md`:**

**Token-replace every occurrence of `N_e` with `N_HH` throughout `Core_Papers\Companion_08_VNTE_Trajectory_v10_19_0.md`.**

**Safety conditions — all must hold, else stop and report:**
1. **Count before = 11**, count after = 11, and **zero remaining `N_e`**.
2. **`N_*` is NOT touched.** §6 equation (7) uses `n_s(N_*) − 1 = −2ε_H(N_*) − ε₂(N_*)` for the **pivot**, which is a different quantity and must stay.
3. **`N_lock` is NOT touched** (distinct token; verify no substring collision).
4. Report the 11 lines verbatim, before and after.

**Then add the definition at first use, §2:**

```
OLD: Upstream of it is the Hartle-Hawking de Sitter sub-phase of roughly N\_HH = −ln(β\_NTE·M\_Pl) ≈ 63.4 e-folds at H ≈ M\_Pl
NEW: Upstream of it is the Hartle-Hawking de Sitter sub-phase of roughly N\_HH = −ln(β\_NTE·M\_Pl) ≈ 63.4 e-folds at H ≈ M\_Pl. **N\_HH is an energy-scale ratio, not the inflationary pivot depth N\_\*; the two are distinct quantities, and their conflation is the origin of the withdrawn native (n\_s, r).**
```

**And the F4 table header, which is the specific locus where the two met:**

```
OLD: n\_s at pivot (N\_HH ≈ 63.4)
NEW: n\_s evaluated at N\_HH ≈ 63.4 (diagnostic only — N\_HH is an energy-scale ratio, not the pivot depth)
```

**Apply the token pass first, then these two blocks** — they are written against the post-relabel text.

**Item 1 of the C8 register — the five exit-(a) loci — is unchanged and stands as drafted.**

---

## 3. Why the relabel still matters after the withdrawal

The observables were withdrawn, which removed the **consequence**. **The label that produced them is still in place**, and C8 is where Scratch identified the anti-re-smuggling anchor.

**A bare "63.4" under the pivot symbol is how this returns** — a future session reads `N_e ≈ 63.4` in a table headed *"n_s at pivot"* and has everything it needs to reconstruct the error from scratch. **The relabel is cheap insurance against exactly that.**

---

— AC, 2026-09-28.
