# Companion 5 flatness derivation — Jammer (adversarial) verdict

**From:** Jammer · **To:** AC · **Cc:** Greg, Scratch, PC · **Date:** 2026-09-24
**Answers:** `Handoffs\Directive_AC_to_Scratch_Jammer_Companion5_Flatness_Derivation_Sunshine_Audit_20260924.md`
**Source read in full:** `Core_Papers\Companion_05_StateSpace_v10_19_0.md`
**Blind:** Scratch's lane not read.
**Register:** standard GR/FRW. No new commitments.

## Forks
AC's four, as pre-registered in the directive: (1) the bilateral argument bears on curvature; (2) the two quantities are conflated and the derivation fails; (3) the dynamical route survives alone; (4) the question is undetermined. Jammer registers no additional fork.

## Headline: fork 2, and slightly worse than AC suspected

Both routes fail. The "zero total energy" intuition is correct physics, but it points the other way: in GR, **any closed universe has zero total energy identically**. Properly stated, it supports item 11 (closure, Ω_k < 0) and not flatness. Companion 5 is also **self-contradictory**: it identifies the universe with a finite closed S³ (abstract, §1, §2) and asserts exact Ω_k = 0 (abstract, §4, §9).

---

## Q1 — does bilateral zero energy imply anything about curvature?

**No.** Companion 5 conflates three quantities, not two.

| # | Quantity | What it constrains |
|---|---|---|
| (i) | **Bilateral CPN sum:** energy, charge and baryon number of the pair vanish (§5) | Additive conserved quantities that are odd under CPN |
| (ii) | **Newtonian shell energy:** per unit mass, ½ȧ² − (4πG/3)ρa² = −k/2. E = 0 ⟺ k = 0 | One sector's k, in the Newtonian analogy |
| (iii) | **GR total energy of a closed universe:** vanishes identically for any k = +1 FRW. There is no asymptotic region and no ADM energy; the Hamiltonian constraint makes the sum zero (Tryon 1973 and the standard literature) | Nothing about k, except that it is automatic for closed slices |

§4's step, "zero total energy requires zero spatial curvature", uses (ii). Its premise is (i). And (iii) refutes the step on the corpus's own geometry: the S³ that Companion 5 identifies as the universe already has zero total energy **with k = +1**.

**Charitable reconstruction, tested and failed.** One could argue that the matter energies cancel bilaterally (E_A = −E_B), and that the curvature contribution must therefore vanish to keep the total at zero, which forces k = 0. This fails twice:
- **Curvature is CPN-even.** The metric is invariant under both the antipodal map and N → −N. So the two sectors carry the **same** k, and the curvature terms add rather than cancel. Nothing in the sum can force them to zero while the matter terms cancel.
- **Negative energy density is inconsistent.** Literal E_A = −E_B for matter energy density puts one sector at ρ < 0, which contradicts each sector's own Friedmann constraint H² = 8πGρ/3 − k/a² with real H, unless ρ = 0. The bilateral "zero energy" must therefore mean (i) for conserved charges, or (iii). Neither touches k.

## Q2 — is the Euler identity doing work?

**For the flatness conclusion: (c), decoration. For CPN: (b), notation.**
- e^{iπ} = −1 is the antipodal map, and §5 uses it correctly as such.
- The only additional content of "+1 = 0" is z + (−z) = 0: a point and its antipode sum to zero. That is a statement about **odd** quantities summing to zero across the pair, i.e. quantity (i).
- Curvature is **even**, so the identity cannot reach it. This is the same pattern as the retired six-note chord and the √6/π characterisation: an identity attached to a conclusion reached another way. The conclusion here was not in fact reached.

## Q3 — the dynamical route, H(N) = β_NTE|Φ_NTE|²

**Fails, independently of Q1.**
- **The constraint sets H, not k.** In H² = (8πG/3)ρ − k/a², it fixes the left-hand side and leaves the curvature term free.
- **It is a relabelling.** By Part 1 §2.3 it is an identity once |Φ|² ≡ v_EW² H/H₀: a renaming of whatever expansion history occurs, including any curvature contribution. A relabelling cannot constrain the thing it relabels.
- **The "maintained" claim is false.** §4 says the Hubble relation "explains how flatness is maintained". But |Ω_k| ∝ 1/(aH)² **grows** during radiation and matter domination (∝ a and ∝ a^{1/2} respectively in conformal-time terms; ∝ a² and ∝ a in aH). This is the flatness problem, and nothing in H = β|Φ|² addresses it.
- **What actually drives |Ω_k| small in NTE is inflation**, via Companion 17's plateau: ordinary dilution by e^{−2N}. It is imported, not derived.

## Q4 — reconciliation

- **Asymptotic sense: yes, defensible.** Ω_k → 0⁻ from inflationary dilution. |Ω_k| ≲ 0.004 needs N_total ≳ 64 (T1). This is standard inflation, stated as such, not a boundary-condition derivation.
- **Magnitude: not constrained.** |Ω_k| ≈ e^{−2(N_total − N_min)} × O(10⁻³). N_total is not fixed: P2 found that selection is an open measure question, and the crossing datum carries at most one real number, already spent (P1–P4, BC recast). **NTE constrains the sign only (closed → Ω_k < 0), as AC expected.**
- **On the positive central value.** Planck + BAO 0.0007 ± 0.0019 is 0.4σ from zero and not in tension with Ω_k < 0. Item 11's falsifier is practical only above the curvature-measurement floor (about 10⁻⁴, set by horizon-scale fluctuations). A **confirmed** Ω_k > 0 at several ×10⁻⁴ or more falsifies; anything below that floor is untestable. Item 11's wording should carry the floor.

## Q5 — replacement text (Greg ratifies; AC authors the patch)

**Every flatness claim in Companion 5:**

| Location | Current | Replacement |
|---|---|---|
| Abstract | "Flatness (Ω_k = 0) is required by the Euler closure condition on S³." | "The closed S³ requires Ω_k < 0 strictly; its observed smallness (\|Ω_k\| ≲ 10⁻³) is inflationary dilution, not a derivation from the boundary identification." |
| §4 **Flatness** paragraph | Euler identity → zero energy → Ω_k = 0; "derives flatness both dynamically … and topologically" | "**Curvature.** The universe is a closed S³ of finite radius, so Ω_k < 0 strictly. Its total energy vanishes identically, as for any closed universe (the Hamiltonian constraint; there is no asymptotic energy). That is a consequence of closure and says nothing about the magnitude of curvature. The observed \|Ω_k\| ≲ 10⁻³ follows from the ≳ 64 e-folds of inflation (Companion 17), standard dilution imported rather than derived. Neither the antipodal identity e^{iπ} = −1 nor the Hubble constraint H = β_NTE\|Φ_NTE\|² constrains spatial curvature." |
| §5 "the CPN-identified boundaries (N → 0 and N → ∞), both flat" | "both flat" | "both **conformally** flat" (Weyl = 0). This is correct as physics, but the word "flat" invites the Ω_k reading. |
| §8 list | "flatness (Euler closure)" | "closure (Ω_k < 0; magnitude by inflation)" |
| §9 falsifier | "Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification)." | "**Spatial closure.** NTE requires Ω_k < 0. A confirmed Ω_k > 0 above the measurement floor (~10⁻⁴) falsifies the closed-S³ identification. Ω_k consistent with zero is expected, and neither supports nor disfavours." |

## Collateral (outside Companion 5; for AC)

- **Manifest §3** still lists "Ω_k = 0" under **Derived / structural**. It should move to match Part 3's patched wording.
- Grep the deposit set for "flatness", "Ω_k = 0" and "Euler identity" / "Euler closure" before any re-render. Companion 5 is unlikely to be the only carrier: Parts 1–2 and the popular editions may repeat it.

## Sunshine, at its true size
The "zero energy" intuition is right: a closed universe is a zero-energy universe. Correctly placed, it **supports item 11** and is internally coherent with the S³ ontology. It is not NTE-specific (Tryon, Hartle–Hawking), so it is **imported, not derived**. And it gives **no magnitude**. That is the most that survives.

— Jammer, 2026-09-24
