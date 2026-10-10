# Sol-A next — **SA-TRH** VERDICT (Scratch, construction)

**From:** Cursor Scratch (Discipline 14) · **Lane:** **SA-TRH**  
**Date:** 2026-10-11  
**Authority:** GO + Directive Sol-A next TRH · EXPLORE inventory · Gauge SYN · ABD verdict · E1B litmap  
**Prereg:** `Working/SolA_Next_TRH_PREREGISTRATION_Scratch_forks_P1_P2_P4_method_original_work_20261011.md`  
**Status:** SCORED AFTER PREREG · ORIGINAL WORK · No Core deposit · No Phase 2  
**Blind note:** Prereg filed **blind** to Jammer Phase1. Adversarial TRH prereg (if present) readable after prereg; self-tests G1–G12 in §10. Jammer Phase 2 awaited.

## Landing: **P4** — Quantitative reheating-corridor map filed. **Pure low-\(T_{\mathrm{RH}}\) alone fails** for Branch-H TeV under free-FP Verner + high-scale \(m_\phi\) (even at BBN). **Near-threshold / low-\(m_\phi\)** is the corridor that improves the abundance gauge (conditional **GAUGE_UP**, unfitted). Overall **GAUGE_FLAT**. Class earned = **None**. Origin / inflaton mass OPEN. Prefer honest **P4** over fake overall UP.

### GAUGE_FLAT

*(Overall abundance-correctness gauge — net. Regional scores in §6.)*

---

## 1. Corpus + lit read (mandatory)

| Source | Used |
|---|---|
| GO + Directive Sol-A next TRH/S1 | Yes |
| EXPLORE_SolA_Next_TRH_S1 | Yes |
| Gauge SYN ABD/BUL/O1S | Yes |
| ABD verdict (regional map) | Yes (baseline to sharpen) |
| E1B litmap | Yes |
| Verner arXiv:2512.19041 (ar5iv) | Yes — eqs. (90)/(92)/(96)/(106); BBN; threshold language |
| Babichev et al. arXiv:1607.03497 | Yes — E1 freeze-in / FO kill / TeV window |

**Target marker (not a fit):** \(\Omega_{\mathrm{DM}} h^{2}\sim 0.12\).

**Depth relative to ABD:** ABD labeled R-TRH conditional **UP** qualitatively. This lane **quantitatively downgrades pure TRH** (high-scale \(m_\phi\) held) to **GAUGE_DOWN / corridor fail**, and isolates **threshold / low-\(m_\phi\)** as the only Verner-condensate honesty UP for Branch-H TeV.

---

## 2. Package TR-VERNER — comparison scaffold

### Ask
What formulas govern free-FP spin-2 yield during perturbative reheating?

### Construction
Verner (free Fierz–Pauli \(X_{\mu\nu}\); graviton-mediated):  
(i) inflaton condensate \(\phi\phi\to XX\); (ii) thermal SM bath. Helicity split for \(\tau=m_2^{2}/m_{\phi}^{2}\ll 1\): \(|\mathcal{M}|^{2}_{S}\sim\tau^{-4}\), \(|\mathcal{M}|^{2}_{V}\sim\tau^{-2}\), \(|\mathcal{M}|^{2}_{T}\sim\mathcal{O}(1)\). Condensate **dominates**; thermal **negligible**.

**Condensate, \(k=2\), helicity-0 dominated, \(m_2\ll m_{\phi}\) (Verner eqs. 90 / 92):**
\[
\Omega h^{2}\;\simeq\;0.12\times\left(\frac{T_{\mathrm{RH}}}{6\,\mathrm{GeV}}\right)\left(\frac{\rho_{\mathrm{end}}}{(5.2\times 10^{15}\,\mathrm{GeV})^{4}}\right)^{1/2}\left(\frac{m_{\phi}}{1.7\times 10^{13}\,\mathrm{GeV}}\right)^{8}\left(\frac{8\times 10^{12}\,\mathrm{GeV}}{m_{2}}\right)^{7}.
\]

**Thermal (eq. 106), leading piece:** \(\Omega^{T}h^{2}\simeq 2.7\times 10^{-4}(T_{\mathrm{RH}}/10^{12}\,\mathrm{GeV})^{11}(8\times 10^{12}/m_{2})^{7}\) — negligible vs condensate in their space.

**BBN:** \(T_{\mathrm{RH}}\gtrsim 2\,\mathrm{MeV}\). Under Verner’s own all-DM strip assumptions this forces \(m_{2}\gtrsim 2.7\times 10^{12}\,\mathrm{GeV}\) — **outside** Branch-H TeV (fence held from ABD).

**Avoiding overproduction (Verner conclusion):** low \(T_{\mathrm{RH}}\) **or** mass near threshold \(2m_{2}\simeq m_{\phi}\).

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-V-A Condensate scaffold** | **OPEN_honest / comparison** | Eq. (90)/(92) |
| **T-V-B Thermal ≪ condensate** | **honesty_pass** | Eq. (106) |
| **T-V-C Verner Ω ⇒ NTE earn** | **Killed** | Import ≠ derive |
| **T-V-D Tensor residual** | **sharpened_constraint** | §5 — still overcloses Branch-H at BBN under Verner norm |

**TR-VERNER sublabel:** **sharpened_constraint / OPEN_honest**.

---

## 3. Package TR-TRHALONE — pure low-\(T_{\mathrm{RH}}\) (high-scale \(m_\phi\) held)

### Ask
Does lowering \(T_{\mathrm{RH}}\) alone rescue Branch-H TeV under free-FP Verner condensate?

### Construction (OOM; \(\rho_{\mathrm{end}}\) at Verner reference; \(m_{\phi}=1.7\times 10^{13}\,\mathrm{GeV}\))

Light-mass formula applied as **stress test** (comparison; not NTE fit):

| Anchor | \(m_{2}\) | \(T_{\mathrm{RH}}\) | \(\Omega h^{2}\) (eq. 90) | Overclose vs 0.12 |
|---|---|---|---|---|
| Mid Branch-H | \(10\,\mathrm{TeV}\) | \(6\,\mathrm{GeV}\) | \(\sim 2.5\times 10^{61}\) | \(\sim 2\times 10^{62}\) |
| Mid + BBN floor | \(10\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 8\times 10^{57}\) | \(\sim 7\times 10^{58}\) |
| Low Branch-H + BBN | \(1\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 8\times 10^{64}\) | \(\sim 7\times 10^{65}\) |
| High Branch-H + BBN | \(66\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 1.5\times 10^{52}\) | \(\sim 1\times 10^{53}\) |

**\(T_{\mathrm{RH}}\) needed for \(\Omega h^{2}\sim 0.12\) at high-scale \(m_{\phi}\) (unfitted marker; formula inversion):**

| \(m_{2}\) | Required \(T_{\mathrm{RH}}\) | vs BBN \(2\,\mathrm{MeV}\) |
|---|---|---|
| \(1\,\mathrm{TeV}\) | \(\sim 3\times 10^{-69}\,\mathrm{GeV}\) | \(\sim 10^{-66}\times\) below BBN |
| \(10\,\mathrm{TeV}\) | \(\sim 3\times 10^{-62}\,\mathrm{GeV}\) | \(\sim 10^{-59}\times\) below BBN |
| \(66\,\mathrm{TeV}\) | \(\sim 2\times 10^{-56}\,\mathrm{GeV}\) | \(\sim 10^{-53}\times\) below BBN |

**Verdict on corridor C-TRH-alone:** **Fails.** Pure low-\(T_{\mathrm{RH}}\) **cannot** bring Branch-H TeV under free-FP Verner + high-scale inflaton into non-overclose territory while respecting BBN. ABD’s qualitative R-TRH **UP** is hereby **downgraded** under these assumptions.

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-L-A BBN-floor OOM** | **Pass (filed)** — **GAUGE_DOWN (corridor)** | Table above |
| **T-L-B \(T_{\mathrm{RH}}\) vs BBN** | **Corridor fail** | Required \(T_{\mathrm{RH}}\) ≪ BBN |
| **T-L-C Pure TRH as earn / UP** | **Killed** | Honesty: corridor fails |

**TR-TRHALONE sublabel:** **GAUGE_DOWN** (corridor fail) + **sharpened_constraint**.

---

## 4. Package TR-MPHI — low-\(m_{\phi}\) marker (bleeds toward threshold class)

### Ask
What inflaton-mass scale would the light-mass formula need (marker only) for Branch-H?

### Construction
Invert eq. (90) for \(\Omega h^{2}\sim 0.12\) at fixed \(T_{\mathrm{RH}}\) (unfitted **marker**, not earn):

| \(m_{2}\) | \(T_{\mathrm{RH}}\) | Marker \(m_{\phi}\) | \(m_{2}/m_{\phi}\) | \(\tau=m_{2}^{2}/m_{\phi}^{2}\) |
|---|---|---|---|---|
| \(1\,\mathrm{TeV}\) | \(6\,\mathrm{GeV}\) | \(\sim 3.7\times 10^{4}\,\mathrm{GeV}\) | \(\sim 0.027\) | \(\sim 7\times 10^{-4}\) |
| \(10\,\mathrm{TeV}\) | \(6\,\mathrm{GeV}\) | \(\sim 2.8\times 10^{5}\,\mathrm{GeV}\) | \(\sim 0.036\) | \(\sim 1\times 10^{-3}\) |
| \(66\,\mathrm{TeV}\) | \(6\,\mathrm{GeV}\) | \(\sim 1.4\times 10^{6}\,\mathrm{GeV}\) | \(\sim 0.046\) | \(\sim 2\times 10^{-3}\) |
| \(1\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 1.0\times 10^{5}\,\mathrm{GeV}\) | \(\sim 0.010\) | \(\sim 1\times 10^{-4}\) |
| \(10\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 7.5\times 10^{5}\,\mathrm{GeV}\) | \(\sim 0.013\) | \(\sim 2\times 10^{-4}\) |
| \(66\,\mathrm{TeV}\) | \(2\,\mathrm{MeV}\) | \(\sim 3.9\times 10^{6}\,\mathrm{GeV}\) | \(\sim 0.017\) | \(\sim 3\times 10^{-4}\) |

**Spot checks (same formula):**  
- \(m_{2}=10\,\mathrm{TeV}\), \(T_{\mathrm{RH}}=6\,\mathrm{GeV}\), \(m_{\phi}=10^{6}\,\mathrm{GeV}\): \(\Omega h^{2}\sim 4\times 10^{3}\) (still overclose \(\sim 3\times 10^{4}\)).  
- Same with \(m_{\phi}=3\times 10^{5}\,\mathrm{GeV}\): \(\Omega h^{2}\sim 0.24\) (order-unity vs marker — **not** a fit claim).  
- Same with \(m_{\phi}=2\times 10^{4}\,\mathrm{GeV}\): strong **undershoot** in light-mass formula; near \(\tau\sim\mathcal{O}(0.1)\) regime where exact rates need threshold kinematics.

**Reading:** Rescue under free-FP condensate requires **\(m_{\phi}\sim 10^{4}\)–\(10^{6}\,\mathrm{GeV}\)** (TeV–PeV), **not** a mild trim of \(10^{13}\,\mathrm{GeV}\). Markers still have \(\tau\ll 1\), so they are “low-\(m_{\phi}\)” rather than exact kinematic threshold — but they are the **same exotic origin class** as near-threshold (non-high-scale inflaton). Joint low-\(T_{\mathrm{RH}}\) + mildly lower \(m_{\phi}\) does **not** restore high-scale inflation: BBN + \(m_{\phi}=10^{6}\,\mathrm{GeV}\) + \(10\,\mathrm{TeV}\) still overcloses by \(\sim 10\times\).

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-M-A \(m_{\phi}\) marker table** | **Pass (filed)** | Above |
| **T-M-B Low-\(m_{\phi}\) ↔ threshold class** | **sharpened_constraint** | Bleeds to TeV–PeV inflaton OPEN |
| **T-M-C Fit \(m_{\phi}\) to Ω** | **Killed** | Markers ≠ earn |

**TR-MPHI sublabel:** **OPEN_honest / sharpened_constraint** — conditional honesty **UP** only as named exotic class, not dial.

---

## 5. Package TR-THR — near-threshold corridor + tensor residual

### Ask
Does \(m_{2}\sim\mathcal{O}(m_{\phi})\) improve the gauge?

### Construction
Verner: overproduction avoided when spin-2 mass lies close to kinematic threshold \(2m_{2}\simeq m_{\phi}\) (phase space \(\sqrt{1-\tau}\to 0\) as \(\tau\to 1\); helicity-0 \(\tau^{-4}\) runaway shut). For Branch-H TeV this **requires TeV-scale inflaton** — Part 3 origin / reheating **OPEN**, exotic vs α-attractor \(m_{\phi}\sim 10^{13}\,\mathrm{GeV}\).

At \(\tau\sim\mathcal{O}(1)\) the light-mass eq. (90) is **invalid** as a quantitative Ω predictor; this corridor is scored as **honesty GAUGE_UP** (removes the parametric overclose mechanism), **not** as computed Ω match.

**Tensor-only residual (eq. 96), high-scale Verner normalization held — if helicity-0 were structurally absent but tensor rate retained:**

| Anchor | \(\Omega_{T}h^{2}\) | Overclose vs 0.12 |
|---|---|---|
| \(10\,\mathrm{TeV}\), \(T_{\mathrm{RH}}=6\,\mathrm{GeV}\) | \(\sim 9\times 10^{4}\) | \(\sim 7\times 10^{5}\) |
| \(10\,\mathrm{TeV}\), BBN | \(\sim 29\) | \(\sim 2\times 10^{2}\) |
| \(66\,\mathrm{TeV}\), BBN | \(\sim 4\) | \(\sim 40\) |

So **helicity-0 kill alone + BBN + high-scale norm does not clear Branch-H** under Verner’s tensor residual. Full E1/bimetric structural relocation (FLEX) remains a separate hypothesis — not adopted here.

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-H-A Threshold honesty** | **Conditional GAUGE_UP** | Primary improve corridor |
| **T-H-B Formula invalid near \(\tau\sim 1\)** | **honesty_pass** | No fake Ω compute |
| **T-H-C Threshold ⇒ deposit / origin closed** | **Killed** | OPEN held |
| **T-H-D Tensor-only at BBN** | **GAUGE_DOWN (residual)** | Still overcloses Branch-H under Verner norm |

**TR-THR sublabel:** **conditional GAUGE_UP** (honesty) + OPEN exotic.

---

## 6. Package TR-E1B — bath scaffold / fences

### Ask
Where does Babichev E1 sit if Verner free-FP condensate is not inherited?

### Construction
Babichev: freeze-out **impossible**; freeze-in via s-channel massless graviton **and** massive spin-2 (α cancels in dual mediation); window \(1\)–\(66\,\mathrm{TeV}\), \(10^{-15}\lesssim\alpha\lesssim 10^{-11}\); longevity \(\Gamma\sim\alpha^{2}m_{\mathrm{FP}}^{3}/m_{\mathrm{Pl}}^{2}\); end-of-inflation gravitational production incompatible with TeV+perturbativity carve. Matching Ω in E1 = **their dial** — refused as NTE earn.

**Dual-channel honesty:** Verner condensate floor (if inherited) **dominates** E1 bath language for free FP. Sol-A must not conflate FP ↔ α. If ghost-free bimetric Branch-H **suppresses** free-FP helicity-0 condensate (FLEX-ABD-A / FLEX-TRH-A), research relocates to E1 bath + portal siblings (Henrich–Mambrini–Olive) — scored **GAUGE_FLAT**, not automatic UP.

**Kills held:** freeze-out; inflationary CGPP (\(H\gg m\)); Ω dial; ultralight.

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-E-A E1 bath scaffold** | **OPEN_honest / GAUGE_FLAT** | If condensate not inherited |
| **T-E-B FP ≠ α; FO; CGPP** | **Fence / kills held** | |
| **T-E-C FLEX ⇒ silent overall UP** | **Killed / refuse** | Named FLEX only |

**TR-E1B sublabel:** **GAUGE_FLAT** + fences.

---

## 7. Package TR-MAP — corridor GAUGE_* map (depth bar)

### 7.1 Corridor table

| Corridor ID | Assumptions (OPEN; not fitted) | Quantitative reading | **GAUGE_*** | vs ABD |
|---|---|---|---|---|
| **C-OC** Default overclose | Branch-H TeV + free-FP Verner condensate + \(m_{\phi}\sim 10^{13}\,\mathrm{GeV}\) + non-tiny \(T_{\mathrm{RH}}\) | \(\Omega\gg 0.12\) by \(\gtrsim 10^{50}\)–\(10^{65}\) | **GAUGE_DOWN** | Held / sharpened |
| **C-TRH-alone** Pure low \(T_{\mathrm{RH}}\) | Same + \(T_{\mathrm{RH}}\downarrow\) to BBN; \(m_{\phi}\) held high-scale | Still overclose \(\gtrsim 10^{53}\); required \(T_{\mathrm{RH}}\ll\) BBN | **GAUGE_DOWN** *(corridor fail)* | **Downgrade** from ABD R-TRH UP |
| **C-MPHI** Low \(m_{\phi}\) | \(m_{\phi}\sim 10^{4}\)–\(10^{6}\,\mathrm{GeV}\) markers; \(T_{\mathrm{RH}}\) ordinary or BBN | Can sit near marker Ω under light-mass formula; exotic inflaton | **GAUGE_UP** *(honesty; unfitted)* | New quantitative class |
| **C-THR** Near threshold | \(2m_{2}\simeq m_{\phi}\) / \(m_{2}\sim\mathcal{O}(m_{\phi})\) ⇒ TeV-scale inflaton for Branch-H | Shuts \(\tau^{-4}\) runaway; eq. (90) invalid as Ω predictor | **GAUGE_UP** *(honesty; unfitted)* | Sharpened primary |
| **C-JOINT** Low \(T_{\mathrm{RH}}\) + lower \(m_{\phi}\) | Combined | Still needs \(m_{\phi}\ll 10^{13}\); bleeds to C-MPHI/C-THR | **GAUGE_UP** *(conditional)* | Not pure TRH |
| **C-E1B** Bath-primary | Free-FP condensate **not** inherited; Babichev freeze-in | Research scaffold; α dial refused | **GAUGE_FLAT** | Held |
| **C-TENS** Tensor-only residual | Helicity-0 off; Verner \(\Omega_{T}\) + BBN + high-scale norm | Still overcloses Branch-H by \(\sim 40\)–\(10^{3}\) | **GAUGE_DOWN** | New OOM |
| **C-KILL-FO** Freeze-out | Any FO | Illegal under E1 | **killed** | Held |
| **C-KILL-DIAL** Ω dial | Fit \(T_{\mathrm{RH}}/m_{\phi}/m_{2}/\alpha\) to force Ω | Fake earn | **killed** | Held |
| **C-KILL-CGPP** Inflationary CGPP | \(H\gg m\) | Ghost / bank | **killed** | Held |

### 7.2 Schematic

```
   observed Ωh² ~ 0.12  (marker only)
            ▲
            │  C-THR / C-MPHI / C-JOINT  … conditional GAUGE_UP (unfitted; OPEN exotic)
            │
   C-E1B  …… GAUGE_FLAT (structure fence / FLEX-named only)
            │
   C-TRH-alone / C-TENS / C-OC  … GAUGE_DOWN (quantitatively fails or overcloses)
            │
   C-KILL-* ………… killed (FO / dial / inflationary CGPP)
```

### 7.3 Overall scores

| Axis | Label | Meaning |
|---|---|---|
| **Chair** | **P4** | Quantitative corridor map filed; pure TRH downgraded; threshold/low-\(m_{\phi}\) named; dials refused; no programme-P1 |
| **Gauge** | **GAUGE_FLAT** | Improve corridors are real but OPEN/exotic; pure TRH fails; net neither earned approach nor pathway-wide kill |
| **Class earned (non-dial NTE)?** | **None** | |
| **Core deposit?** | **No** | |
| **Pathway-wide P2?** | **No** | C-THR / C-MPHI / C-E1B remain research-live |

### Why not GAUGE_UP overall?
Threshold / low-\(m_{\phi}\) **UP** scores are honesty gains, but they demand OPEN exotic reheating/origin supplies. Claiming overall UP would overstate that Sol-A presently improves toward Ω_obs without those supplies. Pure TRH — the “easy” corridor — **fails**.

### Why not GAUGE_DOWN overall?
Pathway kill would erase C-THR / C-MPHI honesty and C-E1B / FLEX research options. Overclose default is severe under free-FP + high-scale ID, but named (unfitted) corridors remain.

### Why not P1?
No non-dial NTE-derived Ω; no origin close; GAUGE ≠ earn.

**TR-MAP sublabel:** **sharpened_constraint** — depth bar **met** (pure TRH quantitatively failed; \(m_{\phi}\) markers filed).

---

## 8. Package TR-NTE — must-add / cannot-claim / OPEN

### 8.1 Must-add (for abundance correctness without dial)

1. **Origin / inflaton honesty:** either TeV–PeV (near-threshold / low-\(m_{\phi}\)) reheating justified non-dial **or** a structural reason Branch-H does **not** inherit free-FP helicity-0 condensate (FLEX-named).  
2. **Pure low-\(T_{\mathrm{RH}}\) is not enough** under high-scale \(m_{\phi}\) — do not treat ABD R-TRH as automatic rescue.  
3. **Channel bookkeeping:** condensate (if present) + decay-bath + grav-bath; FP ≠ α.  
4. **Still elsewhere:** O1/BD (SA-S1 / O1S); Bullet (SA-BUL) — abundance alone ≠ deposit.

### 8.2 Cannot-claim

| Claim | Status |
|---|---|
| Ω_DM derived / CDM identity earned | **Cannot** |
| Fit \(T_{\mathrm{RH}}\) / \(m_{\phi}\) / \(m_{2}\) / α to Ω_obs as P1 | **Cannot** |
| Pure low-\(T_{\mathrm{RH}}\) rescues Branch-H TeV + high-scale \(m_{\phi}\) | **Cannot** (quantitatively false under Verner eq. 90) |
| Freeze-out live / inflationary CGPP rescue | **Cannot** |
| Verner analytic Ω ⇒ NTE production earn | **Cannot** |
| Silent Core deposit from corridor UP | **Cannot** |

### 8.3 Remains OPEN

- Part 3 origin exit; whether TeV-scale / PeV-scale \(m_{\phi}\) is supplied  
- Whether bimetric Branch-H inherits free-FP helicity-0 condensate  
- Helicity-0 EFT completion (\(\Lambda_{5}\)); tensor residual under completion  
- Relative weights condensate / decay-bath / grav-bath  
- Ω_DM / CDM identity; O1; Bullet coupling  

### Lemmas

| Lemma | Result | Note |
|---|---|---|
| **T-N-A Must-add** | **Pass** | §8.1 |
| **T-N-B Cannot-claim** | **Pass** | §8.2 |
| **T-N-C OPEN ledger** | **Pass** | §8.3 |

**TR-NTE sublabel:** **OPEN_honest** + bans held.

---

## 9. ONTOLOGY_FLEX (named only — not adopted)

**FLEX-TRH-A — Helicity-0 / free-FP condensate suppression (extends FLEX-ABD-A).**  
If ghost-free bimetric Branch-H (or UV completion at \(\Lambda_{5}\)) structurally removes Verner-style free-FP helicity-0 condensate production while retaining E1 bath freeze-in, C-OC / C-TRH-alone pressure drops and C-E1B becomes primary.  
**Status:** **ONTOLOGY_FLEX proposal only** — Working/Handoff. **Not** Core edit. **Not** Ω earn. Does **not** by itself upgrade overall **GAUGE_FLAT** → **GAUGE_UP**. Tensor residual (§5) warns that “helicity-0 off” alone may be insufficient under Verner norms.

---

## 10. Fake-P1 / fake-GAUGE self-tests (G1–G12)

| # | Score | Note |
|---|---|---|
| **G1** Amp / 5.50 | **PASS** | Absent |
| **G2** Fit-as-earn / fake UP | **PASS** | Markers labeled unfitted; pure TRH failed not faked UP |
| **G3** Deposit | **PASS** | P4; investigation only |
| **G4** Verner ⇒ NTE Ω | **PASS** | T-V-C killed |
| **G5** Soft-P1 via corridors | **PASS** | Overall GAUGE_FLAT + chair P4 |
| **G6** FO laundering | **PASS** | Held killed |
| **G7** FP ≡ α | **PASS** | Fence held |
| **G8** Ultralight | **PASS** | Held |
| **G9** Inflationary CGPP | **PASS** | Held |
| **G10** Force pathway P2 | **PASS** | C-THR/C-MPHI/C-E1B live |
| **G11** Depth stall | **PASS** | Pure TRH OOM fail + \(m_{\phi}\) markers beyond ABD |
| **G12** Gauge ⇒ deposit / O1 / Bullet | **PASS** | Dependence only |

**G1–G12: 12/12 PASS.**

---

## 11. Package ratification

| Package | Sublabel |
|---|---|
| **TR-VERNER** | **sharpened_constraint / OPEN_honest** |
| **TR-TRHALONE** | **GAUGE_DOWN** (corridor fail) |
| **TR-MPHI** | **OPEN_honest** (markers; conditional UP class) |
| **TR-THR** | **conditional GAUGE_UP** (honesty) |
| **TR-E1B** | **GAUGE_FLAT** + fences |
| **TR-MAP** | Chair **P4** · overall **GAUGE_FLAT** |
| **TR-NTE** | **OPEN_honest** + bans |
| **Overall** | **P4** + **GAUGE_FLAT** |

---

## 12. Standing

Investigation only. No Core deposit. Ontology held (FLEX-TRH-A named, not adopted). Banked kills stand. Prefer-kill posture retained; honest **P4** + **GAUGE_FLAT** stands on quantitative corridor map. Soft-P1 via gauge refused. Ω dial refused. Freeze-out / inflationary CGPP kills held.

**Key corridor claims (chair brief):**  
1. **C-TRH-alone fails** for Branch-H TeV + high-scale \(m_{\phi}\) (BBN insufficient by many tens of orders).  
2. **C-THR / C-MPHI improve** the gauge as honesty corridors (TeV–PeV inflaton / near threshold) — unfitted; origin OPEN.  
3. **C-E1B** remains FLAT research path if condensate not inherited.  
4. Overall abundance gauge stays **FLAT** — not deposit-ready.

— Cursor Scratch (SA-TRH), 2026-10-11
