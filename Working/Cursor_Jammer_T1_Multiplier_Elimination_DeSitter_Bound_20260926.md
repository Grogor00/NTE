# T-1 VERIFICATION — Cursor Jammer: multiplier elimination and de Sitter bound (Door-A / H5 cost branch)

**From:** Cursor Jammer · **To:** AC · **Cc:** Greg, Claude Scratch (blind peer) · **Date:** 2026-09-26 (filed 2026-09-27)  
**Tasking:** `Handoffs/AC_F2_Tensor_Discrepancy_Resolved_Is_The_Mismatch_Restated_Plus_T1_T2_T3_Tasking_20260926.md` §3 T-1  
**Claim source:** `Working/F_Phi_F1_VERDICT_Jammer_H5_slaved_but_consequential_multiplier_flips_sign_AC_H3_2beta_rho_wrong_sign_no_deSitter_above_40_60_TeV_withdrawal_reinforced_not_reopened_20260926.md`  
**Computation:** `Working/_t1_multiplier_elim_clean.py` (sympy minisuperspace, this lane)  
**Blind:** Claude Scratch T-1 not read. **Nothing patched.**

---

## 0. Door B register (mandatory)

**Corpus law now is Door B** (Companion 9 v10.19.0 rewrite, 2026-09-26/27): μ and RΦ² withdrawn; GR restored; Φ_NTE is an identity label, not an action-level constrained field.

**This T-1 does not compute current gravity.** It verifies the **pre-Door-B / Door A / H5 action** AC tasked: the cost branch of keeping

\[
F = M^2 + \Phi^2/6,\qquad
L \supset \mu\bigl[H - \beta\Phi^2\bigr]
\]

at action level (old C9 eq. (1)). Verdicts below are properties of that withdrawn action, not of the live deposit.

---

## 1. Setup (old action, as tasked)

**Old C9 eq. (1) form (historical):**

\[
L = \frac{R}{16\pi G} - \tfrac12(\partial\Phi)^2 + \tfrac1{12}R\Phi^2 - V(\Phi) + \mu\bigl[H - \beta\Phi^2\bigr] + \cdots
\]

equivalent to \(\tfrac12 F R\) with \(F = M^2 + \Phi^2/6\), \(M^2 = 1/(8\pi G)\).

**Minisuperspace** (FLRW lapse \(n\), scale \(a\), homogeneous \(\Phi\), multiplier \(\mu\)):

\[
L = -\frac{3Fa\dot a^2}{n} - \frac{3a^2\dot a\,\dot F}{n} + \frac{a^3\dot\Phi^2}{2n} - n a^3 V + 3 F k\, a\, n + L_\mu.
\]

**Two multiplier measures** (C9’s \(\int\{L+\mu(N)[\ldots]\}\) is ambiguous):

- √−g: \(L_\mu = \mu(a^2\dot a - n a^3\beta\Phi^2)\)
- dN-style: \(L_\mu = \mu(\dot a/a - n\beta\Phi^2)\)

**Procedure:** EL(Φ) → solve for μ algebraically → substitute into ∂L/∂n = 0 → impose \(\Phi^2 = H/\beta\) (and the differentiated constraint for \(\dot\Phi,\ddot\Phi\)).

**Potentials:**

- Quartic (F-1 claim): \(V = \lambda\Phi^4\)
- Full C8 eq. (6a): \(V_{\mathrm{NTE}} = (3\beta^2/(8\pi G))\Phi^4 - (\beta^2/8)\Phi^6 = 3\beta^2 M^2\,\Phi^4 - (\beta^2/8)\Phi^6\)

**Curvature:** \(k = 0\) and \(k = +1\).

Constants used for numerics (Part 3 / F-4): \(\beta = 2.38\times 10^{-47}\,\mathrm{GeV}^{-1}\), \(M = 2.435\times 10^{18}\,\mathrm{GeV}\).

---

## 2. Result — quartic, \(k=0\): **claim CONFIRMED**

Both measures give the **identical** on-shell Friedmann constraint:

\[
\boxed{
3M^2 H^2 + \frac{\lambda}{\beta^2}H^2 - \frac{H^3}{2\beta}
+ \frac{1}{\beta}\Bigl[\tfrac34 H\dot H + \tfrac14\ddot H - \frac{\dot H^2}{4H}\Bigr]
= \rho_{\mathrm{matter}}
}
\]

(Exact match to Jammer F-1 §3. Vacuum = set \(\rho_{\mathrm{matter}}=0\); \(V=\lambda\Phi^4\) already folded into the \(\lambda/\beta^2\) term.)

### 2.1 Sign flip vs AC’s \(H^3 \approx 2\beta\rho\)

| Treatment | de Sitter constraint (\(\dot H=0\)) |
|---|---|
| **Drop μ** (directive “\(3FH^2\approx\rho\)”) | \(3M^2 H^2 + H^3/(2\beta) = \lambda\Phi^4\) → **\(+H^3/(2\beta)\)** (AC’s sign) |
| **Eliminate μ** via EL(Φ) | \(3M^2 H^2 + (\lambda/\beta^2)H^2 - H^3/(2\beta) = \rho_m\) → **\(-H^3/(2\beta)\)** |

On de Sitter, \(\mu = (H^2 - 2\lambda\Phi^2)/\beta\). The multiplier enters at the **same order** as the \(F\) correction and **flips the sign** of the \(H^3\) piece. **AC’s \(H^3 \approx 2\beta\rho\) has the wrong sign** for this action; it is the drop-μ formula, not the eliminated-μ formula.

**Sign flip: SURVIVES.**

### 2.2 de Sitter bound (quartic)

For \(\dot H = 0\): \(f(H) = (3M^2 + \lambda/\beta^2)H^2 - H^3/(2\beta) = \rho_{\mathrm{vac}}\).

| λ | \(H\) at max \(f\) | \(\rho_{\mathrm{vac,max}}^{1/4}\) |
|---|---|---|
| 0 | \(4\beta M^2 \approx 5.64\times 10^{-10}\,\mathrm{GeV}\) | **\(\approx 37.1\,\mathrm{TeV}\)** |
| \(3\beta^2 M^2\) (C8 on-trajectory leading) | \(8\beta M^2 \approx 1.13\times 10^{-9}\,\mathrm{GeV}\) | **\(\approx 62.4\,\mathrm{TeV}\)** |

No de Sitter solution with vacuum energy above \(\sim(37{-}62\,\mathrm{TeV})^4\), and none with \(H \gtrsim 10^{-9}\,\mathrm{GeV}\). High-scale inflation (Higgs, Starobinsky, AC’s \(7\times 10^5\,\mathrm{GeV}\) recompute) is **not** a solution of the Door-A action.

**de Sitter bound: SURVIVES.**

---

## 3. Extension — \(k = +1\)

Same H-polynomial and same kinetic bracket; spatial curvature after μ-elimination contributes **\(+3M^2/a^2\)** only (the \(\Phi^2/6\) piece of \(3Fk/a^2\) is absorbed by the multiplier).

\[
3M^2 H^2 + \frac{\lambda}{\beta^2}H^2 - \frac{H^3}{2\beta}
+ \frac{1}{\beta}\Bigl[\tfrac34 H\dot H + \tfrac14\ddot H - \frac{\dot H^2}{4H}\Bigr]
+ \frac{3M^2}{a^2}
= \rho_m.
\]

At the high-\(H\) scales of the bound, \(3M^2/a^2\) does not open a high-scale de Sitter window: the maximum of the \(H\)-dependent piece remains \(\sim(37{-}62\,\mathrm{TeV})^4\). **Sign flip and dS bound survive at \(k=+1\).**

---

## 4. Extension — full C8 \(V_{\mathrm{NTE}}\) (eq. 6a)

On \(\Phi^2 = H/\beta\), both measures, \(k=0\):

\[
\boxed{
6M^2 H^2 - \frac{3H^3}{4\beta}
+ \frac{1}{\beta}\Bigl[\tfrac34 H\dot H + \tfrac14\ddot H - \frac{\dot H^2}{4H}\Bigr]
= \rho_m.
}
\]

(\(k=+1\): add \(+3M^2/a^2\).)

- Leading \(3\beta^2 M^2\Phi^4\) doubles the \(M^2 H^2\) coefficient (3 → 6) relative to λ = 0.
- The \(-\beta^2\Phi^6/8\) term shifts the cubic coefficient from \(-1/(2\beta)\) to \(-3/(4\beta)\).
- **Sign of \(H^3\) remains negative** (same flip vs drop-μ). Drop-μ on full \(V_{\mathrm{NTE}}\) gives \(+5H^3/(8\beta)\) with no \(3M^2 H^2\) piece — structurally different and wrong for this action.

**de Sitter bound (full \(V_{\mathrm{NTE}}\)):** max of \(f(H) = 6M^2 H^2 - 3H^3/(4\beta)\) at \(H = 16\beta M^2/3\) gives

\[
\rho_{\mathrm{vac,max}}^{1/4} \approx 50.9\,\mathrm{TeV},
\]

inside the claimed \(\sim(37{-}62\,\mathrm{TeV})^4\) band. **Bound survives under full C8 (6a).**

---

## 5. Measure robustness

√−g and dN measures produce **identical** on-shell constraints in every case run (quartic/full × \(k=0,+1\)). Only the off-shell expression for μ rescales (dN μ carries extra \(a^3\) factors). C9’s measure ambiguity does not affect the claim.

---

## 6. Verdicts (T-1 answers)

| Claim | Verdict |
|---|---|
| (1) Sign flip vs AC \(H^3\approx 2\beta\rho\); multiplier cannot be dropped | **SURVIVES** (Y) |
| (2) No de Sitter above \(\sim(37{-}62\,\mathrm{TeV})^4\) | **SURVIVES** (Y) |
| Ext. \(k=+1\) | Sign flip and bound **unchanged** at high \(H\) |
| Ext. full C8 \(V_{\mathrm{NTE}}\) (6a) | Sign flip **holds**; bound \(\approx(51\,\mathrm{TeV})^4\) **inside** band |

**Door B note:** Live corpus gravity is Door B (GR). These results price the **Door-A / H5 cost branch** AC asked to re-check; they are not the current law of the metric sector.

---

## 7. What this does / does not do

- **Does:** independently recompute the F-1 elimination from the old action; confirm both claims; extend to \(k=+1\) and full (6a).
- **Does not:** reopen Door A; patch Companion 9; read or reconcile Claude Scratch T-1; recompute F-2 mismatch under Door B (already closed).

— **Cursor Jammer**, 2026-09-26/27.
