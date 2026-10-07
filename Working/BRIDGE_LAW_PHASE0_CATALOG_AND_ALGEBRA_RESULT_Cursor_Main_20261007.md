# Bridge Law — Phase 0 catalog & algebra result

**Author:** Cursor Main · **Ran:** 2026-10-06 13:22 UTC
**Parent:** `Handoffs/Directive_Cursor_Main_Bridge_Law_From_Snu_Or_Bigravity_Research_Programme_20261007.md`
**κ₀ = 3/√(4π) = 0.846284** (input; not fitted)

## Candidate table

| ID | Name | Fund. | r_bg | Amp? | Status |
|---|---|---|---|---|---|
| C0 | No bridge | True | 0.0000 | False | algebra_done |
| C1 | Linear cross-sourcing at α=κ₀ | False | 0.8463 | False | algebra_done |
| C2 | Total-feedback / Einstein-tensor mixing | False | 5.5055 | True | algebra_done |
| C3 | Historical bilinear T·T + S_cons (quarantine) | False | 5.5055 | True | quarantine_control |
| C4 | Bilkinetic Majorana S_ν (Track N target) | True | — | False | bl1_open |
| C5 | Hassan–Rosen ghost-free bigravity (+ optional ν) | True | — | False | bl1_open |
| C6 | Wrong-sign metric kinetic mixing | False | 5.5055 | True | default_fail_bl4 |

## Phase-0 algebraic verdict

- κ₀ = 0.846284
- **C1 (linear, α=κ₀):** r_bg = 0.8463, total/baryon = 1.8463 — simultaneous mutual solve, **no** amplifier.
- **C2/C3 (total-feedback / historical):** r_bg = 5.5055 (≈5.50). Decimal proximity to Planck 5.38 is **not** Phase-0 success; law is not fundamental until derived.
- **C4/C5:** open — require BL-1 variational work; r_bg not assumed.
- **C6:** default BL-4 fail (ghost risk).
- **Landing so far:** E1–E3 confirmed algebraically; terminal fork still **F-OPEN** pending BL-1.

## Per-candidate notes
### C0 — No bridge

- Track: `null` · Fundamental: **True**
- EOM: `G± = 8π T_m±`
- r_bg formula: 0
- Ghost risk: none
- Perturbation character: n/a
- Notes: Baseline: no cross-sector gravity.

### C1 — Linear cross-sourcing at α=κ₀

- Track: `N-effective` · Fundamental: **False**
- EOM: `G± = 8π (T_m± + κ₀ T_m∓)`
- r_bg formula: α = κ₀
- Ghost risk: low_if_from_matter
- Perturbation character: inherits twin: baryon-like / hot under CPN
- Notes: Natural variation target for shared channel copying bare twin stress. Mutual solve is simultaneous, not a geometric series in total G.

### C2 — Total-feedback / Einstein-tensor mixing

- Track: `amplifier` · Fundamental: **False**
- EOM: `G± − κ₀ G∓ = 8π T_m±`
- r_bg formula: κ₀/(1−κ₀)
- Ghost risk: high_if_kinetic_mixing
- Perturbation character: still not Planck CDM under P2 (location-blind / hot twin)
- Notes: Produces ~5.50. Requires mixing solved gravity or hand S_cons. Not entailed by 'two sectors interact' alone.

### C3 — Historical bilinear T·T + S_cons (quarantine)

- Track: `historical` · Fundamental: **False**
- EOM: `S_bridge∝T_b+ T_b− ; S_cons: T̃=T_b+κ₀ T̃`
- r_bg formula: κ₀/(1−κ₀) via S_cons inversion
- Ghost risk: ill_posed_as_fundamental
- Perturbation character: same as C2 for background; P2 blocks CDM ID
- Notes: Pathway A A3: bilinear not first-principles forced; T in action is not a fundamental field. Control case only.

### C4 — Bilkinetic Majorana S_ν (Track N target)

- Track: `N` · Fundamental: **True**
- EOM: `G± = 8π (T_m± + T_ν[g±,ν]); joint Dirac/Majorana EOM`
- r_bg formula: ρ_ν / ρ_b  (from ν solution; not κ₀/(1−κ₀) a priori)
- Ghost risk: low_standard_spinor
- Perturbation character: light ν → hot / free-streaming; ΔN_eff risk under CPN
- Notes: BL-1 deliverable: write S_ν, vary, reduce. Phase 0 does not invent ρ_ν.

### C5 — Hassan–Rosen ghost-free bigravity (+ optional ν)

- Track: `B` · Fundamental: **True**
- EOM: `G(g)=8π T_m(g)+τ(g,f); G(f)=8π T_m(f)+τ(f,g)`
- r_bg formula: interaction / branch dependent (not fixed by κ₀ alone)
- Ghost risk: healthy_on_HR_branch
- Perturbation character: branch-dependent; often DE-like / modified gravity, not CDM
- Notes: Track B. Adopt-and-credit HR; identify NTE metrics with (g,f).

### C6 — Wrong-sign metric kinetic mixing

- Track: `killed_unless_proven` · Fundamental: **False**
- EOM: `□h + κ₀ □l = −T_h (schematic)`
- r_bg formula: can mimic C2 algebraically
- Ghost risk: typically_ghost
- Perturbation character: n/a if ghostly
- Notes: BL-4 default FAIL. Only revive with a proof of health.

## Next gates

1. **BL-1 Track N (Scratch):** write concrete `S_nu`, vary, show whether C1 or something else emerges.
2. **BL-1/4 Track B (parallel):** Hassan–Rosen identification + healthy branch.
3. **Jammer:** attack any smuggling of `S_cons` or T-in-action as derived.
4. **AC:** ratify programme; no Core patch at Phase 0.
