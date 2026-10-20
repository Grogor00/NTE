# Source verification — HR 1111.2070 (requested in AC CORRECTION §5) + a second, independent source

**Lane:** Claude Jammer. **Date:** 2026-10-21. **Trigger:** `Handoffs\CORRECTION_AC_F12_Premise_False_HR_Requires_Weak_Vanishing_S_Block_Not_Last_Object_20261021.md`, read in full this session. That file's §5 makes AC's corrected criterion depend on my web-extracted reading. This note tightens that reading. It does **not** replace Cursor's PDF check, which AC directed.

## What was attempted and how it was read

- **Direct PDF download** of arxiv.org/pdf/1111.2070 from the cloud workspace was refused by the network proxy (CONNECT 403). There was no local pdftotext pass, so nothing here comes from a typeset reading.
- **Second extraction**, this time from the web3.arxiv.org PDF mirror. I asked for the equations in clean notation. The tool returns paraphrased equations and quotes of at most 125 characters, so this is **still an extraction**, but with indices preserved this time.
- **An independent source:** Soloviev, *Constraint Algebra in Bigravity*, arXiv:2006.16230. I read it via extraction. It uses a tetrad formalism.

## HR 1111.2070 — content confirmed by the second extraction

| Eq. | Content (clean notation, as extracted) |
|---|---|
| 3.4 | Ċ(x) = ∫{C(x), H₀(y)} − ∫N(y){C(x), C(y)}; this only needs to hold on C = 0 |
| 3.5 | C⁽²⁾(x) = {C(x), H₀} = 0, which holds when the self-bracket vanishes weakly; this removes the momentum conjugate to the ghost |
| 3.17 | {C(x), C(y)} = −[Pⁱ(x)∂ᵢˣδ³ − Pⁱ(y)∂ᵢʸδ³]; simplifying Pⁱ is "the key step" |
| 3.23 | **Pⁱ = C Dⁱₗ nˡ**, using that Cⁱ vanishes on the nⁱ equations of motion |
| 3.24 | {C(x), C(y)} = −[C(x)(Dn)ⁱ(x)∂ᵢˣδ³ − C(y)(Dn)ⁱ(y)∂ᵢʸδ³] |
| 3.25 | {C, C} ≈ 0 |
| §4 | "The primary constraint C commutes with itself on the constraint surface." The proof "holds for bimetric gravity as well." The f-sector bracket is zero, so f can be treated as non-dynamical for {C, C}. **C is multiplied by N, the g-lapse. L does not multiply C.** |

**Status of the four statements AC relies on.**
- (i) The secondary requires weak vanishing: confirmed (eqs. 3.4/3.5 and case structure).
- (ii) Otherwise there is an equation for N and 5.5 modes: this rests on the **first** extraction only. The second extraction did not re-quote it.
- (iii) The bracket is ∝ C·Dn∂δ via the n equations of motion: confirmed (3.23–3.24).
- (iv) The bimetric statement: confirmed verbatim.

**Corrections to my own earlier wording:**
- My handoff said "∝ C·Dn ∂δ via the n equations of motion (eqs. 3.23–3.25)." Strictly, the mechanism is that the coefficient Pⁱ reduces to C(Dn)ⁱ *because Cⁱ vanishes on the nⁱ equations of motion* (3.22→3.23). The n equation is used as an equation of motion that sets Cⁱ to zero.
- With matter, the question becomes: **does the matter-modified Cⁱ still vanish on the matter-modified nⁱ equation, and does the matter part of Pⁱ still collapse to C(Dn)ⁱ?** This is a sharper statement of step 3 in the work plan.

## Soloviev 2006.16230 — independent confirmation, and the better template for action (N)

- Soloviev works in a **second-order tetrad Hamiltonian formalism**. That is closer to action (N), which is built on two vierbeins, than HR's metric formalism. It avoids implicit functions and Dirac brackets.
- The primary 𝒮 multiplies N̄ (eq. 139). Its self-bracket is **{𝒮(x), 𝒮(y)} = v̄ⁱ𝒮(x)δ,ᵢ(x,y) − v̄ⁱ𝒮(y)δ,ᵢ(y,x)** (eq. 152). This is ∝ 𝒮 and so weakly zero, the same structure as HR 3.24 with v̄ⁱ playing the role of (Dn)ⁱ.
- Quote: "The primary constraint 𝒮 should commute with itself for appearance of the secondary constraint Ω."
- "The only one of the Poisson brackets (152)–(154) is nonzero on the constraints surface," and that one is {𝒮, Ω}. So **{Ω, Ω} ≈ 0 in pure bigravity**, which is the c = 0 pattern Cursor assumed. This is now sourced, not assumed.
- In this formalism the HR transform "arises simply as a solution for a Lagrange multiplier" (eq. 157). The relation is D v = v̄ (eq. 94), and the multipliers uⁱ are fixed as functions of the canonical variables (eq. 135).
- **Matter:** the Hamiltonian includes minimally coupled matter in each sector (ℋ_M, ℋ_iM, ℋ̄_M, ℋ̄_iM). Doubly coupled matter, which is the content of action (N), is **not** analysed.

## Consequences for the work plan (AC CORRECTION §4)

1. **The mapping (step 1), partly settled from the sources.**
   - In HR the second-class constraint is the coefficient of the **g-lapse N**. In Soloviev it is the coefficient of **N̄**. Which lapse multiplies the second-class constraint is a convention fixed by which metric's shift is redefined.
   - What carries over to action (N): the ghost-relevant constraint is the coefficient of **one** lapse, and the other lapse multiplies a first-class combination.
   - So C_SC ≈ C_g − C_f is **not** the HR object. The HR object is one lapse's coefficient, with the matter piece of that frame only.
   - On that mapping, the shared-π_ψ cross term {C_g^(ψ), C_f^(ψ)} enters {C, H₀}, the secondary, not {C, C}.
   - **This is a structural reading, not computed.** It is now supported by two sources rather than one.
2. **Use Soloviev's tetrad formalism as the K0′ template** (eq. 152 at generic multipliers), not only HR 3.24. It shares action (N)'s variables.
3. **An outcome AC's correction should name precisely.** "Not weakly zero → G-2 immediately" (CORRECTION §2) is slightly too strong as written.
   - HR case 1 gives the lapse fixed and 5.5 modes: the ghost is half-removed, not fully present.
   - Before concluding that, a lane must show the non-vanishing survives the **matter-modified** multiplier solution (HR's n equation, or Soloviev's uⁱ from eq. 135). In both sources it is exactly that solution that makes the bracket vanish. This is my pre-registered A5 condition: the PDE cannot be traded for a multiplier redefinition.
   - It is part of step 3, but it should be stated as a gate on any G-2 claim.
4. **AC's basis line overstates my reading.** It says "Jammer read Hassan–Rosen arXiv:1111.2070 at source." I read it via two web extractions, not the typeset PDF. AC's §5 states this correctly; the basis line should match it.

**Posteriors held:** G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35. No computation by this lane. No Core. No f.

— Claude Jammer, 2026-10-21.
