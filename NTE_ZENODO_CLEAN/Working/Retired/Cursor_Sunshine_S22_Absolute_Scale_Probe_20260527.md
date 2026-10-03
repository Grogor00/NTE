# Sunshine probe: S22-1k hunt re-run vs absolute-scale pathways

**Date:** 2026-05-27  
**Owner:** Cursor (Jammer parallel)  
**Parent:** `Jammer_S22_1k_Sunshine_Exit_Closure_v0_1_20260524.md`; `Open_Gaps_Derivation_Pathways_Sunshine_Map_v0_1_20260524.md`

---

## §1 — What was done

Re-executed `paper_s22_1k_sunshine_exit_hunt_numerics.py` after Greg AFK autonomous block.

**Signed closure (v0.1k)** remains best for **ratios:**
- dim(ℍ)=4 lock → m_μ/m_e ≈ **207.0** (0.1% vs PDG)
- m_τ/m_μ ≈ **18.0** (~7%; balanced p=dim(G₂)/4 → both ~3%)

**Hunt grid:** lock variants, ζ(2)/ζ(3) weights, Feigenbaum, entropy splits, off-diagonal Y — all **fail** to beat v0.1k on joint (τ/μ, μ/e) score.

**Best near-miss (hunt tail):** `lock3 + zeta2^(L/3) on electron` → τ/μ=17.98, μ/e=67.6 (err≈1.26) — **worse** than v0.1k on μ/e.

**Off-diagonal on sunshine diagonal:** blows ratios (τ/μ ~ 10³) — **dead end** confirmed.

---

## §2 — Sunshine verdict

| Rabbit hole | Verdict |
|-------------|---------|
| New multiplicative blocks on Y | **DEAD** (hunt) |
| Off-diagonal Yukawa rescue | **DEAD** |
| Additive δ + lock + electron ζ/HK (1k) | **SUNSHINE** (ratio tier) |
| Absolute lab masses ~0.35× PDG | **OPEN** — not ratio rescue |

---

## §3 — Pathways for absolute scale (do not re-hunt ratios)

Per sunshine map **S2-NF** and S22-1m:

1. **g_eff(T_GB)** thermal dof vs spectral N_F=180 — closes N_lock 19% slack; may lift overall Y normalisation without touching ratios.
2. **D5 lab formula** m^lab = m^(G)(8π)^{1/3}/1.12 — all species ~1–4% (Jammer 1m); tier-2 absolute.
3. **Y₀ = 8/3** universal uplift (S22-1l) — pred/obs ~3/8 on scale; ratios unchanged.

**Cursor action:** no corpus patch from hunt alone; flag Jammer if void-bias / CMB work needs ratio vs absolute distinction.

---

## §4 — P0 derive IDs (Jammer-owned; Cursor support only)

- **J6-D2:** prove Φ_inf = 2√(N_e) M_Pl from saddle (G-NS identity).
- **S2-NF1:** g_eff(T_GB) numerical table at T_GB.

— Cursor, 2026-05-27
