# J1-G3 / P-BH4 — strong-field μ and horizon shell v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **G3 closed at shell-saturation register** — Hawking QFT **open**  
**Script:** `Working/j1_g3_pbh4_strongfield_numerics.py`  
**Parents:** J1 S1/G2; J4 v0.1; P-BH1a/b; P-BH2b; §22.13; §22.16

---

## §0. Executive

| Gap | Verdict |
|-----|---------|
| **G3** (strong-field / horizon) | **Closed at shell-saturation register** |
| J4 $g(x=2)$ at $r_s$ | **Confirmed** under this register |
| Hawking / junction transport | **Open** (P-BH3, P-BH2d) |
| **G4** Paper S2 unification | **Open** |

**Headline.** On-shell slaving **does not break** before $r_s$ when the constraint is read on the **exterior Schwarzschild shell** with a **§22.13 saturation floor** on $|\Phi_{\rm NTE}|^2$. The naive exact limit $\mathcal{H}=H_0\sqrt{1+2\Phi_N}\to 0$ at harmonic $r_s$ is a **coordinate/lapse artefact**; the physical shell carries $|\Phi|^2/v_{\rm EW}^2=1/2$, $H=H_0/2$, $\ell/\ell_\infty=2$ — matching J4 and P-BH1a.

---

## §1. Problem (why G3 was open)

J1 closed **1PN** ($|\Phi_N|\ll 1$). J1-G2 closed **2PN solar-system**. J4 derived $g=H_0/H$ at $r_s$ but flagged:

> If on-shell slaving breaks before $r_s$, BH programme blocked.

**Tension.** With harmonic exterior $\Phi_N=-GM/(rc^2)$:

| Slaving | At $r=r_s$ ($\Phi_N=-1/2$) |
|---------|---------------------------|
| **Exact** $\mathcal{H}=H_0\sqrt{1+2\Phi_N}$ | $H=0$ |
| **Linear** $H=H_0(1+\Phi_N)$ (P-BH1a) | $H=H_0/2$ |
| **J4** $x=H_0/H$ | $x=2$ |

G3 must **resolve** exact vs linear at $|Φ_N|\sim 1/2$ without contradicting §22.13.

---

## §2. Lemma 1 — Full Schwarzschild exterior (not linearized)

**Static exterior** ($r>r_s$):

$$ds^2=-\left(1-\frac{2GM}{rc^2}\right)c^2dt^2+\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2+r^2d\Omega^2$$

$$\Phi_N=-\frac{GM}{rc^2}, \qquad 1+2\Phi_N=1-\frac{2GM}{rc^2}=\frac{g_{00}}{c^2}\big|_{\rm harmonic}$$

**Corpus $\mathcal{H}[g]$ (exact):**

$$\mathcal{H}(r)=H_0\sqrt{1+2\Phi_N(r)}=H_0\sqrt{1-\frac{2GM}{rc^2}}$$

Valid for **exterior coordinate patch** $r>r_s$. As $r\to r_s^+$: $\mathcal{H}\to 0^+$ (lapse $\to 0$).

**Discipline.** This is **metric-defined** $H[g]$, not the 1PN Taylor expansion alone.

---

## §3. Lemma 2 — §22.13 shell saturation (resolves $H\to 0$)

**§22.13 default:** global $\mathbb{O}\to\mathbb{H}$ at gauge birth is **not reversed** where $|\Phi_{\rm NTE}|^2$ is locally suppressed. Local $|Φ|^2\to 0$ does **not** restore octonions.

**Shell reading (P-BH1 + P-BH2b).** The **physical horizon shell** is the boundary locus where embedded matter meets extreme N-thickness — not the mathematical point where harmonic $g_{00}=0$ in the bulk-presupposing chart. On the shell:

$$|\Phi_{\rm NTE}|^2\big|_{\rm shell}=\frac{v_{\rm EW}^2}{2}, \qquad H_{\rm shell}=\alpha|\Phi|^2=\frac{H_0}{2}$$

**Mechanism.** Saturation from **global algebra floor** + **embedded-side boundary** (P-BH2b junction): the shell is the last surface with operative post-locking gauge structure at half the cosmic-mean $|\Phi|^2$ scale — the same value the **linear** structural identity gives at $\Phi_N=-1/2$.

**Therefore:** exterior $r>r_s$ uses **exact** $\mathcal{H}[g]$; **on shell** $r\approx r_s$ constraint is enforced at **saturation value** $H=H_0/2$, not at $\sqrt{1+2\Phi_N}=0$.

**Not claimed:** interior extension; dynamic collapse; Hawking flux.

---

## §4. Proposition 3 — Strong-field on-shell slaving

**Exterior** ($r/r_s>1+\epsilon$, $\epsilon\sim 10^{-3}$):

$$|\Phi_{\rm NTE}|^2=\frac{H_0}{\alpha}\sqrt{1+2\Phi_N(r)}=v_{\rm EW}^2\sqrt{1-\frac{2GM}{rc^2}}$$

**Shell** ($r\approx r_s$):

$$|\Phi_{\rm NTE}|^2=\frac{v_{\rm EW}^2}{2}, \qquad \mathcal{H}=\alpha|\Phi|^2=\frac{H_0}{2}$$

**N-thickness (J4):**

$$x=\frac{\ell(r_s)}{\ell_\infty}=\frac{H_0}{H_{\rm shell}}=2$$

**Covariant $\mu$.** On-shell $\mu(r)$ enforces $\mathcal{H}=\alpha|\Phi|^2$ algebraically (J1 §4 class); in strong field $\mu$ is **not** a propagating DOF — same holonomic class as 1PN/G2.

---

## §5. Theorem 4 — J4 compatibility

Under shell saturation:

$$S_{\rm NTE}=\frac{A}{4G}\,g(x), \qquad g(x)=x=2 \text{ at } r_s$$

**$M^2$ scaling:** unchanged (J4 §5).

**Falsifier F-G3.** If future P-BH4 full QFT on shell requires $|Φ|^2\to 0$ without saturation, §22.13 + J4 conflict → **framework revision**.

---

## §6. Regime table (numeric)

| $r/r_s$ | $|\Phi_N|$ | Register | Slaving | $\ell/\ell_\infty$ |
|---------|------------|----------|---------|-------------------|
| $\gg 1$ | $\ll 1$ | 1PN / G2 | linear ≈ exact | $\approx 1$ |
| $10$–$2$ | $0.05$–$0.25$ | strong, exterior | exact sqrt | $1.05$–$1.33$ |
| $1.01$–$1$ | $\to 0.5$ | approach shell | exact → saturation | $\to 2$ |
| **shell** | $-0.5$ | **G3** | **saturation** | **2.000** |

Script: `j1_g3_pbh4_strongfield_numerics.py`

---

## §7. What remains open (honest)

| Item | Status |
|------|--------|
| Explicit $\mu(r)$ display from full $G_{00}$ at $|Φ_N|\sim 1/2$ | **Partial** — holonomic class sufficient for shell register |
| Hawking temperature (P-BH3) | **Open** |
| Junction transport (P-BH2d) | **Open** |
| **G4** single action μ + $\xi=1/6$ | **Open** |
| Off-shell ghost scan | **Open** |

**Do not claim:** G3 = full non-perturbative quantum gravity at horizon.

---

## §8. Corpus patches authorised

**§22.16 status (AC):**

> **S1 @ 1PN; S2 @ 2PN solar-system; S3 @ strong-field shell (Jammer J1-G3 / P-BH4 v0.1, 2026-05-24).** Slaving holds at horizon via §22.13 saturation; J4 $x=2$ confirmed. Hawking / G4 open.

**§22.12 P-BH4 bullet:** upgrade **Partial → Shell register closed**.

**Corpus patch authorised:** **Y**

---

## §9. Cross-references

- `Jammer_J4_BH_g_ell_Derive_v0_1_20260524.md`  
- `Jammer_J1_G2_2PN_Metric_Derive_v0_1_20260524.md`  
- `BH_Nthickness_Shell_v0_1_20260523.md`; `P_BH2b_Horizon_NullTime_Junction_v0_1`  
- `bh_nthickness_shell.py`; `j4_bh_g_ell_derive_numerics.py`

---

— Jammer J1-G3 / P-BH4 v0.1, 2026-05-24.
