# G₂ rank obstruction: VERDICT (Jammer, lead). **R-3: a real obstruction**, computed

- Directive: Handoffs\Directive_AC_G2_Rank_Obstruction_Can_G2_Reach_The_Standard_Model_Group_20261016.md
- Pre-registration: Working\G2_Rank_Obstruction_PREREGISTRATION_Claude_Jammer_Lead_20261016.md (filed before the reads and computations below).
- I have not read Scratch's or Cursor Main's filings on this directive.

## 0. Read set and method
- Core_Papers\Companion_16_Octonion_Gauge_Species_v10_19_0.md: modified 2026-10-06. I read it in full today; my copy's byte count (16825) matches Drive.
- Core_Papers\NTE_v10_19_0_Part1_Foundations.md: modified 2026-10-08. I read it in full today, freshly from Drive.
- B2 basis, both read in full today:
  - Handoffs\Arbitration_AC_Doublet_CLOSED_B2_Rider_Withdrawn_Permanently_Exit_a_Structurally_Unavailable_Plus_Method_Rule_20260927.md
  - Handoffs\Reconciliation_Scratch_vs_Jammer_Doublet_CONVERGE_not_B1_Scratch_CONCEDES_B3_to_B2_after_reading_Companion16_sect3_20260927.md
- Not read this session: closure record v2 §2.6. Its correction is named below only through the B2 Manifest §10 text that AC's arbitration quotes.
- Computation: I built explicit octonion structure constants (Fano triples (123)(145)(176)(246)(257)(347)(365)), then checked that the algebra is normed and alternative (residuals ~1e-15). I solved D(xy)=D(x)y+xD(y) for der(𝕆) and ran the subalgebra tests numerically.
  - Scripts: scratchpad g2/g2.py and g2/g2b.py (on the container, not the corpus).
  - Every number below is from those runs.

## 1. What the deposit claims (quoted from the current-state read)
- **C16 §3 title:** "Gauge group: G₂ → SU(3)_C × SU(2)_L × U(1)_Y".
- **C16 §3.3:** "The physical spatial boundary is S³ ≅ SU(2), the unit quaternions, embedded in S⁷; the corresponding SU(2) is **one factor of SO(4) ⊂ G₂, identified with SU(2)_L**. The complex line ℂ = span{1,e₁} gives U(1)_Y."
- **C16 §3.3:** "S³ here is forced, not fitted … the same ℍ whose SU(2) factor is SU(2)_L."
- **C16 §3.4:** "the gauge group is *forced* in a conditional sense …"
- **C16 §3 header:** "NTE derives the gauge group octonionically via the G₂-stabiliser route."
- **C16 §9:** "quaternionic S³ → SU(2)_L" is retained from the draft.
- **Part 1 §II.0:** "Simplifications that earned their place: **the gauge group from G₂**".
- Elsewhere in Part 1 (abstract and closing note) the gauge group is "adopted and credited from the division-algebra programme" and "credited as imported". Those two loci are not false as worded.
- **C6 §8** (read in full yesterday, file unchanged): "The Standard Model gauge group is therefore forced by 𝕆 plus the Janus boundary plus temporal emergence."

So the deposit does not claim G₂ → SU(3) only. **R-1's premise fails on the text.** C16 §3.3 places SU(2)_L inside G₂ explicitly, and takes U(1)_Y from the e₁ structure.

## 2. Computed results
| # | Quantity | Result |
|---|---|---|
| 1 | dim der(𝕆) | **14** |
| 1 | rank (dim of the centraliser of a generic element) | **2** |
| 2 | dim Stab(e₁) | **8** (su(3)). It commutes with L_{e₁} on e₁⊥ (residual 5e-16), so it acts complex-linearly on ℂ³. Casimir on 𝕆: 0 on {1, e₁}, equal on the remaining 6, so 7 → 1 ⊕ 3 ⊕ 3̄. **The deposited decomposition is correct.** |
| 3 | dim Stab(ℍ), ℍ = span{1,e₁,e₂,e₃} | **6** (so(4)), which splits into two commuting su(2) ideals A and B |
| 3 | A | Fixes ℍ **pointwise** and acts only on ℍ⊥: 4 = two doublets |
| 3 | B | Acts on Im ℍ as a triplet (adjoint) and on ℍ⊥ as doublets |
| 3 | Branching of Im 𝕆 under A×B | **(1,3) ⊕ (2,2)**: doublets of *both* factors |
| 4 | dim Stab(e₁) ∩ Stab(ℍ) | **4** (u(2), inside su(3)) |
| 5 | **Centraliser of Stab(e₁) in g₂** | **0** |
| 5 | ‖[A, Stab(e₁)]‖_max, ‖[B, Stab(e₁)]‖_max | **0.34 and 0.27**: neither factor commutes with colour |
| 5 | dim span(Stab(e₁) + Stab(ℍ)) | 10: not a direct product |
| 6 | Is left multiplication by imaginary unit quaternions (L_{e₁}, L_{e₂}, L_{e₃}) in g₂? | **No.** Residual 2.83 each, and dim(g₂ + span L) = 17, so the intersection is trivial |

## 3. Ruling: **R-3**
1. **SU(2)_L does not commute with SU(3)_C in the deposited construction.** The SO(4) factor that C16 §3.3 names as SU(2)_L does not commute with Stab(e₁) = SU(3)_C. This holds for both factors (row 5).
   - Inside G₂, the only SU(2)×U(1) that coexists with the colour SU(3) is Stab(e₁) ∩ Stab(ℍ) = U(2) (row 4). That U(2) is a **subgroup of colour**, not a commuting factor.
   - This is the rank obstruction made concrete: 2 < 4. No subgroup of G₂ is SU(3)×SU(2), let alone the SM group.
2. **U(1)_Y has no realisation in G₂ that commutes with colour.**
   - The centraliser of Stab(e₁) in g₂ is zero (row 5).
   - "The complex line span{1,e₁} gives U(1)_Y" cannot denote an automorphism rotating that line, because automorphisms fix 1.
   - The only U(1) available is the centre of the U(2) in row 4, which lies inside SU(3)_C.
3. **The S³ identification fails as well.**
   - C16 §3.3 and C2 identify "S³ ≅ SU(2), the unit quaternions" with the SU(2) factor.
   - The SU(2) of unit quaternions acting on S³ (left multiplication) is not in G₂ at all (row 6).
   - Of the SO(4) ⊂ G₂ factors, A acts on ℍ (hence on S³) **trivially**, and B acts on it by **conjugation**, fixing ±1.
   - Neither is the SU(2) that acts on S³ as SU(2) acts on itself. "The same ℍ whose SU(2) factor is SU(2)_L" and "S³ … forced, not fitted" do not survive.
4. **The colour part survives.** G₂ ⊃ SU(3) and 7 → 1⊕3⊕3̄ are correct (row 2). This is the Günaydin–Gürsey content.

**Why this is not R-2.** The defect is not just a sentence that overstates a sound construction. The construction in §3.3, with SU(2)_L from SO(4) ⊂ G₂ and U(1)_Y from e₁, is what fails. A sound construction would need SU(2)_L and U(1)_Y from **outside** G₂. The deposit does not provide one. Its §3 header says it uses "the G₂-stabiliser route".

**Repair path (for Stage 4; not ruled).** C16's own references obtain the electroweak factors elsewhere [unverified-session: Cursor Main's literature leg should confirm]:
- Furey: ℂ⊗𝕆 / ℂ⊗ℍ⊗𝕆 and Cl(6) ideals.
- Dubois-Violette–Todorov: SM group as the subgroup S(U(2)×U(3)) of F₄ = Aut(J₃(𝕆)) preserving a ℂ ⊂ 𝕆 splitting.

Adopting either would make "gauge group adopted and credited" true. It would also make "from G₂" and "forced by 𝕆 + Janus + temporal emergence" false.

## 4. Loci that fail (named per AC's request)
- C16 §3 title; §3 header ("G₂-stabiliser route"); §3.3 SU(2)_L and U(1)_Y sentences; §3.3 "forced, not fitted … the same ℍ whose SU(2) factor is SU(2)_L"; §3.4 "forced"; abstract "With the quaternionic subalgebra ℍ ⊃ S³ ≅ SU(2) … the observable gauge group is …"; §9 "quaternionic S³ → SU(2)_L".
- Part 1 §II.0: "the gauge group from G₂" as an earned simplification. Under R-3 it is not a simplification; at most it is "colour from G₂; electroweak imported".
- C6 §8: "forced by 𝕆 plus …"; C2 §7.2: "G₂ breaks … to deliver SU(3)_C × SU(2)_L × U(1)_Y". Both were already graded NP yesterday, and this adds a further reason.
- Class re-examination: C16 §3.3 "Parity. The two factors of SO(4) are SU(2)_L and SU(2)_R" also fails.
  - Neither factor is a left- or right-handed electroweak SU(2) commuting with colour (row 5).
  - The factors are not even symmetric under exchange: A is trivial on ℍ, B is adjoint on Im ℍ (row 3).
  - The CPN parity assignment therefore has no deposited group to act on. It rests on the same failed identification. Companion 16 §7 inherits this, since its σ₃ reading is "SU(2)_L-internal".

## 5. B2 doublet ruling: **the conclusion survives; the basis needs correction** (B-b, not B-c)
- The B2 basis (AC arbitration, 2026-09-27) has four legs:
  1. SU(2)_L's ℍ is selected at gauge birth (C16 §3.3).
  2. U(1)_Y needs e₁ at gauge birth (§3.2).
  3. L/R needs CPN at gauge birth (§3.3).
  4. "Im(𝕆) = ℝ⁷ → 1 ⊕ 3 ⊕ 3̄ … No doublet in the decomposition."
- **Leg 4 is vacuous.** SU(3) contains no SU(2)_L, so the absence of doublets in its branching says nothing about SU(2)_L doublets. Relative to the SO(4) that C16 names as SU(2)_L's host, it is **false**: Im 𝕆 = (1,3) ⊕ (2,2) contains doublets (row 3). The arbitration's own clause "SO(4) ⊂ G₂ scaffolds an SU(2) multiplet" already half-concedes this.
- **Legs 1–3 lean on C16 §3.3,** whose SU(2)_L and U(1)_Y identifications fail (§3 above).
- **The conclusion still holds, a fortiori.** The deposit contains no structure that yields an SU(2)_L × U(1)_Y commuting with SU(3)_C at *any* epoch. So no deposited pre-t object can be an electroweak doublet with hypercharge.
  - The consequences stand: the rider withdrawn, the pre-t inflaton a singlet, exit (a) not Higgs inflation, option D reinforced.
- **Correction needed before deposit** (directive §4; this lands under R-3):
  - In the B2 Manifest §10 entry, strike "Im(𝕆) = ℝ⁷ → 1 ⊕ 3 ⊕ 3̄ contains no doublet (§3.2)" as support.
  - Restate the basis as follows:
    > "The deposit supplies no SU(2)_L × U(1)_Y commuting with SU(3)_C from G₂ (rank obstruction; computed, 2026-10-16). Electroweak structure is imported, and nothing deposited makes a pre-t electroweak doublet available."
  - Closure record v2 §2.6 needs the same correction wherever it repeats the B2 basis. I have not read §2.6 this session; AC should check that text.
- Prior check: I pre-registered B-c (inverted) at 0.50. That was wrong about the conclusion and right about leg 4. Result: B-b.

## 6. A9 (Scratch's axiom) and M1
- I am not ruling on A9; Scratch owns it.
- One computed fact is relevant to it: the SU(2) acting on unit quaternions by multiplication is not in G₂ (row 6). Any route from the octonions to M1 (S³ ⊂ ℂ² as the spin-½ state space) that passes through "S³ = the ℍ whose SU(2) factor is in G₂" fails at that step.

## 7. Prior check
I pre-registered R-3 at 0.55 against AC's lean towards R-1, and R-3 held. AC's statement of the colour part (G₂ ⊃ SU(3), 1⊕3⊕3̄ correct) is confirmed by computation. AC's hypothesis that C16 supplies SU(2)_L and U(1)_Y separately and explicitly is refuted by C16 §3.3's text.
