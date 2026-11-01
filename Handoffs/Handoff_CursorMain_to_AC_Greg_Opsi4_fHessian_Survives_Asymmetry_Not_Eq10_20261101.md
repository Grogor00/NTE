# Handoff — O(ψ⁴) ³f Hessian, landing survives

**From:** Cursor Main
**To:** AC, Greg, Scratch, Jammer
**Date:** 2026-11-01

No new handoff had arrived since the Stage 3 header report. Render was not started. The deferred test was run once, after its pre-registration.

**Pre-registration:** `Working\Opsi2_Opsi4_fHessian_PREREGISTRATION_CursorMain_20261101.md`
**Numbers:** `Working\Opsi2_Opsi4_fHessian_RESULTS.json`
**Verdict:** `Working\Opsi2_Opsi4_fHessian_VERDICT_CursorMain_20261101.md`

Hessian A = L ³f + N ³f D. D⁻ᵀ = ³f D⁻¹ ³f⁻¹. Forty backgrounds. Medians.

- Frozen g-only: 2.3592239273284576e-16. Control passes.
- Full: 0.17213192083195888.
- Identity residual: 1.057043420910219.
- Both above 10⁻³ and on the same side of the bars. Pre-registered landing: **survives**.
- Live g-only: 0.0013650566187831947. Diagnostic.
- Relative asymmetry of ³f D: 0.23477974400100576. This D is not symmetric with respect to ³f. The passing control does not say otherwise: A = ³f (L I + N D) makes the g-only piece linear for any D.

The ghost is not declared. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

The node `doubly_coupled_bd_ghost` records this landing beside the earlier no-decision. Map view regenerated: 23 nodes, 22 edges, 4 orphans, 0 dangling, 0 premise, 0 leaks.

No PDF. No cut. No commit.
