# Cursor Main — Sequencing GB vs Inflation: numerics + F1 cold read

**Author:** Cursor Main  
**Date:** 2026-09-25  
**Directive:** `Handoffs/Directive_AC_to_ALL_Sequencing_Contradiction_GaugeBirth_vs_Inflation_Sunshine_RabbitHole_20260925.md`  
**Register:** open question. **Nothing patched.**

---

## Fork declared before results

**Working fork (pre-compute):** **F6 leaning F2**, with **F5 live as corpus self-warning**.

Rationale before numerics: Companion 9 §1 places Lorentzian continuation (= inflationary trajectory) at the equator whose geometric signature is the gauge-birth kink; Part 2 §8.2 excludes inflaton decay and identifies T_GB as the hot Big Bang. That combination is the reheating gap (F2), unless a commitment not yet made separates the counters (F6 / Book Ch 7 three-counters caution). F5 remains open because Part 2 §8.1 already calls Euclidean slow-roll artefactual.

**Not chosen a priori:** F1 as “ordering already stated and consistent” — that is checked, not assumed.

---

## Read set (discipline 11)

| File | Scope read |
|------|------------|
| Part 2 §VIII (esp. 8.1–8.3) | Full section this session |
| Companion 9 §1, §4–§7 | Full this session |
| Companion 17 §3 | Full this session |
| Part 3 accounting / falsifiability item 5 | Grep + relevant blocks |
| Companion 1, 3, 4, 11, 14, 16, 19, 20 | Grep for inflation/reheat/GB ordering |
| Book Ch 7 v5 (three counters) | Relevant paragraphs |
| Book App C / Ch 12 / Ch 15 | Grep T_GB / reheat |
| Prior ItemA register memos | Context only — not used as deposit |

**Terms searched:** `gauge birth`, `inflation`, `reheat`, `inflaton`, `T_GB`, `N_lock`, `signature`, `equator`, `ordering`, `N_HH`, `N_*`, `N_total`.

**Grok independent read:** **not executed this session** (no Grok tool in Cursor lane). Cold read below is Cursor Main’s own, deliberately without importing AC’s four-statement framing into the question asked of the three sources — then compared.

---

## F1 result

**No file AC listed as unread supplies an explicit, consistent single-timeline ordering that closes the reheating gap.**

- **Companions 1, 3, 4, 11, 14, 16, 19, 20:** no statement of GB-before/after-inflation that places T_GB, plateau e-folds, and reheating together.
- **Companion 9 §1 (deposit):** HH saddle’s Lorentzian continuation “gives the inflationary trajectory”; equator = Euclidean→Lorentzian = “signature change whose geometric signature is the C¹ kink at gauge birth”; also “gauge birth occurs after [HH sub-phase] ends.”
- **Book Ch 7:** **three counters, three jobs** — N_lock ≈ 0.1 is *span of locking*, *not* depth on the inflationary counter; total run ∼140; inflationary counter is horizon-exit depth. This is a **commitment-shaped warning**, not a resolved timeline.

**F1 does not dissolve the contradiction.** At best it licenses F6 (“undetermined without a further commitment”) while the four deposited physics claims still co-imply F2’s reheating gap if read onto one axis.

---

## Cold read of Part 2 §VIII + C9 §1 + C17 §3 (Grok substitute)

**Question asked of the three texts alone:** in what order do these place gauge birth and inflation, and is the sequence physically consistent?

**Answer from the texts:**
1. Gauge birth **is** the Euclidean→Lorentzian signature change (Part 2 §8.1; C9 §1 equator kink).
2. After that change, Lorentzian continuation **is** the inflationary trajectory (C9 §1).
3. At gauge birth, reorganisation energy **is** the hot Big Bang at T_GB ∼ 0.4 M_Pl, **not** inflaton decay (Part 2 §8.2–8.3).
4. (n_s, r) are evaluated on an α=2 plateau map at N_e = 63.4 / alternate 55, with **explicit Euclidean-section caveat** (C17 §3; Part 2 §8.1; Part 3).

**Physical consistency on one timeline:** **No.** Hot Big Bang at lock + subsequent ∼56 e-folds of inflation ⇒ plasma diluted; inflaton decay forbidden ⇒ **no deposited post-inflation reheating**. Alternate (GB after inflation) fails T_GB ≫ max reheat from V_* (numerics below). **The contradiction is real on the deposit, not an artefact of AC’s framing.**

---

## Numerics (Python; Wolfram not required for these closed-form bounds)

### (i) Max reheat for V_*^{1/4} ≈ 9 × 10¹⁵ GeV

| Convention | Value |
|------------|-------|
| Instantaneous upper envelope T_reh ≲ V_*^{1/4} | **9.0 × 10¹⁵ GeV** |
| Radiation conversion T ≈ V^{1/4} (30/(π² g_*))^{1/4}, g_*=106.75 | **≈ 3.70 × 10¹⁵ GeV** |
| T_GB = 0.4 M_Pl (non-reduced, M_Pl = 1.221 × 10¹⁹ GeV) | **4.88 × 10¹⁸ GeV** |
| T_GB = 0.4 M_Pl (reduced, M_Pl = 2.435 × 10¹⁸ GeV) | **9.74 × 10¹⁷ GeV** |
| Ratio T_GB / V^{1/4} (non-reduced) | **≈ 5.4 × 10²** |
| Ratio T_GB / V^{1/4} (reduced) | **≈ 1.1 × 10²** |

**F3 quantitative:** T_GB exceeds inflaton-scale max reheat by **∼10²–10³**, matching AC’s statement.

### (ii) Dilution of T ∼ 0.4 M_Pl through 56 e-folds

Assuming radiation-like T ∝ a⁻¹ = e^{−N} (illustrative; makes “inflated away” quantitative):

| Quantity | Value |
|----------|-------|
| Dilution factor e^{−56} | **4.78 × 10⁻²⁵** |
| T_residual from T_0 = 0.4 M_Pl (non-reduced) | **≈ 2.3 × 10⁻⁶ GeV ≈ 2.3 keV** |
| T_residual (reduced Planck) | **≈ 4.7 × 10⁻⁷ GeV ≈ 0.47 keV** |
| T_CMB | ∼ 2.3 × 10⁻¹³ GeV |

Residual after 56 e-folds is **∼10⁷ × T_CMB** if nothing else happens — still **∼10¹⁵ below T_GB**, and **far below any BBN-useful reheat** if one needed a post-inflation hot phase from that diluted plasma alone. The hot Big Bang *as deposited at lock* does not survive as the post-inflation thermal bath.

### (iii) E-fold budget (four counters)

| Counter | Deposit / directive value | Role |
|---------|---------------------------|------|
| N_lock | ≈ 0.1 | Locking **span** (Ch 7) / Part 2 lock label |
| N_HH | ≈ 63.4 | HH / slow-roll depth used in C17 |
| N_* | ≲ 55.9 | Horizon-matched pivot ceiling (Item A register) |
| N_total | ≈ 140 | Total run (Part 1 / Ch 7) |

Arithmetic:
- N_HH + N_* ≈ 63.4 + 55.9 = **119.3** < 140 → **∼20.7 e-folds** remain for post-inflationary + other budget if both N_HH and N_* are sequential Lorentzian depths after the same zero.
- N_lock ≈ 0.1 **cannot** sit on the same axis as N_HH ≈ 63.4 without Ch 7’s three-counter split; treating them as one N falsifies the Book’s own caution.

**Consistency:** N_total ≈ 140 is **not self-contradictory** as a sum of unlike counters, but **is under-specified** as a single timeline. Placing all four on one axis without new commitments fails.

---

## Verdict (Cursor Main lane only)

| Question | Answer |
|----------|--------|
| Is AC’s contradiction real? | **Yes** (cold read agrees) |
| F1 save? | **No** |
| Preferred fork after numerics | **F2** as deposit-implied, with **F6** as the honest “what would settle it,” and **F5** as live withdrawal risk for (n_s, r) |
| Reheating other than GB / inflaton decay? | **None found** in read set (Jammer lane owns exhaustive attack) |
| Patch? | **None** |

**Withdrawal-permitted outcomes named for AC arbitration (not applied):**
- Withdraw “T_GB *is* the hot Big Bang” and/or “not inflaton decay”
- Withdraw or demote inflationary observables if F5 is forced
- Or add an explicit post-inflation reheating commitment (new physics — not in deposit)

---

— Cursor Main, 2026-09-25.
