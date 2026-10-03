# Farnsworth Stage 0 — Charged-Higgs Yukawa: Fixed vs Free (G₂×G₂ over 𝕆⊕𝕆)

**Author:** Cursor Jammer  
**Stream:** ac_jammer  
**Task:** JAMMER-FARNWORTH-S0  
**Date:** 2026-06-20  
**Sources:** Farnsworth (2025) arXiv:2506.21496 §4–§5 + Appendix E; Boyle–Farnsworth (2013) JHEP 07 (2015) 023 §3–§4.3 (`SeedPapers/2506.21496v1.pdf`; `SeedPapers/NCG/Non-Associative Geometry and the Spectral Action Principle.pdf`)  
**Upstream:** `Handoffs/Handoff_Scratch_to_Cursor_AC_BUILD_SPEC_Farnsworth_Triple_nu2_Yukawa_HopfS3_Octonion_Octonion_Staged_DecisiveTests_20260619.md`

---

## Stage 0 verdict

**Answer: MIXED** (representation / sector structure **FIXED**; coupling **magnitudes FREE** within Hermiticity and ϵ′ constraints)

**Qualifiers:**

| Layer | Fixed by alternative-law / specialization / Leibniz–bimodule conditions | Still free |
|-------|---------------------------------------------------------------------------|------------|
| **Allowed scalar reps** | Charged vs uncharged sector; reconstituted vs split bimodule class; which DF block patterns carry G₂×G₂ charge | — |
| **Bimodule product form** | Reconstituted left/right actions (Eqs. 115–116, 122–123); involution forces **S = ½** (not a continuous family) | — |
| **Discrete sign choices** | ϵ′_F = ±1 splits D± sectors (Eqs. 111–112, 113); ϵ′ = ±1 selects derivation-compatible branch (§5.2.1 vs §5.2.2) | Which branch NTE selects (CPN may narrow) |
| **Dirac / Higgs coefficients** | Block off-diagonal Hermitian structure; Φ_IJ constrained by **F J = ϵ′ J F** (Appendix E) | Real matrix elements **M_IJ** in Eq. (92); symmetric **κ(ab)** in derivations (Eqs. 79–80); fluctuation coefficients **Φ_IJ** magnitudes |

**Bottom line for NTE Paper S2 item #4:** Farnsworth's "novel conditions arising from the associative properties of the coordinate algebra" (abstract; specialization Eq. (1); alternative Leibniz rule Eq. (95)) **restrict which Yukawa/Higgs structures exist and which are charged under G₂×G₂** — they do **not** fix the numerical Yukawa magnitudes. Outcome **(ii)** of the BUILD SPEC applies to **(8π)^(−1/3)** as an overall magnitude: geometry may fix **4π vs 8π** normalization (Stage 4), but the internal **M_IJ / κ / Φ** scale remains a **free bimodule/spectral-data parameter** unless NTE's CPN-constrained 𝕆⊕𝕆 embedding adds further fixation (not shown in Farnsworth §4–§5).

---

## Evidence from Farnsworth §4–§5

### §4.1 — Internal data and free Dirac matrix

Coordinate algebra **A_F = 𝕆 ⊕ 𝕆** on **H_F = A_F** with left/right octonion actions (Eqs. 84–89). The finite Dirac operator is the general Hermitian off-diagonal form

> **DF = M_IJ** (0, e_I ⊗ e*_J ; e_J ⊗ e*_I, 0) — Eq. (92),

with **real coefficients M_IJ** not determined by the alternative identities alone. The Leibniz constraint (Eqs. 93–95) links DF to the bimodule of 1-forms but leaves the **M_IJ** as input spectral data.

### §4.2 — Uncharged case: explicit "free parameter"

Restricting to nucleus-only DF (Eq. 102) yields **[D_F, δ′_ab] = 0** — Dirac blind to G₂×G₂. The paper states directly:

> *"this Dirac operator would give rise to a single, real, uncharged Higgs field corresponding to the **single free parameter in the internal space M_00**"* (§4.2, after Eq. 103).

This is the clearest in-text admission that **magnitude is not fixed** by alternative-law structure in the simpler sector.

### §4.3 — Charged case: structure fixed, S fixed, M_IJ still free

Using imaginary octonion units (D± split, Eqs. 111–112) breaks **[D_F, δ′_ab] = 0** → **charged Higgs** (§4.3 closing paragraph; Appendix E). Key steps:

1. Specialization / alternative identity rewrites the obstructing associator term (Eq. 110).
2. An **infinite family** of bimodule products parameterised by **S** is compatible with Hermitian D_F (Eq. 1004 area: *"We have found an infinite family of bimodule products parameterised by S"*).
3. **Involution extension forces S = ½** — discrete fixation, not a continuous Yukawa prediction.
4. Charged sector confirmed: *"DF … will no longer commute with the lifted derivations … will give rise to a gauge theory with **charged Higgs fields**"* (§4.3 end).

**No statement fixes M_ij, M_0i, M_i0, or M_00 to specific numbers** — only their **pattern** (which blocks are nonzero) and compatibility with **D_F J_F = ϵ′_F J_F D_F**.

### §3.4 / §5 — Derivation coefficients κ(ab) free

For split/reconstituted bimodules over 𝕆⊕…⊕𝕆, derivations have a **unique form up to coefficients**:

> *"We see that **up to the coefficients κ(ab)** there is a single unique form that derivations can take from A into A ⊗ A"* (§3.4, after Eq. 80).

Standard case sets all κ(ab) = 1; physical models can rescale per (ab) block. §5.2 reconstituted maps **Φ_cd ∘ ∆_κ** inherit the same **κ(cd)** freedom.

### §5 — Formal charged bimodule; representation selection, not magnitude

Section 5 defines **reconstituted alternative bimodules** over **A = ⨁_i 𝕆** (Eqs. 121–123), with §4.3 1-forms as the **V_12 = V_21 = ℝ** case. Automorphism covariance (Eqs. 129–130) and ϵ′ = ±1 branching (§5.2.1 / §5.2.2) fix **which (7,7) or (7,1) representation** charged derivations occupy — not their overall scale.

### Appendix E — Higgs from fluctuations; partial constraint only

Gauge theory completion (Eqs. 188–193): Higgs **Φ_IJ(x)** appear in fluctuation **F** with structure tied to **D_F** off-diagonal blocks. Coefficients are *"constrained such that F J = ϵ′ J F"* — **compatibility constraint**, not a unique numerical prediction. Dynamics follow from spectral action on **D + F** (Eq. 193–195); Yukawa-like fermion–scalar couplings inherit **free internal spectral data**, not values fixed by alternative laws alone.

---

## BF 2013 heat-kernel under non-associativity

**Check: PASS** (brief)

BF §4.3 (*The spectral action*) states that after constructing the fluctuated **D_A** from non-associative representation data, **non-associativity need no longer enter the heat-kernel step**:

> *"From this point on, as far as evaluating the spectral action is concerned, all we need to know is that H is an ordinary Hilbert space, and D_A is an ordinary linear operator on H … **Theorems 3.3 and 3.7 directly apply**."*

The Seeley–deWitt expansion **Tr f(D_A/Λ) = Σ f_n Λ^(4−2n) a_n(D_A²)** (Eq. 4.10) proceeds on **D_A²** as in the associative almost-commutative case. Non-associativity enters **upstream** (representation, derivation-based gauge/Higgs fluctuations, §3.4); the Gilkey coefficients depend on **D_A²** and the metric, not on (ab)c = a(bc) in the algebra product.

**Caveat (NEEDS-MORE scope, not FAIL):** BF's worked example has **D_F = 0** (no Higgs/mass); Farnsworth 2025 charged **D_F ≠ 0** extends the fluctuation sector. The **heat-kernel mechanism** still applies once **D + F** is a standard self-adjoint operator on **H** — but NTE Stage 3 must implement the **envelope/ordering** for **L_a L_b ≠ L_{ab}** per BUILD SPEC §2.2. That is implementation subtlety, not a BF collapse of the expansion.

**Programme implication:** Outcome **(iii)** (foundational block) is **not** triggered at Stage 0 on heat-kernel grounds.

---

## Gates interpretation for Stages 1–5

| Stage | If magnitudes FREE (this memo) | Gate |
|-------|----------------------------------|------|
| **1** Octonion algebra + L_a | Proceed — exact infrastructure | **OPEN** (coding) |
| **2** 𝕆⊕𝕆 bimodule | Proceed — implement reconstituted actions (S=½, ϵ′ branch) | **OPEN**; record **M_IJ, κ(ab)** as explicit free inputs |
| **3** D_F neutrino block | Extract **raw** ν_L^(2)–ν_R^(2) entry from chosen **M_IJ** | **Interpretation gate:** magnitude is **Ansatz-scaled**, not derived |
| **4** Hopf-S³ overlap | **Decisive for 4π vs 8π geometric normalization only** | Can **refute or support (8π)^(−1/3) power prefactor**; cannot derive absolute Y_ν2 without fixing free **M_IJ** |
| **5** Assemble + compare | Report **(ii)** unless NTE CPN/σ₂ constraints fix **M_IJ** independently | **(8π)^(−1/3)** remains **Ansatz** for magnitude; geometric branch still testable |

**Fixed-vs-free gate (BUILD SPEC §1):** **CLOSED at MIXED/FREE-magnitude** — Stages 1–4 may run for **structural + geometric normalization**; Stage 5 **must not** claim a derived **Y_ν2** numeric without an additional NTE fixation mechanism.

---

## Recommendation

**Proceed to Stage 1** — with **outcome (ii) flagged for magnitude**.

- **Do not stop** at outcome (iii): BF heat-kernel PASS.
- **Do stop** claiming **(8π)^(−1/3)** is derived from Farnsworth alone: report **outcome (ii)** for the overall Yukawa scale after Stage 5 unless CPN/σ₂ embedding fixes **M_IJ**.
- **Still run Stages 1–4** — the **4π vs 8π** and **−1/3 vs −1/2** decisive tests (BUILD SPEC §4) remain meaningful on the **geometric/overlap** side even when internal magnitudes are free.

---

## Files read

- `SeedPapers/2506.21496v1.pdf` — full text extract, §4–§5 + Appendix E
- `SeedPapers/NCG/Non-Associative Geometry and the Spectral Action Principle.pdf` — §3.4, §4.3

— Cursor Jammer, 2026-06-20.
