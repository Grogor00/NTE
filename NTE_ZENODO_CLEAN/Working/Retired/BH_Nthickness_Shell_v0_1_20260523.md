# P-BH1 — extreme N-thickness shell model v0.1 (§22.12)

**Stream:** Cursor scaffold → Jammer strong-field  
**Date:** 2026-05-23  
**Status:** **S0 programme** — no Hawking claim; no-interior reading only  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-BH1

---

## §1. Mission

Positive account of black holes under §16 no-bulk ontology: mass-energy as **extreme local N-thickness** / $|Φ_{\rm NTE}|^2$ suppression shell, enforced by pointwise $H = \\beta_{\\mathrm{NTE}}|Φ|^2$ (§6.2, §17.5.3).

**Not claimed:** Hawking temperature, information paradox resolution, interior geometry.

---

## §2. Model (shell ansatz)

Static spherically symmetric exterior; Schwarzschild mass $M$ at $r \gg r_s$.

**Schwarzschild radius:** $r_s = 2GM/c^2$.

**Structural identity (§2.3, weak-field → strong-field extension):**

$$|\Phi_{\rm NTE}(r)|^2 = v_{\rm EW}^2\left(1 + \Phi_N(r)/c^2\right), \qquad \Phi_N = -\frac{GM}{rc^2}$$

**Shell region:** $r \sim r_s$ where $|\Phi_{\rm NTE}|^2$ reaches minimum on exterior:

$$|\Phi_{\rm min}|^2 \approx v_{\rm EW}^2\left(1 - \frac{1}{2}\right) = \frac{v_{\rm EW}^2}{2} \quad\text{(at } r=2r_s \text{ leading)}$$

**N-thickness proper length (F1):**

$$\ell(r) = \frac{1}{\alpha|\Phi_{\rm NTE}(r)|^2}$$

At horizon shell: $\ell(r_s) \sim 2/(\alpha v_{\rm EW}^2)$ vs $\ell(\infty)=1/(\alpha v_{\rm EW}^2)$ — **factor ~2 thinning** at leading Schwarzschild order.

**Numerics (P-BH1a, solar mass):** `bh_nthickness_shell.py` — at $r=r_s$: $|\Phi|^2/v_{\rm EW}^2=0.5$, $\ell/\ell_\infty=2.0$; at $r=2r_s$: $\ell/\ell_\infty=1.33$. Regime **strong field** for $r\lesssim 10r_s$ ($|\Phi_N|>0.05$).

**Constraint check:** $H(r)=\alpha|\Phi|^2$ slaved pointwise; $\mu(x,N)$ action (§22.16 v0.2) enforces algebraically.

---

## §3. Area-law target (P-BH1b v0.1)

Bekenstein–Hawking: $S_{\rm BH} = A/(4G) = \pi r_s^2/G \propto M^2$.

**Additive integral FALSIFIED:** $\int (\ell/\ell_\infty - 1)\,dr \propto M$ — see `P_BH1b_Area_Law_Check_v0_1_20260523.md`, `bh_area_law_check.py`.

**Viable programme (not derived):**

$$S_{\rm NTE} \stackrel{?}{=} \frac{A}{4G}\,g\!\left(\left.\frac{\ell(r_s)}{\ell_\infty}\right.\right), \qquad g \approx 2 \text{ at } r_s \text{ (Schwarzschild exterior trial)}$$

Jammer: derive $g(\ell)$ from Janus §22.17 + $\mu(x,N)$ — not ship until action-derived.

---

## §4. Relation to P-BH4 (μ PPN)

- **1PN exterior:** §22.16 v0.2 + `mu_xN_ppn_check.py` — PASS solar system  
- **Strong field:** $|\Phi_N| \sim 1$ at $r_s$ — structural identity **breaks down** at $\mathcal{O}(1)$ potential; need $\mathcal{O}(\Phi^2)$ metric from full $\delta g_{\mu\nu}$  
- **Discipline:** no BH numerics ship until P-BH4 strong-field pass

---

## §5. Falsifiers

1. Shell model requires bulk interior to reproduce observed ringdown — contradicts §16  
2. $|Φ_{\rm NTE}|^2 \to 0$ at horizon implies local octonion restoration — **excluded** by §22.13  
3. N-thickness integral fails to scale as $M^2$ area law without new parameters

---

## §6. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| P-BH1a | Shell $\ell(r)$, $|\Phi(r)|^2$ plots | `bh_nthickness_shell.py` | **Done** |
| P-BH1b | $S_{\rm NTE}$ vs $A/4G$ | `P_BH1b_Area_Law_Check_v0_1` + `bh_area_law_check.py` | **Done** — additive FAIL; multiplicative programme |
| P-BH1c | Tie to null-time / ν carrier (P-BH2) | Open |

---

## §7. Cross-references

- §22.12, §16, §6.2, §22.16  
- `Mu_xN_Local_Lagrange_Action_Worksheet_v0_2_20260523.md`

— Cursor P-BH1 v0.1, 2026-05-23.
