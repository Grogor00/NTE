# BL-1 template — concrete \(S_\nu\) (Track N)

**Fill before varying. Scratch owns the constructive fill; Jammer attacks.**

## 1. Fields and metrics

- Metrics: \(g^+_{\mu\nu}\), \(g^-_{\mu\nu}\) (two orientations)
- Shared spinor: Majorana \(\nu\) (Companion 7: unresolved on conjugation axis; LH under SU(2)_L)
- Orientation-local matter: \(\psi^\pm\) (do **not** appear inside \(S_\nu\) except via metric / spin connection)

## 2. Proposed action (must be a scalar density)

Write explicitly:

\[
S_\nu = \int d^4x\; \Big(\cdots\Big)
\]

**Forbidden in this template:** factors of \(T_b^\pm\), Lagrange multipliers that impose \(\tilde T = T_b+\kappa_0\tilde T\), undetermined “self-consistency constraints.”

**Allowed examples to try:**

- **N1 bilkinetic:**
  \[
  S_\nu = \tfrac12\int\sqrt{-g^+}\,\bar\nu\,i\not\nabla_+\nu
  + \tfrac12\int\sqrt{-g^-}\,\bar\nu\,i\not\nabla_-\nu
  - \tfrac12\int\big(\sqrt{-g^+}+\sqrt{-g^-}\big)\,M\,\bar\nu\nu
  \]
  (measures and relative weights are part of the proposal — justify).

- **N2 single measure with mixed vielbein** — state the measure and prove diffeomorphism covariance.

## 3. Variation checklist

1. \(\delta S/\delta g^{\pm\mu\nu}\) → \(T_\nu^\pm\)  
2. \(\delta S/\delta\nu\) → joint EOM  
3. FLRW + CPN: \(g^+=g^-\), extract \(\rho_\nu/\rho_b\)  
4. Does \(\kappa_0=3/\sqrt{4\pi}\) appear? How?  
5. Linearised: sound speed, free-streaming, \(\Delta N_{\mathrm{eff}}\)

## 4. Pre-registered landing for this fill

- [ ] F-LIN (C1-type)
- [ ] F-AMP (only if C2 emerges without hand \(S_{\mathrm{cons}}\))
- [ ] F-NU with hot-only bridge
- [ ] F-NONE for Track N
- [ ] F-OPEN (named blocker: ________)

## 5. File result as

`Working/BRIDGE_LAW_BL1_Snu_VARIATION_<lane>_YYYYMMDD.md`
