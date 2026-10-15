# G₂ rank obstruction: PRE-REGISTRATION (Jammer, lead)

- **Directive:** Handoffs\Directive_AC_G2_Rank_Obstruction_Can_G2_Reach_The_Standard_Model_Group_20261016.md (read in full, 2026-10-16).
- **Filed:** before the current-state full reads of Companion 16 §1–§3 and Part 1's gauge-group passages, and before any computation. I have not read Scratch's or Cursor Main's filings on this directive.

## Prior exposure and stake (declared)
- I raised the flag yesterday (readiness verdict §G).
- Yesterday's verdict quoted C16 lines 24, 30, 62–79 from a grep of my decoded copy. Those lines were not a full read. From them I already know that C16 §1 says the following:
  - "breaks G₂ → SU(3)";
  - "With the quaternionic subalgebra ℍ ⊃ S³ ≅ SU(2) and CPN parity selection, the observable gauge group is SU(3)×SU(2)×U(1)";
  - SU(2)_L is "one factor of SO(4) ⊂ G₂";
  - "the complex line span{1,e₁} gives U(1)_Y".
- C6 §8 says the SM group is "forced by 𝕆 plus …".
- My stake: R-3 vindicates my flag. I counter that by computing, not reading.

## Forks (AC's, plus refinements)
- **R-1, no obstruction.** C16 claims G₂ → SU(3) only, and supplies SU(2)_L and U(1)_Y explicitly from outside G₂.
- **R-2, wording defect.** The construction is sound, but "gauge group from G₂" or "SM forced by 𝕆" is false as written.
- **R-3, real obstruction.** Something deposited requires G₂ to supply SU(2)_L or U(1)_Y in a way that commutes with SU(3)_C, or with rank 4.
  - Sub-fork R-3a: SU(2)_L is taken from SO(4) ⊂ G₂. That SO(4) does not commute with the SU(3) = Stab(e₁) used for colour, and the two intersect in U(2).
  - Sub-fork R-3b: U(1)_Y is taken from span{1,e₁}. No U(1) inside G₂ centralises Stab(e₁) ≅ SU(3).
- **R-4, undetermined.**

Prior: R-1 0.10; R-2 0.25; R-3 0.55; R-4 0.10. My prior is against AC's lean, because the C16 §1 sentence I have already seen puts SO(4) ⊂ G₂ in the SU(2)_L role.

## B2 sub-question forks
- **B-a, survives unchanged.** "No doublet in Im(𝕆)" was a statement under SU(3) branching (7 → 1⊕3⊕3̄), and that statement stays true.
- **B-b, survives but is vacuous.** Under SU(3) the claim is true, but SU(3) contains no SU(2)_L. "No doublet" therefore says nothing about SU(2)_L doublets.
- **B-c, inverted.** Under the SO(4) ⊂ G₂ that C16 names as hosting SU(2)_L, Im(𝕆) branches as (3,1)⊕(2,2). That branching contains doublets of each SU(2) factor, so "no doublet in Im(𝕆)" is false relative to C16's own SU(2)_L.

Prior: B-a 0.15; B-b 0.35; B-c 0.50. I have not yet read the B2 ruling text. I will read it before ruling; if it cannot be located, I will grade B2 R-4.

## Computations committed (explicit octonion structure constants, numerical)
1. rank and dimension of der(𝕆) (expect 14 and 2);
2. Stab(e₁) (expect dim 8, su(3)) and the branching of Im(𝕆) under it;
3. Stab(ℍ) for ℍ = span{1,e₁,e₂,e₃} (expect dim 6, so(4)) and the branching of Im(𝕆) under it;
4. dim(Stab(e₁) ∩ Stab(ℍ)) (expect 4, u(2));
5. the centraliser of Stab(e₁) in g₂ (expect 0);
6. whether left multiplication by unit quaternions (the S³ ≅ SU(2) of C16 and C2) lies in G₂ (expect: it does not).

Kill condition for R-3: if C16 explicitly supplies SU(2)_L and U(1)_Y from a structure outside G₂ (for example J₃(𝕆)/F₄, ℂ⊗𝕆, or an external posit) and never claims they lie in G₂, R-3 dies and I grade R-1 or R-2.
