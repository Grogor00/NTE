# NODE_mirror_baryons_x_le_0p3

| Field | Content |
|---|---|
| **id** | `mirror_baryons_x_le_0p3` |
| **claim** | Ciarcelluti and Wallemacq, arXiv:1401.4763: with CMB and large-scale structure, \(x<0.297\) (pure mirror) and \(x<0.315\) (mixed), both 95% c.l. The abstract also says the upper limits are around 0.3 for models with a dominant mirror fraction. Foot, astro-ph/0407623, gives the BBN bound \(T'<0.64\,T\) from \(\delta N_\nu<1\), not 0.3. |
| **source** | arXiv:1401.4763, HTML fetched 2026-10-27. hep-ph/0008105, HTML fetched 2026-10-27, equation (9). astro-ph/0407623, HTML fetched 2026-10-27. |
| **type** | constraint |
| **assumes** | Mirror sector with analogous microphysics; thermal history parameterised by x; structure-formation / BBN / CMB requirements of the cited analyses. |
| **establishes** | Equal-temperature mirror baryons are **not** a viable all-DM candidate under those analyses. |
| **does not establish** | That no mirror model works. That 0.3 is a single universal threshold. Foot's fetched bound is 0.64, from BBN. That identical Lagrangians force \(T'=T\). They do not: `tested_mirror_symmetry_x_free`. |
| **status** | established for the bounds in the fetched papers |
| **verified** | Cursor Main, 2026-10-27 — the three HTML primaries fetched. `verified: YES`. |

**Edges:** `assumes`-context → `neff_act_dr6`. `is-compatible-with` cold asymmetric mirrors; `excludes` naive x=1 mirror CDM.
