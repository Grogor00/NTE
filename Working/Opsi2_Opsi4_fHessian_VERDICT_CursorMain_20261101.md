# O(ψ⁴) with the ³f Hessian — verdict

**Source:** `Working\Opsi2_Opsi4_fHessian_RESULTS.json`, seed 20261101, forty backgrounds. Pre-registration: `Working\Opsi2_Opsi4_fHessian_PREREGISTRATION_CursorMain_20261101.md`, filed before the run.

**Landing: survives.**

| readout | median |
|---|---|
| frozen g-only defect | 2.3592239273284576e-16 |
| full defect | 0.17213192083195888 |
| identity relative residual | 1.057043420910219 |
| live g-only defect | 0.0013650566187831947 |
| relative asymmetry of ³f D | 0.23477974400100576 |

The frozen control is below 10⁻⁸. The full median and the identity residual are both above 10⁻³. They agree, so the run is not void.

The frozen g-only piece is linear for any matrix D. With this Hessian, A = ³f (L I + N D), so the g-only quartic reduces to a form linear in the two lapses. The control checks that reduction. It does not check that D is symmetric with respect to ³f. The asymmetry median, 0.23477974400100576, says this engine's D is not.

The live figure is diagnostic. It is not a bar.

The ghost is not declared. Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.
