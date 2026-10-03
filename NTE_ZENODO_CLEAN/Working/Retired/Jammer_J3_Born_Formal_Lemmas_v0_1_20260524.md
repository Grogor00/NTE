# J3 — Born formal lemmas v0.1 (P-B1b / P-B2b)

**From:** Jammer (R&D) — Sprint C  
**Date:** 2026-05-24  
**Status:** **LEMMAS DERIVED** — sharpens §17.5.13; Gap 5 remains **mechanism level**  
**Parents:** `P_Born_P1_*`, `P_Born_P2_*`; Companion 2 v2 §3.3–§3.4

---

## §0. Register

These lemmas **do not** close "Born rule from less than complex + U(1)." They **remove** two hidden premises in Paper 2 Step 1:

1. Kähler structure on projective space is **forced** after gauge birth (J3a).  
2. Quadratic dependence on coordinates is **forced** by Hopf geometry (J3b).

Full $P=|\langle\phi|\psi\rangle|^2$ still requires complex overlap identification (Route C in P-B2).

---

## §1. Lemma J3a — U(1) quotient ⇒ Fubini–Study Kähler

**Statement.** Let $M=U(1)\backslash S^3$ with $S^3\hookrightarrow\mathbb{C}^2\setminus\{0\}$ the unit sphere and U(1) acting by $(z_1,z_2)\mapsto(e^{i\xi}z_1,e^{i\xi}z_2)$. Then $M\cong\mathbb{CP}^1$ carries a **unique** U(1)-invariant Kähler metric — the Fubini–Study metric.

**Proof sketch.** $\mathbb{CP}^1$ is a homogeneous Kähler manifold under U(2). U(1)-invariant Kähler metrics on $\mathbb{CP}^1$ are classified; uniqueness up to scale fixes FS normalization. Gauge birth activates global U(1) phase unobservability (Companion 6 §3.2) ⇒ physical states are rays in $\mathbb{CP}^1$, not points on $S^3$.

**Corpus input:** S1–S2 of P-B1 chain (U(1) fibre + Hopf quotient).

**Does not derive:** $\mathbb{C}$ from $\mathbb{R}$ spinors pre-gauge-birth (P-B1 Routes R1–R3 still open).

---

## §2. Lemma J3b — Hopf quadratic coordinates force $f(r)=r$ on $|z_1|^2$

**Statement.** Let $S^3\subset\mathbb{R}^4$ with Hopf map $\pi:S^3\to S^2$ whose components are homogeneous quadratics in $(x_1,\ldots,x_4)$. Identify $z_1=x_1+ix_2$, $z_2=x_3+ix_4$. Then $|z_1|^2=x_1^2+x_2^2$ is a **quadratic coordinate function** induced by $\pi$, not an independent $|ψ|^2$ axiom.

Let $P_\uparrow=g(r)$ with $r=|z_1|^2$ be U(1)-invariant on $S^3$ with $P_\uparrow+P_\downarrow=1$ and SU(2)-stabilizer + additivity (Companion 2 Step 3). Then $g(r)=r$ uniquely; $g(r)=\sqrt{r}$ and $g(r)=r^2$ are **excluded**.

**Proof sketch.**

- Route A: Hopf components are degree-2 polynomials — bilinearity is in the **map**, not postulated on amplitudes.  
- Route B: On $S^3$, $|z_1|^2+|z_2|^2=1$. Additivity + smoothness at $z_1=0$ + U(1) invariance ⇒ $g(r)=r$ (Companion 2 §3.4).

**Corollary.** Exponent 2 in Born weights is **forced by complex-sphere level-set geometry** once $\mathbb{C}^2$ representatives are identified.

---

## §3. Lemma J3c (partial) — FS overlap ⇒ $\cos^2(\theta/2)$

**Statement (conditional on J3a).** With FS metric on $\mathbb{CP}^1$, transition probability between rays $[\phi],[\psi]$ is

$$P(\phi\to\psi)=|\langle\phi|\psi\rangle|^2=\cos^2(\theta/2)$$

for Bloch angle $\theta$.

**Status:** Standard FS geometry; **not new**. Links J3a+J3b to Paper 2 Step 1 once complex inner product is identified.

---

## §4. §17.5.13 discipline (unchanged)

| Claim | Register |
|-------|----------|
| Gap 5 mechanism (gauge birth + Hopf) | **Closed** |
| Born rule from **less** than complex + U(1) | **Open** |
| J3a–J3c | **Sharpen** mechanism; do not relabel as "from less" |

---

## §5. Falsifiers

1. Admissible U(1)-invariant $P$ linear in $|z_1|$ with additivity — **excluded** (J3b).  
2. Non-quadratic Hopf coordinate producing Born weights — **excluded** (degree argument).  
3. Alternative U(1)-invariant Kähler on $\mathbb{CP}^1$ — **excluded** (uniqueness).

---

## §6. Corpus patch authorised

- **§17.5.13:** cite J3a–J3b as formal lemmas (`Jammer_J3_Born_Formal_Lemmas_v0_1`)

---

— Jammer J3 v0.1, 2026-05-24.
