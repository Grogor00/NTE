---
title: "Robertson–Walker spectral-action coefficients (prior-art extract)"
subtitle: "Chamseddine–Connes a₀–a₁₀ for Euclidean RW metrics, and their relation to the NTE substrate"
author: "Gregory Lyndon White"
date: "2026-08 (Companion 14; prior-art extract)"
---

*Part of NTE Corpus v10.19.0. Companion 14.*

*Independent researcher, Auckland, New Zealand · gregwhite00@gmail.com · ORCID 0009-0003-3680-2363*

*This companion is a **prior-art extract**, not an NTE derivation. It records the Seeley–DeWitt / spectral-action coefficients for Euclidean Robertson–Walker metrics computed by Chamseddine and Connes (arXiv:1105.4637; JHEP 10 (2012) 101), states their honest scope relative to the framework's canonical substrate, and parks the explicit formulae for reference by Companions 11–12 and the accounting ledger. No new physics is claimed.*

---

## Abstract

Chamseddine and Connes computed the asymptotic expansion of the spectral action for Euclidean Robertson–Walker (RW) metrics with round $S^3$ spatial sections, checking through $a_6$ against Gilkey's universal formulae and extending the direct method through $a_{10}$. This companion extracts those coefficients — $a_0$, $a_2$, $a_4$, $a_6$, $a_8$, and the structure of $a_{10}$ — in a form usable inside the NTE corpus.

The extract is scoped tightly. NTE's *canonical* gravitational substrate is the product $S^3\times S^1$ (with octonionic finite algebra), on which $a_4=0$ by the Weyl-flat / Euler-zero combination (Companions 11–12). The RW family studied here is a different geometry: a time-dependent scale factor $a(t)$ with $S^3$ fibres. The RW coefficients are **imported prior art** — useful as (i) the standard dynamical spectral-action cosmology for a scale factor, (ii) a check-suite for any future heat-kernel work that touches an evolving $a(t)$, and (iii) the source of the known fact that RW $a_4$ is topological (total derivative / Gauss–Bonnet) and does not drive the scale-factor dynamics, while $a_6$ does. They are not a substitute for the substrate computation on $S^3\times S^1$, and they do not derive $\Lambda$, $n_s$, or $r$.

---

## 1. Source and scope

**Source.** A. H. Chamseddine and A. Connes, *Spectral action for Robertson–Walker metrics*, JHEP **10** (2012) 101 [arXiv:1105.4637]. Method: reduce the Dirac spectrum on Euclidean RW to a family of one-dimensional Schrödinger operators; evaluate the heat expansion by Feynman–Kac / Brownian-bridge integrals plus Euler–Maclaurin (later Poisson) summation; cross-check even terms through $a_6$ against Gilkey. Extended confirmation through $a_{12}$ and a rationality theorem: Fathizadeh, Ghorbanpour, and Khalkhali, JHEP **12** (2014) 064 [arXiv:1407.5972].

**Geometry.** Euclidean RW with round $S^3$ symmetry:

$$ds^2 = dt^2 + a(t)^{2}\bigl(d\chi^2 + \sin^2\chi\,d\theta^2 + \sin^2\chi\sin^2\theta\,d\phi^2\bigr).$$

Scalar curvature (their convention):

$$R = 6\left(\frac{a''}{a} + \frac{(a')^{2}-1}{a^{2}}\right).$$
The Weyl tensor vanishes identically on this family.

**What this companion is not.** It is not a re-derivation; not a claim that NTE's canonical $a_4=0$ result is an RW statement; not a derivation of the observed $\Lambda$; not a route to $K(\Phi)$, $n_s$, or $r$. Those remain as in Part 3.

**ArXiv note.** The nearby identifier `1105.4200` is an unrelated quant-ph paper; the RW spectral-action paper is **1105.4637**.

---

## 2. Spectral action through $a_6$

With cutoff function $f$ and Planck mass $M_{\mathrm{Pl}}$,

$$I = \operatorname{Tr} f\!\left(\frac{D^2}{M_{\mathrm{Pl}}^2}\right) = M_{\mathrm{Pl}}^4 f_4\,a_0 + M_{\mathrm{Pl}}^2 f_2\,a_2 + f_0\,a_4 + M_{\mathrm{Pl}}^{-2} f_{-2}\,a_6 + \cdots,$$

where

$$f_4=\int_0^\infty u\,f(u)\,du,\quad f_2=\int_0^\infty f(u)\,du,\quad f_0=f(0),\quad f_{-2}=-f'(0).$$
Odd local densities vanish for the full Dirac operator (time-reversal symmetry $H_n^+\oplus H_n^-$). Below, $a_0$, $a_2$, $a_6$, $a_8$, $a_{10}$ are quoted as **local densities of $dt$** after the $S^3$ integral (Chamseddine–Connes convention); $a_4$ is written in integrated form as in their eq.\ (62).

---

## 3. The coefficients

### 3.1 $a_0$ — volume

$$a_0 = \tfrac{1}{2}\,a^{3}.$$

(Equivalent: $\frac{1}{16\pi^2}\times 4\times\mathrm{Vol}(S^3_a)$ with $\mathrm{Vol}(S^3_a)=2\pi^2 a^3$.)

### 3.2 $a_2$ — Einstein–Hilbert

$$a_2 = \frac{a^{3}}{4}\left(\frac{a''}{a}+\frac{(a')^{2}-1}{a^{2}}\right).$$

(Equivalent: $\frac{1}{16\pi^2}\times 4\times\mathrm{Vol}(S^3_a)\times R/12$.)

### 3.3 $a_4$ — topological / non-dynamical for $a(t)$

$$a_4 = \frac{1}{120}\int\!dt\,\bigl(3a^{2} a^{(4)} + 9\,a\,a'\,a^{(3)} + 3\,a\,(a'')^{2} - 4\,(a')^{2} a'' - 5\,a''\bigr).$$

This is a linear combination of $\square R$ and the Gauss–Bonnet density. On RW the Weyl tensor vanishes, so

$$a_4 = \frac{1}{16\pi^{2}}\frac{1}{360}\int d^{4}x\sqrt{g}\,\bigl(-18\,C^{2} + 11\,R^{*}R^{*} + 12\,\square R\bigr)$$

reduces to topological plus surface content. Consequence recorded by Chamseddine–Connes: $a_4$ does not contribute to the dynamical equation for $a(t)$.

*Relation to NTE.* The framework's $a_4=0$ on the product $S^3\times S^1$ is a different statement (pointwise vanishing of $-18C^{2}+11E_4$ on that substrate; Companions 11–12). Do not conflate RW topological $a_4$ with substrate $a_4=0$.

### 3.4 $a_6$ — first dynamical higher term

$$
\begin{aligned}
a_6
&= -\frac{(a')^{2} a''}{240\,a^{2}}
  -\frac{(a')^{4} a''}{84\,a^{2}}
  +\frac{(a'')^{2}}{120\,a}
  +\frac{(a')^{2}(a'')^{2}}{21\,a}
  -\frac{(a'')^{3}}{90} \\
&\quad
  +\frac{a'\,a^{(3)}}{240\,a}
  +\frac{(a')^{3} a^{(3)}}{84\,a}
  -\frac{a'\,a''\,a^{(3)}}{20}
  -\frac{a\,(a^{(3)})^{2}}{1680}
  -\frac{a^{(4)}}{240} \\
&\quad
  -\frac{(a')^{2} a^{(4)}}{120}
  +\frac{a\,a''\,a^{(4)}}{840}
  +\frac{a\,a'\,a^{(5)}}{140}
  +\frac{a^{2} a^{(6)}}{560}.
\end{aligned}
$$

Sphere check ($a=\sin t$): $\int_0^\pi a_6\,dt = 31/1890$.

Chamseddine–Connes note that because $a_4$ is non-dynamical for $a(t)$, **$a_6$ is the first spectral-action correction with non-trivial effects on standard cosmological dynamics** in this expansion.

### 3.5 $a_8$

$$a_8 = -\frac{1}{10080\,a^{4}}\,P(a),$$

where $P(a)$ is the degree-homogeneous polynomial in $a$ and its derivatives through $a^{(8)}$ given in §8 of arXiv:1105.4637 (their display following the Poisson-summation reduction). Sphere check:

$$a_8(S^4)=\frac{41\sin^{3} t}{10080},\qquad \int_0^\pi a_8\,dt = \frac{4}{3}\times\frac{41}{10080}.$$

### 3.6 $a_{10}$

$$a_{10} = \frac{1}{665280\,a^{6}}\,Q(a),$$

with $Q(a)$ the explicit polynomial through $a^{(10)}$ in the same section of the source paper. Sphere check:

$$a_{10}(S^4)=\frac{31\sin^{3} t}{15840},\qquad \int_0^\pi a_{10}\,dt = \frac{4}{3}\times\frac{31}{15840}.$$

(The integrand display in the arXiv PDF is the authoritative expansion; it is omitted here only for length.)

### 3.7 Rationality (later result)

Fathizadeh–Ghorbanpour–Khalkhali prove that each even coefficient has the form

$$a_{2n} = \frac{Q_{2n}\bigl(a,a',\ldots,a^{(2n)}\bigr)}{a^{2n-3}}$$

with $Q_{2n}$ a polynomial with rational coefficients, and extend the explicit computation through $a_{12}$. That confirms the Chamseddine–Connes $a_8$, $a_{10}$ and settles their rationality conjecture.

---

## 4. How this sits in the NTE corpus

| Item | Status in NTE |
|------|----------------|
| RW $a_0$–$a_{10}$ formulae | **Imported prior art** (this companion). |
| Canonical substrate $a_4=0$ on $S^3\times S^1$ | **Framework structural fact** (Companions 11–12; F₁/heat-kernel line) — *not* an RW claim. |
| Unimodular / boundary-only $\Lambda$ suppression | Structural; acts at the extensive $a_0$ mode; independent of RW $a_6$ (Companion 11). |
| Dynamical use of RW $a_6$ for $a(t)$ cosmology | Available as prior art if/when the corpus treats an evolving scale factor spectrally; **not** currently load-bearing for deposited Parts 1–3 predictions. |
| $n_s$, $r$, $K(\Phi)$ | Remain open / conditional (Part 3); the RW expansion does not close $K(\Phi)$. |

The useful cross-check for the framework is discipline, not substitution: when the corpus speaks of spectral-action cosmology with a scale factor, these are the coefficients; when it speaks of the deposited substrate chord, the geometry is $S^3\times S^1\times(\mathbb{O}\oplus\mathbb{O})$ and Companion 12 governs.

---

## 5. Open pointers (prior-art side)

From Chamseddine–Connes §9, still useful as external open items (not NTE claims):

1. Match $a_8$, $a_{10}$ against the universal Gilkey / Vassilevich local formulae in full generality.
2. Closed form for all $a_{2n}=P_n(a,\ldots,a^{(2n)})/a^{2n-4}$ (partially settled by the 2014 rationality theorem; full generating function open).
3. Conceptual reading of the Brownian-bridge integration as a fluctuation of the time variable — interpretive, not required by NTE.

---

## References

1. A. H. Chamseddine and A. Connes, "Spectral action for Robertson–Walker metrics," JHEP **10** (2012) 101 [arXiv:1105.4637] — primary source for §§2–3 of this companion.
2. F. Fathizadeh, A. Ghorbanpour, and M. Khalkhali, "Rationality of spectral action for Robertson–Walker metrics," JHEP **12** (2014) 064 [arXiv:1407.5972] — $a_{12}$ and rationality of $Q_{2n}$.
3. P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (Publish or Perish / CRC); D. V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rep. **388**, 279 (2003) — universal Seeley–DeWitt formulae used as the $a_0$–$a_6$ check.
4. A. H. Chamseddine and A. Connes, "The Spectral Action Principle," Commun. Math. Phys. **186**, 731 (1997); and subsequent spectral-action unification papers — the parent programme.
5. NTE corpus: Companion 11 (Λ / unimodular suppression); Companion 12 (chord / substrate $a_4=0$); Part 3 (accounting — $a_4=0$ on $S^3\times S^1$; $K(\Phi)$ open).
