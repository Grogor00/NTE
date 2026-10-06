# Handoff — Cursor Main → AC: **C17 register + C8 residual — OLD match report. Ready on GO.** Nothing patched.

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC, Scratch, Jammer · **Date:** 2026-09-28
**Source:** `Handoffs\AC_Patch_Register_Companion17_Body_Lags_Banner_Four_Items_Plus_C8_Residual_20260928.md`
**Status on register:** DRAFT (awaiting Greg). **No GO file yet — nothing applied.**

---

## C8 residual — OLD **MATCH**

Disk (`Companion_08` L16): `when exit (a) is adopted`  
NEW drafted: `if exit (a) were adopted`  
**Ready on GO.**

---

## C17 — four items, OLD match

| Item | Locus | OLD on disk | Status |
|------|-------|-------------|--------|
| **1** | Banner L19 | `Early-universe spectrum, if any, is imported under **exit (a)** (SM Higgs \(\xi_H\gg1\), credited) — not from this companion.` | **MATCH** (register’s double-escaped `\\(\\xi…\\)` is presentation only; disk is single-escaped) |
| **2a** | §3 heading L57 | `## 3. Conditional $(n_s,r)$` | **MATCH** |
| **2b** | §3 flags lead-in L65 | `**Conditional flags (must travel with the numbers):**` | **MATCH** |
| **3** | Flag 2 L67 | `2. $N_e$ pinning: the corpus default $N_e=63.4$ is retained; alternate pinning moves the pair as above.` | **MATCH** |
| **4a** | Data anchors lead-in L70 | `**Data anchors (shown side by side):**` | **MATCH** |
| **4b** | Closing L75 | `These replace imported Starobinsky numbers previously circulated as conditional survivors. They are **not** zero-parameter predictions.` | **MATCH** |

**§1 / §2 / §4 Companion 9 eq. (1) — untouched**, as designed. κ_cfm note L53 correct.

---

## Notes for apply (not defects)

1. **Item 3 NEW escaping.** Register shows `$N\_\*` / `$N\_\*\\lesssim55.9$`. On apply Cursor will write clean markdown/TeX: `$N_*$` and `$N_*\lesssim55.9$` unless AC specifies otherwise.
2. **Live `N_e=63.4` still in §3 calculation body** (L59, L63) — historical statement of what was computed, parallel to leaving the frame derivation. **Not in the four items.** Flag only if AC wants those relabelled or marked historical in prose.
3. **YAML title** still: `"…frame closure and conditional (n_s, r)"` — outside register; leave unless drafted.

---

## Standing

Await Greg GO on C8 residual + C17 Items 1–4. Then apply + render both; report.

— Cursor Main, 2026-09-28.
