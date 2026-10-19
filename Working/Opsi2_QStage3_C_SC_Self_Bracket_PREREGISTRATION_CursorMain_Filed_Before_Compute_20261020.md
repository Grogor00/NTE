# PRE-REGISTRATION — Cursor Main: Q-Stage3 — `{C_SC,C_SC}` excess over pure-HR absorption

**Filed before any Q-Stage3 compute result.**  
**GO:** `Handoffs\GO_AC_Run_Q_Stage3_C_SC_Self_Bracket_Correctly_Staged_20261020.md`  
**Authority:** Scratch constraint-chain reference (2026-10-20).  
**Independent of Scratch’s Q-Stage3 computation.** Jammer attacks what lands.  
**No Core. No f. P04 unchanged.**  
**Engines available:** NumPy, SymPy, **Wolfram Engine 15 (activated)** — will use and report which produced each statistic.

---

## 0. Binding corrections

- Stage-3 object only: `{C_SC,C_SC}` ∂δ. **No Stage-4 D-matrix / Ṡ comparison.**
- **F12:** `{C_SC,C_SC}≠0` is expected in pure HR and **not** a ghost signal by itself.
- Question is **excess** over what the pure-HR `C_SC`/`𝒮` second-class pair absorbs.
- R_j = h_g(I−X)² p_j (not I−X²); residual 3-d; n=0 / φ₀=0 special; 90/90 struck; X-only identity withdrawn.
- Posteriors held until earned: G-1 0.20 · G-2 0.35 · G-3 0.10 · G-4 0.35.

---

## 1. Object

> Does R_j make `{C_SC,C_SC}` fail to close **beyond** what the pure-HR C_SC/𝒮 second-class pair already absorbs?

**Not in scope:** Stage-4 `{𝒮,H}`, L(Dn)∂𝒮, δ(Dn) cancel tests (R6).

---

## 2. Pre-committed method

### K0′ (method gate)
Reproduce pure-HR reference fact at generic n≠0 (chain §4): `{C_SC,C_SC}≠0` is healthy because `(C_SC,𝒮)` is second-class — **not** because the self-bracket vanishes.  
If method cannot state/verify this, stop.

### Algebraic excess (Wolfram + NumPy check)
For C_SC ≈ C_g − C_f (K1 weights):
- Grav ∂δ skeleton: ~ h_g π_g + h_f π_f  
- Matter ∂δ: W p with W = h_g(I−X)² (= h_g+h_f−2G on SVC)  
- On-shell C_i: π_g+π_f+p ≈ 0  

Derive **on-shell remainder** with/without matter; define  
`excess := rem_matter − rem_pureHR`  
(at matched π_g, with π_f fixed by C_i).

### Class / absorption test (F12 core)
Dirac matrix of the pair φ=(C_SC, 𝒮):
```
| a  b |   a={C_SC,C_SC}, b={C_SC,𝒮}, c={𝒮,𝒮}
| −b c |
det = a c + b²
```
**Pre-commit:**
- If c=0 and b≠0 (standard ultralocal/second-class pattern), then **det=b²≠0 independent of a** ⇒ matter contribution to `a` (including R_j) **does not by itself** destroy second-class invertibility. That is “absorbed” in the F12 sense → **no G-2 from Stage-3 alone**; fork deferred to Q-Stage4.
- If matter makes b→0 or c spoil det at O(ψ²), report that as **genuine excess / class risk**.
- ΔS ultralocal (S3): track whether `{𝒮+ΔS,𝒮+ΔS}` and `{C_SC,𝒮+ΔS}` change the det diagnosis; if uncomputed, **say so**.

### Decision rule
| Outcome | Landing |
|---|---|
| Excess in `a` only; det still nonzero (b≠0,c=0 pattern holds) | **G-4** — Q-Stage3 closed as “no class loss”; Q-Stage4 remains |
| det fails / b killed at O(ψ²) by matter | **G-2 candidate** (K3-ish at Stage-3) — flag for Jammer |
| Cannot decide det / 𝒮 brackets | **G-4** or *“chain cannot close at O(ψ²) with current methods”* — honest terminal per GO §4 |
| Claiming ghost from `a≠0` alone | **Forbidden (F12)** |

---

## 3. Reproducibility

- Script: `Working\Opsi2_QStage3_C_SC_Self_Bracket_COMPUTE_CursorMain.py` (+ Wolfram `.wl` if used)
- Every verdict number ∈ JSON from that run
- Wolfram unavailable ⇒ say so (currently available)

---

## 4. § Soften status

(N) undetermined already filed; S1–S4 stand.

— Cursor Main, 2026-10-20. **Prereg filed. Compute starts after this exists on disk.**
