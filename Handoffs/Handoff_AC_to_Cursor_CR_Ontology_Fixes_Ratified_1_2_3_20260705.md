# Handoff: AC → Cursor — ratified CR-ontology fixes (Patches 1–3), render

**From:** AC · **To:** Cursor (apply + render) · **Cc:** CR, Greg · **Date:** 2026-07-05
**Status:** CR-cleared (verification pass 2026-07-05) + Greg-ratified. Apply these three, re-render, report back. Patches 4 and 5 are held (θ₁₂ de-quarantine; involution construction-check) and are NOT in this batch.
**Refinements folded in from CR's pass:** Patch 1 trims "Born rule" from Φ's linkage list; Patch 2 ships with the abstract rider.

**Application rule:** match on distinctive prose, not whitespace. All three land in `NTE_v10_18_0_Part1_Foundations.md` (LaTeX `$…$` — preserve, do not convert). After each edit re-read and confirm NEW present / OLD gone. **If any OLD block does not byte-match, stop and report — do not force** (the LaTeX is AC's reconstruction; your local file is authoritative). Keep the Core_Papers and paper-build/scratch-src copies in sync; re-render Part 1; confirm the set holds at 29/29; return a completion handoff.

---

## PATCH 1 — §2.3 (soften "addition is forced"; Born-rule trimmed per CR)

**OLD:**
```
The addition is forced: $H = \beta_{\mathrm{NTE}}|\Phi|^2$ requires a scalar whose value varies cosmologically as $|\Phi_{\mathrm{NTE}}(N)|^2 = v_{\mathrm{EW}}^2 (H(N)/H_0)$, from $v_{\mathrm{EW}}$ today to $\sim 10^{8.5} v_{\mathrm{EW}}$ at BBN; the SM Higgs, stiff against such variation by its potential curvature, cannot supply it.
```
**NEW:**
```
In the cosmological (FRW) sector this addition introduces no independent dynamics: adopting $|\Phi_{\mathrm{NTE}}(N)|^2 = v_{\mathrm{EW}}^2 (H(N)/H_0)$ makes $H = \beta_{\mathrm{NTE}}|\Phi|^2$ an identity with $\beta_{\mathrm{NTE}} = H_0/v_{\mathrm{EW}}^2$, so there $\Phi_{\mathrm{NTE}}$ is a relabelling of the expansion history — consistent with Part 3 carrying $H_0$, $w$, and $\Omega_k$ as construction/inherited rather than as new FRW dynamics. What the added scalar contributes is structural, not cosmological-dynamical: it ties the boundary-expansion sector to the electroweak scale $v_{\mathrm{EW}}$ and, through the $S^3$ Hopf geometry, to the sectors where the framework's results actually live — the cross-thickness coupling $\kappa$ and gauge birth. Its profile still runs from $v_{\mathrm{EW}}$ today to $\sim 10^{8.5} v_{\mathrm{EW}}$ at BBN, a range the SM Higgs — stiff against such variation by its potential curvature — could not supply; but that range is read off the expansion history, not predicted by it.
```

---

## PATCH 2a — §I (photon paradox restated)

**OLD:**
```
The Standard Model answers cleanly. Every entity with zero proper-time accumulation has zero Higgs (Yukawa) coupling — photons, gluons. Every entity that accumulates proper time has nonzero Higgs coupling — electrons, quarks, W/Z; neutrinos, barely, with $y_\nu \sim 10^{-12}$. The correlation is exact, with no Standard-Model exceptions. NTE takes it as structural: the boundary expansion field $\Phi_{\mathrm{NTE}}$ parameterises the map from e-fold increments to proper-time increments, and entities without Yukawa coupling do not participate — they accumulate zero proper time (null-time).
```
**NEW:**
```
The Standard Model answers in two steps. For *fundamental* particles the correlation is clean: those accumulating zero proper time are exactly the massless ones (photons, gluons), and for fundamental fermions rest mass *is* Higgs (Yukawa) coupling — so among them proper-time accumulation tracks Higgs coupling (neutrinos barely, with $y_\nu \sim 10^{-12}$). But the exception-free statement is the relativistic one: an entity accumulates proper time if and only if it carries rest energy and moves sub-luminally. That covers the composite case a Higgs-only framing would miss — a proton accumulates proper time although $\sim$99% of its mass is the QCD binding energy of massless gluons (§III). NTE takes *this* correlation as structural: proper-time accumulation is e-fold embedding depth (§VII), sourced by rest energy from whatever mechanism — Higgs coupling for fundamental fermions, confinement for hadrons — while entities with no rest energy (photons, gluons) do not embed and accumulate zero proper time (null-time).
```

## PATCH 2b — Abstract rider (matches 2a; ship together per CR)

**OLD:**
```
A photon accumulates zero proper time between emission and absorption ($ds^2 = 0$) and has zero Higgs coupling; every massive particle accumulates nonzero proper time and has nonzero Higgs coupling.
```
**NEW:**
```
A photon accumulates zero proper time between emission and absorption ($ds^2 = 0$) and carries no rest energy; every massive entity accumulates nonzero proper time and carries rest energy (Higgs-generated for fundamental fermions, QCD confinement for hadrons).
```

---

## PATCH 3 — §II.0 (even-handed regrade of Born-as-Hopf and t=iΔN)

**OLD:**
```
NTE's record therefore includes both. Simplifications that earned their place: the gauge group from $G_2$, the Born rule as a Hopf projection on $S^3$, the dark-matter coupling from $S^3$ topology.
```
**NEW:**
```
NTE's record therefore includes both. Simplifications that earned their place: the gauge group from $G_2$, and the dark-matter coupling from $S^3$ topology. Two items earlier listed as earned simplifications are, by the test just stated, better classed as *reformulations*: the Born rule as a Hopf projection on $S^3$ (§IV) is Gleason's theorem read on an imported qubit geometry — a coherent geometric restatement, but not a reduction in independent postulates unless it yields a consequence Gleason does not; and $t = i\,\Delta N$ as the Euclidean saddle (§2.1.2) is Wick rotation plus the Hartle–Hawking no-boundary condition in NTE vocabulary, wholly within the unobservable pre-temporal regime. Both are kept for the coherence they supply, not counted as postulate reductions — and either is upgraded the moment it makes a distinguishing prediction.
```

---

Three edits, one file (Part 1), plus the abstract rider. Re-render, confirm 29/29, return the completion handoff. — AC, 2026-07-05.
