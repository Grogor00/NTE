# Paper S2 — Scope and attack route (Programme S central deliverable)

**Stream:** Cursor draft → **Scratch / Jammer** execution; **AC** corpus integration.  
**Date:** 2026-05-23.  
**Charter baseline:** `Stage/Connes_Programme_Charter_v1_3.md` §1, §2.2, §4.3.  
**Master baseline:** `NTE_v10_10_Part3_Accounting.md` §22.14–§22.15, §17.5.1, §17.5.14–§17.5.15.  
**Prerequisite papers:** `Paper_S1_v0_4.md`; `Paper_OctonionExtension_v10_9.md`; Companions 7, 8, 9.

---

## §1. Mission (one computation)

Derive from a **single heat-kernel / Seeley–DeWitt computation** on the spectral triple

**`Hopf-S³ × S¹_{β_GB} × A_F`**, with `A_F = O ⊕ O` (Farnsworth–Boyle octonionic finite algebra),

the structural origins of NTE's five Charter predictions (§2.2 table) and the open legs in master §22.14(b).

**Not in scope:** wholesale import of Chamseddine–Connes SM spectral action; RH-neutrino σ field identification with Φ_NTE (confluence only — Charter §1).

---

## §2. P0 gate (resolved → Paper S2 unblocked)

| ID | Question | Charter v1.3 | Master sync (v10.11) |
|----|----------|--------------|----------------------|
| P0.3 | Closed-S³ + NTE §VIII/§22 compatible with CC 2008 kinematical relation eq (1)? | ✓ PASS | Recorded §22.15 |
| P0.7 | Gilkey heat-kernel applicable under FB non-associativity? | ✓ PASS (v1.2) | Recorded §22.15 |
| P0.10 | Rigorous Tomita–Takesaki on `A_F = O ⊕ O` | **OPEN** | Parallel; does not block heat-kernel spine |

Wick-invariance contingency: **dormant** (Charter §4.3).

---

## §3. Deliverable registry (maps to §22.14(b))

| # | Output | Master / companion hook | Success criterion |
|---|--------|-------------------------|-------------------|
| D1 | **κ₀** from Hopf harmonics (not convention-only) | §22.14 T_GB vs κ₀ asymmetry; Companion 7 alt route | `κ₀` traceable to `Y₀₀(S¹)` / adjoint data on S³; Marcolli convention sensitivity resolved |
| D2 | **T_GB** = `M_Pl/√(2π)` from Gaussian saddle on Hopf fibre | Companion 9 Session 3 | Matches existing structural closure; re-verify under ξ = 1/6 |
| D3 | **M₁³** spectral mode (S2) | Gap 1 S2 uniqueness; Companion 10 | Prefactor uniqueness beyond S1 cube-root |
| D4 | **M_R⁴** charged Killing-spinor sector | §22.2 | Higgs-sector coupling at v_EW |
| D5 | **Λ_NTE residual** via unimodular `dμ(V)` | §22.15 | Predicted Λ vs Λ_obs test |
| D6 | **K(Φ)** boundary kinetic term | §17.5.15, §18.4 reading (iii) | Hilltop r ≈ 4×10⁻³ from first principles |
| D7 | **V_NTE** off-trajectory / λ, e magnitudes | §17.5.1, §22.14(a)–(b) | Wick-invariance fixes form; S2 fixes numbers |
| D8 | **n_s, r** re-verification under ξ = 1/6 | §17.5.14, §18.4 | Sessions 6+ closure; preserve n_s = 0.9685 at structural level |
| D9 | **√(2π) pattern** audit | §22.14 recurring π-factors | T_GB clean; κ₀ leg promoted or demoted with proof |

---

## §4. Attack route (sequenced sessions)

### Phase S2-A — Geometry and operator setup (1 session)

1. Fix explicit Dirac operator `D` on `S³ × S¹` with CC 2008 normalisation; document β_GB identification with Hopf fibre modulus.
2. Attach `A_F = O ⊕ O`; state representation on finite space per OctonionExtension §3–§6.
3. Write heat-kernel expansion targets: `a₀, a₂, a₄` (and selected `a₆` cross-check per Paper S1 F1).

**Output:** `Working/Paper_S2_S2A_Operator_Setup_v0_1.md` + worksheet stub.

### Phase S2-B — Leading coefficients and κ₀ / T_GB (1–2 sessions)

1. Compute `a₂` on round `S³ × S¹`; extract `(R_{S³}/2) × Y₀₀(S²)` pathway (Paper S1 F2 / C1).
2. Gaussian saddle along S¹ → T_GB normalisation.
3. Compare to Sonner–Tong `κ₀ = 3/√(4π)` and Marcolli `κ_M` conventions (Charter §2.2 two-κ disclaimer).

### Phase S2-C — Inflation sector K(Φ), n_s, r (1–2 sessions)

1. Dilaton / non-minimal coupling channel for `K(Φ)` (Paper S1 O4).
2. Re-run Companion 9 Session 3–4 logic under explicit ξ = 1/6 action.
3. Document which readings (i)–(iii) in §18.4 survive first-principles K(Φ).

### Phase S2-D — Λ residual and M₁ / M_R modes (1–2 sessions)

1. Unimodular volume constraint → `dμ(V)` under `H = β_NTE|Φ_NTE|²` (§22.15).
2. Spectral mode counting for M₁, M_R slots (Charter §2.2).

### Phase S2-E — AC integration package

Handoff to AC: master §22.14(b) tick-down, §17.5.1 status upgrade, optional §17.X six-way + S2 footnote.

---

## §5. Dependencies and blockers

| Dependency | Location | Note |
|------------|----------|------|
| OctonionExtension v10.9 | Papers/ | Algebra and gauge birth |
| Companion 8 v10.8 | Papers/ | V_NTE confluence |
| Companion 9 + session notes | Papers/ + depreciated/ | Inflation logic (sessions archived) |
| Unimodular note | Working/ `Unimodular_Gravity_Verification_CC2008_v1.md` | §22.15 mechanism |
| P0.8 octonion crosscheck | Working/ `NTE_Connes_Programme_P0_8_*` | Closed per Charter |

**Blocker:** none on P0.3/P0.7. **Parallel:** P0.10 (σ_t) should not delay S2-A/B.

---

## §6. Falsifiers / honesty

- If κ₀ leg remains convention-dependent after S2-B → keep §22.14 "fragile" status; do not promote in master.
- If hilltop r moves outside [10⁻³, 10⁻²] under derived K(Φ) → update §18.4 three-readings table.
- If Λ_NTE residual misses Λ_obs by orders of magnitude → record as Programme falsifier candidate (Charter §2.2 Λ row).

---

## §7. Continuation prompt (Scratch / Jammer)

```
Programme S Paper S2 — attack route intake 2026-05-23.

Read: Working/Paper_S2_Scope_and_Attack_Route_v0_1_20260523.md
Read: Stage/Connes_Programme_Charter_v1_3.md §1–§2.2, §4.3
Read: Papers/Paper_S1_v0_4.md §3 (F2, C1); Papers/Paper_OctonionExtension_v10_9.md

Execute Phase S2-A: operator setup on Hopf-S³ × S¹_{β_GB} × A_F.
Deliver: Working/Paper_S2_S2A_Operator_Setup_v0_1.md

Do not conflate σ (CC SM) with Φ_NTE (Path B). Confluence framing only.
```

— Cursor, 2026-05-23
