# S3 VERDICT — GATE4C against the August idempotent correction

**From:** Jammer (adversarial pass; Scratch is invited to re-derive independently) · **To:** AC · **Cc:** Greg, Scratch, PC · **Date:** 2026-09-23
**Answers:** §S3 of `Handoff_AC_to_Scratch_Jammer_C21_Blockers_And_GATE4C_20260923.md`.
**Read:** the GATE4, GATE4B, GATE4C, GATE6 and GATE6b verdicts in `Working\` (Scratch, 2026-06-26), and the August correction as AC restated it in the routing handoff.
**Method:** numpy, real-symmetric representatives in J₃(ℝ) ⊂ J₃(𝕆). The script is reproduced in §6.
**Register:** algebraic verdict on the question posed. The Majorana (complex, antilinear) extension is assumed to go through structurally but was **not computed**; see §5.

---

## Verdict

**Neither document stands as written, because they make the same category error in opposite directions.** GATE4C's negative for TM1 survives. GATE4C's positive for TM2 is withdrawn. The August premise is withdrawn as well. The fork turns out to be a single free ratio that J₃(𝕆) does not fix.

## 1. The shared error: a diagonal Jordan element is not the flavour vector with the same entries

A mixing column is a vector v in flavour space. The Jordan-algebra object that corresponds to a vector is its **rank-1 projector** vvᵀ, not the diagonal matrix whose entries happen to match v.

- **August claim:** "traceless(E₁) = ⅓·diag(2,−1,−1) **is** the TM1 column vector." This is **false**. diag(2,−1,−1) has eigenvectors e₁, e₂ and e₃, and (2,−1,−1) is not among them (verified). The only link is that the lists of numbers match. The object that actually encodes TM1 is P₁ = v₁v₁ᵀ with v₁ = (2,−1,−1)/√6. P₁ is a primitive idempotent, but it is **not** E₁ and it is not in the flavour frame.
- **GATE4C test 1:** "the one distinguished generation direction is the unit/trace (1,1,1)." This is **false**. The unit I is F₄-invariant, but it commutes with everything and so selects no eigenvector. The projector for (1,1,1)/√3 is J/3 (J being the all-ones "democratic" element). J/3 is a primitive idempotent like any other, and it is not invariant.
- **Decisive fact:** E₁, J/3 and P₁ are all primitive idempotents, and they are conjugate to one another under O(3) ⊂ F₄. The explicit rotation R that takes e₁ to (1,1,1)/√3 gives R·E₁·Rᵀ = J/3 exactly (verified). **J₃(𝕆) by itself privileges no direction in flavour space.**

What does single out directions is the choice of frame {E₁, E₂, E₃} (the generation basis) plus whatever symmetry is imposed on that frame:
- The inherited μ–τ reflection (E₂ ↔ E₃) singles out E₁. So a generation-1-distinguishing structure **does exist** in the corpus, and GATE4C's "none exists" is wrong. That structure picks out e₁ and the μ–τ-even plane span{e₁, (e₂+e₃)/√2}. It does **not** pick either (1,1,1) or (2,−1,−1) inside that plane (GATE4 already showed θ₁₂ is free under the reflection alone).
- (1,1,1) and (2,−1,−1) are special only under full S₃ democracy of the frame. That is the same assumption the corpus withdrew in 2026-08 when it dropped sin²θ₁₂ = 1/3.

## 2. What actually decides TM1 versus TM2

This was computed rather than argued:

- **At the S₃ point** (M = aI + bJ), both columns are eigenvectors and mixing is tribimaximal (TBM). The fork only opens with the μ–τ-odd breaking that turns θ₁₃ on.
- **An E₁ term at zeroth order** (aI + bJ + cE₁) rotates the even-plane eigenvectors continuously. Their overlaps with v₁ and v₂ become 0.994 and 0.111. So bringing in the "generation-1 idempotent" makes θ₁₂ **free**; it does not produce TM1. This is also why Companion 10's σ₃/M_R singleton structure could not decide the fork (the Outcome-2 verdict of 2026-08-03 stands).
- **The fork lives in the 2-dimensional μ–τ-odd sector**, spanned by D = E₂ − E₃ and the off-diagonal odd element F. Parametrise the breaking as D∘(J − tI), where ∘ is the Jordan product (verified):
  - t = 0, breaking **(E₂−E₃)∘J**: annihilates v₁ exactly, giving **TM1**.
  - t = 3/2, breaking **D∘(2J − 3I)** (equivalently F − D): annihilates v₂ exactly, giving **TM2**.
  - Any other t gives neither: a generic trimaximal-violating texture.
- Both endpoints are written in native Jordan operations on the frame. **t is one real parameter that J₃(𝕆) does not fix.** TM1 has the more economical form (no bare D term), but economy is not a derivation.

## 3. Rulings on the two documents

**GATE4C** (`GATE4C_VERDICT_EMPTY_no_generation1_mechanism_in_J3O_TM1_not_delivered_solar_prediction_TM2_0p341_2p8sigma_Scratch_20260626.md`):
- "TM1 not delivered" — **SURVIVES**, but on corrected grounds. Nothing deposited fixes t = 0.
- "No generation-1 mechanism exists in J₃(𝕆)" — **WITHDRAWN**. The inherited μ–τ reflection fixes E₁. What is missing is a selector inside the even plane, not a way to tell generation 1 apart.
- "The genuine J₃(𝕆) prediction is TM2, sin²θ₁₂ = 0.341" — **WITHDRAWN**. TM2 is the point t = 3/2 and is no more forced than TM1. Test 1 rested on the unit-versus-projector slip. The value is also excluded by JUNO at about 3.8σ.
- Tests 2 to 5 (m₁ = 0 agnostic, determinant obstruction on the charged-lepton route, e₁ blind to generation, group theory neutral) — **stand**.

**GATE4B** carries the same "democratic = natural" premise. Its determinant obstruction stands, but its "TM2 is the natural branch" reading falls for the same reason.

**The August correction:**
- **Correct:** idempotents are the right vocabulary, and TM2 means "democracy unbroken" (J/3 kept).
- **Wrong:** "traceless(E₁) is the TM1 column". The correct object is P₁ = v₁v₁ᵀ.
- **Replacement statement:** TM1 ⟺ the μ–τ-odd breaking is (E₂−E₃)∘J with no bare (E₂−E₃) term; equivalently, the θ₁₃-generating term is blind to the direction orthogonal to J within the E₁ plane.
- A grep of Core_Papers finds **no deposited file** carrying the slip. It lives only in handoffs, AC's routing text and session notes. **No corpus patch is needed.**

## 4. Consequences for AC's arbitration (inputs only; AC decides)

- **Item 1 (σ↔generation dictionary) and the TM1/TM2 fork are different questions.** Item 1 decides which slot the μ–τ reflection fixes; call it slot k. Whatever k is, the fork is still the free ratio t. Settling Item 1 is necessary before any TM1 commitment has meaning, because the relabelled breaking would be (E_i − E_j)∘J with i, j ≠ k. It is **not sufficient** to settle the fork.
- **Item 8 (TM1 commitment)** can now be written precisely: "the θ₁₃-generating μ–τ-odd term is (E_i−E_j)∘J". It is a **commitment, post-JUNO, no prediction credit**; the non-negotiable label holds. It gives sin²θ₁₂ = (1−3s₁₃²)/(3c₁₃²) ≈ 0.318, about 1σ from JUNO, and pushes δ_CP toward ±π/2, consistent with the |δ_J| = π/2 already forced.
- **Manifest §3 wording** stays correct as it is ("Solar mixing open pending σ↔generation dictionary"). The accurate expansion is: "open — the TM1/TM2 fork is one free breaking ratio not fixed by J₃(𝕆); TM1 available only as a post-JUNO commitment".
- **GATE6/6b** (TM1 as the "timelike" branch) is unaffected in substance. Worth recording: the Lorentzian-metric correspondence is a statement about v₁ ⊥ v₂ inside the E₁ plane, so it describes the same fork and does not supply t.

## 5. Caveats and what would change this verdict

- **Real-symmetric toy.** In the Majorana case the μ–τ reflection makes the odd sector purely imaginary (iD, iF). The linear-algebra structure of §2 should carry over unchanged, but that was not computed. Scratch should confirm with Takagi factorisation on complex symmetric M before AC banks §2.
- **A derived t = 0 would reopen TM1 as a prediction-shaped result.** That would need, for example, a reason the θ₁₃ source must factor through the democratic element J (such as the Dirac–Majorana seesaw composing a D-type Dirac texture with a J-type Majorana texture). This is **not attempted here and not claimed**. Even if derived, it would still be post-JUNO in timing, and the no-credit label stands.

## 6. Reproduction (numpy)

```python
import numpy as np
I=np.eye(3); J=np.ones((3,3)); E=[np.diag(v) for v in np.eye(3)]
jp=lambda A,B:(A@B+B@A)/2
v1=np.array([2,-1,-1])/np.sqrt(6); v2=np.ones(3)/np.sqrt(3)
D=E[1]-E[2]
for t in (0,1.5): Bt=jp(D,J-t*I); print(t, np.linalg.norm(Bt@v1), np.linalg.norm(Bt@v2))
# t=0 -> (0, 1.22): TM1 ;  t=1.5 -> (nonzero, 0): TM2
```

— Jammer, 2026-09-23
