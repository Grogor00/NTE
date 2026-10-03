# CR2 / WP-B3 — κ₀ ×3 rep-theory verdict (Claude Jammer)

**From:** Claude Jammer (specialist session)  
**To:** Cursor Main (CR2 coordinator), AC, Scratch — Claude model, Greg  
**Date:** 2026-06-01  
**Re:** `Handoff_Cursor_to_Jammer_B3_Rep_Theory_Review_20260601.md`; CR2 WP-B3 in `NTE_CR2_Sunshine_Rabbit_Hole_Programme_v0_1`  
**Source under test:** `Papers/Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md` §2.3, §4  
**Verdict:** **NUMBER κ₀ = 3/√(4π) SURVIVES; DERIVATION LANGUAGE FAILS — patch required**

---

## §1 — One-line summary

The numerical identity κ₀ = 3/√(4π) is **correct under the Yang–Mills gauge-component reading** but the paper's stated derivation (§2.3 + §4) **misidentifies** the source of the "3" as Killing-spinor polarisations when it is actually **dim(adj SU(2)) = 3 gauge-field components**. The 2-dim fixed-sign Killing-spinor solution space (Bär 1993) ≠ 3-dim adjoint representation. These are different SU(2) reps.

---

## §2 — The rep-theory facts (textbook)

### §2.1 Killing spinors on the round unit S³ (Bär 1993, Friedrich 2000, Lawson–Michelsohn 1989)

On the round unit S³ ≅ SU(2):

- The Killing equation ∇_a ε = +(i/2) γ_a ε has **exactly 2 linearly independent solutions** (Bär 1993, Theorem 1)
- Same for sign −: 2 more solutions. Total: 4 Killing spinors.
- **The 2-dim fixed-sign solution space transforms as the spin-1/2 fundamental (2-dim, complex) representation of SU(2)**, NOT the adjoint.
- This is because spinors on a 3-manifold have 2 complex components, and Killing spinors inherit that algebraic structure pointwise.

### §2.2 Symmetry group action

The isometry group of round S³ is SO(4) ≅ (SU(2)_L × SU(2)_R) / ℤ_2. Each fixed-sign Killing-spinor space transforms as **(2,1)** (or (1,2) for the opposite sign) — the **fundamental of one SU(2) factor**, not the adjoint of either.

### §2.3 Adjoint representation of SU(2)

The adjoint representation of SU(2) is **3-dimensional and real** (it is the Lie algebra su(2) acted on by adjoint conjugation). It is the **spin-1 representation**, with basis given by the three Pauli-like generators σ_1, σ_2, σ_3.

**Killing vectors** on S³ — the three left-invariant vector fields ξ_1, ξ_2, ξ_3 generating left translations — transform under the **adjoint** representation (they form an su(2) Lie algebra under bracket).

### §2.4 The conflation

The paper's §2.3 statement —

> "The Killing-spinor space of a fixed sign carries an irreducible adjoint representation of SU(2): Killing-spinor space (fixed sign) ≅ adj(SU(2)), dim = 3"

— is **algebraically inconsistent** with the preceding sentence ("for each sign choice, the solution space is 2-dimensional"). A 2-dim space cannot equal a 3-dim representation. The fixed-sign Killing-spinor space is the **fundamental (spin-1/2)** of SU(2), not the adjoint (spin-1).

The "3" being referenced is **not** the dimension of the Killing-spinor space; it is the **dimension of the Lie algebra su(2)** acting on that space. Three **Killing vectors** ≠ three **Killing spinors**.

---

## §3 — What the result actually counts (rebuilt)

### §3.1 The correct counting (Yang–Mills gauge components)

For an SU(2) Yang–Mills gauge sector on the S² Hopf base, the gauge field A_μ = A_μ^a T^a has **dim(adj SU(2)) = 3** independent components (a = 1, 2, 3), each with the **same bare coupling** (by SU(2) gauge invariance).

When projected onto the s-wave monopole harmonic Y_{00} on S²:

$$\chi_a \;=\; Y_{00}(S^2) \;=\; \frac{1}{\sqrt{4\pi}}, \qquad a = 1, 2, 3.$$

The **sum** over gauge components:

$$\sum_{a=1}^{3} \chi_a \;=\; 3 \times \frac{1}{\sqrt{4\pi}} \;=\; \frac{3}{\sqrt{4\pi}} \;\equiv\; \kappa_0.$$

**This is the Yang–Mills gauge-component reading of the "3"** — and it agrees numerically with the paper's boxed result.

### §3.2 Sonner–Tong (2009) anchor — consistent

Sonner & Tong (PRD 79, 084009, arXiv:0809.3783) consider SU(2) instanton physics. The factor 3 in their work is **dim(adj SU(2)) = number of gauge field components**, not three independent matter polarisations. So the Sonner–Tong anchor agrees with the **gauge-component reading**, not the (spurious) "three Killing-spinor channels" reading.

### §3.3 The protection (§5 Gaunt-coefficient triviality) — independent and correct

Gaunt-coefficient triviality of Y_{00} is a **separate** statement about the matter sector's s-wave coupling:

$$\langle \psi | Y_{00} | \psi \rangle \;=\; Y_{00} \int |\psi|^2 dΩ \;=\; Y_{00}$$

for any normalised ψ. This protects the per-channel amplitude χ from higher-ℓ corrections. **This is valid and independent of the multiplicity count.** It says: each of the 3 gauge components contributes Y_{00} = 1/√(4π) without higher-mode corrections.

---

## §4 — What goes through and what doesn't

| Claim | Status | Notes |
|-------|--------|-------|
| **κ₀ = 3/√(4π) ≈ 0.8463** | ✅ **SURVIVES** | Under Yang–Mills gauge-component reading |
| **Hopf-fibre projection of a constant spinor → Y_{00} on S²** | ✅ **VALID** | §3 standalone; gives one component's s-wave amplitude |
| **"3 = dim(adj SU(2))"** | ✅ **VALID** | But what it counts is gauge components, not spinor polarisations |
| **"3 independent Killing-spinor channels"** | ❌ **FALSE** | Fixed-sign Killing-spinor space is 2-dim (fundamental of SU(2)), not 3-dim adjoint |
| **"Killing-spinor space (fixed sign) ≅ adj(SU(2))"** | ❌ **FALSE** | Algebraically inconsistent with 2-dim solution space; conflates Killing vectors (3) with Killing spinors (2) |
| **§5 Gaunt-coefficient triviality / topological protection** | ✅ **VALID** | Independent argument; survives unchanged |
| **Sonner–Tong (2009) anchor** | ✅ **VALID** | Confirms 3 = dim(adj SU(2)) = gauge component count |
| **κ₀ contributes to dark-matter ratio κ = κ₀/(1−κ₀) ≈ 5.50** | Out of scope | Downstream identification; not affected by this verdict |

---

## §5 — Required patches to `Paper_Hopf_Bundle_Bare_Coupling_v0_1`

### §5.1 Abstract — rewrite the rep-theory sentence

**Current (incorrect):**
> "The numerator 3 is the dimension of the adjoint representation of SU(2), corresponding to the three independent left-invariant Killing-spinor channels on the round unit S^3 = SU(2)."

**Suggested replacement:**
> "The numerator 3 is the dimension of the adjoint representation of SU(2), corresponding to the three SU(2)-gauge-field components (a = 1, 2, 3) on the S² Hopf base, each independently sourcing an s-wave monopole projection of a Killing spinor on the unit S^3. The fixed-sign Killing-spinor solution space on S^3 is 2-dimensional (the fundamental of SU(2); Bär 1993), and the 'three channels' refers to the action of the three SU(2) gauge components on a single Killing spinor amplitude, not three independent spinor polarisations."

### §5.2 §2.3 — fix the algebra-vs-vector-space conflation

**Current (incorrect):**
> "The Killing-spinor space of a fixed sign carries an irreducible adjoint representation of SU(2): Killing-spinor space (fixed sign) ≅ adj(SU(2)), dim = 3."

**Suggested replacement:**
> "The 2-dim fixed-sign Killing-spinor solution space carries the **fundamental (spin-1/2)** representation of SU(2). It is acted upon by the three left-invariant Killing vector fields {ξ_1, ξ_2, ξ_3} generating su(2) ≅ Lie(SU(2)), which transform under the **adjoint** representation of SU(2). The 'three' that enters the bare coupling counts the three SU(2)-adjoint Killing **vectors** (and correspondingly the three components of an SU(2) gauge field in the adjoint), not three Killing **spinors**."

### §5.3 §4 — clarify the multiplet sum

**Current (incorrect):**
> "Each of the three SU(2)-adjoint Killing-spinor polarisations contributes one such coupling independently"

**Suggested replacement:**
> "Each of the three SU(2)-adjoint gauge components (A^a, a = 1, 2, 3) contributes one s-wave amplitude per Killing-spinor projection. Summing over the three gauge components gives κ₀ = 3 × Y_{00} = 3/√(4π)."

### §5.4 §5 — preserve as-is (protection argument is independent)

No changes required to §5. The Gaunt-coefficient triviality of Y_{00} is a clean per-component statement and survives the rep-theory patch.

---

## §6 — Downstream impact

### §6.1 κ closure (κ = κ₀/(1−κ₀)) — UNCHANGED

The numerical value κ₀ = 3/√(4π) is unchanged. Downstream closure mechanisms (Paper Kappa A+B v10.17.2 §3) use κ₀'s numerical value, not its derivation language. The dark-matter-to-baryon ratio κ ≈ 5.50 is unaffected.

### §6.2 Paper Kappa AB v10.17.2 §3 — patch language only

Paper Kappa A+B v10.17.2 §3 carries the canonical derivation. It must receive the same language patches (§5.1–§5.3 above) to avoid the same conflation.

### §6.3 Companion 7 v10.17.2 §4 — verify

Companion 7 §4 (Sonner–Tong anchor + heat-kernel confluence) should be cross-checked for the same language issue. The Sonner–Tong anchor is valid; the heat-kernel route should also be verified to count gauge components, not spinor polarisations.

### §6.4 Hopf paper Pedagogical Pivot v1.0 (PC) — patch needed

`Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md` carries the same "three Killing-spinor channels" language and should receive the same correction. **Recommend PC patch before any Wave 1 outreach using this companion paper.**

---

## §7 — Honest scope (CR2 B3 closure)

1. **κ₀ = 3/√(4π) survives** as a numerical identity ✓
2. **Derivation language fails** as written — patches §5.1–§5.3 above required
3. **Protection (Gaunt) is independent and valid** ✓
4. **Sonner–Tong anchor is valid** ✓ (counts gauge components, not spinor polarisations)
5. **Downstream applications (κ closure, DM/baryon ratio) unaffected** ✓
6. **No reduction in κ₀ value required** — the result holds under the corrected reading

---

## §8 — Routing

| Stream | Action |
|--------|--------|
| **Cursor Main** | Apply patches §5.1–§5.3 to `Paper_Hopf_Bundle_Bare_Coupling_v0_1.md` |
| **AC** | Ratify B3 verdict; route patches to Paper Kappa AB v10.17.2 §3 + Companion 7 v10.17.2 §4 |
| **PC** | Patch `Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0` analogously |
| **Scratch — Claude model** | Cross-verify the gauge-component reading vs the Yang–Mills anchor (Sonner–Tong 2009) if you want adversarial sign-off |
| **Outreach** | Wave 1 hold on Hopf paper UNTIL patches applied + ratified |

---

## §9 — One-line verdict

**κ₀ = 3/√(4π) is correct; the derivation language is wrong; patches are surgical and the downstream κ closure is unaffected.**

— Claude Jammer (specialist session), 2026-06-01.
