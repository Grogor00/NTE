# P-Born P-B2 — Hopf bilinearity without $|ψ|²$ premise v0.1 (§17.5.13)

**Stream:** Cursor scaffold → Jammer / Paper 2 Step 1 extension  
**Date:** 2026-05-23  
**Status:** **Attack route mapped** — Hopf map is intrinsically quadratic in $\mathbb{R}^4$ coords; linear-in-$|z|$ alternatives **falsified**; full Born rule still needs complex overlap identification (P-B1 chain)  
**Parent:** `Priority_IV_Pathway_Programmes_v0_1_20260523.md` P-B2  
**Depends:** P-B1 (FS/Kähler on $\mathbb{CP}^1$); Companion 2 §3.3–§3.4

---

## §1. Mission

Paper 2 Step 1 **imports** complex coordinates and lists $|z_1|^2$ as a U(1)-invariant monomial. §17.5.13 flags this as **bilinearity in amplitude taken as premise**.

**P-B2 target:** derive the **quadratic** (not linear) dependence from **Hopf projection geometry alone** — before naming $|⟨·|·⟩|^2$.

**Honest v0.1 register:** the Hopf map's polynomial degree and S³ normalisation **force** $f(r)=r$ on $|z_1|^2$ **once** complex representatives are identified; a **real-only** route yields quadratic Bloch coordinates but not full inner-product bilinearity without P-B1.

---

## §2. Diagnosis — what Step 1 actually assumes

| Step | Companion 2 content | Hidden premise |
|------|---------------------|----------------|
| **Facts 1–2** | $S^3 \subset \mathbb{C}^2$, $|z|^2=1$, U(1) phase | **Complex** 2-spinor |
| **Step 1** | U(1)-invariants: $|z_1|^2$, $z_1\bar z_2$, … | **Mod-squared** already in candidate list |
| **Step 3** | Stabilizer kills cross-terms; $f(r)+f(1-r)=1$ + additivity $\Rightarrow f(r)=r$ | **Linear in** $|z_1|^2$ — exponent 2 not yet explained |
| **§3.4** | Exponent 2 from **quadratic** S³ constraint $|z_1|^2+|z_2|^2=1$ | **Closes exponent** given complex sphere |

**P-B2 split:**

1. **Exponent / functional form** — why $P \propto |z_1|^2$ not $|z_1|$? → Hopf + normalisation (§3 below).  
2. **Bilinear overlap** — why $|⟨φ|ψ⟩|^2$? → FS metric on $\mathbb{CP}^1$ (P-B1 §3) or Gleason-grade Hilbert import.

---

## §3. Route A — Hopf map is quadratic in $\mathbb{R}^4$ (partial closure)

Embed $S^3 \hookrightarrow \mathbb{R}^4$ as unit 4-vector $x=(x_1,x_2,x_3,x_4)$.

**Standard Hopf map** (to $S^2 \subset \mathbb{R}^3$):

$$\pi(x)=\bigl(2(x_1x_3+x_2x_4),\;2(x_2x_3-x_1x_4),\;x_1^2+x_2^2-x_3^2-x_4^2\bigr)$$

Every component is **homogeneous quadratic** in $(x_i)$. No $|ψ|^2$ symbol — **bilinearity is in the map**, not in a postulated probability functional.

**Identification with complex coords** (when P-B1/Cayley-Dickson supplies $\mathbb{C}$):

$$z_1=x_1+ix_2,\quad z_2=x_3+ix_4 \quad\Rightarrow\quad |z_1|^2=x_1^2+x_2^2,\; |z_2|^2=x_3^2+x_4^2$$

So $|z_1|^2$ is a **quadratic coordinate function on $S^3$** induced by the Hopf fibration — not an independent amplitude-squared axiom.

**Register:** Route A closes "why quadratic in coords" at the **projection** level; it does not yet define **transition probability** without a measure / metric choice (§4–§5).

---

## §4. Route B — normalisation kills $|z_1|$ (exponent selection)

On $S^3$: $|z_1|^2+|z_2|^2=1$. Candidate $P_\uparrow = g(|z_1|)$ with U(1) + stabilizer symmetry → $g$ depends on radius $|z_1|\in[0,1]$ only.

| Candidate | On $S^3$? | Smooth at $z_1=0$? | Complementarity $P_\uparrow+P_\downarrow=1$ |
|-----------|-----------|-------------------|---------------------------------------------|
| $g(r)=r$ with $r=|z_1|^2$ | ✓ | ✓ | ✓ linear in $r$ |
| $g(r)=|z_1|= \sqrt{r}$ | ✗ (simplex, not sphere) | cusp at 0 | fails additivity across partitions (Companion 2 §3.4) |
| $g(r)=r^2$ | ✓ | ✓ | fails unless renormalised; breaks additivity |

**Conclusion (Companion 2 §3.4, sharpened):** the **quadratic constraint** defining $S^3$ as a complex sphere forces probabilities **linear in $|z_1|^2$**, not in $|z_1|$. This is **geometry of the level set**, not a free Born postulate.

**P-B2 partial closure:** exponent 2 is **forced** by (i) complex-sphere constraint + (ii) Step 3 additivity/consistency. Remaining import: **why complex sphere** (P-B1).

---

## §5. Route C — FS / fibre measure (links P-B1)

**Programme for probability as geometry:**

1. **Haar** on $S^3$ → **pushforward** along Hopf fibres → **Fubini–Study** volume on $\mathbb{CP}^1$.  
2. **Projection probability** for outcome subspace = **FS overlap** = $\cos^2(\theta/2)$ on Bloch sphere (P-B1 §3).

**Register:** Route C derives $|\langle\phi|\psi\rangle|^2$ as **metric overlap** given Kähler structure — **not** as a separate $|ψ|^2$ axiom. Requires P-B1 (U(1) fibre → FS).

---

## §6. Route D — real spinor only (open)

Pre–gauge-birth: real spinor modes on $S^3$ (Companion 6 §2). **Question:** define transition weights using only $\mathbb{R}^4$ inner product + Hopf $\pi$.

**Obstacle:** orthogonal real 4-vectors can project to **same** Bloch point; probabilities need **complex ray** structure. Cayley-Dickson / P-B1 route is the intended bridge.

**Status:** **Open** — real-only Born rule without importing $\mathbb{C}$ is not closed in v0.1.

---

## §7. Synthesis — theorem vs sharpened vs open

| Claim | Status |
|-------|--------|
| Hopf components are quadratic polynomials on $\mathbb{R}^4$ | **Theorem** (standard) |
| $P_\uparrow$ linear in $|z_1|^2$ given U(1)+SU(2) stabilizer + additivity | **Theorem** (Companion 2 Step 3) |
| $|z_1|^2$ is Hopf-induced quadratic coord, not free $|ψ|^2$ | **Sharpened** (Route A) — v0.1 |
| Full $P=|\langle\phi|\psi\rangle|^2$ without complex Hilbert import | **Open** (needs P-B1 + Route C) |
| Born rule from **less** than complex + U(1) | **Open** — §17.5.13 discipline |

---

## §8. Falsifiers

1. Admissible U(1)-invariant $P$ **linear in $|z_1|$** satisfying additivity — **excluded** (§4).  
2. Non-quadratic Hopf coordinate map producing Born weights — **excluded** (Route A degree).  
3. Claim P-B2 closes Gap 5 **from less** while still using $\mathbb{C}^2$ — **scope violation**.

---

## §9. Deliverables checklist

| ID | Task | Status |
|----|------|--------|
| P-B2a | This attack-route note | **Done v0.1** |
| P-B2b | Formal lemma: Hopf quadratic coords $\Leftrightarrow$ $|z_1|^2$ | Jammer |
| P-B2c | Haar pushforward → FS probability (Route C) | Jammer |
| P-B2d | Paper 2 Step 1 rewrite draft (real-coords first) | Jammer / PC |

---

## §10. Cross-references

- Companion 2 v2 §3.3–§3.4, §7.2; Companion 6 v2 §3.3  
- `P_Born_P1_Complex_Structure_Gauge_Birth_v0_1`; `P_Born_P3_Zurek_Scope_Pairing_v0_1`  
- §17.5.13, §20.5 (Zurek complement)

— Cursor P-Born P-B2 v0.1, 2026-05-23.
