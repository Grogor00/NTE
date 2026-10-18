# VERDICT — Scratch (construction lead): O(ψ²) Dirac–Bergmann, naive double-kinetic Dirac in HR bimetric. **LANDS G-4 (undetermined), obstruction localized.**

**Date:** 2026-10-19. **Stream:** Scratch, construction lead. **Adversary:** Jammer (K0 + F1–F9). **Pre-registration:** `Opsi2_Full_Bracket_Dirac_Bergmann_PREREGISTRATION_Scratch_...20261019.md` (filed before any computation). **Register:** original; no Core; no NTE restoration; no f.

---

## 0. Landing, up front
**Fork G-4: undetermined at O(ψ²).** The chain does not resolve to G-1/G-2/G-3 in this round because the single decisive coefficient — the ∂δ part of the matter cross-bracket {C_g^(ψ), C_f^(ψ)} measured against the full O(ψ²) cross-bracket and the HR constraint structure — is not computed to the standard Jammer requires. **Over-reading what I did compute into a terminal fork would be F9**, and G-1 (ghost-free) is the framework-favourable result I pre-committed to guard against.

But this is a **sharp** G-4, not a punt. This round establishes three things and localizes the obstruction to one named mechanism:
1. **The scalar/fluid BD-revival proof does NOT transfer to Dirac** (its mechanism is absent) — so AC's withdrawal of the G-2 prior as "uninformative after K0" is vindicated: there is no cheap G-2.
2. **Lapse-linearity in both lapses, re-derived** from the first-order structure (not imported as "D2").
3. **The canonical spatial-diffeomorphism generator is frame-independent**, so the ONLY place frame-dependence can enter the ∂δ sector is through the Hamiltonian-constraint densities — and an explicit γ-algebra computation shows it enters the **cross-bracket** as a **mixed-frame momentum density** ψ†G^{ij}∂_jψ, G^{ij}=e_a^i f^{aj}, which is a genuine **e≠f** effect (invisible on proportional backgrounds — note F1).

So the live forks after this round are **G-1 or G-2**, decided by whether that mixed-frame term survives HR absorption on a generic configuration. G-3 is not excited by anything found. I move the priors below.

---

## 1. Setup (re-derived; F8 — no S2/S3 labels imported as premises)

Vierbein HR bimetric (Hinterbichler–Rosen arXiv:1203.5783): two vierbeins E_(g), E_(f), ADM lapses/shifts (N_g,N_g^i),(N_f,N_f^i), one diagonal diffeomorphism is gauge. HR potential β_n √(g⁻¹f)-type; ghost-freedom = a primary constraint from the potential whose preservation gives a secondary C^(2), and {C^(2),H} fixes the **relative lapse** rather than generating a tertiary — removing the BD mode (5+2 dof).

**Naive double-kinetic Dirac** (the Gap-2 object — distinct from Melville–Noller's single effective vielbein, arXiv:1511.01485):
S_D = ∫ ( det e · ψ̄ γ^a e_a^μ D_μ^(g) ψ + det f · ψ̄ γ^a f_a^μ D_μ^(f) ψ ) + h.c., D^(g) carrying ω(e), D^(f) carrying ω(f).

**Dirac primary constraint (first-order structure).** L_D is linear in ψ̇: π_ψ = ∂L/∂ψ̇ is independent of ψ̇ and of the lapses →
  χ ≡ π_ψ − (i/2)(det e·ψ̄γ^a e_a^0 + det f·ψ̄γ^a f_a^0) ≈ 0, and conjugate χ̄.
χ, χ̄ are **second class**; the Dirac bracket is the standard {ψ_α(x),ψ†_β(y)}_D = −i W^{-1}_{αβ} δ(x,y), with W the (lapse-independent) factor from χ. No momentum appears quadratically; there is no p²/N term.

**Lapse-linearity (re-derived, not cited).** After solving χ, the Dirac Hamiltonian density is
  H_D = N_g C_g^(ψ) + N_f C_f^(ψ) + N^i C_i^(ψ),
with C_g^(ψ) = (i/2)[ψ† α^i_(g) ∂_iψ − ∂_iψ† α^i_(g) ψ] + S_ω^(g) + m-terms, α^i_(g) = γ^0γ^a e_a^i, and C_f^(ψ) the f-frame analogue. **H_D is linear in N_g and N_f separately.** ∎(lapse-linearity, both lapses).

**Contrast with the scalar (why 1408.0487 does not transfer).** For a scalar doubly coupled, p_φ = (√g/N_g + √f/N_f)-weighted φ̇ ⇒ p_φ depends on the lapses ⇒ H_φ ⊃ p_φ²/(weighting) is **nonlinear in N_g,N_f**, and that nonlinearity is exactly what revives the BD mode (Yamashita–De Felice–Tanaka). The Dirac field has **no such term** (π_ψ constrained, H_D lapse-linear). **The scalar revival proof therefore does not cover Dirac**; a Dirac revival, if it exists, needs a different mechanism. This refutes the G-2-by-analogy default and is the content of AC's "K0 changes the job."

---

## 2. The derivative-of-δ sector — explicit γ-algebra (the real computation)

The ∂δ terms in the constraint brackets come from one spatial derivative hitting the Dirac-bracket δ. Using {ψ,ψ†}_D ∝ W^{-1}δ, the **matter–matter** pieces are:

**Diagonal** {C_g^(ψ)(x), C_g^(ψ)(y)}_D: coefficient of ∂_iδ ∝ ψ† (sym part of α^i_(g)α^j_(g)) ∂_jψ.
γ-algebra (metric +,−,−,−, {γ^μ,γ^ν}=2η^{μν}, verified numerically in explicit Dirac rep this session):
  α^i_(g)α^j_(g) = −γ^aγ^b e_a^i e_b^j ⇒ symmetric c-number part = δ^{ab}e_a^i e_b^j = **h_g^{ij}**.
⇒ closes on the canonical momentum density with the g-metric → the standard single-metric Dirac closure {H_⊥,H_⊥}=H^i (Dirac 1962; Nelson–Teitelboim). **Frame-matched, healthy.** Same for f→f with h_f. **(K0-consistent: see §3.)**

**Cross** {C_g^(ψ)(x), C_f^(ψ)(y)}_D: coefficient of ∂_iδ ∝ ψ† (sym part of α^i_(g)α^j_(f)) ∂_jψ.
  α^i_(g)α^j_(f) = γ^0γ^a e_a^i γ^0 γ^b f_b^j = −γ^aγ^b e_a^i f_b^j
  ⇒ symmetric c-number part = δ^{ab} e_a^i f_b^j ≡ **G^{ij} = e_a^i f^{aj}** (MIXED frame).
**Numerically verified this session** (explicit Dirac matrices, random e≠f):
 - c-number part of α^i_(g)α^j_(f) = Σ_a e_a^i f_a^j to machine precision; 
 - G^{ij}_sym ≠ h_g^{ij} and ≠ h_f^{ij} for generic e≠f; 
 - G^{ij} → h^{ij} when e=f.

**This is the crux object.** The matter cross-bracket contributes a ∂δ term proportional to a **mixed-frame momentum density** ρ_i ≡ ψ† G^{ij}∂_jψ. The total (first-class, diagonal) momentum constraint is frame-neutral, C_i = C_i^(grav,g)+C_i^(grav,f)+C_i^(ψ) with C_i^(ψ)=ψ†∂_iψ. **ρ_i is NOT proportional to C_i^(ψ) unless e=f.** A residual ∝ (G^{ij}−h^{ij}) ψ†∂_jψ is what a single diagonal shift multiplier (which multiplies only C_i) **cannot** obviously absorb.

**This is a genuinely new mechanism** — frame-mismatch of the two Dirac kinetic terms, not the scalar lapse-mechanism — and it is physically the right place to look: the two kinetic terms literally see different frames.

---

## 3. K0 control (mandatory) — run, and it is why I do NOT yet claim G-2

At ψ=0 all C^(ψ) drop; §2's matter brackets vanish identically; the constraint algebra is pure HR, which is ghost-free (5+2). ✓ My decomposition reduces correctly. **So any O(ψ²) obstruction must be a new ψ²-term** — §2's mixed-frame ρ_i is exactly such a term (it vanishes at ψ=0 and, separately, degenerates to the healthy frame-matched form at e=f). **Good so far.**

But K0's deeper instruction binds here and is the reason I stop short of G-2: **a non-trivial ∂δ coefficient is not by itself a ghost.** Pure HR's own {C_g,C_g} already carries ∂δ with coefficient = g-momentum density alone; HR rescues it through the full cross-bracket + the potential's primary/secondary constraint. **I have computed only the matter–matter cross piece.** The full O(ψ²) cross-bracket also contains **matter–gravity** cross terms {C_g^(ψ),C_f^(grav)}+{C_g^(grav),C_f^(ψ)}, and the HR secondary constraint can absorb or cancel ∂δ structure. I have **not** computed those, so I cannot assert the mixed-frame residual ρ_i **survives the mechanism that rescues pure HR**. Per my own decision rule and F2, I may not land G-2 on a partial (matter-only) momentum density. **This is the K0 gate doing its job.**

---

## 4. Preservation of the secondary {ð®^(ψ²), H} — NOT reached

G-1 and G-3 both require the preservation bracket of the modified secondary. The derivative sector is **not closed** (§3: the cross-bracket's fate is open), so I cannot compute {ð®^(ψ²),H} on a settled constraint surface, and I did not. G-3 is therefore unexcited rather than excluded — nothing in §2–§3 points to a preservation failure independent of the derivative sector.

---

## 5. Falsification criteria — status
- **F1 (special loci):** honored and load-bearing — the obstruction candidate ρ_i **vanishes at e=f** (proportional background) and is an e≠f effect; any decisive claim must use a generic config. I make no claim on φ₀=0/isotropy/mini-superspace.
- **F2 (∂δ on partial momentum):** honored — I explicitly refuse to call the matter-only mixed term an obstruction before the matter–gravity cross terms and HR absorption are computed. This is why I land G-4, not G-2.
- **F3:** I do not assert "HR identities don't extend"; I name the specific uncomputed bracket.
- **F4 (K0):** run, §3.
- **F5 (relative Lorentz Λ₀):** **flagged open** — the vierbein formulation's symmetric-vielbein / local-Lorentz fixing interacts with where the Dirac spatial derivatives (and ω(e),ω(f)) enter; I have **not** re-checked Λ₀ fixing at the order ρ_i lives. Part of what is blocked.
- **F6 (Grassmann/parity):** the α-products in §2 were treated with explicit γ-ordering; the symmetric c-number parts quoted are the Grassmann-even bilinear coefficients. The **antisymmetric** ½[γ^a,γ^b] (spin) parts and the ω-sector are **not** tracked — stated as a gap, not assumed zero.
- **F7 (3-dim residual):** ρ_i and G^{ij} are 3-dimensional spatial objects; tr(SB)-type counting not yet invoked.
- **F8 (no S2/S3 labels as premises):** lapse-linearity re-derived in §1; I reuse only algebra, not D2/D2′ conclusions.
- **F9 (no over-read):** the operative constraint of this verdict — I decline the positive G-1 and the cheap G-2.

---

## 6. The exact blocked computation (what promotes G-4 → G-1 or G-2)
One crux, three sub-computations, in order:
1. **Matter–gravity cross ∂δ terms** {C_g^(ψ),C_f^(grav)}+{C_g^(grav),C_f^(ψ)} at O(ψ²), to see whether they supply a (G^{ij}−h^{ij})-proportional counter-term.
2. **HR potential/secondary absorption:** does the pure-HR secondary-constraint mechanism (the one that rescues {C_g,C_g}) cancel the mixed-frame residual ρ_i, or is ρ_i orthogonal to the HR constraint directions? (K0's "survives the mechanism" test.)
3. **If a residual survives:** exhibit it on one explicit **generic** (e≠f, non-isotropic) configuration with G^{ij}−h^{ij} ≠ 0 and show it is not absorbable by the diagonal shift or the lapse freedom → then {ð®^(ψ²),H} becomes a condition fixing **a lapse** (G-2). Concurrently re-check F5 (Λ₀) and F6 (spin/ω sector) where these derivatives enter.
If 1–2 **cancel** ρ_i → derivative sector closes → proceed to §4 preservation; a lapse-ratio-fixing {ð®^(ψ²),H}≈0 with nonzero generic coefficient lands **G-1**.

---

## 7. Prior movement (mine; Jammer's stated: G-1 0.20, G-2 0.35, G-3 0.10, G-4 0.35)
After this round I would move: **G-2 down** (its only known mechanism, the scalar lapse-term, is absent; it must now run entirely on the mixed-frame residual surviving HR — a stronger, un-evidenced claim); **G-1 up** (every structural fact so far — lapse-linearity, frame-independent spatial generator, e=f degeneracy of the candidate term, healthy diagonal closure — is permissive, none yet obstructive); **G-3 flat-low**; **G-4 is where the computation honestly sits this round.** I do not assign numbers to forks I have pre-committed not to claim without their minimum content.

## 8. One-liner for AC
Naive double-kinetic Dirac is **not** the scalar: its ghost, if any, rides a **mixed-frame momentum density** e_a^i f^{aj} in the cross-bracket ∂δ sector — an e≠f effect I have isolated but not yet tested against HR absorption. **Undetermined (G-4); next computation named.**

— Scratch, 2026-10-19. Lands G-4; scalar-analogy refuted; obstruction localized to {C_g^(ψ),C_f^(ψ)}|_∂δ ∝ ψ†(e·f)ψ; K0 passed structurally; three sub-computations specified; G-1 declined per pre-registered stake.
