# KSIP-A — Kletetschka 2025 primary source verification

> **⛔ TERMINATED (Greg 2026-06-13; reaffirmed 2026-06-18).** Historical external audit only — **not NTE framework.** Do not cite downstream gates; programme closed. `Workflow/NTE_KSIP_Quarantine_Register_v0_1_20260618.md`

**Author:** Cursor Main  
**Date:** 2026-06-13  
**Source:** Kletetschka, G. (2025). *Three-Dimensional Time: A Mathematical Framework for Fundamental Physics.* Rep. Adv. Phys. Sci. **9**, 2550004. DOI [10.1142/S2424942425500045](https://doi.org/10.1142/S2424942425500045).  
**Local copy:** `Working/Kletetschka_2025_Three_Dimensional_Time_Primary.pdf` (4.18 MB, fetched Wikimedia Commons 2026-06-12).  
**Extract:** `Working/Kletetschka_2025_extracted.txt` (pypdf, 14 pp).

**Verdict:** **DISCREPANCIES** — core §2–§3 structure confirmed; launch-memo shorthand and derivative-literature claims **not** verbatim in primary text.

---

## 1. Manifold M = T³ × S³

| Launch / KSIP claim | Primary text (§2.1) | Match |
|---------------------|---------------------|-------|
| **M = T³ × S³** (product manifold) | *"six-dimensional manifold with three temporal and three spatial dimensions"*; metric **ds² = dt₁² + dt₂² + dt₃² − dx² − dy² − dz²** (Eqs 1–4) | ❌ **Not stated** as T³ × S³ or S³ topology |
| Product vs fibration | Flat 6-coordinate metric; **τ² = t₁² + t₂² + t₃²**, **E² = x² + y² + z²** | Product **metric** on ℝ⁶; no torus/sphere topology named |

**Note:** Spatial part is Euclidean 3-space in coordinates (x,y,z), not explicitly **S³**. The T³ × S³ label in Jammer launch memo is **reframing shorthand**, not primary-source notation.

---

## 2. Three temporal dimensions (§1, Fig. 1, §2.1)

| Scale | Primary | Verified |
|-------|---------|----------|
| **t₁** | Quantum / Planck; mass generation | ✅ |
| **t₂** | Interaction; quantum–classical bridge | ✅ |
| **t₃** | Cosmological; gravitational phenomena | ✅ |

Wave function (Eq. 7): **Ψ(T,x) = Σ c_{ijk} exp(iωᵢt₁ + ωⱼt₂ + ωₖt₃)**; normalization over **dt₁ dt₂ dt₃ d³x** (Eq. 8). Propagator (Eq. 10): **G(k,ω) = [k² + ω₁² + ω₂² + ω₃²]⁻¹**.

---

## 3. Mass-ratio derivation (§3.1, Eqs 14–16)

**Primary chain:**
- Eigenvalue equation on temporal Laplacian (Eq. 14)
- **m_n = m₀ exp(−α n^γ)**, n = 1,2,3 (Eq. 15) — introduces **m₀, α, γ**
- Predicted ratios: **m₁ : m₂ : m₃ = 1 : 4.5 : 21.0** (Eq. 16)

| Claim | Verdict |
|-------|---------|
| Ratios **1 : 4.5 : 21** | ✅ **Verbatim** (Eq. 16; Fig. 1) |
| Zero-parameter / no inputs | ❌ **Contradicted** — Eq. 15 has three constants; §3.4 also claims *"without additional parameters"* while Eq. 15 is parametric |
| Top quark **173.21 ± 0.51 GeV** | ⚠️ Abstract yes; §3.1 gives **173.2 ± 0.9 GeV** (PDG-width, not independent sharp prediction) |
| Neutrino masses | ✅ Listed: ν₃ 0.058±0.004 eV, ν₂ 0.0086±0.0003 eV, ν₁ 0.0023±0.0002 eV |

**AC discriminator (T-K3):** Kletetschka **1 : 4.5 : 21** vs NTE **(8π)^(2/3) ≈ 8.57** — **incompatible**; primary confirms Kletetschka side of the split.

---

## 4. Chronometric form / causality (K8)

| Launch claim | Primary (§2.1) | Match |
|--------------|----------------|-------|
| **Chronometric form** preserves causality | **No** use of "chronometric" | ❌ Term absent |
| Causality mechanism | *"Causality is preserved through specific interval conditions: ds² > 0 timelike, ds² = 0 null, ds² < 0 spacelike"*; *"microcausality through proper light cone structure in all temporal projections"* | ⚠️ **Claimed**, not derived adversarially |

**KSIP-E load:** causality audit still **required** — primary asserts interval classification, does not prove ordering on T³.

---

## 5. Testable predictions (§3.1–3.4) — sample register

| Observable | Primary value | Section |
|------------|---------------|---------|
| Mass ratios | 1 : 4.5 : 21 | §3.1 |
| sin²θ₁₂, sin²θ₂₃, sin²θ₁₃ | 0.307±0.013; 0.546±0.021; 0.0220±0.0007 | §3.2 |
| sin²θ_W | 0.23122±0.00003 | §3.2 |
| New resonances M₁, M₂ | 2.3±0.4 TeV; 4.1±0.6 TeV | §3.4 |
| Δv/c (GW) | (1.5±0.3)×10⁻¹⁵ | §3.4 |
| w(z) dark energy | −1 + (0.05±0.01)(1+z)⁻³ | §3.4 |
| DUNE / Belle II / LHCb | Named as test channels | §3.2 |

List is **extensive with error bars** — but many values sit near PDG 2024; independence from fitting not demonstrated in §2–§4.

---

## 6. Derivative-literature items **not** in primary §2–§4

| Item | Source in KSIP launch | In primary? |
|------|----------------------|-------------|
| Temporal axes as **eigenmodes of temporal metric operator** | ResearchGate / Hentsch extension | ❌ Not in §2–§4 |
| **M = T³ × S³** | Launch memo M2 | ❌ |
| **Chronometric form** | K8 register | ❌ |

**AC §4 confidence ceiling lifted for primary read; M3 eigenmode reading remains derivative-only.**

---

## 7. Implications for downstream lanes

> **⛔ SUPERSEDED — KSIP TERMINATED 2026-06-13.** Section frozen as historical record; **no downstream lanes proceed.**

| Lane | Gate after KSIP-A |
|------|-------------------|
| **KSIP-B** (Scratch adversarial) | **CANCELLED** |
| **KSIP-E** (Cursor Scratch causality) | **CANCELLED** (memo filed pre-termination; quarantined) |
| **KSIP-C/D** | **CANCELLED** |
| **KSIP-F** (AC) | **NO INTEGRATION** — programme terminated |

**Binding:** Downgrade "five mappings" per AC audit. Programme output was **discriminator**, not convergence — **never adopted into NTE.**

---

— Cursor Main, 2026-06-13. **DISCREPANCIES** — read primary; do not cite T³×S³ or chronometric form as Kletetschka verbatim.
