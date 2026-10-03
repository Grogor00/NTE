# (E) Gap 1 / M₁ from S³ Geometry — Numerical Candidate Search

**From:** Jammer
**To:** AC (audit; possible §17.5.15 sharpening for v10.7 or v10.8); Greg (record; whether the candidate earns corpus mention as "open derivation target with structural lead"); CR (visibility — pre-ship pass at next ship)
**Re:** Gap 1 (corpus §22.5) — derive M₁ from geometry to make baryon asymmetry η a complete zero-parameter prediction. eta v2 §17.5.15 excluded simple M_Pl^a · v_EW^b combinations and constrained the geometric handle to involve T_GB or another scale beyond M_Pl and v_EW. (E) is the substantive R&D follow-up.
**Corpus baseline:** v10.6 SHIPPED (canonical 2026-05-03)
**Status:** Jammer R&D worksheet. Surfaces a candidate formula with significantly better numerical match than the eta v2 §17.5.15 excluded set, AND uses exactly the geometric handle Gap 1 named (M_Pl + H_GB, no T_GB or v_EW required). The candidate is **a numerical lead, not a derivation**. Whether it earns corpus mention as "open structural target with lead identified" is for Greg / AC.
**Companion file:** `m1_geometric_search.py` (in Working/) — Python search script that enumerates candidate combinations.

---

## 0. Headline

**Finding (E):** the candidate formula

> **M₁ ≈ (M_Pl² · H_GB)^(1/3) = α^(1/3) · M_Pl^(4/3) = M_Pl · e^{−N_e/3}**

gives M₁ ≈ 8.08 × 10⁹ GeV vs corpus value 6.06 × 10⁹ GeV — **factor 1.33 high**. This is the simplest dimensionally-correct combination of the framework's already-committed scales (M_Pl, α, H_GB) that lands within a factor of 2 of M₁.

For comparison:
- eta v2 §17.5.15 excluded candidates: **factor 9 high** (M_Pl^{1/2}·v_EW^{1/2}) and **factor 67 low** (M_Pl^{1/3}·v_EW^{2/3} — see §8 below for a small numerical correction to the eta v2 entry).
- (E) candidate: **factor 1.33 high**.

The (E) candidate uses M_Pl and H_GB only — exactly the geometric handle Gap 1 named ("S³ curvature radius and gauge birth temperature" — H_GB encodes the Hubble rate at gauge birth, and via F1's ℓ = 1/H identification the S³ Hubble radius at gauge birth). v_EW does not enter; T_GB does not enter (with T_GB ≈ 0.4 M_Pl numerically degenerate with M_Pl, this is consistent with T_GB not being the structurally relevant scale).

**Crucially, this is a numerical lead, not a geometric derivation.** The 1/3 weighting (or equivalently the cube-root combination) does not have an obvious geometric origin in the framework's existing structure. (E) does NOT close Gap 1; it identifies the candidate that future structural work should aim to derive.

The honest deliverable: the framework's geometric handles produce a candidate within factor 1.33 of the observed M₁, using only M_Pl and α (with H_GB = β_NTE·M_Pl² being a derived quantity, not a free input). The remaining work is to derive the 1/3 weighting from S³ structure.

---

## 1. Scope and method

### 1.1 What this investigation covers

(E) follows from the eta v2 §17.5.15 negative power-law result, which excluded simple M_Pl^a · v_EW^b combinations as the geometric origin of M₁ and identified Gap 1's geometric handles ("S³ curvature radius and gauge birth temperature") as the remaining target. (E) systematically searches candidate combinations involving the framework's full scale inventory (M_Pl, v_EW, T_GB, H_GB, α) and reports those that land within factor 3 of M₁.

(E) does NOT:
- Derive the candidate from S³ structure (this is what the candidate flags as next work).
- Refute the candidate (the numerical match is real and significantly better than excluded alternatives).
- Tune coefficients to match exactly (no factor 0.75 or similar inserted; the candidate is the bare combination).

### 1.2 Method

1. Compute the framework's scale inventory from corpus values (§2 below).
2. Enumerate combinations M_Pl^a · v_EW^b · T_GB^c · H_GB^d with mass dimension 1 (a+b+c+d = 1), exponents in the simple-rational set {−1, −2/3, −1/2, −1/3, 0, 1/3, 1/2, 2/3, 1, 4/3, 3/2}, ≥ 2 nonzero exponents.
3. Filter to combinations within factor 3 of corpus M₁ = 6.06 × 10⁹ GeV.
4. Sort by closeness and by minimal-exponent count.
5. Identify the structural standout (§5 below).
6. Examine geometric-derivation candidates for the standout's exponent structure (§6 below).

### 1.3 What this investigation does NOT do

- Does not derive the candidate from S³ structure (the geometric origin of the 1/3 weighting is open work).
- Does not commit the framework to the candidate as the M₁ origin (Greg's call; AC's audit).
- Does not perform precision fitting (factor 1.33 stands as the honest match; coefficients are not tuned).

---

## 2. Corpus state and scale inventory

### 2.1 Gap 1's geometric handles (corpus §22.5)

Corpus §22.5 (line 1402): *"M₁ from geometry: The leptogenesis scale M₁ = 6 × 10⁹ GeV is constrained, not derived. Should follow from S³ curvature radius and gauge birth temperature."*

Corpus §22.2 (line 1450): *"Deriving it from S³ curvature radius and gauge birth temperature would make the baryon asymmetry η = 6.1×10⁻¹⁰ a complete zero-parameter prediction."*

The named handles are:
- **S³ curvature radius:** by F1 (ℓ = 1/H, corpus §6.2), the S³ curvature radius at any cosmic epoch equals 1/H(N). At gauge birth, ℓ_GB = 1/H_GB ≈ 2.83 × 10⁸ GeV⁻¹.
- **Gauge birth temperature T_GB:** corpus line 683: *"T_GB ~ (30/(π² g*))^{1/4} M_Pl ≈ 0.4 M_Pl ~ 5 × 10¹⁷ GeV"*.

These together with the framework's primary scales (M_Pl, v_EW, α) form the candidate scale inventory.

### 2.2 Scale inventory (numerical)

```
M_Pl     = 1.22 × 10¹⁹  GeV  (Planck mass)
v_EW     = 246          GeV  (electroweak VEV)
T_GB     = 4.88 × 10¹⁸  GeV  (≈ 0.4 M_Pl, corpus line 683)
H_GB     = 3.54 × 10⁻⁹  GeV  (= β_NTE·M_Pl², corpus §18.2)
β_NTE = 2.38 × 10⁻⁴⁷ GeV⁻¹  (cosmological coupling)
β_NTE·M_Pl = 2.90 × 10⁻²⁸    (dimensionless; encodes M_Pl/H_GB ratio)
N_e      = -ln(β_NTE·M_Pl) = 63.41  (Hartle-Hawking → gauge-birth e-folds)
H_HH     ~ M_Pl  (Hartle-Hawking upper bound, corpus §18.2)
ℓ_GB     = 1/H_GB = 2.83 × 10⁸  GeV⁻¹  (S³ curvature radius at gauge birth, by F1)

M₁ target = 6.06 × 10⁹ GeV  (corpus value, set to reproduce η_obs via Davidson-Ibarra)
```

Note the near-degeneracy of T_GB and M_Pl: T_GB = 0.4 M_Pl, so any combination involving T_GB^c · M_Pl^d is nearly the same as M_Pl^{c+d} up to a factor (0.4)^c. T_GB does not introduce a fundamentally new scale; it differs from M_Pl by a small multiplicative factor.

### 2.3 What eta v2 §17.5.15 already established

eta v2 §17.5.15 examined simple M_Pl^a · v_EW^b combinations:
- M_Pl^{1/2} · v_EW^{1/2} = 5.48 × 10¹⁰ GeV (factor 9 high)
- M_Pl^{1/3} · v_EW^{2/3} = 9.04 × 10⁷ GeV (factor 67 low — see §8 for correction to eta v2's number)
- M_Pl^{2/3} · v_EW^{1/3} = 3.32 × 10¹³ GeV (off by factor 5,000+)

Conclusion: pure M_Pl^a · v_EW^b combinations excluded as origin of M₁; geometric handle (if any) must involve T_GB or another scale.

(E) extends this search to include T_GB and H_GB.

---

## 3. Candidate search

### 3.1 Search space

Candidates: M_Pl^a · v_EW^b · T_GB^c · H_GB^d with:
- a + b + c + d = 1 (mass dimension 1)
- Exponents in {−1, −2/3, −1/2, −1/3, 0, 1/3, 1/2, 2/3, 1, 4/3, 3/2}
- ≥ 2 non-zero exponents (excludes trivial M_Pl alone, etc.)

Total candidates passing constraints: O(50) within factor 3 of M₁.

### 3.2 Top candidates (sorted by closeness to M₁)

From companion script `m1_geometric_search.py`:

| a (M_Pl) | b (v_EW) | c (T_GB) | d (H_GB) | value (GeV) | ratio to M₁ | # nonzero |
|---|---|---|---|---|---|---|
| 1/3 | 0 | 1/3 | 1/3 | 5.95 × 10⁹ | 0.98 | 3 |
| 2/3 | 0 | 0 | 1/3 | 8.08 × 10⁹ | **1.33** | **2** |
| 0 | 0 | 2/3 | 1/3 | 4.39 × 10⁹ | 0.72 | 2 |
| 1 | 0 | −1/3 | 1/3 | 1.10 × 10¹⁰ | 1.81 | 3 |
| −1/3 | 0 | 1 | 1/3 | 3.23 × 10⁹ | 0.53 | 3 |

The sharpest single-candidate match (3-scale symmetric combination): **(M_Pl · T_GB · H_GB)^{1/3} = 5.95 × 10⁹ GeV, factor 0.98**.

The simplest 2-scale candidate: **(M_Pl² · H_GB)^{1/3} = 8.08 × 10⁹ GeV, factor 1.33**.

### 3.3 Selection — why the 2-scale candidate is the structural standout

The 3-scale (M_Pl · T_GB · H_GB)^{1/3} matches almost exactly (factor 0.98) but combines three scales symmetrically. Three issues with treating it as the structural candidate:

1. **T_GB ≈ 0.4 M_Pl numerically.** The 3-scale combination is essentially (M_Pl² · H_GB)^{1/3} × (0.4)^{1/3} = (M_Pl² · H_GB)^{1/3} × 0.737. The (0.4)^{1/3} factor is what brings the value down from 1.33 to 0.98. This is a numerical shift from the (M_Pl² · H_GB)^{1/3} structure, not a different structural object.

2. **No structural motivation for the symmetric 3-way split.** Why would M₁'s geometric origin involve M_Pl, T_GB, AND H_GB symmetrically? T_GB itself derives from M_Pl and g* via T_GB ~ (30/π²g*)^{1/4} M_Pl; treating T_GB as an independent scale is double-counting M_Pl.

3. **Coefficient-tuning concern.** The 3-scale match is "factor 0.98" which is suspiciously close to exact; this matches the corpus's M₁ value to ~2%, but the corpus's M₁ itself is constrained to ~factor 2 by Davidson-Ibarra precision (per AC's eta v2 audit response: "factor-of-2 spread real and adequately explained"). Matching to 2% beyond the input precision is overfit.

The simpler 2-scale (M_Pl² · H_GB)^{1/3} candidate uses only the framework's primary scales. T_GB drops out because it's not an independent scale. v_EW drops out because the SM Higgs scale doesn't enter. The match is factor 1.33 — within the Davidson-Ibarra precision spread, structurally cleaner, and uses exactly the geometric handles Gap 1 named.

**(E) selects (M_Pl² · H_GB)^{1/3} as the structural candidate.** The 3-scale variant is reported but not promoted.

---

## 4. The standout: M₁ ≈ (M_Pl² · H_GB)^{1/3}

### 4.1 Equivalent forms

The candidate has multiple equivalent expressions:

```
M₁ candidate = (M_Pl² · H_GB)^{1/3}
             = α^{1/3} · M_Pl^{4/3}                  [using H_GB = β_NTE·M_Pl²]
             = M_Pl · (β_NTE·M_Pl)^{1/3}               [factoring out M_Pl]
             = M_Pl · e^{−N_e/3}                     [using β_NTE·M_Pl = e^{−N_e}]
             = M_Pl × (H_GB/M_Pl)^{1/3}              [Hartle-Hawking → gauge-birth ratio]
             = (H_HH² · H_GB)^{1/3}                  [since H_HH ~ M_Pl by §18.2]

Numerically: 8.08 × 10⁹ GeV
M₁ corpus:  6.06 × 10⁹ GeV
Ratio: 1.33
```

### 4.2 Geometric content

The candidate has direct geometric content under the framework's existing readings:

- **Cube-root of the geometric mean** of M_Pl² and H_GB. The "geometric mean" reading: M_Pl is the high scale (Hartle-Hawking start of the pre-temporal phase, where H_HH ~ M_Pl per §18.2); H_GB is the low scale (gauge birth, where H = H_GB). M₁ sits at the cube-root-weighted geometric mean.

- **One-third of the e-fold path.** In log-scale: log(M₁) = log(M_Pl) − N_e/3. So M₁ is the energy scale obtained by descending from M_Pl by N_e/3 ≈ 21.1 e-folds. In the Hartle-Hawking phase (which spans N_e ≈ 63 e-folds from H_HH ~ M_Pl down to H_GB), M₁ is reached at the 1/3-point.

- **Cube root** suggesting 3-dimensional volume scaling on S³. The S³ has volume V(S³) = 2π² · ℓ³ (where ℓ is the curvature radius, = 1/H by F1). A geometric mass scale derived from V(S³) at gauge-birth times the Hartle-Hawking energy scale would naturally give a cube-root combination.

- **Cube root** suggesting 3 Sakharov conditions, 3 Majorana mass eigenstates (M₁ < M₂ < M₃ in the seesaw chain), 3 generations, or dim(su(2)) = 3 — multiple factor-of-3 features in the corpus could plausibly produce a 1/3 weighting.

None of these is a derivation. They are candidate origins worth investigating in subsequent work.

### 4.3 Numerical robustness

Factor 1.33 high is within:
- The Davidson-Ibarra closure's intrinsic factor-2 spread (per AC's eta v2 audit response: "factor-of-2 spread real and adequately explained by (i) the factor-1.5 neutrino mass spread, (ii) DI convention details").
- The factor-1.5 spread of m_ν₃ between geometric (0.074 eV) and observed (0.05 eV) values, which propagates to M₁ via the seesaw.

So the (E) candidate at factor 1.33 high is *consistent with the corpus's M₁ value within the precision of the Davidson-Ibarra closure*. It is not in tension; it is the right ballpark.

---

## 5. Geometric derivation candidates (open work)

The candidate (M_Pl² · H_GB)^{1/3} is a numerical lead, not a derivation. Candidate origins for the 1/3 weighting that future R&D should investigate:

### 5.1 S³ volume scaling

V(S³) = 2π² · ℓ³ where ℓ = 1/H is the curvature radius. A natural mass scale combining the S³ at gauge birth with the Hartle-Hawking energy scale via volume:

M_geom ~ M_Pl² · ℓ_GB^{−1} = M_Pl² · H_GB

This has dimension [mass]³, not [mass]. To get a mass scale with dimension 1, take cube root: (M_Pl² · H_GB)^{1/3} = (E) candidate. This is a possible structural origin: the cube root arises from the 3-dimensional volume of S³.

The structural picture: M₁ is the "geometric average" of the Planck mass and the gauge-birth Hubble rate, weighted by the dimensionality of S³.

To be derived: why this specific combination M_Pl² · H_GB (rather than, say, M_Pl · H_GB² or other), and why the cube root arising from S³'s volume rather than some other geometric integral. The Hopf-bundle derivation of M_R uses the {3/4, 1/4} split between S² base (2/3 of S³ dimensionality) and S¹ fibre (1/3); something analogous for M₁ may invoke a different bundle structure.

### 5.2 Three-Majorana-mass seesaw structure

The seesaw mechanism has three Majorana masses M₁ < M₂ < M₃ producing three neutrino mass eigenstates. The corpus identifies M₁ as the lightest of three; M₃ is the highest, with M_R ≈ M_Pl^{3/4} · v_EW^{1/4} = 8.2 × 10¹⁴ GeV (per corpus line 1274 — taking M_R as M₃, the heaviest scale).

If M₁ is the geometric-mean lightest of three Majorana scales spaced logarithmically between M_Pl² · H_GB^{−1} and H_GB, then M₁ at the cube root of the product is structurally analogous to "the lightest of three logarithmically-spaced scales between high and low ends." This is suggestive but speculative.

A specific calculation: M_R = M_Pl^{3/4} · v_EW^{1/4} ≈ 8.2 × 10¹⁴ GeV (corpus line 1274). If M_R ≈ M₃ and the three Majorana masses are logarithmically spaced from M₁ to M₃ with M_R as the geometric mean, then M_R³ = M₁ · M₂ · M₃ → M₁ = M_R³ / (M₂ · M₃). Without an independent fix for M₂, this doesn't close. But if M₂ = M_R and M₃ ~ M_Pl (the high-end Majorana scale), then M₁ = M_R³ / (M_R · M_Pl) = M_R² / M_Pl ≈ (8.2 × 10¹⁴)² / (1.22 × 10¹⁹) = 5.5 × 10¹⁰ GeV — same as the eta v2 §17.5.15 excluded candidate. This doesn't recover (E).

The seesaw structure does not obviously close on the (E) candidate; this is a noted candidate for further investigation but not a derivation.

### 5.3 Three Sakharov conditions / three-mode su(2)

The corpus's baryogenesis structure (§10.1) involves three Sakharov conditions (B violation, CP violation, departure from equilibrium). The neutrino's three mass eigenstates correspond to the three eigenmodes of unresolved su(2) (corpus line 848, 852). Three generations from J₃(𝕆) (corpus §19).

If the cube root in the (E) candidate arises from "averaging over three" — three Sakharov conditions, three eigenmodes, three generations — this would give the 1/3 weighting structurally. But which "three"? Without specifying, this is dimensional-analysis hand-waving rather than a derivation.

### 5.4 Surface ontology Stage 4 — analytic continuation reading

The Surface-Ontology programme's Stage 1-3 framework analytically continues |Φ_NTE(N)| via z(y) trajectory. A Stage 4 extension could analyse where on the trajectory M₁ corresponds to. If the 1/3-point (N = N_e/3 ≈ 21 e-folds into the Hartle-Hawking phase) corresponds to a specific geometric feature in the analytic-continuation framework — e.g., a saddle, a zero of a specific function, or a structural intersection — then M₁ might emerge as the energy scale at that geometric feature.

This is a candidate investigation rather than a result. The feasibility of this Stage 4 analysis depends on extending the analytic-continuation machinery into the Hartle-Hawking sub-phase (which Stage 3 does not cover; Stage 3 covers only the locking transition y ∈ (0, N_lock)). This is the same investigation flagged in (B′) §6.5 as "candidate worked application — primordial perturbation spectrum"; M₁ emerging as a feature of the same calculation would be a natural by-product.

### 5.5 Honest summary

(E) provides a numerical candidate; the geometric derivation is open. Candidates 5.1 (S³ volume), 5.2 (three-Majorana), 5.3 (three-Sakharov), 5.4 (Stage 4) all merit investigation, but none currently closes Gap 1.

The (E) candidate's value to the framework: it sharpens Gap 1 from "open question with no leads" to "open question with a specific candidate to derive." Future structural work has a target.

---

## 6. Implications for the corpus

### 6.1 §17.5.15 sharpening (recommended for v10.7 or v10.8)

The §17.5.15 entry currently in eta v2 (and queued for v10.7 integration) reads:

> *"Negative result constraining the geometric pathway: simple power-law combinations M_Pl^a · v_EW^b with natural rationals (a, b) do not cleanly land at M₁; the closest, M_Pl^{1/2}·v_EW^{1/2} ≈ 5.5 × 10¹⁰ GeV and M_Pl^{1/3}·v_EW^{2/3} ≈ 9.3 × 10⁸ GeV, miss by factors of 9 and 6.5 respectively. This excludes pure Hopf-bundle-style power laws on M_Pl and v_EW alone as the geometric origin of M₁; the geometric handle (if any) must involve T_GB or another scale beyond M_Pl and v_EW."*

Recommended update once (E) is integrated:

> *"...the geometric handle (if any) must involve T_GB or another scale beyond M_Pl and v_EW. **A candidate structural lead**: M₁ ≈ (M_Pl² · H_GB)^{1/3} = α^{1/3} · M_Pl^{4/3} ≈ 8.08 × 10⁹ GeV (factor 1.33 high vs corpus M₁ = 6.06 × 10⁹ GeV; within the Davidson-Ibarra closure's intrinsic factor-2 precision). The candidate uses only M_Pl and H_GB (with H_GB = β_NTE·M_Pl² being a derived quantity) — exactly the geometric handles Gap 1 named, without requiring T_GB or v_EW. The cube-root weighting's geometric origin is open work; candidate derivations include S³ volume scaling, a three-Majorana-mass seesaw chain, or analytic-continuation features in the Hartle-Hawking sub-phase. Closing Gap 1 requires deriving the 1/3 weighting from S³ structure; (E) provides the target."*

This sharpening turns §17.5.15 from "negative result" into "negative result + structural lead." This is a stronger statement of the open work.

### 6.2 §22.5 sharpening (Gap 1 catalogue)

Corpus §22.5 currently states: *"M₁ from geometry: The leptogenesis scale M₁ = 6 × 10⁹ GeV is constrained, not derived. Should follow from S³ curvature radius and gauge birth temperature."*

Recommended addition: *"A numerical candidate (Jammer (E), May 2026) gives M₁ ≈ (M_Pl² · H_GB)^{1/3} ≈ 8 × 10⁹ GeV (factor 1.33 of the corpus value). The candidate uses M_Pl and H_GB, parallel to §22.5's geometric handles; the geometric origin of the 1/3 weighting is open structural work."*

### 6.3 Sequencing recommendation (Jammer)

The (E) candidate is structurally tied to (B′)'s findings: both involve the Hartle-Hawking sub-phase, both flag the N_e/3 e-fold count or Hartle-Hawking → gauge-birth ratio as a structural feature. Natural sequencing:

**Option A:** Pair (E) and (B′) in v10.8. Both honestly qualify the corpus's current presentations of M₁ and n_s as "candidates / imports requiring derivation" and surface specific structural targets. Eta v2 ships in v10.7 alone (positive rhetorical work); (B′) + (E) honesty/research-target work ships in v10.8 together.

**Option B:** (E) ships separately at v10.7 (paired with eta) since it's a positive structural lead that strengthens §17.5.15; (B′) ships at v10.8 alone. Reasoning: (E) augments the §17.5.15 entry already in eta v2 with a positive lead; it's not a downgrade.

**Option C:** (E) sits as Jammer's working note for now; v10.7 ships eta v2 alone with no (E) addition; v10.8 ships (B′) + (E) combined.

Jammer's preference: **Option B** — (E) is a structural sharpening of the §17.5.15 entry in eta v2 (turns the negative result into "negative result with candidate lead") and naturally pairs with eta v2 in v10.7. Greg's call.

---

## 7. Implications for downstream Jammer R&D

### 7.1 (D′) v2 candidate scope expansion

If Greg authorises (D′) v2 (per Handoff `Handoff_Jammer_to_AC_Bprime_Companion8_registration.md` §3.3), the proper Hartle-Hawking calculation in NTE's regime would be the central worked application. (E)'s candidate suggests a related question for (D′) v2: where does M₁ ≈ M_Pl · e^{−N_e/3} appear in the analytic-continuation framework? If the cube-root structure has a derivable origin in the Hartle-Hawking sub-phase calculation, (D′) v2 closes both (B′)'s n_s formula-import question AND (E)'s M₁ derivation simultaneously.

This would be a substantial finding — Hartle-Hawking → gauge-birth e-fold structure giving both n_s and M₁ from a single calculation. It does not yet close Gap 1, but it sharpens the target.

### 7.2 Stage 4 surface-ontology programme

The geometric origin of the 1/3 weighting may live in a Stage 4 extension of the surface-ontology programme — Stage 3's analytic continuation of z(y) into the Hartle-Hawking sub-phase (y ∈ (−∞, 0) in some natural coordinate). If a Stage 4 calculation produces a feature at N_e/3, M₁ emerges as the energy scale at that feature.

This is a candidate research arc, not a current deliverable.

### 7.3 Cross-derivation with M_R

The corpus's M_R = M_Pl^{3/4} · v_EW^{1/4} (Hopf bundle, line 1274) and the (E) candidate M₁ = (M_Pl² · H_GB)^{1/3} could in principle be derived from a common geometric structure. The {3/4, 1/4} split for M_R reflects S² base + S¹ fibre on Hopf S¹ → S³ → S². The {2/3, 1/3} split for M₁ might reflect a different bundle structure on S³ — perhaps S³ as a fibration over a 1-dim space, or S³ as a 3-volume directly. Investigating whether M_R and M₁'s exponents arise from related-but-distinct S³ structures is a natural unifying question.

---

## 8. Side finding: small numerical bug in eta v2 §17.5.15

While performing the (E) calculation, I noticed a numerical inconsistency in eta v2's §17.5.15 entry that the AC re-audit did not catch. Reporting for AC's correction before integration into v10.7 baseline.

### 8.1 The bug

eta v2 §17.5.15 (carried forward from eta-precondition-check worksheet) states: *"M_Pl^{1/3}·v_EW^{2/3} ≈ 9.3 × 10⁸ GeV (factor 6.5 low)"*.

Recomputation (Python, full precision):
- M_Pl^{1/3} = (1.22 × 10¹⁹)^{1/3} = 2.30 × 10⁶ GeV^{1/3}
- v_EW^{2/3} = (246)^{2/3} = 39.25 GeV^{2/3}
- Product: 9.04 × 10⁷ GeV (not 9.3 × 10⁸)
- M₁ target = 6.06 × 10⁹ GeV
- Ratio: 6.06 × 10⁹ / 9.04 × 10⁷ = **67** (not 6.5)

**The eta v2 entry has a factor-of-10 error in both the numerical value and the cited "factor X low" ratio.** Correct text:

> *"M_Pl^{1/3}·v_EW^{2/3} ≈ 9.0 × 10⁷ GeV (factor 67 low)"*

### 8.2 Severity assessment

**Severity: minor.** The qualitative conclusion of §17.5.15 (M_Pl^a · v_EW^b combinations excluded) is unchanged — a candidate that misses by factor 67 is even more conclusively excluded than one that misses by factor 6.5. The numerical correction strengthens rather than weakens the §17.5.15 finding.

**Routing:** AC should incorporate the correction during v10.7 baseline integration of eta v2 §17.5.15. No re-audit of eta v2 is needed; the bug is a numerical-precision item, not a structural finding.

### 8.3 Source of the bug (best guess)

The eta-precondition-check worksheet that produced the original numbers (Jammer R&D, May 2026) likely had an arithmetic slip — perhaps treating M_Pl as 1.22 × 10¹⁸ instead of 1.22 × 10¹⁹ for that one calculation, which would give 9.3 × 10⁷ (still not exactly matching the cited 9.3 × 10⁸, but within an order of magnitude of the bug). Or a typesetting error in transcription from worksheet to audit document.

The other §17.5.15 candidate (M_Pl^{1/2}·v_EW^{1/2} ≈ 5.5 × 10¹⁰ GeV, factor 9 high) is correct to my recomputation: 5.48 × 10¹⁰ GeV, ratio 9.04. So only the M_Pl^{1/3}·v_EW^{2/3} entry has the bug.

### 8.4 Discipline reminder

Lesson #12: *"AC's audit assertions need the same evidentiary discipline AC demands of other streams."* The AC re-audit verdict in `Handoff_AC_re-audit_verdict_eta_v2.md` confirms refinement compliance but does not appear to have re-verified the §17.5.15 numerical values (which were carried over from v1 unchanged). The bug propagated v1 → v2 → re-audit unflagged. (E)'s catch is a routine cross-check that the next ship cycle should perform.

This is not a criticism of AC's work — the re-audit's scope was refinement compliance, not numerical re-verification of carry-over content. But it's a useful reminder that numerical claims persist through audit cycles unless explicitly re-checked.

---

## 9. Awaiting

AC audit of:

(a) §3's search method — candidate space, exponent set, dimensional constraints — exhaustive of natural readings? Or are there scale combinations I should have considered (e.g., involving the dimensionless N_lock, or g* = 106.75 from corpus line 683)?

(b) §4's selection of (M_Pl² · H_GB)^{1/3} as the structural standout over (M_Pl · T_GB · H_GB)^{1/3} — does AC concur with the reasoning (T_GB ≈ 0.4 M_Pl is not an independent scale; the 3-scale match's near-exactness is overfit to Davidson-Ibarra precision)?

(c) §5's geometric-derivation candidates — substantive content correct? Are there candidates I have missed that AC sees from the corpus's structure?

(d) §6.1 and §6.2's proposed §17.5.15 / §22.5 sharpenings — wording aligned with §II.0 track-record-over-advocacy discipline? "Candidate structural lead" the right rhetorical class (vs claiming "Gap 1 partially closed" which would overclaim)?

(e) §6.3's sequencing recommendation — Option B preferred? (E) pairs with eta v2 in v10.7 vs separate timing?

(f) §8's bug catch — does AC concur the eta v2 §17.5.15 numerical error is real and the corrected text is right?

Greg's strategic call on:

(g) Whether (E)'s candidate earns corpus mention as a structural lead in §17.5.15 / §22.5 (with appropriate humility — "candidate to derive" not "Gap 1 closed"), or stays as a Jammer working note for now.

(h) Sequencing of (E) relative to (B′) and eta v2 — Option A/B/C from §6.3.

(i) Whether (D′) v2 takes on M₁ derivation alongside the n_s re-derivation as part of its scope (cross-listed with the (D′) v2 strategic call in `Handoff_Jammer_to_AC_Bprime_Companion8_registration.md` §3.4).

CR:

(j) Visibility. Pre-ship CR pass at v10.7 (if Option B) or v10.8 (if Option A/C) ship-readiness will be the first formal CR review of the (E) findings. CR adversarial discipline appropriate for the rhetorical question of whether the candidate earns "structural lead" status vs "honest numerical match without derivation" — these are different rhetorical classes.

— Jammer.

---

## 10. Companion files

- `m1_geometric_search.py` — Python search script that produces the candidate table in §3.2. Runs in <1s; reproducible. To be uploaded to `Working/` alongside this worksheet.

— End (E) Gap 1 / M₁ from S³ Geometry worksheet.
