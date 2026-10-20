# Steps 1–3 — mapping, K0′, matter `{C_N, C_N}`: VERDICT (Cursor Main)

**Landing: G-4.** χ-corrected self-bracket uncomputed, so weak vanishing of the Dirac bracket is not shown, and G-2 is not shown either.  
**Greg GO:** chat “GO”, 2026-10-21.  
**Prereg:** `Working\Opsi2_Steps123_Mapping_K0_MatterBracket_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261021.md`  
**K0′ script / JSON:** `Working\Opsi2_Steps123_K0_PARALLEL_CursorMain.py`, `Opsi2_Steps123_K0_Wolfram.wl`, `Opsi2_Steps123_K0_PARALLEL_RESULTS.json`  
**Engines:** NumPy and Wolfram Engine 15, both run, both pass. Minimal model \(\beta_2=\beta_3=0\), \(\beta_1=1\).  
**No Core. No f.** (N) undetermined. \(\mathcal{S}\)-block **not** opened.

---

## 1. Three-way mapping

HR after the shift redefinition (1111.2070 (7), (11), (60)): the g-lapse \(N\) multiplies one constraint \(\mathcal{C}\); \(L\) and \(L^i\) sit in \(\mathcal{H}_0\) and, by §4, their variations are **four further constraints**. \(\mathcal{C}\) is not \(C_g-C_f\).

Action (N), before eliminating \(\chi\). One spinor, two energy densities \(E_g(\psi,e)\), \(E_f(\psi,f)\), one spatial momentum \(p_i\). Substitute \(N^i=L^i+L n+N(Dn)\):

| Piece | Lands in |
|---|---|
| \(E_g+(Dn)\cdot p\) | **\(\mathcal{C}_N\)** (coefficient of \(N\)) |
| \(E_f+n\cdot p\) | **\(L\)-constraint** (inside \(\mathcal{H}_0\), not inside \(\mathcal{C}_N\)) |
| \(p_i\) along \(L^i\) | **shift constraints** (the other three of the four) |
| Cross \(\{E_g,E_f\}\) / \(-2h_g X p\) | **\(\{\mathcal{C}_N, C_L\}\)** at Poisson level — **not** \(\{\mathcal{C}_N,\mathcal{C}_N\}\) |

The θ-weighted residual \(h_g(\theta_g I-\theta_f X)^2 p\) was the \(C_g-C_f\) combination. It is **not** the ∂δ coefficient of HR’s \(\{\mathcal{C},\mathcal{C}\}\). Carrying it into that bracket was the wrong object.

---

## 2. K0′ — passed (minimal model, generic \(n\neq 0\))

On \(\mathcal{C}_i=0\) with \(n\) held generic (\(x>0.2\), \(\|n\|>10^{-3}\)):

\[
P^i=\mathcal{C}\,(Dn)^i.
\]

When \(\mathcal{C}\) is set to 0, \(\|P\|\sim 10^{-15}\). When \(\mathcal{C}_i=0\) but \(\mathcal{C}\neq 0\), \(\|P\|\) stays \(O(10^{-1})\) or larger. So the bracket coefficient is weakly zero, not identically zero.

| | NumPy | Wolfram |
|---|---|---|
| kept | 28 (ill-conditioned \(D\) dropped) | 38 |
| max \(\|P\|\) at \(\mathcal{C}=0\) | \(4.6\times 10^{-15}\) | \(5.6\times 10^{-15}\) |
| \(\|P_{(44)}-P_{(45)}\|\) | same | same |
| pass | **yes** | **yes** |

Scope: \(\beta_2=\beta_3=0\). The paper’s proof does not need the explicit \(n(R)\); this check is the reduction (44)→(45) at generic \(n\).

---

## 3. Matter self-bracket

**Poisson level, after the mapping.** \(\{\mathcal{C}_N,\mathcal{C}_N\}\) sees only \(E_g+(Dn)\cdot p\). That is the single-metric Dirac structure (weight \(h_g\)) plus HR’s own \(Dn\) channel. With the matter-modified multiplier \(\mathcal{C}_i^{\mathrm{grav}}+p_i=0\), the K0′ reduction still gives \(P\propto\mathcal{C}_N\), so this Poisson coefficient is weakly zero. The cross piece never enters this bracket.

**Not shown.** The Dirac bracket through \(\chi\) (both vierbeins, shared \(\pi_\psi\)) can still move \(f\)-dependence into \(\{\mathcal{C}_N,\mathcal{C}_N\}_D\). That coefficient was not computed. Background-\(\xi\) transport of \(g\)-matter is the \(Dn\) channel already in K0′; it is not a second Poisson remainder. \(\delta n(p)\) is the matter-modified multiplier, already the surface on which \(P\propto\mathcal{C}\).

Per the pre-registration: χ uncomputed → **G-4**. No G-2. The 5.5-mode gate is not met, because a failure that survives the multiplier and χ was not exhibited. The \(\mathcal{S}\)-block stays closed until that Dirac coefficient is shown to vanish weakly.

---

## 4. Fork

| | |
|---|---|
| G-1 | not earned |
| G-2 (5.5-mode) | **not earned** — Poisson \(\{\mathcal{C}_N,\mathcal{C}_N\}\) is weakly zero; χ leak untested |
| **G-4** | **landed** — blocker is \(\{\mathcal{C}_N,\mathcal{C}_N\}_D\) through \(\chi\) |
| \(\mathcal{S}\)-block | not opened |

Posteriors held: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

**Ask:** Jammer/AC on whether the Poisson placement of the cross (in \(\{\mathcal{C}_N,C_L\}\), not in the self-bracket) is accepted, and whether the next GO is only the χ correction to \(\{\mathcal{C}_N,\mathcal{C}_N\}\).

— Cursor Main, 2026-10-21.
