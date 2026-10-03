# GHY DERIVATION — Scratch (Claude): does the surface vacuum energy come out ~M_Pl²H², and how far does it pin ρ_Λ?

**From:** Scratch (Claude) · **To:** Greg (Cc: AC). **Date:** 2026-09-28.
**Purpose:** the load-bearing computation Greg asked for before the Dark Sector companion — the boundary / de Sitter-horizon (Gibbons–Hawking–York) route to the vacuum energy. **Register: constructive derivation. Nothing patched.** Forks declared before computing; failure licensed.

---

## Pre-registered forks

- **G1 — surface vacuum energy is ~M_Pl²H² with no UV-large term.** The surface picture removes the catastrophe; §XII's "category error" is vindicated by an actual computation. Scale + mechanism reached.
- **G2 — the surface vacuum energy reintroduces a UV-large term** (~M_Pl⁴ or ~M_Pl²Λ_UV²). **Then the surface-only move does NOT solve the CC problem**, and §XII's reframing is undermined — a concrete failure to report first.
- **G3 — reached, and the number too:** the coefficient *and* scale are pinned → ρ_Λ derived.
- **G4 — undetermined without a further commitment.** Name it.

---

## The computation (de Sitter horizon, reduced M_Pl, 8πG = 1/M_Pl², L = 1/H)

| Quantity | Closed form |
|---|---|
| Horizon area A | 4π/H² |
| Entropy S = A/4G | 8π²M_Pl²/H² |
| Gibbons–Hawking temperature T | H/2π |
| Surface dof N ~ A/G | 32π²M_Pl²/H² |
| Crude equipartition ρ = ½NT / V | **6 M_Pl²H²** |

- **The vacuum energy is a *horizon* quantity.** Each of the N ~ A/G ~ M_Pl²/H² surface dof carries energy ~ T = H/2π — the **IR horizon temperature**, not a UV cutoff. So ρ_vac ~ (A/G)·T / V ~ **M_Pl²H²**, not M_Pl⁴, not M_Pl²Λ_UV². This is the Cohen–Kaplan–Nelson (1999) IR–UV relation, realised: the horizon size L = 1/H caps the vacuum energy at M_Pl²/L².
- **Coefficient.** The crude static equipartition gives 6 M_Pl²H² (right scale, O(1)). The rigorous horizon-thermodynamic derivation (Jacobson 1995, dQ = TdS ⇒ Einstein equations; Padmanabhan equipartition) reproduces the de Sitter Friedmann relation exactly: **ρ_Λ = 3 M_Pl²H_dS²**, coefficient = 3 — **given S = A/4G**.

**Numbers:** (H₀/M_Pl)² = 3.5×10⁻¹²¹ vs observed ρ_Λ/M_Pl⁴ = 7.2×10⁻¹²¹ (the ratio is 3Ω_Λ ≈ 2, i.e. the Friedmann coefficient × the not-yet-asymptotic factor). The entire 120-order gap is the surface swap M_Pl⁴ → M_Pl²H².

---

## Result → forks

**G1 holds. G2 is excluded. Not G3. — This is the honest, and it is a real advance.**

- **G1 (reached):** the surface vacuum energy is the IR horizon energy ~M_Pl²H²; **no UV-large term appears**, because the energy is set by T = H/2π. The surface-only ontology genuinely removes the UV catastrophe — not by cancellation but because (a) there is no bulk domain for a volume M_Pl⁴ term (§XVI: "the interior is not a place"), and (b) the surviving surface energy is IR-capped by the horizon. **§XII's "category error" now has a computation behind it, not just an assertion.**
- **G2 (excluded):** no reintroduced UV scale. Good — this was the way the surface picture could have failed, and it didn't.
- **Coefficient = 3, given the 1/4.** The Friedmann coefficient is fixed by the horizon thermodynamics *given* S = A/4G. The 1/4 is imported Bekenstein–Hawking; **deriving it from NTE's own bilateral boundary action is the one residual ingredient** (§XVI already flags "the 1/4 coefficient is not yet derived from NTE").
- **Not G3 — the *number* is still not reached, and here is exactly why:** ρ_Λ = 3 M_Pl²H_dS² with H_dS = β|Φ_∞|², where **|Φ_∞| is the asymptotic boundary field — the endpoint of the |Φ|(N) evolution, which NTE does not derive** (the profile is "read off the expansion history," §2.3 / §XII). So the *scale* H_dS is inherited from an underived endpoint, **not** simply from β. (I checked and rejected the tempting shortcut "ρ_Λ = β": β + today's |Φ|=v_EW fix H₀, but the *asymptotic* |Φ_∞| is a separate, underived quantity — claiming otherwise would be a manufactured positive.)

---

## What the GHY computation actually buys — stated precisely

**The cosmological-constant problem is converted, not solved:**
1. The **UV catastrophe is removed** (structural: no bulk term + IR horizon capping). The "why not 10¹²⁰" question is answered.
2. What remains is **one number: |Φ_∞|**, the asymptotic boundary field, which sets H_dS and hence ρ_Λ = 3M_Pl²H_dS². The 120-order problem becomes a single-number problem the boundary evolution should eventually determine.
3. Two smaller residuals: the **1/4** (import → derive from NTE's action), and the **coincidence** (why |Φ_∞| lands where Ω_Λ≈0.7 today).
4. The **w = −1 asymptote is trivial** (constant H_dS). The Hsu (2004) w=0 worry applies only to the *approach* (matter era) and is set by the |Φ|(N) profile — a separate calculation, flagged not done.

That is a genuine, honestly-scoped result: **NTE removes the UV part of the CC problem outright and reduces the rest to the asymptotic boundary-field value.** It does *not* yet predict ρ_Λ.

---

## Read set / provenance (discipline 11)
- Corpus, full this session: Part 2 §XII (unloading, w=−1, "ρ_Λ not derived"), §XVI (surface-only, S=A/4G, "1/4 not derived"); Part 1 §VI (ℓ=1/H), §2.3 (|Φ|² = v_EW² H/H₀), §2.4 (β input).
- External, standard (pre-cutoff): Gibbons–Hawking (1977); Jacobson (1995); Padmanabhan (equipartition/emergent gravity); Cohen–Kaplan–Nelson (1999); Hsu (2004). Cited as external physics.
- Arithmetic verified in code this session (numpy).

**Not claimed:** a derived ρ_Λ; a derived 1/4; the approach-era w(z); resolution of the coincidence.

**Feeds:** the companion's §4 (`Working\Dark_Sector_Companion_DRAFT_SKELETON_..._20260928.md`), whose central DE claim is now the precise "UV catastrophe removed; CC problem reduced to |Φ_∞|," not "ρ_Λ derived."

— Scratch (Claude), 2026-09-28.
