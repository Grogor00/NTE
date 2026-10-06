# T-2 — G4 hot-bath recollapse under Door B vs H5 ST Raychaudhuri

**From:** Cursor Scratch (owner F-3)  
**To:** AC  
**Cc:** Greg, PC, Cursor Main, Jammer  
**Date:** 2026-09-26 (filed against AC T-2; Door B C9 rewrite already closed in corpus)  
**Tasking:** `Handoffs/AC_F2_Tensor_Discrepancy_Resolved_Is_The_Mismatch_Restated_Plus_T1_T2_T3_Tasking_20260926.md` §3 T-2  
**Scope:** redo ρ+3p → ä at HH equator with ST / Jammer H5 EOM. **Nothing patched.** Blind to unrelated Claude T-1.

---

## 0. What was asked

Jammer’s G4 step used the **GR** acceleration equation. F-3 already banked: geometric **a′ = 0 does not change**; the ρ+3p → ä **dynamics** must be rederived under scalar–tensor / H5.

Report whether the **hot-bath recollapse conclusion** survives, structured as:

1. **Door B / current corpus** (GR restored),
2. **H5 / pre-Door-B action** (what AC asked to re-check).

---

## 1. Read set (this turn)

| Source | Use |
|---|---|
| AC T-2 tasking | Scope; assign Scratch / F-3 |
| Jammer F-1 verdict §3 (EOM) and §5 (G4 flag) | H5 constraint after μ elimination; recollapse flagged not withdrawn |
| Jammer G4 verdict §2 | GR ä/a = −(ρ+3p)/(6M²); a_birth ≈ 0.073 ℓ_Pl,red |
| Companion 9 Door B register + §1–§3 | μ and RΦ² withdrawn; GR Raychaudhuri restored in deposit |
| Cursor Scratch F-3 §3.1 | a′=0 geometric; ST redo of ρ+3p test owned here as T-2 |

**Not read / not used:** Claude T-1 bodies (blind). No corpus patches.

---

## 2. Door B / current corpus — GR Raychaudhuri

**Ruling in deposit.** Companion 9 Door B: \(H=\beta|\Phi|^2\) is identity, not action-level μ; \(F(\Phi)R\) removed; gravity is Einstein–Hilbert (+ SM; + ξ_H|H|²R only if exit (a) adopted).

**Acceleration (C9 §3, deposited):**

\[
\frac{\ddot a}{a} = -\frac{4\pi G}{3}(\rho+3p).
\]

Equivalently with reduced Planck mass \(M^2 = 1/(8\pi G)\):

\[
\frac{\ddot a}{a} = -\frac{\rho+3p}{6M^2}.
\]

**At the HH equator:** geometric \(a'=0\) ⇒ Lorentzian \(\dot a = 0\) (unchanged; F-3 / Gibbons–Hartle). Hot gauge-birth bath: \(w=1/3\) ⇒ \(\rho+3p = 2\rho > 0\) ⇒ \(\ddot a < 0\) ⇒ birth at a **maximum** ⇒ **recollapse**.

**Numerics (GR, unchanged under Door B):** closed Friedmann at \(H=0\), \(k=+1\): \(a_b^2 = 3M^2/\rho\). With \(T_{\mathrm{GB}} = M_{\mathrm{Pl}}/\sqrt{2\pi}\), \(g_*\approx 106.75\): \(a_b \approx 0.073\,\ell_{\mathrm{Pl,red}}\), lifetime \(\sim a_b\) — Jammer G4 / Scratch G4 arithmetic.

### Verdict 1 — Door B

**Recollapse conclusion SURVIVES.** Original G4 stands for a hot bath at \(a'=0\). GR Raychaudhuri applies; ST corrections are off the load-bearing action.

---

## 3. H5 / pre-Door-B — ST acceleration from Jammer’s EOM

### 3.1 Action and EOM (cited, not re-derived from scratch)

Pre-Door-B C9 eq. (1) (historical): Einstein–Hilbert + canonical Φ + \((1/12)R\Phi^2\) + \(V\) + \(\mu(N)[\mathcal{H}-\beta|\Phi|^2]\).

Jammer F-1 §3 (minisuperspace, multiplier eliminated through the Φ equation; \(k=0\), \(\lambda\) kept):

\[
3M^2 H^2 + \frac{\lambda}{\beta^2}H^2 - \frac{H^3}{2\beta} + \frac{1}{\beta}\Bigl[\tfrac34 H\dot H + \tfrac14\ddot H - \tfrac{\dot H^2}{4H}\Bigr] = \rho.
\tag{H5}
\]

Closed \(S^3\) adds \(-3F/a^2\) structure (Jammer caveat); near \(H\to 0\), \(\Phi^2=H/\beta\to 0\) so \(F\to M^2\).

**Jordan ST Raychaudhuri (standard, for orientation).** With \(F = M^2+\Phi^2/6\),

\[
\frac{\ddot a}{a} = -\frac{\rho_m+3p_m}{6F} - \frac{\dot\Phi^2-V}{3F} - \frac{\ddot F}{2F} - \frac{H\dot F}{2F}
\]

(up to conventional grouping of φ stress). At the Janus point \(H\to 0\Rightarrow\Phi\to 0\Rightarrow F\to M^2\), but \(\Phi^2=H/\beta\) makes \(\dot\Phi^2 \sim \dot H^2/(4\beta H)\) **singular unless \(\dot H\to 0\)**. So the GR evaluation \(\ddot a/a = -(\rho+3p)/(6M^2)\) at \(H=0\) with \(\dot H\neq 0\) is **not** a regular point of the H5 system. The right tool is the eliminated EOM (H5), not naive GR ρ+3p.

### 3.2 Regular \(H\to 0\) limit of (H5)

Clear denominators (multiply (H5) by \(4\beta H\), \(\lambda=0\) for the hot-bath sector). Taylor-expand \(H(t) = h_1 t + h_2 t^2/2 + \cdots\) about a geometric turning time with \(H(0)=0\).

| Order | Result |
|---|---|
| \(t^0\) | \(-h_1^2 = 0\) ⇒ \(\dot H(0) = 0\) |
| Hence | \(\dot a(0)=\ddot a(0)=0\) (because \(\ddot a/a = \dot H + H^2\)) |
| Flat, finite \(\rho\) | \(h_2\big(-4\beta\rho - h_2\big)=0\) ⇒ \(h_2=0\) or \(h_2=-4\beta\rho\) |
| Physical branch | \(h_2=-4\beta\rho<0\) for \(\rho>0\) |

On that branch: \(\dddot a(0) = a\,h_2 = -4\beta\rho\,a < 0\), and locally

\[
\dot a(t) \approx \tfrac12 a_0 h_2\, t^2 \le 0.
\]

**No expanding Lorentzian neighbourhood** of a regular \(H=0\) point with finite density.

**Closed universe at GR turnaround radius** (\(k=+1\), \(\rho=3M^2/a_0^2\)): the same clearing forces \(h_1=h_2=0\); higher orders then force \(h_3=h_4=\cdots=0\) in the power series — i.e. the only analytic solution through that radius is the **static** \(H\equiv 0\) slice, which is **not** a radiation solution of the acceleration sector. Again: **no expanding hot-bath birth**.

### 3.3 What this means for “ρ+3p → ä”

- The **GR** test “ρ+3p>0 ⇒ ä<0 ⇒ quadratic maximum” is **replaced**, not copied, under H5: ä is forced to vanish with ȧ, and the first non-trivial flat branch has \(\dot a\le 0\) nearby.
- The **operational G4 claim** — a hot bath at the HH equator does **not** yield an expanding classical Lorentzian universe — **is not reversed**. ST / H5 does not open an escape hatch that GR closed.
- Geometric **a′=0** remains (F-3). Birth-radius numerics \(a_b\approx 0.073\,\ell_{\mathrm{Pl}}\) are GR Door-B numbers; under H5 the regular turnaround structure itself changes (higher-order contact / no analytic radiation turnaround), so those numerics are **not** re-banked as H5 outputs — only the **no-expansion** conclusion is.

**Out of T-2 scope but noted:** H5 also forbids high-scale de Sitter (Jammer F-1), so the plateau *cure* that Door B uses for existence is separately unavailable under H5. T-2 only needs the hot-bath side.

### Verdict 2 — H5

**Recollapse / no-expansion conclusion SURVIVES.** Hot bath at \(a'=0\) still fails to expand under Jammer’s H5 EOM; the GR ρ+3p sign test is superseded by a stronger regular-structure obstruction, not flipped.

---

## 4. Structured summary

| Frame | Acceleration law | Hot bath at \(a'=0\) | Recollapse / no-expansion? |
|---|---|---|---|
| **Door B (current corpus)** | GR: \(\ddot a/a = -(\rho+3p)/(6M^2)\) | ρ+3p=2ρ>0 ⇒ ä<0 ⇒ maximum | **SURVIVES** (original G4) |
| **H5 (pre-Door-B action)** | (H5) third-order; regular \(H=0\) ⇒ \(\dot H=0\), flat branch \(\dot a\le 0\) | No expanding neighbourhood; GR ä≠0 point irregular | **SURVIVES** (not reversed) |

**Geometric a′=0:** unchanged in both frames (F-3).

---

## 5. Non-claims

- Did not re-verify Jammer’s multiplier elimination (that is T-1). Used deposited (H5) as the EOM AC assigned.
- Did not patch Companion 9 or reopen Door B.
- Did not soft-pass exit (a) sequencing (existence-gate OPEN under Part 2 §8.1).
- Blind to Claude T-1.

---

— Cursor Scratch, 2026-09-26.  
T-2 complete. Recollapse survives under Door B (GR) and under H5 (ST/H5 EOM). Nothing patched.
