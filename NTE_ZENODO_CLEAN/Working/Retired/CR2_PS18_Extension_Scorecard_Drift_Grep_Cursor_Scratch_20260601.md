# PS-18 — Extension scorecard drift grep

**From:** Cursor Scratch  
**To:** Cursor Main, AC, Greg  
**Date:** 2026-06-01  
**Reference:** `Working/NTE_Extension_Scorecard_20260601.md`  
**Verdict:** **PASS** — **0 false claims** requiring patch; **no corpus edit**

---

## §1 — Patterns searched

| Pattern | Intent |
|---------|--------|
| `0.997` | Retracted atmospheric comparand |
| `simultaneous sub-1%` | False two-leg Tier A |
| `Killing2 closed` | Unratified closure |
| `sqrt(2/3)` / `√(2/3)` as **derived** | Programme S not PASS |
| Bare `1.05×` / `1.05 x` **active** (no strikethrough/reroute) | CR-H2 retired Λ numeric |

**Targets:** P1 (`Paper_E1_F1_*`), P4 (`Paper_P4_Theta23_*`), P5 (Solar + pivot), κ₀ (`Paper_Hopf_*`), Popular Full + Reader, `Outreach/Distribution_Campaign_v1_20260530.md`.

---

## §2 — Results

| Target | 0.997 | simul. sub-1% | Killing2 closed | √(2/3) derived | active 1.05× |
|--------|------:|--------------:|----------------:|---------------:|-------------:|
| P1 F1 v0.2 | 0 | 0 | 0 | 0 | 0 |
| P4 θ₂₃ v0.2 | 0 | 0 | 0 | 0 | 0 |
| P5 v0.2/v0.3 + pivot | 0 | 0* | 0 | 0 | 0 |
| κ₀ v0.1 | 0 | 0 | 0 | 0 | 0 |
| Popular Full + Reader | 0 | 0* | 0 | 0 | 0** |
| Campaign | 0 | 0 | 0 | 0 | 0 |

\* Honest-scope **negations** only ("not simultaneous sub-1%").  
\** All `1.05×` in **~~strikethrough~~** or explicit **reroute-or-retire** (CR-H1/H2 sync blocks).

---

## §3 — Spot-check vs scorecard rows

| Row | Scorecard claim | Grep |
|-----|-----------------|------|
| E1 solar Tier A | P5 abstract §4–§6 | **Consistent** (0.993×; atmospheric ≈1.49×) |
| E8 Λ numeric retired | Popular CR-H1/H2 notes | **Consistent** |
| E9 NOT CLOSED | No "√(2/3) derived" in Tier 1 | **Consistent** |

---

## §4 — Action

**No patch.** Sustain next wave: re-grep after any Programme S PASS attempt.

— **Cursor Scratch**, 2026-06-01.
