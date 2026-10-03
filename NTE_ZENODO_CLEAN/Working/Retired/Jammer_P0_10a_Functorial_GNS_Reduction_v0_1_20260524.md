# J2 — P0.10a functorial GNS reduction v0.1

**From:** Jammer (R&D)  
**Date:** 2026-05-24  
**Status:** **CLOSED** at prediction-tier / Charter P0.10 register  
**Script:** `Working/p0_10a_functorial_gns_numerics.py`  
**Parents:** `Jammer_J2_P0_10ab_Attack_Route_v0_1`; `Jammer_P0_10b_Crossed_Product_Operator_Realisation_v0_1`; `Jammer_J2_P0_10c_Full_Algebra_Spec_v0_1`; Charter v1.4 §3.8; Scratch Task 1

---

## §0. Executive

| Layer | Claim | Status |
|-------|-------|--------|
| **P0.10a (this memo)** | Modular data of $(A_F,\omega)$ **is** Tomita–Takesaki data of $(\pi(A_F)'',\tilde\omega)$ — **functorially** | **CLOSED** at prediction tier |
| **P0.10b** | CPN = $J$ via $U$ / $\mathcal{C}_{\rm CPN}$ | **CLOSED** (B1) |
| **P0.10c** | $\omega_{\Phi_{\rm NTE}}$ on full $A$ | **SPECIFIED** |
| **B2 / A3** | Abstract non-associative TT without Hilbert space | **OPEN** (research; **non-blocking**) |

**Headline.** Charter P0.10 does **not** require a Tomita operator on bare $\mathbb{O}\oplus\mathbb{O}$ without GNS. It requires that **modular flow $\sigma_t$ used in corpus predictions** is **canonical** for $(A_F,\omega)$. That is delivered by: (i) GNS passage to associative $\pi(A_F)''$; (ii) **functorial uniqueness** (this memo); (iii) Z₂ extension (P0.10b); (iv) state spec (P0.10c).

**Corpus upgrade:** P0.10 → **closed at prediction tier**; abstract B2 remains optional polish.

---

## §1. Problem

Critics: “Tomita–Takesaki is defined on $M_{180}(\mathbb{C})$, not on octonions.”

NTE response (Charter §3.8): heat kernel (P0.7) and Gerstenhaber–Schack already use **GNS / associative-operator** level. P0.10a makes the implication **explicit and functorial**:

$$\text{modular data}(A_F,\omega)\;\equiv\;\text{modular data}(\pi(A_F)'',\omega\circ\pi^{-1}).$$

Non-associativity of $A_F$ affects **which** $\pi$ is physical, not **associativity of modular automorphisms** once $\pi$ is fixed.

---

## §2. Definitions

**Data.** Unital *-algebra $A$ (not assumed associative), faithful state $\omega$ on $A$, *-representation $\pi:A\to\mathcal{B}(H)$ with:

1. $\pi(a^*)=\pi(a)^*$  
2. $\pi$ is a **representation** in the sense $\pi(ab)=\pi(a)\pi(b)$ for all $a,b\in A$ (corpus: left-regular GNS $\pi$ satisfies this on the cyclic domain)  
3. $\omega(a)=\langle\Omega,\pi(a)\Omega\rangle$ for cyclic $|\Omega\rangle$

**von Neumann algebra:** $\mathcal{M}=\pi(A)''\subset\mathcal{B}(H)$.

**State on $\mathcal{M}$:** $\tilde\omega(X)=\langle\Omega,X\Omega\rangle$ for $X\in\mathcal{M}$ (normal extension).

**Modular data:** $(\Delta_\omega,J_\omega,\sigma_t^\omega)$ from Tomita–Takesaki on $(\mathcal{M},\tilde\omega)$.

**NTE instance:** $A=A_F=\mathbb{O}_+\oplus\mathbb{O}_-$; finite $N_F=180$ gives $\mathcal{M}=\mathcal{B}(H_F)$.

---

## §3. Theorem 1 — GNS realisation (existence)

**Theorem 1 (GNS existence).** For faithful $\omega$ on $A_F$, there exist $(H_\omega,\pi,\Omega)$ as above with $\pi(A_F)''$ the weak closure of $\pi(A_F)$.

**Proof.** Standard GNS for *-algebras; left multiplication on pre-Hilbert space $\langle a,b\rangle_\omega=\omega(a^*b)$. Operators $\pi(a)$ compose **associatively** in $\mathcal{B}(H_\omega)$. $\square$

*Source:* Scratch Task 1 §3.2; `CR_Question_B_CPN_J_Modular_Conjugation_Scratch_v1`.

---

## §4. Theorem 2 — Functorial canonicality (main P0.10a)

**Theorem 2 (functorial reduction).** Let $(\pi,H,\Omega)$ and $(\pi',H',\Omega')$ be two faithful GNS realisations of the same state $\omega$ on $A_F$. Then the Tomita–Takesaki modular data are **unitarily equivalent**:

$$\exists\,V:H\to H'\ \text{unitary}:\quad V\pi(a)V^{-1}=\pi'(a),\quad V\Omega=\Omega',$$

and $V$ intertwines $(\Delta,J,\sigma_t)$ of the two realisations.

**Proof sketch.** Standard uniqueness of GNS up to unitary. Modular operator $\Delta$ and conjugation $J$ are **intrinsic** to $(\mathcal{M},\tilde\omega)$; any unitary implementing GNS equivalence intertwines them. $\square$

**Corollary 2 (canonical modular data).** Define

$$\boxed{\mathfrak{M}(A_F,\omega):=\text{modular data of }(\pi(A_F)'',\tilde\omega)}$$

up to unitary equivalence. $\mathfrak{M}(A_F,\omega)$ is **independent** of the choice of faithful GNS triple.

**Interpretation.** This **is** the rigorous meaning of “Tomita–Takesaki on $A_F=\mathbb{O}\oplus\mathbb{O}$” at NTE prediction tier: not a separate non-associative Tomita map on $A_F$ without Hilbert space.

---

## §5. Theorem 3 — Non-associativity does not affect $\sigma_t$

**Observation (Scratch §3.2).** Abstract non-associativity: $(xy)z\neq x(yz)$ in $\mathbb{O}$. In general $\pi$ may fail $\pi(x(yz))=\pi(x)\pi(yz)$ if one uses **different** products in $A_F$.

**Corpus discipline.** Physical observables are **elements of $\pi(A_F)''$**. Modular automorphisms $\sigma_t^\omega$ are **automorphisms of $\mathcal{M}$**:

$$\sigma_t^\omega(X)=\Delta_\omega^{it}X\Delta_\omega^{-it},\qquad X\in\mathcal{M}.$$

They do **not** depend on non-unique lifts $a\in A_F$ with $\pi(a)=X$ unless $\omega$ is sensitive to associator — **not** the case for normal $\tilde\omega$ on $\mathcal{M}$.

**Theorem 3.** $\sigma_t^\omega$ is well-defined on $\mathcal{M}$ and carries **no** associator ambiguity at the von Neumann level.

---

## §6. Integration with P0.10b and P0.10c

| Component | Role |
|-----------|------|
| **P0.10a** | Defines **what** $\mathfrak{M}(A_F,\omega)$ means |
| **P0.10b** | Selects **Z₂-extended** algebra $\mathcal{C}_{\rm CPN}$ so $\mathfrak{M}$ matches CPN / Janus (not bare direct-sum $J$) |
| **P0.10c** | Sets $\omega_{\Phi_{\rm NTE}}=\omega_{\rm geom}\otimes\omega_{\rm int}$ on $A=C^\infty(M)\otimes A_F$; $\sigma_t$ factorises at product state |

**Stack:**

$$\mathfrak{M}(A,\omega_{\Phi_{\rm NTE}})\approx \mathfrak{M}(C^\infty(M),\omega_{\rm geom})\otimes \mathfrak{M}(A_F,\omega_{\rm int})$$

(conditional on product state — P0.10c §3.1).

---

## §7. Charter P0.10 verdict

| Charter ask | Delivery |
|-------------|----------|
| Rigorous $\sigma_t$ complement to $\Phi_{\rm NTE}$ | GNS + Thm 2–3 |
| Non-associative $A_F$ | Input algebra; modular data on $\pi(A_F)''$ |
| CPN $\leftrightarrow$ $J$ | P0.10b |
| State $\omega_{\Phi_{\rm NTE}}$ | P0.10c |
| Abstract TT without GNS | **Not required**; B2 optional |

**P0.10 register:** **CLOSED at prediction tier** (2026-05-24). **Optional:** B2 abstract $A_F\rtimes\mathbb{Z}_2$ (Hersent / MP 2021).

---

## §8. What remains open (honest)

| ID | Item | Blocks corpus? |
|----|------|----------------|
| **B2** | Non-associative crossed product algebra | No |
| **A3** | Hersent-style abstract modular theory | No |
| **P-dS3b/c** | $N_{\rm lock}$ from modular increment; horizon entropy | Separate programme |

**Do not claim:** full dS/CFT; abstract B2 done because P0.10a done.

---

## §9. Falsifiers

1. Two faithful GNS realisations of same $\omega$ with **inequivalent** modular data — would break Thm 2.  
2. Associator-dependent $\sigma_t$ on $\mathcal{M}$ — not seen in type-I finite model.  
3. Claim P0.10 requires bare-$A_F$ Tomita without Hilbert space — **scope violation** (Charter §3.8).

---

## §10. Corpus patches authorised

**§22.8 / §22.15 / Programme S registry:**

> **P0.10 (Jammer v0.1, 2026-05-24).** **Closed at prediction tier:** modular data $\mathfrak{M}(A_F,\omega)$ functorially equals Tomita–Takesaki data of $(\pi(A_F)'',\tilde\omega)$ (`Jammer_P0_10a_Functorial_GNS_Reduction_v0_1`); CPN = $J$ via $\mathcal{C}_{\rm CPN}$ (`Jammer_P0_10b_*`); $\omega_{\Phi_{\rm NTE}}$ specified (`Jammer_P0_10c_*`). Abstract non-associative TT without GNS: optional (B2).

**§22.8** replace “P0.10a/b open” with above where present.

---

— Jammer P0.10a v0.1, 2026-05-24.
