# Susskind Test D1 — Janus cross-sector correlator (AJ-21)

**From:** Cursor Jammer  
**Date:** 2026-06-02  
**Re:** `Handoff_Cursor_Main_to_Jammer_Susskind_D1_Cluster_Test_20260601.md`

---

## Setup (minimal toy)

Chirality space $\mathcal H = \mathrm{span}\{|R\rangle,|L\rangle\}$, $|\Psi_{\text{Janus}}\rangle = \frac{1}{\sqrt2}(|R\rangle+|L\rangle)$.

**Sector-local** observables: $\mathcal O_R = \Pi_R \hat A \Pi_R$, $\mathcal O_L = \Pi_L \hat B \Pi_L$ with $\Pi_{R,L} = |R\rangle\langle R|, |L\rangle\langle L|$.

Then $\mathcal O_R\mathcal O_L$ has **no support** on $|\Psi_{\text{Janus}}\rangle$:

$$\langle \Psi_{\text{Janus}} | \mathcal O_R \mathcal O_L | \Psi_{\text{Janus}} \rangle = 0.$$

**Interpretation:** For strictly sector-diagonal $\mathcal O_R,\mathcal O_L$, the symmetric Janus state shows **no** irreducible cross-sector **local** correlator — it **factorises** to zero (not a Susskind-style cluster violation).

---

## Extension (non-local / dressed, schematic)

Susskind's load-bearing object is **dressed** $\bar C = C\cdot\Pi_-$ with $C=[A(-s),A(s)]$ — **non-local** in clock labels.

NTE analog requires specifying **dressed** bilinear $C_{\mathrm{NTE}}$ on the same $\mathcal H$ (not yet canonical in corpus). A **2-qubit** embedding $|R\rangle=|01\rangle$, $|L\rangle=|10\rangle$, $|\Psi\rangle=(|01\rangle+|10\rangle)/\sqrt2$ with $\mathcal O_R=\sigma_x^{(1)}$, $\mathcal O_L=\sigma_x^{(2)}$ gives $\langle \sigma_x^{(1)}\sigma_x^{(2)}\rangle=1$ — **nonzero**, but this is **not** the corpus Janus state without an explicit lifting map from 2-dim chirality to product space.

---

## Verdict

**NEEDS-MORE** — sector-local D1 on $|\Psi_{\text{Janus}}\rangle$ is **trivially zero** (factorises). A defensible PASS requires:

1. Canonical definition of **dressed** $\mathcal O_R,\mathcal O_L$ on NTE bilateral space (Harlow–Numasawa analog).  
2. Explicit finite-dimensional model tied to Companion 5 / Ch 10 (not schematic 2-qubit alone).

**Not FAIL** on parallel — v0.2 already marks cluster claims **conjecture** until this closes.

---

— Cursor Jammer, 2026-06-02.
