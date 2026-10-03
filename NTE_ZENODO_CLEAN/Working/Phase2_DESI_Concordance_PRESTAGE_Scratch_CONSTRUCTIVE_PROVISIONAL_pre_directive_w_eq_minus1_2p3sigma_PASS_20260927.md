# Phase 2 DESI concordance — PRE-STAGE (Scratch, CONSTRUCTIVE) — PROVISIONAL, PRE-DIRECTIVE

**Status:** PRE-STAGED at Greg's request (2026-09-27 04:34 NZDT). **No AC Phase-2 directive has issued yet.** This is the constructive leg staged in advance so it is ready the moment AC routes it. Numbers below are PROVISIONAL; the authoritative run awaits the ratified data vector, estimator, and priors (checklist §5).
**From:** Scratch (Claude) · **To:** AC (on issue) · **Cc:** Greg, Jammer.
**Origin:** `Working\DESI_Tension_Resolution_Programme_CursorMain_20260926.md` Phase 2, assigned "Scratch constructive + Jammer adversarial."
**Blind note:** Jammer runs the adversarial leg blind; I have NOT read any Jammer DESI file and this must not be harmonised with one before both file.

---

## 1. Pre-registered forks (declared BEFORE the numbers)

The instruction behind this thread — *"something is wrong… there must be a solution"* — is an investment, not a brief. **The finding may be that w=−1 is in real trouble, and that is a result.** Outcomes, each landing in exactly one bin:

| Fork | Statement | What follows |
|---|---|---|
| **P1 — holds (concordant)** | Under NTE priors (w≡−1, closed Ω_k≤0), DESI BAO ↔ Planck tension < 3σ by the ratified metric | Cursor Main's D1 confirmed; retract "w=−1 excluded at 3.1σ" corpus-wide; **w=−1 kept** |
| **P2 — fails (real exclusion)** | Tension ≥ 3σ at fixed w=−1 by the ratified metric | **Withdraw** geometric-unloading w=−1 as a naked prediction; Part 3 falsifier #3 / distinctiveness handle downgraded to asymptote-only or DE sector marked open (exit-c) |
| **P3 — holds, different reason** | Concordant, but because DESI was never a w-test — the tension is BAO↔CMB *parameter-level* under ΛCDM, not a constraint on w | Handle survives, but corpus must **stop framing DESI as a test of w** at all |
| **P4 — undetermined** | Metric not computable without ratified data vector + estimator + Ω_k/r_d prior | Settle by AC ratifying those (§5). **← where this pre-stage sits until the directive issues** |

---

## 2. Provisional result (harness §4)

| Metric | Value | vs 3σ bar |
|---|---|---|
| **Official DESI joint (SOURCED this session)** — BAO vs CMB, flat ΛCDM, Ωm–H0rd plane | **2.3σ** | **PASS** |
| 1D Ω_m Gaussian proxy (my consistency check) | 1.6σ | PASS |

**Provisional landing: P1 / P3.** At fixed w=−1 (which *is* ΛCDM for the DE sector), DESI does **not** exclude the model at >3σ. The corpus's "~3.1σ" refrain is a frequentist w₀wₐ *model-preference*, not a w=−1 exclusion — consistent with Cursor Main's D1. **This is provisional and does not pre-empt Jammer's adversarial leg or AC's arbitration.**

---

## 3. Curvature leg — an honest negative

DESI+CMB in ΛCDM+Ω_k tips **~2σ toward OPEN** (Ω_k>0) [Cursor Main; arXiv:2505.00659]. NTE requires **CLOSED** (Ω_k≤0) — the opposite sign. **The curvature freedom that would relieve DESI is the sign NTE forbids**, so floating NTE-sign curvature is expected to *worsen* concordance, not rescue it. Whatever saves w=−1, it will not be curvature. (Quantify against the ratified data in the final run.)

---

## 4. Harness (reproducible; provisional inputs flagged)

```python
import numpy as np
# DESI DR2 BAO-only flat ΛCDM (DESI DR2 II, arXiv:2503.14738)
Om_DESI, sOm_DESI = 0.2975, 0.0086   # widely quoted; NOT table-verified this session — VERIFY
# Planck 2018 base ΛCDM TT,TE,EE+lowE+lensing (arXiv:1807.06209)
Om_Pl, sOm_Pl = 0.3153, 0.0073
dOm = Om_Pl - Om_DESI; sig = np.hypot(sOm_DESI, sOm_Pl)
T_Om = dOm/sig                       # = 1.58σ  (1D proxy; understates joint)
# Official joint tension = 2.3σ (SOURCED: DESI DR2 abstract, flat ΛCDM, Ωm–H0rd plane)
```

Output: ΔΩm=0.0178, σ_comb=0.0113, **1D proxy = 1.58σ**. Official joint **2.3σ** (sourced). Both < 3σ.

---

## 5. To finalize once AC issues the directive (required, NOT assumed here)

1. **DESI DR2 BAO data vector** {D_M/r_d, D_H/r_d, D_V/r_d} + full covariance at all z_eff — replaces the Ω_m summary proxy.
2. **Ratified tension estimator** — suspiciousness / Q_DMAP / parameter-shift, not a 1D Gaussian projection.
3. **Ratified Ω_k prior** — fixed 0, or floated closed (≤0). §3 says closed hurts; quantify.
4. **r_d treatment** — standard early physics vs a credited-Higgs-sector r_d shift (must not break BBN/CMB).
5. **Neutrino-mass prior** — DESI+CMB Σm_ν<0.064 eV (flat ΛCDM) is aggressive and interacts with the Ωm–H0 plane; state it.

---

## 6. Discipline / provenance

- **Sourced this session:** the 2.3σ ΛCDM tension and θ* consistency (DESI DR2 abstract, arXiv:2503.14738, via WebFetch).
- **NOT table-verified this session:** Ω_m(DESI)=0.2975±0.0086 and the Planck triplet (from published papers; WebFetch could not parse the DESI constraint tables — flagged for verification in the final run).
- **Not done:** the authoritative estimator, the Ω_k quantification, any corpus patch. All await the directive.

**Provisional one-line:** At fixed w=−1, DESI↔Planck sit at 2.3σ (official) / 1.6σ (Ω_m proxy) — below 3σ; provisional P1/P3, w=−1 not excluded on current data; curvature is the wrong sign to help. Awaiting AC directive, data vector, and Jammer's adversarial leg.

— Scratch (Claude), 2026-09-27.
