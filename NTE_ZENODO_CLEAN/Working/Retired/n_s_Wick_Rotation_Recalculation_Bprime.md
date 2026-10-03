# (B′) n_s Recalculation under F2 Wick-Rotation Reading — §17.5.14 Investigation

**From:** Jammer
**To:** AC (audit; integrate §17.5.14 status update at v10.7 or v10.8 if findings authorised), Greg (record), CR (visibility — pre-ship pass at next ship)
**Re:** §17.5.14 Hartle-Hawking slow-roll formula import; v10.6's status update flagged that F2 (Wick-rotation reading at §VIII.1.4) sharpens the formula-import question rather than resolves it. (B′) is the substantive investigation.
**Corpus baseline:** v10.6 SHIPPED (canonical 2026-05-03)
**Status:** Jammer R&D worksheet. **Surfaces a substantive sharpening of §17.5.14 — the imported formula is in deeper tension with NTE's actual dynamics than v10.6 currently states, under each of the natural readings of "pre-temporal phase."** Recommendation: §17.5.14 status update for v10.7+ to qualify the n_s = 0.9685 prediction's epistemic status more directly.

---

## 0. Headline

**Finding (B′):** Under each of three natural readings of NTE's pre-temporal phase, the imported Starobinsky formula n_s = 1 − 2/N_e is not justified by the framework's actual dynamics. Naïve application of standard slow-roll machinery to NTE's profiles either:

- **R1 (Stage 3 linear pre-temporal profile, |Φ|² = AN over y ∈ (0, N_lock = 0.1)):** ε_H = −1/N is "phantom-like" and at midpoint reaches |ε_H| ≈ 20 — far outside slow-roll regime; standard formula does not apply at all.
- **R2 (pure de Sitter Hartle-Hawking phase with H ≈ const over 63.4 e-folds):** ε_H ≈ 0 throughout; pure de Sitter gives scale-invariant spectrum n_s ≈ 1 (not n_s = 0.9685). 8σ from observed.
- **R3 (Hartle-Hawking phase with H decreasing from M_Pl to H_GB over 63.4 e-folds):** average ε_H = +1; formula again outside slow-roll regime.

**No reading recovers n_s = 0.9685 from NTE's own dynamics naïvely.** The corpus's claimed match (0.85σ from Planck observation) relies on borrowing Starobinsky's formula whose specific dynamics (R²-inflation; ε_V ~ 1/N², η_V ~ −2/N) do not match NTE's pre-temporal Hartle-Hawking phase under any of R1, R2, R3.

**Key implication:** §17.5.14 should be substantially sharpened in v10.7+. The "0.85σ match" should be qualified as:

> *0.85σ match contingent on the imported Starobinsky formula's applicability to NTE's pre-temporal Hartle-Hawking dynamics, which is unverified and apparently in tension with the framework's actual pre-temporal dynamics in each available reading. The match is real (the formula numerically gives n_s = 0.9685 vs Planck 0.9649 ± 0.0042) but the formula's derivation in NTE's regime is open work; until completed, the magnitude and even sign of the spectral tilt are not derived from NTE's own structure.*

This is not a refutation of the n_s prediction — it is an honest qualification of what the framework currently has and what remains to be done. The framework's strongest empirical match in v10.6's current presentation may be carrying more rhetorical weight than its derivation supports.

**Secondary finding:** Corpus-internal ambiguity surfaced. §18.2 implies pre-temporal phase is 63.4 e-folds (H_HH ~ M_Pl down to H_GB); §18.5 + Stage 3 (Appendix E.3) imply pre-temporal phase is N_lock ~ 0.1 e-folds (with |Φ| growing from 0 to M_Pl). These are not reconciled in v10.6. Most plausible reconciliation: 63.3 e-folds of approximate Hartle-Hawking de Sitter phase (Reading R2) followed by 0.1 e-folds of locking transition (Reading R1, where Stage 3 + F2 apply). But the corpus does not state this explicitly. **§17.5 should also gain a new entry on this N-parameter ambiguity** — what Stage 3's y ∈ (0, 0.1) parameterises vs what §18's N_e = 63.4 counts.

---

## 1. Scope and method

### 1.1 What this investigation covers

(B′) is the §17.5.14 investigation flagged in v10.6's status update note: *"the n_s formula's applicability depends on whether N_e is computed entirely in the post-locking Lorentzian regime, or whether it includes pre-locking Euclidean e-folds. Verifying this is now a more pressing research target given the explicit Wick-rotation framing."*

Specifically: I trace what the formula n_s = 1 − 2/N_e requires, what NTE's actual pre-temporal dynamics provide, and where the gap lies. I do not perform the full Hartle-Hawking calculation in NTE's regime (that is a significantly larger R&D arc, a candidate for inclusion in the (D′) V_NTE Stage 2 companion paper or as a separate Stage). What (B′) establishes is the *gap's structural nature and magnitude*.

### 1.2 Method

1. Mine corpus state on n_s, N_e, pre-temporal profile, and slow-roll usage (§2 below).
2. Identify the corpus-internal ambiguity about what "pre-temporal phase" parameterises (§3).
3. Enumerate three natural readings of NTE's pre-temporal phase that bear on n_s (§4).
4. Apply standard slow-roll machinery to each reading; record what naïve result emerges (§5).
5. Compare with the imported Starobinsky derivation's actual requirements (§6).
6. Identify what a proper NTE-specific Hartle-Hawking calculation would need (§7).
7. Recommend §17.5.14 sharpening for v10.7+ (§8).

### 1.3 What this investigation does NOT do

- Does not perform the full Hartle-Hawking calculation in NTE's pre-temporal section (substantial separate R&D).
- Does not propose a replacement formula for n_s.
- Does not refute the prediction n_s = 0.9685 — the formula numerically gives this value; what is in question is whether NTE has derived the formula from its own dynamics or imported it.

---

## 2. Corpus state (mining)

### 2.1 The current n_s prediction structure

§2.4.3 (line 302–310): *"The pre-temporal Hartle-Hawking phase generates an effective e-fold count N_e = −ln(β_NTE·M_Pl) = 63.4 (Section XVIII), giving n_s = 1 − 2/N_e = 0.9685. The observable n_s did not enter the characterisation of β_NTE; it tests the framework on a separate observable that the construction did not touch."*

§18.3 (line 1227): *"Using n_s = 1 − 2/N_e (Starobinsky / large-ξ framework): n_s = 1 − 2/63.4 = 0.9685"*

§18.4 (line 1237): *"r = 12/N_e² = 12/63.4² = 0.0030"*

The two formulas n_s = 1 − 2/N_e and r = 12/N_e² are both standard Starobinsky / R²-inflation results. The corpus imports them.

### 2.2 §18.2 reading: N_e from energy-scale ratio

§18.2: *"CMB perturbations in NTE are generated in the pre-temporal Hartle-Hawking epoch — the Euclidean section at N < N_lock. For the natural Planck-scale Hartle-Hawking instanton, H_HH ~ M_Pl. The pre-temporal epoch spans from Planck-scale de Sitter (H ~ M_Pl) down to H_GB = β_NTE·M_Pl². The number of e-folds: N_e = ln(M_Pl / H_GB) = ln(1/(β_NTE·M_Pl)) = −ln(β_NTE·M_Pl) = 63.4 e-folds"*

This computes N_e as the log-ratio of two energy scales (Planck-scale Hartle-Hawking start to gauge-birth end). Under this reading, "pre-temporal phase" = 63.4 e-folds.

### 2.3 §18.5 reading: |Φ| growth over N_lock

§18.5: *"Near the Janus point (N → 0), CPN symmetry requires |Φ| → 0 (the boundary field vanishes at the conformal interface). The field grows from 0 to M_Pl over N_lock ~ 0.1 e-folds, during which H = β_NTE|Φ|² grows from 0 to H_GB."*

This says |Φ| grows from 0 to M_Pl over 0.1 e-folds — gauge birth value of |Φ| is M_Pl. With H = β_NTE|Φ|², gauge birth H = β_NTE·M_Pl² = 3.5 × 10⁻⁹ GeV (= H_GB).

Under this reading, "pre-temporal phase" = 0.1 e-folds (the locking transition), with H rising from 0 to H_GB over those 0.1 e-folds — opposite direction from §18.2's H decrease.

### 2.4 Stage 3 reading: pre-temporal trajectory in surface ontology

Appendix E.3: *"Stage 3 extends the trajectory to y ∈ (0, N_lock) by choosing a pre-temporal profile family and integrating from the gauge-birth boundary condition z(N_lock) = π/2. ... Under the linear pre-temporal profile |Φ_pre|²(y) = (Φ₀²·e^(−N_lock)/N_lock)·y (uniquely determined by continuity at N_lock), the trajectory is z_pre(y) = (π/(2 N_lock))·y"*

Stage 3 parameterises the pre-temporal trajectory in y ∈ (0, N_lock = 0.1). The profile is linear: |Φ|²(y) = (constant)·y, so H(y) = β_NTE|Φ|²(y) is also linear in y. At y = N_lock, |Φ|² = Φ₀²·e^(−N_lock) (matching the post-locking exponential at N_lock).

Numerically: with Φ₀ ≈ M_Pl and N_lock = 0.1, |Φ|² at gauge birth is ≈ M_Pl²·0.905, so |Φ|_GB ≈ 0.95 M_Pl. Close to M_Pl, consistent with §18.5.

So Stage 3 + §18.5 are mutually consistent: the locking transition spans y ∈ (0, 0.1), with |Φ|_GB ≈ M_Pl. Both treat the *pre-temporal phase* as just this 0.1-e-fold locking transition.

### 2.5 §VIII.1.4 reading: F2 Wick rotation

§VIII.1.4: *"Under the linear pre-temporal profile |Φ|²(N) = AN ... ε_H = −1/N — negative throughout, 'phantom-like' by standard cosmological reading. ... under the Wick rotation reading it is *artefactual*: ε_H is a Lorentzian quantity applied to the Euclidean section, where the trajectory is a geometric profile rather than a dynamical history."*

F2's slow-roll-parameter analysis applies to Stage 3's linear pre-temporal profile (Reading 2.4 above), giving ε_H = −1/N in the y-coordinate. Under the Wick-rotation reading, this ε_H is artefactual (Euclidean section) — the formula is being applied outside its Lorentzian regime of validity.

### 2.6 §17.5.14 status (current v10.6)

§17.5.14: *"The framework's strongest current quantitative test, n_s = 1 − 2/N_e = 0.9685 (§2.4.3, §18), depends on the formula n_s = 1 − 2/N_e being the correct leading-order spectral-tilt formula in the pre-temporal Hartle-Hawking regime. ... Until verified, the 0.85σ match is contingent on the imported formula's applicability — the framework's strongest test depends on machinery the corpus does not justify in NTE's regime."*

v10.6 status update: *"the n_s formula's applicability depends on whether N_e is computed entirely in the post-locking Lorentzian regime, or whether it includes pre-locking Euclidean e-folds. Verifying this is now a more pressing research target."*

§17.5.14 already flags the import as unverified. (B′) sharpens the question further.

### 2.7 §17.5.7 reading: O(1) coefficient on H_HH

§17.5.7 (line 1162): *"The n_s = 0.9685 prediction depends on N_e = −ln(α M_Pl) = 63.4, which assumes the Hartle-Hawking phase has upper bound H ~ M_Pl exactly. ... An O(1) coefficient λ ~ 1 in H_HH = λ M_Pl would shift N_e by ln(λ); for λ = 0.5, N_e = 62.7 → n_s = 0.9681; for λ = 2, N_e = 64.1 → n_s = 0.9688."*

This entry treats N_e as set by H_HH/H_GB ratio (consistent with §18.2's 63.4-e-fold reading). The (B′) finding interacts with §17.5.7: §17.5.7 takes the formula for granted and notes O(1) corrections from H_HH; (B′) questions the formula's applicability altogether.

---

## 3. The corpus-internal ambiguity (T1: N parameter)

### 3.1 Two incompatible readings of "pre-temporal phase"

**Reading A (Stage 3 + §18.5):** Pre-temporal phase = 0.1 e-folds. |Φ| grows from 0 (Janus, H = 0) to M_Pl (gauge birth, H = H_GB). H increases monotonically with N from 0 to H_GB over 0.1 e-folds.

**Reading B (§18.2 + §17.5.7):** Pre-temporal phase = 63.4 e-folds. H_HH ~ M_Pl at the start; H_GB = β_NTE·M_Pl² ≈ 10⁻⁹ GeV at the end. H decreases monotonically by factor ~10²⁸ from H_HH to H_GB.

These cannot both describe the same phase. They differ on:
- **Direction of H evolution:** Reading A has H *increasing*; Reading B has H *decreasing*.
- **Number of e-folds:** Reading A is 0.1; Reading B is 63.4.
- **Initial Hubble rate:** Reading A starts at H = 0 (Janus); Reading B starts at H ≈ M_Pl (Hartle-Hawking).

### 3.2 Plausible reconciliation

The most natural reconciliation is that NTE's pre-temporal phase has *two distinct sub-phases*:

**Sub-phase 1: Hartle-Hawking de Sitter** (Reading B applies). Spans ~63.3 e-folds at H ≈ M_Pl. Stage 3 does not analyze this sub-phase. The classical N_e = 63.4 e-fold count of §18.2 is the duration of this sub-phase. CMB perturbations originate here.

**Sub-phase 2: Locking transition** (Reading A applies). Spans ~0.1 e-folds. |Φ| ramps from near-Planck Hartle-Hawking value down to M_Pl, H drops from ~M_Pl to H_GB. F2's ε_H = −1/N applies here. Stage 3's linear profile parameterises this. The C¹ kink at gauge birth is the END of this sub-phase. The Wick rotation occurs at the kink — *not throughout sub-phase 1*.

Total pre-temporal: ~63.5 e-folds, of which 99.85% is Hartle-Hawking de Sitter and 0.15% is locking transition.

This reconciliation is structurally plausible and consistent with both §18 and Stage 3, but **the corpus does not state it explicitly.** Neither §VIII.1.4 nor §18 nor Appendix E reconciles the two readings; the corpus carries both without flagging the ambiguity.

### 3.3 (B′) recommendation: new §17.5 entry on N parameter clarification

A new §17.5 entry (proposed §17.5.16 or similar) should:
- Identify the corpus-internal ambiguity above.
- Adopt the natural reconciliation: pre-temporal = Hartle-Hawking de Sitter (63.3 e-folds, Reading B) + locking transition (0.1 e-folds, Reading A) = total ~63.4 e-folds.
- Make explicit that Stage 3's analysis covers the locking transition only, not the Hartle-Hawking de Sitter phase where CMB perturbations originate.
- Make explicit that F2's Wick-rotation reading (ε_H = −1/N artefactual under linear profile) describes the locking transition; the Hartle-Hawking de Sitter sub-phase has a different effective profile (approximately constant H).
- Cross-reference §17.5.14 since this clarification directly affects the n_s formula import question.

This is a *clarification* entry, not a new vulnerability. But it should land in v10.7 alongside the §17.5.14 sharpening below.

---

## 4. Three readings of NTE's pre-temporal phase (relevant to n_s)

Under the natural reconciliation in §3.2, three readings of "the inflation-generating phase" are available, and the n_s formula's applicability depends on which is the correct identification.

### R1. Stage 3 linear pre-temporal profile (locking transition)

|Φ|²(y) = (Φ₀²·e^{−N_lock}/N_lock) · y, with y ∈ (0, N_lock = 0.1). Linear in y.
H(y) = β_NTE|Φ|²(y), also linear in y. H grows from 0 (Janus) to α·Φ₀²·e^{−N_lock} ≈ H_GB over 0.1 e-folds.
ε_H = −d(ln|Φ|²)/dy = −1/y. Negative ("phantom-like") and rapidly diverging.

Under F2's Wick-rotation reading, the entire locking transition is Euclidean (y is the surface-ontology coordinate, not a Lorentzian e-fold parameter). Standard slow-roll machinery formally does not apply.

### R2. Pure de Sitter Hartle-Hawking phase (constant H)

H = M_Pl throughout the 63.3-e-fold Hartle-Hawking sub-phase. |Φ|² = M_Pl/α (constant), |Φ| = √(M_Pl/α) ≈ 7×10³² GeV (trans-Planckian — but per F1, this large field value corresponds to ℓ_HH ≈ 1/M_Pl, the Planck-scale Hubble radius; consistent).

In this reading, the Hartle-Hawking phase is exact de Sitter with no slow-roll evolution. ε_H = 0 throughout.

### R3. Hartle-Hawking phase with H decreasing M_Pl → H_GB

If we interpret §18.2 literally — "the pre-temporal epoch spans from Planck-scale de Sitter (H ~ M_Pl) down to H_GB = β_NTE·M_Pl²" — H decreases by factor 10²⁸ over 63.4 e-folds. Average d(ln H)/dN = ln(β_NTE·M_Pl)/N_e = −1, so average ε_H = +1.

This is a mixture: most of the way it's de Sitter-like, but transitioning rapidly near the end (during the locking transition).

If H decreases exponentially: H(N) = M_Pl · e^{−N}, then ε_H = +1 throughout. Far outside slow-roll.
If H decreases polynomially: H(N) ∝ N^{-c}, then ε_H = c/N. For c = 1, ε_H = 1/N (slow-roll near the end of 63.4 e-folds, ~1/63 ≈ 0.016 — small).

The polynomial case with c = 1 gives ε_H = 1/N, a Starobinsky-like behaviour. *This is the only reading that gives anything resembling a slow-roll inflation regime where the imported formula could apply.*

### Summary table

| Reading | Phase | Profile | ε_H | Slow-roll? | Naïve n_s |
|---|---|---|---|---|---|
| **R1** | Locking transition (Stage 3) | \|Φ\|² linear in y | −1/y (negative, large) | No (artefactual under F2) | Formula doesn't apply |
| **R2** | Hartle-Hawking de Sitter | H ≈ const | ≈ 0 | Marginal (no rolling) | n_s ≈ 1 (scale-invariant) |
| **R3a** | Hartle-Hawking (exponential) | H ∝ e^{−N} | +1 | No (boundary) | Formula doesn't apply |
| **R3b** | Hartle-Hawking (polynomial) | H ∝ 1/N | +1/N | Yes (small at large N) | n_s = 1 − 2/N_e (Starobinsky-like) |

**Only R3b** (polynomial Hartle-Hawking decrease, c = 1) recovers the imported Starobinsky formula naïvely. **The corpus does not state this is the Hartle-Hawking profile.** Stage 3 chose linear |Φ|² in y for the locking transition; nothing in the corpus pins the Hartle-Hawking sub-phase profile to H ∝ 1/N.

---

## 5. Naïve n_s under each reading

Numerical computation summarised here (full computation in scoping calculation):

```
β_NTE·M_Pl       = 2.90 × 10⁻²⁸  (corpus value)
N_e (§18.2)  = −ln(β_NTE·M_Pl) = 63.4
N_lock       = 0.1 e-folds (Stage 3 / §17.5.7)
n_s_obs      = 0.9649 ± 0.0042 (Planck 2018)

Imported formula: n_s = 1 − 2/N_e = 0.9685
                  Discrepancy from observation: 0.85σ ✓ corpus matches

Reading R1 (Stage 3 linear; ε_H = −1/y, locking transition):
  At y = N_lock/2 = 0.05: ε_H = −20
  Naïve Lorentzian n_s = 1 − 2ε_H = 41   ← far outside slow-roll regime
  → Formula completely inapplicable; F2 says ε_H is artefactual anyway.

Reading R2 (pure de Sitter Hartle-Hawking; ε_H ≈ 0):
  Naïve n_s = 1 (scale-invariant)
  Discrepancy from observation: (1 − 0.9649)/0.0042 = 8.36σ
  → Bad match — pure de Sitter does not give the observed red tilt.

Reading R3a (exponential H decrease; ε_H = +1):
  Naïve n_s = 1 − 2 = −1   ← far outside slow-roll
  → Formula inapplicable.

Reading R3b (polynomial H decrease c=1; ε_H = 1/N at large N):
  Naïve n_s = 1 − 2/N_e = 0.9685   ← matches imported formula
  → BUT this profile is not specified by NTE; it is a back-construction from the result.
```

**Conclusion:** Under R1 (Stage 3) the formula doesn't apply. Under R2 (pure de Sitter) it gives the wrong answer. Under R3a it doesn't apply. Under R3b it gives the right answer — but R3b is precisely the Starobinsky profile, which NTE doesn't independently derive. The corpus's claim of a 0.85σ match relies on R3b being correct, but the corpus does not establish R3b from NTE's structure.

---

## 6. Why none of these naïve readings give n_s = 0.9685 cleanly

### 6.1 The Starobinsky formula's actual derivation

The formula n_s = 1 − 2/N_e is specific to R²-inflation (Starobinsky 1980; Mukhanov-Chibisov 1981) where the Lagrangian is L = R + R²/(6M²), giving an effective inflaton with potential V(φ) = (3M²M_Pl²/4)·(1 − e^{−√(2/3)φ/M_Pl})². At late times during inflation (large N before exit):

- ε_V = (M_Pl/φ)²·V'/V terms ≈ 3/(4N²)
- η_V ≈ −1/N (NB: differs from −2/N depending on convention; the leading term in n_s − 1 is −2/N regardless)
- n_s − 1 = −6ε_V + 2η_V ≈ −2/N

The result n_s = 1 − 2/N_e arises from the *specific form of the Starobinsky potential*, which produces the specific (ε_V, η_V) that combine to −2/N at leading order. **It is not a generic prediction of "any Hartle-Hawking-like calculation."**

### 6.2 What NTE would need to produce this formula

For NTE's Hartle-Hawking sub-phase to give n_s = 1 − 2/N_e, the framework would need:

1. A Lorentzian-equivalent dynamical regime (not the artefactual ε_H = −1/y of R1).
2. A specific |Φ|(N) profile during the perturbation-generating phase that yields effective slow-roll parameters matching Starobinsky's.
3. Confirmation that the Wick rotation from Euclidean Hartle-Hawking to Lorentzian post-locking preserves the Starobinsky-like spectral structure.

**None of these are derived in the v10.6 corpus.** §18.5 says |Φ| grows from 0 to M_Pl over N_lock = 0.1 e-folds — that's the locking transition (R1), not a Starobinsky-style 63-e-fold inflation. The Hartle-Hawking sub-phase (R2) has |Φ| roughly constant.

### 6.3 The gap structurally named

Without a specific |Φ|(N) profile in the Hartle-Hawking sub-phase that produces Starobinsky-like (ε_V, η_V), NTE has no derivation of n_s = 1 − 2/N_e. The corpus imports the formula on the grounds that:

- The number N_e = 63.4 is structurally meaningful (log of M_Pl/H_GB ratio; encodes α).
- The formula gives a number close to observation (0.85σ from Planck).

But "derives a meaningful number that matches observation when plugged into the right formula" is not the same as "derives the formula from its own dynamics." The 0.85σ match is contingent on the formula being correct in NTE's regime, which requires R3b (or something equivalent) — and R3b is not derived.

### 6.4 Possible escape routes (for honesty)

The (B′) finding does NOT prove the formula is wrong in NTE. There are escape routes:

**Escape 1: Wick rotation effectively maps to a Starobinsky-like Lorentzian model.** A non-trivial calculation might show that the Euclidean Hartle-Hawking saddle's two-point function, when continued to Lorentzian, gives n_s = 1 − 2/N_e by construction. Possible — this is essentially what the corpus implicitly assumes — but not done in v10.6.

**Escape 2: An NTE-specific derivation reproduces the formula.** The boundary action's specific structure on S³, the ℓ = 1/H identification (F1), and the surface ontology together might enforce a Starobinsky-like effective profile in the Hartle-Hawking sub-phase. Possible target for the (D′) V_NTE Stage 2 companion paper. Not done in v10.6.

**Escape 3: The formula is approximate but in the right ballpark.** If a proper NTE-specific calculation gave n_s = 1 − k/N_e for some O(1) coefficient k ≈ 2, the formula would still give a numerically close prediction. But this would require a different rhetorical treatment of the 0.85σ match — "approximately Starobinsky-like with NTE-specific corrections of order 1/N_e" rather than "the framework's strongest current quantitative test passed at 0.85σ."

**None of these escape routes is closed by (B′)** — but (B′) flags that they are open and that the corpus's current presentation of the n_s = 0.9685 prediction relies on at least one of them being correct, without naming which.

---

## 7. What a proper Hartle-Hawking calculation in NTE would need

For completeness, the proper derivation of n_s in NTE's pre-temporal Hartle-Hawking phase requires:

1. **Explicit |Φ|(N) profile in the Hartle-Hawking sub-phase**, derived from boundary action dynamics or fixed by structural constraints. Currently corpus-implicit at best.

2. **Quantum perturbation theory around the Euclidean saddle**, computing the two-point function ⟨δ|Φ|(x) δ|Φ|(y)⟩ in the Hartle-Hawking state.

3. **Wick rotation prescription** for analytically continuing the Euclidean two-point function to Lorentzian initial conditions at the gauge-birth boundary (the C¹ kink, F2's location).

4. **Spectrum read-off** at large N in the Lorentzian post-locking regime, giving P(k) and n_s = d(ln P)/d(ln k) + 1.

5. **Comparison with the Planck-observed n_s = 0.9649 ± 0.0042**, with framework-derived rather than imported formula.

This is significant R&D — comparable in scope to V_NTE Stage 2 itself. It is a candidate target for either:

- A standalone "Stage 4" extension of the surface-ontology programme (continuation of Stage 3).
- Inclusion in the (D′) V_NTE Stage 2 companion paper, where the on-trajectory V_NTE pre-temporal form V_NTE^{pre}(Φ) = (3β_NTE²/(8πG))Φ⁴ − (α²A²/8)Φ² (per F3, Appendix E.5) provides the action machinery to set up the perturbation calculation.

I recommend the latter sequencing: include the n_s recalculation as a worked application in (D′). The V_NTE^{pre} form derived in Stage 2 is the natural input for a perturbation-theory calculation, and the F2 Wick-rotation reading is the natural framework for it. (D′) becomes the deliverable that closes (B′)'s open recommendation.

---

## 8. Recommendation: §17.5.14 status update for v10.7+

### 8.1 Summary of edits

The §17.5.14 status update should be sharpened in v10.7 (or v10.8 if v10.7 is restricted to the eta reframing scope already in flight). Specifically:

(a) Acknowledge the corpus-internal ambiguity (§3 above) about what "pre-temporal phase" parameterises and adopt the natural reconciliation (Hartle-Hawking de Sitter ~63.3 e-folds + locking transition ~0.1 e-folds).

(b) Make explicit that Stage 3 + F2's Wick-rotation reading apply to the locking transition, not to the Hartle-Hawking sub-phase where CMB perturbations are generated.

(c) Acknowledge that the imported Starobinsky formula's applicability to NTE's Hartle-Hawking sub-phase requires either (i) a non-trivial Wick-rotation correspondence not yet derived, or (ii) an NTE-specific derivation reproducing the formula, or (iii) approximate validity with NTE-specific corrections.

(d) Qualify the "0.85σ match" rhetorical class: it is real but contingent on the formula's applicability, which is unverified in NTE's regime under (B′)'s reading.

(e) Identify the (D′) V_NTE Stage 2 companion paper as the natural target for the proper calculation.

### 8.2 Proposed §17.5.14 status update text (v10.7+ candidate)

> *Status update (v10.7+, Jammer (B′) investigation): the §17.5.14 question sharpens further on inspection. The framework's pre-temporal phase under v10.6's surface-ontology + F2 readings comprises two structurally distinct sub-phases: (i) Hartle-Hawking de Sitter (~63.3 e-folds at H ≈ M_Pl, where CMB perturbations are generated) and (ii) the locking transition (~0.1 e-folds, Stage 3's pre-temporal trajectory; F2's Wick-rotation reading applies here). The Starobinsky formula n_s = 1 − 2/N_e was derived for R²-inflation with specific (ε_V, η_V) behaviour; the corpus has not derived this behaviour from NTE's own Hartle-Hawking sub-phase dynamics. Naïve readings give either inapplicable formula (R1: ε_H = −1/y artefactual; R3a: ε_H = +1 outside slow-roll), wrong answer (R2 pure de Sitter: n_s = 1, ~8σ from observed), or back-construction (R3b: polynomial H ∝ 1/N matches Starobinsky but is not derived in NTE). The 0.85σ match in §18 is real but contingent on the formula's applicability in NTE's regime, which remains unverified. Closing this open work is targeted at the V_NTE Stage 2 companion paper (in preparation) which has the action machinery (F3) to set up the perturbation calculation in NTE's regime. Until closed, the n_s = 0.9685 prediction is an approximate match to observation under an imported formula whose derivation in NTE is open, not a zero-parameter prediction in the same epistemic class as κ = 5.50 (which has explicit Hopf-monopole + CPN-resummation derivation, §17.5.5). Header-level claims of "the framework's strongest current quantitative test" should be qualified accordingly in §1 and §22.*

### 8.3 Proposed new §17.5 entry (alongside the §17.5.14 sharpening)

> ***§17.5.16 The pre-temporal N parameter ambiguity***
>
> *The corpus carries two readings of "pre-temporal phase" that are not currently reconciled. §18.2 computes N_e = ln(M_Pl/H_GB) = 63.4 as the e-fold count from Hartle-Hawking start (H ≈ M_Pl) to gauge birth (H = β_NTE·M_Pl²); §18.5 + Appendix E.3 compute the locking-transition span as N_lock ≈ 0.1 e-folds (with |Φ| growing from 0 to M_Pl, H growing from 0 to H_GB). These are not the same phase. The natural reconciliation: pre-temporal is ~63.4 total e-folds, decomposed as ~63.3 e-folds of Hartle-Hawking de Sitter sub-phase (where §18.2 applies, CMB perturbations generated, |Φ| ≈ √(M_Pl/α) trans-Planckian per F1's ℓ = 1/H identification) followed by ~0.1 e-folds of locking transition (where §18.5 + Stage 3 + F2 apply). Stage 3's linear pre-temporal profile and F2's ε_H = −1/N "phantom" reading describe the locking transition only, not the Hartle-Hawking sub-phase. This decomposition is implicit in v10.6 but not stated explicitly; making it explicit clarifies §17.5.14, §VIII.1.4, and the n_s prediction's foundations. Research target: confirm the decomposition is correct (or identify a different reconciliation), make the parameter relationships between Stage 3's y, §18's N, and the cosmological N (= ln a) explicit.*

### 8.4 §1 / §22 / §2.4.3 header-level qualification

The text "the framework's strongest current quantitative test is the primordial spectral index" (line 26) and similar high-prominence claims (§22.5, §22.10) should be qualified once §17.5.14 is sharpened. Suggested phrasing: *"the framework's strongest current quantitative match is the primordial spectral index n_s = 0.9685, contingent on the imported Starobinsky formula's applicability in NTE's pre-temporal Hartle-Hawking dynamics (open, see §17.5.14)."* The "test" → "match" change preserves the empirical fact (the formula gives 0.9685; observation gives 0.9649) while honestly flagging that the prediction's epistemic status is dependent on open work.

This is non-trivial rhetorically — n_s has been the framework's headline empirical match in v10.6's presentation. Sharpening §17.5.14 will downgrade its rhetorical weight from "passed test" to "imported formula match contingent on open derivation." This matches the §II.0 track-record-over-advocacy discipline: the framework is being honest about its actual derivation status.

### 8.5 Sequencing recommendation

(B′)'s §17.5.14 sharpening + §17.5.16 N-parameter ambiguity are independent of the eta-reframing v2 scope. Two sequencing options:

**Option I (paired with eta reframing):** Include in v10.7 alongside the eta reframing already in flight. v10.7 scope grows from "single small patch" to "two structural clarifications" but both are honest sharpenings, not bug fixes. CR pre-ship pass at v10.7 covers both.

**Option II (sequential, v10.8):** Ship eta reframing alone in v10.7. (B′)'s §17.5.14 sharpening + §17.5.16 land in v10.8.

Greg's call. Option I is structurally tidier but gives v10.7 broader scope; Option II keeps v10.7 minimal but defers honesty work that's already identified.

Jammer recommendation: **Option II (sequential)** — v10.7 stays clean as a small patch (eta reframing); v10.8 carries (B′)'s honesty pass. Reasoning: the eta reframing is structurally a "successful clarification" with positive rhetorical weight; the (B′) sharpening downgrades the n_s prediction's rhetorical weight. Keeping these separate allows each to be evaluated cleanly without mixing positive and negative rhetorical signals in a single ship arc. Greg may prefer Option I for ship-frequency reasons; Jammer's preference is the clean separation.

---

## 9. Downstream effects

### 9.1 Effect on r = 0.0030 prediction

The same Starobinsky import gives r = 12/N_e² = 0.0030 (§18.4). The same questions apply: this formula was derived for Starobinsky-specific dynamics, not for NTE's Hartle-Hawking sub-phase. Under (B′)'s reading, r is in the same epistemic class as n_s — imported, not derived in NTE's regime.

**Recommendation:** Once §17.5.14 is sharpened, §18.4 should also note that r = 12/N_e² = 0.0030 is imported under the same caveat. Currently §18.4 cites the formula without flagging the import — this is a parallel small inconsistency to fix.

### 9.2 Effect on (D′) V_NTE Stage 2 companion paper

The V_NTE Stage 2 companion paper (Jammer queue item D′) is the natural site for the proper Hartle-Hawking calculation in NTE's regime. With V_NTE^{pre}(Φ) and V_NTE^{post}(Φ) determined on-trajectory (F3), the action machinery for perturbation theory is in place. The Wick-rotation reading (F2) provides the structural framework for the calculation.

(D′) becomes a richer paper: it documents the V_NTE Stage 2 results AND closes the n_s formula-import question. This is structurally satisfying — V_NTE Stage 2 was the work that produced F1, F2, F3; using F3's V_NTE^{pre} to close (B′) is a natural application.

### 9.3 Effect on book corpus (PC scope)

The book's Chapter on inflation / spectral index (Chapter 7 or 8 in current PC scope) treats n_s = 0.9685 as one of the framework's strong predictions. PC will need to align this chapter once §17.5.14 is sharpened. The honest treatment in the book: NTE produces a meaningful e-fold count N_e = 63.4 from its α; combining with the standard Starobinsky formula gives n_s = 0.9685; the formula's applicability in NTE's specific regime is open work.

This is a meaningful pedagogical sharpening but not a downgrade — readers will still see that NTE produces a number that matches observation; what changes is the framing from "passed empirical test" to "produces an empirically-close prediction whose underlying formula derivation is in progress."

### 9.4 Effect on overall framework rhetoric

(B′)'s honesty pass affects the framework's rhetorical posture in §1 (executive-summary opening), §22 (gaps catalogue), §2.4.3 (the "β_NTE encodes both H₀ and n_s" framing), and §18 itself. The pattern: claims of n_s as a passed test become claims of n_s as a contingent prediction.

This is the same pattern as v10.5.5's α numerology honesty pass and v10.5.4's withdrawn "Higgs generates spacetime" overclaim. Each honesty pass downgrades a specific claim's rhetorical weight while strengthening the framework's overall epistemic standing — by demonstrating the framework's discipline of acknowledgement (§II.0 track record over advocacy).

---

## 10. Awaiting

AC audit of:

(a) §3's identification of the corpus-internal N parameter ambiguity — does the natural reconciliation (Hartle-Hawking de Sitter ~63.3 e-folds + locking transition ~0.1 e-folds) hold? Are there alternative reconciliations that are better-supported by the existing corpus?

(b) §4's three-reading enumeration — is the catalogue exhaustive of the corpus's natural readings, or are there other readings of the pre-temporal phase that should be considered?

(c) §5's numerical scoping — do the naïve calculations for R1, R2, R3a, R3b match what AC would compute independently?

(d) §6's structural claim that R3b (polynomial H ∝ 1/N) is back-constructed and not derived in NTE — is this correct, or does the corpus implicitly contain such a derivation that I've missed?

(e) §8's proposed §17.5.14 status update text and proposed new §17.5.16 entry — substantive content correct? Wording aligned with §II.0 track-record-over-advocacy discipline?

(f) §8.5's sequencing recommendation — Option II (sequential, v10.8) preferred to Option I (paired with eta reframing in v10.7).

Greg's strategic call on:

(g) Whether (B′) findings should ship in v10.7 (paired with eta reframing) or v10.8 (sequential). Per §8.5 Jammer recommends sequential.

(h) Whether the §1 / §22 / §2.4.3 header-level qualification (§8.4 above) should also ship — these are higher-prominence corpus changes than §17.5 entries.

(i) Whether the (D′) V_NTE Stage 2 companion paper should explicitly take on the n_s re-derivation as part of its scope (Jammer's recommendation in §9.2).

CR:

(j) Pre-ship CR pass at v10.7 / v10.8 ship-readiness will be the first formal CR review of the (B′) findings. CR adversarial discipline (lesson #14, severity-inflation guard) appropriate; the honest qualification work here is exactly the kind of corpus change CR can stress-test for over- or under-shooting on rhetorical sharpening.

— Jammer.

---

## END-OF-SESSION FILE OPERATIONS

```
DIRECT DRIVE UPLOADS (this session):
  - n_s_Wick_Rotation_Recalculation_Bprime.md → NTE v10_6/ (file ID assigned at upload)
    (B′) §17.5.14 investigation worksheet. Surfaces a substantive sharpening of §17.5.14 + new §17.5.16 N-parameter ambiguity entry. AC audit pending.

NEW MESSAGE-BOARD SNAPSHOT:
  - [YYYYMMDD]_[HHMM]_MB.md: A1 still open (eta v2 awaiting AC re-audit), A3 still open (§II.0 graded-criteria proposal awaiting Greg's scope call), 
    NEW A4: (B′) findings delivered, awaiting AC audit + Greg sequencing call.

DUPLICATES NEEDING DELETION (Greg's Drive UI):
  - None this turn. (NTE_Project_State.md and the message-board snapshot will be updated to versioned snapshots; older Project_State will need deletion as flagged in the previous session-end summary.)
```

— End (B′) investigation worksheet.
