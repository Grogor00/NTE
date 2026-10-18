# NODE_neff_act_dr6

| Field | Content |
|---|---|
| **id** | `neff_act_dr6` |
| **claim** | Current CMB analyses combining ACT DR6 with Planck yield **N_eff ≈ 2.86 ± 0.13** (campaign figure used in Core/Working), consistent with the SM expectation ≈ 3.04 within uncertainties and tightly constraining large extra radiation. |
| **source** | ACT Collaboration, “The Atacama Cosmology Telescope: DR6 constraints on extended cosmological models,” arXiv:**2503.14454** (*JCAP* 2025). Quote (abstract): $N_{\mathrm{eff}} = 2.86 \pm 0.13$ (P-ACT-LB); with BBN abundances $N_{\mathrm{eff}} = 2.89 \pm 0.11$. **Fetched** Cursor Main 2026-10-18. |
| **type** | experimental result |
| **assumes** | ΛCDM-like cosmological model class used in those fits; standard neutrino decoupling assumptions for the SM comparison value. |
| **establishes** | Strong observational upper bound on extra dark radiation / ΔN_eff. |
| **does not establish** | Particle identity of any extra component. That mirror sectors with x=1 are allowed (they typically overproduce ΔN_eff — see `mirror_baryons_x_le_0p3`). Theory uniqueness. |
| **status** | established as a measured constraint (central value/error may update with new releases) |
| **verified** | Cursor Main, 2026-10-18 — arXiv:2503.14454 abstract fetched; figure matches. `verified: YES`. |

**Edges:** `excludes` large thermalized extra sectors at x≈1. Constrains `mirror_baryons_x_le_0p3` and `bft_cpt_universe` abundance mechanisms when they add radiation.
