# P-BH1b — area law vs N-thickness entropy v0.1 (§22.12)

**Date:** 2026-05-23  
**Script:** `Working/bh_area_law_check.py`  
**Status:** **Scaling test complete** — multiplicative candidate viable; additive integral falsified

---

## §1. Target

Bekenstein–Hawking: $S_{\rm BH} = A/(4G) = \pi r_s^2/G \propto M^2$.

NTE programme: relate $S_{\rm BH}$ to **N-thickness shell geometry** without bulk interior (§16).

---

## §2. Candidates tested

### (A) Additive thickness integral — **FALSIFIED**

$$I_{\rm thick} = \int_{r_s}^{r_{\rm cut}} \left(\frac{\ell(r)}{\ell_\infty} - 1\right) dr, \quad \ell/\ell_\infty = \frac{1}{1+\Phi_N}$$

At weak field $\ell/\ell_\infty - 1 \approx GM/(rc^2)$ → $I_{\rm thick} \sim (GM/c^2)\ln(r_{\rm cut}/r_s) \propto M$.

**Not $M^2$.** Fails area-law scaling (script: 10 $M_\odot$ gives $\sim 10\times$ on $I$, not $10^2$).

### (B) Multiplicative horizon factor — **VIABLE (programme)**

$$S_{\rm NTE} \stackrel{?}{=} \frac{A}{4G}\,g\left(\frac{\ell(r_s)}{\ell_\infty}\right), \qquad g(x)=x \text{ (trial)}$$

Preserves $M^2$ because $A/(4G)$ carries mass scaling; $g=\ell/\ell_\infty|_{r_s} \approx 2$ (solar mass, P-BH1a).

**Not derived** — thickness factor at horizon must come from Janus + $\mu(x,N)$ (Jammer).

---

## §3. Numerics (solar vs 10 $M_\odot$ vs $10^6 M_\odot$)

| Quantity | $M^2$ scaling? |
|----------|----------------|
| $S_{\rm BH}$ | ✓ |
| $I_{\rm thick}$ | ✗ ($\sim M$) |
| $S_{\rm NTE}$ multiplicative | ✓ (same as $S_{\rm BH}$ × O(1)) |

---

## §4. Discipline

- Do **not** claim NTE derives BH entropy until $g(\ell)$ is derived from action
- Additive e-fold phase integral (P-BH1 §3 naive form) **deprecated** for area law
- P-BH4 strong-field still required for $|Φ_N|\sim 1/2$ at $r_s$

---

## §5. Cross-references

- `BH_Nthickness_Shell_v0_1_20260523.md`, `bh_nthickness_shell.py`

— Cursor P-BH1b v0.1, 2026-05-23.
