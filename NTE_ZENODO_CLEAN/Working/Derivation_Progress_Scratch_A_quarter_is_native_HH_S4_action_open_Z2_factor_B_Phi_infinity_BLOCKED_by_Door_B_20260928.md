# DERIVATION PROGRESS — Scratch (Claude): the two Dark-Sector residuals

**From:** Scratch (Claude) · **To:** Greg (Cc: AC). **Date:** 2026-09-28.
**Targets (Greg-ratified):** (A) derive the entropy normalisation 1/4 from NTE's own action; (B) pin |Φ_∞| (hence ρ_Λ). **Register: constructive derivation. Nothing patched.** Forks declared before results. Wolfram used for the GR; Cursor (Grok 4.5) tasked with an independent leg on A.

---

## Derivation A — the 1/4: **native, up to one computable Z₂ factor**

### Pre-registered forks
- **A1** — 1/4 is native and unmodified: S = A/4G. The imported ingredient becomes NTE's own.
- **A2** — NTE's CPN/Z₂ structure modifies it to **S = A/8G** (Z₂ acts freely on the saddle). This is not a failure — it is a **genuine NTE prediction**: a factor-2 deviation from Bekenstein–Hawking, changing the DE coefficient (ρ_Λ = 6M_Pl²H² instead of 3), falsifiable in principle.
- **A3** — undetermined without pinning the explicit Z₂ action on the S⁴ and its horizon.

### Result: A1 holds for the base manifold; the Z₂ factor is the sole remaining question.

The 1/4 is the on-shell Euclidean action of the round S⁴, computed this session (Wolfram):
$$I_E = -\\frac{1}{16\\pi G}\\int_{S^4}(R-2\\Lambda)\\sqrt{g}\\,, \\quad R=12/a^2,\\ \\Lambda=3/a^2,\\ V_4=\\tfrac{8\\pi^2}{3}a^4 \\;\\Rightarrow\\; I_E=-\\frac{\\pi}{GH^2},$$
$$S=-I_E=\\frac{\\pi}{GH^2}=\\frac{A}{4G}\\quad(A=4\\pi a^2=4\\pi/H^2).\\ \\checkmark$$

**The decisive point for NTE:** this S⁴ is *not borrowed from black-hole thermodynamics* — it is **NTE's own deposited Hartle–Hawking Euclidean saddle** (Part 1 §2.1.2: "the pre-temporal epoch is the Hartle–Hawking Euclidean section; gauge birth is the signature-change saddle"). So the 1/4 is the on-shell action of a manifold NTE already commits to. The §XVI flag "the 1/4 coefficient is not yet derived from NTE" is answered at the level of the base saddle: it is the Gibbons–Hawking evaluation of NTE's HH S⁴.

**The one remaining question** is whether NTE's **CPN / Z₂ orbifold structure** leaves this unmodified (A1, S=A/4G) or halves it (A2, S=A/8G). The deposit pulls both ways and must be computed, not asserted:
- Toward A1: Part 1 §VI calls the Janus pair "**one manifold** viewed from two CPN-conjugate orientations" — one S⁴, two coordinate viewpoints, no physical quotient → A/4G.
- Toward A2: §VI also says the pair "**admits a Z₂-orbifold description**" (Pin⁻ spin structure). A *freely-acting* Z₂ on S⁴ gives S⁴/Z₂ = ℝP⁴ with half the volume → potentially A/8G.

Resolving it needs the explicit Z₂ action on the S⁴ **and on the observer's horizon S²** (a free action that also halves the horizon area behaves differently from one with fixed points). **This is the leg tasked to Cursor (Grok 4.5), independent and blind.** Either outcome is a result: A1 confirms the 1/4 is native; A2 is a falsifiable NTE prediction of a modified horizon entropy and DE coefficient.

---

## Derivation B — pin |Φ_∞|: **BLOCKED by Door B. Honest negative.**

### Pre-registered forks
- **B1** — |Φ_∞| is pinned by some NTE principle → ρ_Λ predicted.
- **B2** — |Φ_∞| is not pinnable in the current framework → the number stays inherited; name why, concretely.
- **B3** — undetermined pending a specific commitment.

### Result: B2. The number is structurally unreachable under Door B.

Door B (ratified 2026-09-27, `Working\REGISTER_Door_B_Exit_a_Step2_RATIFICATION_CLOSED_20260927.md`) makes **H = β_NTE|Φ|² an identity / relabelling, not an action-level dynamics** — and locks out "restoring Φ-inflation / C17 as predictive." Consequences for B:
- Φ_NTE has **no potential and no equation of motion** — it is a relabelling of the expansion history (Part 1 §2.3). There is therefore **no dynamical fixed point** whose value is |Φ_∞|.
- |Φ_∞|² = v_EW²(H_dS/H₀), and H_dS = √(ρ_Λ/3M_Pl²) — **circular** with the quantity we want. No independent equation closes it.
- The one candidate external principle, the conformal reset, is **scale-invariant** (`Working\GHY_Derivation_...`, §4.3): it fixes T_reset/H_dS = 1.60 for any H_dS, so it does not pin the scale.

**So pinning |Φ_∞| would require one of two things, both currently unavailable:** (i) give Φ genuine dynamics (a potential whose minimum sets Φ_∞) — **locked out by F-1/Door B** (Φ is a relabelling); or (ii) a *new* scale-fixing principle beyond the reset — none is in the deposit. **The ρ_Λ number is unreachable as a matter of the corpus's ratified structure, not for lack of effort.** This is worth stating in its own right: the same Door B ratification that cleaned the inflaton sector also removes the only handle that could have pinned ρ_Λ. The honest companion claim ("reduced to |Φ_∞|, no new parameter; not predicted") is therefore not provisional pending more work on B — it is the correct end state unless Door B is revisited.

---

## Net

- **A:** the 1/4 is native (on-shell HH S⁴ action = A/4G, Wolfram-verified). Remaining: the CPN/Z₂ factor (A/4G vs A/8G) — tasked to Cursor, independent leg; either outcome is a result.
- **B:** blocked by Door B (Φ relabelling ⇒ no dynamical endpoint; reset scale-invariant). ρ_Λ stays inherited; the companion's register is correct as written.

**Read set (discipline 11):** Part 1 §2.1.2 (HH saddle), §2.3, §VI (one manifold / Z₂-orbifold, Pin⁻); Part 2 §XVI — full, this session. Door B ratification register — read this session. Euclidean dS₄ action computed in Wolfram this session. External: Gibbons–Hawking 1977.

— Scratch (Claude), 2026-09-28.
