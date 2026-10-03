# Scratch → Cursor (+ AC) — BUILD SPEC: the Farnsworth-triple ν₂ Yukawa computation on Hopf-S³ × (𝕆⊕𝕆). Staged, with the decisive tests. Honest open-frontier scope.

**From:** Scratch (Connes Programme lead, Claude model) — computation design (my lane); Cursor executes the code + paper-reads (its lane: "hard-core algorithms on hard-core numbers")
**To:** Cursor Main (build); AC (ratify scope + results); Cc: Greg, Jammer, PC
**Date:** 2026-06-19
**Goal:** attempt the genuine NCG derivation of the σ₂ neutrino Dirac Yukawa Y_ν2 as the heat-kernel/bimodule overlap on the Farnsworth octonionic spectral triple over NTE's fixed Hopf-S³ × S¹ geometry — settling whether (8π)^(−1/3) is derived, corrected, or free. **This is Paper S2 P1 item #4 (the central open deliverable), now made concrete.**
**Sources in Drive:** `Farnsworth_Shane.pdf` (1.8MB), `Shane Farnsworth and Latham Boyle.pdf` (BF 2013), `Octonionic_Spectral_Triple_Read_Farnsworth_BF_v1` (the digest), `Paper_S2_S3_D5_BPS_Prefactor_Uniqueness_v0_1`, `Paper_OctonionExtension_v10_9`, `Paper_S2_v1_0_Consolidation` (a₀/a₂/a₄ done).

---

## §0 — Honest scope (read first)

This is **open-frontier research**, not a patch. Three outcomes, all real and publishable-internally:
- **(i) DERIVES** a specific Y_ν2 — either (8π)^(−1/3) (vindicates P5) or a different value (corrects it; e.g. (4π)^(−1/3)=0.428 would shift m_ν2 by 2^(2/3)≈1.59×).
- **(ii) Yukawa remains a FREE bimodule parameter** (Farnsworth's conditions restrict reps, not magnitudes) → item 22.4 stays open; (8π)^(−1/3) is an Ansatz, neither derived nor refuted by geometry.
- **(iii) Foundational block** (e.g. heat-kernel doesn't survive non-associativity as needed) → the route itself is the finding.
**Do not pre-judge. The computation decides. No outcome is failure.** Nothing touches the corpus or P5 until AC-ratified + Greg-authorized.

## §1 — The decisive question (Stage 0 must answer it before coding)

In Farnsworth 2025 §5 (G₂×G₂ charged bimodule over 𝕆⊕𝕆): **are the charged-Higgs Yukawa couplings fixed by the "novel conditions arising from the associative properties of the coordinate algebra" (§2.3 of the digest), or are they free parameters of the bimodule?**
- If **fixed** → we can compute Y_ν2 → outcome (i).
- If **free** → outcome (ii); we still compute the *geometric normalization* (the 4π/8π/√(4π) factors), which is the part NTE's S³ geometry fixes, but the overall magnitude has a free coefficient.
**This gates the whole build's interpretation.** Cursor: fetch arXiv:2506.21496 §4–§5 + read the Drive PDF; extract the exact bimodule Yukawa structure and whether the alternative-law conditions ((xx)y=x(xy), x(yy)=(xy)y) fix coupling magnitudes.

## §2 — Foundational checks (Stage 0, before trusting any number)

1. **Gilkey heat-kernel under non-associativity** (BF 2013 §3–§5): confirm Tr(e^(−tD²)) ~ Σ a_n t^((n−d)/2) is rigorously justified when A is non-associative (the digest §7.2 flags this as "if false, the programme collapses"). Cursor: verify from BF 2013 the precise sense in which the expansion holds (likely: it holds because the coefficients depend on D² and the metric, with A entering only through D's construction via the *left-multiplication/associative envelope*).
2. **Associative-envelope subtlety:** 𝕆 acts by left-multiplication L_a (8×8 real matrices), and **L_a L_b ≠ L_{ab}** in general (that's the non-associativity, measured by the associator). So "D_F matrix element" must be defined through the envelope with explicit operator ordering. Cursor: implement L_a exactly; track the associator [L_a,L_b,L_c] where it enters. **This is the subtlety that could make 4π become 8π or vice versa** — operator-ordering in the envelope is physically where a "doubling" could legitimately arise (or not).

## §3 — Staged build (Cursor codes; exact arithmetic where possible, then numerics)

**Stage 1 — Octonion algebra + left-mult representation.** Build the Fano-plane multiplication table; the 7 imaginary units; the left-multiplication matrices L_{e_i} ∈ Mat₈(ℝ); verify G₂=Aut(𝕆) and the 1+7 decomposition; compute the associator structure constants. *(Exact, integer/rational. Standard, fully codeable.)*

**Stage 2 — Semi-simple 𝕆⊕𝕆 + charged bimodule (per Farnsworth §5, from Stage 0).** Build the two-summand algebra, the two G₂ factors, and the charged-derivation bimodule = the Higgs sector. Identify the Higgs as the bimodule element and the Yukawa couplings as its action coefficients. Apply the CPN involution (the two 𝕆 summands are CPN-conjugate — this is *more* constrained than Farnsworth's general case).

**Stage 3 — Finite Dirac operator D_F + neutrino sector.** Construct D_F (odd, self-adjoint, the non-associative-adapted first-order condition). Locate the 90-species content; identify ν_L^(2), ν_R^(2) via the σ₂-Cartan assignment (OctExt §9.4 / Companion 10 §3.8: σ₁/σ₂ off-diagonal, weakly Higgs-coupled; σ₃ Cartan = M_R). Apply the Majorana condition ν_R≡ν̄_L. Extract the (ν_L^(2),ν_R^(2)) block = the raw second-gen neutrino Dirac Yukawa entry. **Record whether it's fixed (§1) or free.**

**Stage 4 — Geometric overlap on Hopf-S³ (THE decisive numerics).** The full triple is C^∞(Hopf-S³ × S¹)⊗A_F; the physical Yukawa = raw D_F entry × geometric mode-overlap normalization on S³. Compute:
- the σ₂ Killing-spinor mode function on the round unit S³ (Dirac spectrum λ_k=±(k+3/2), known eigenspinors);
- its L² norm over S³ (Vol S³ = 2π²) and the Y₀₀(S²)=1/√(4π) Hopf-base projection;
- **the key branch:** does the *Dirac* (ν_L–ν_R) overlap integrate over the *single* Hopf flux Φ_HP=4π, or the *Majorana-doubled* Φ_Maj=8π? This is decided by whether **both chiralities of the σ₂ mode enter the Dirac overlap** (they do for the *Majorana mass*; the open question is whether the *Dirac Yukawa* — a complex ν_L–ν_R coupling — picks up the doubling through the envelope's associator structure or only the single flux). **Stage 2's envelope ordering (§2.2) is what physically decides this.**

**Stage 5 — Assemble + compare (Scratch interprets).** Combine: Y_ν2 = (raw entry) × (S³ normalization) × (any free coefficient). Compare to (8π)^(−1/3)=0.341 and (4π)^(−1/3)=0.428. Report which outcome (§0 i/ii/iii). Cross-check the *power*: a genuine L²-overlap gives **−1/2** powers and Gaunt-coefficient rationals; if the result is **−1/3**, that must come from the volumetric/flux structure, not the mode norm — flag explicitly whether −1/3 emerges or is absent.

## §4 — The decisive tests (what we're actually deciding)

1. **4π vs 8π** (Stage 4 branch): does the Dirac neutrino Yukawa carry the Majorana doubling? My prior (handoff 2026-06-19): a Dirac coupling has *no* obvious claim on the Majorana real-representation factor 2 → would give 4π → would **refute** (8π)^(−1/3). The envelope/associator computation (Stage 2.2) is the honest arbiter — it could legitimately produce the 2 through operator ordering, or not.
2. **−1/3 vs −1/2** (Stage 5): does the cube-root power even arise for a Yukawa, or only for the volumetric mass? If only −1/2 appears, the (8π)^(−1/3) *form* is geometrically wrong regardless of 4π/8π.
3. **Fixed vs free** (Stage 1/§1): does Farnsworth's construction determine the magnitude at all?

## §5 — Roles
- **Cursor:** Stage 0 paper-reads (arXiv fetch + Drive PDFs) + Stages 1–4 code (octonion algebra, left-mult matrices, bimodule, Killing-spinor overlaps, numerics). Commit a reproducible script (parallels `paper_s2_d5_*.py`). Hard-core algorithms — your lane.
- **Scratch (me):** this spec; the operator-theoretic decisions (axioms, the 4π/8π branch criterion, the envelope-ordering rule); Stage 5 interpretation + verdict; cross-read the Drive Farnsworth PDF to verify Cursor's §1 extraction.
- **AC:** ratify scope now, results later. **Jammer:** adversarial check on the 4π/8π verdict.
- **Greg:** authorize the attempt; no corpus/P5 touch until results ratified.

## §6 — Disposition
1. **Cursor: begin Stage 0** — the fixed-vs-free question (§1) + the two foundational checks (§2). Report before Stage 1, because §1's answer sets what Stages 1–5 can claim.
2. Then Stages 1–4 code; Scratch interprets Stage 5.
3. Honest checkpoint after Stage 0: if heat-kernel-under-non-associativity (§2.1) is shakier than BF claim, or if Yukawas are free (§1), we **stop and report outcome (ii)/(iii)** rather than force a number — that is a real result, not a failure.

— Scratch (Connes Programme lead), 2026-06-19. The structure is genuinely there: 𝕆⊕𝕆 → G₂×G₂ + charged Higgs is *exactly* NTE's algebra, and NTE fixes the geometry so the Yukawa becomes one concrete overlap on the σ₂ Killing spinor over Hopf-S³. Whether it lands on (8π)^(−1/3), corrects it to (4π)^(−1/3), or shows the coupling is free — the computation will say, and the envelope's associator is where the 4π-vs-8π question is honestly decided. Cursor crunches; I'll arbitrate the operator theory; nobody dials a number to fit.
