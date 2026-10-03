# Wagenveld Sprint — Coordination Register (Cursor v0.4)

**Coordinator:** Cursor (Desktop render lane — **autonomous AC+Jammer scope**)  
**Updated:** 2026-05-31 (AC **OVERRIDE** — Phase IV OPEN on G-A→G-D; §2.7 closure reverted)  
**Foundation:** `AC_Wagenveld_Sprint_Architectural_Scoping_v0_1_20260528.md`

---

## Phase III execution order (2026-05-30)

```
Jammer §2.7 ──► launch now (n(z) only; no HEALPix)
       │
Scratch §5.1 ✅ ──► §5.2–§5.4 analytic arm AC-verified
       │
       ├── §5.4 quantitative refresh ── **✅ v0.2** ──────────┐
       │   (Scratch catalogue verification on nside16 JSON)  │
Jammer §2.3 ───────────────────── **UNBLOCKED** ──────────────┤
       │                                                       │
Phase IV discrimination ── **OPEN (G-A→G-D)** — Test A/C harness run ✅; **no §2.7-primary closure**
       └── AC override: `Handoff_AC_to_Cursor_OVERRIDE_Phase_IV_2_7_NOT_Closed_Gates_Open_20260531.md`
```

**Escalation:** `Handoffs/BLOCKER_ESCALATION_Cursor_HEALPix_Footprints_P0_Phase_III_5_4_Jammer_2_3_20260530.md`  
**Cursor ack:** `Handoffs/Handoff_Cursor_to_Jammer_Scratch_AC_HEALPix_P0_Ack_Execution_Order_20260530.md`  
**Cursor P0 complete:** `Handoffs/Handoff_Cursor_to_Scratch_Jammer_HEALPix_P0_Complete_20260530.md`  
**§5.4 v0.2 integration:** `Handoffs/Handoff_Cursor_to_AC_Scratch_Section_5_4_v0_2_Catalogue_Refresh_Integration_20260530.md`

---

## Greg clarification (authoritative)

**Phase II.5 "implicit"** = no Greg-gate; **Phase III begins when AC top-3 lands** (not blocked on joint II.5 doc). Phase II.5 review may continue in parallel as advisory.

Handoff: `Handoffs/Handoff_Cursor_Sprint_State_Update_Phase_III_Unblock_20260529.md`

---

## Sprint phase status

| Phase | Owner | Status | Deliverable |
|-------|--------|--------|-------------|
| **II Top-3** | AC | ✅ Locked (provisional) | `Handoff_AC_to_Cursor_Jammer_Scratch_Wagenveld_Sprint_Phase_II_Top3_Ranking_20260529.md` |
| **II.5** | AC + Scratch + Jammer | 🔄 **Co-rank-1 accepted** (AC evening) | `Handoff_AC_to_Jammer_Scratch_Cursor_Greg_Wagenveld_Sprint_Phase_II_5_Disposition_Co_Rank_1_Accepted_20260529.md` — binding top-3 pending Jammer §2.7-side input; **Greg: Phase III unblocked per Cursor handoff** |
| **III Scratch** | Scratch | **✅ §5.4 v0.2** | Catalogue refresh on nside16 JSON; P_wag=0.22 (LoTSS caps); merged §2.5 geometry **FAIL** 3/4 surveys (AC) |
| **III Jammer** | Jammer | **§2.7 v0.1 filed** · **§2.3 ✅ v0.1** | §2.7: resonance vector integrated in harness — **not closed primary** (AC override). **G-C open:** derive/refute resonance |
| **I.5+ Cursor** | Cursor | **✅ P0 DONE** | LoTSS-DR2 HEALPix (astropy-healpix, Nside=16); ~3.1× proxy retired |
| **IV** | Cursor + Jammer + AC | **🟡 OPEN — G-A→G-D** | Test A/C harness ✅ (numbers credited); **Phase III NOT closed §2.7-primary** |

**Parallel (Greg Phase 0 2026-05-30):** v10.17.7 patches, S6 promote, Ch 16 draft, Prelude rebuild — no further Greg gate (`Handoff_Greg_Ratification_Blocker_Clearance_Phase0_20260530.md`).

---

## Top-3 (AC provisional vs Scratch II.5)

| Rank | AC | Scratch II.5 |
|------|-----|--------------|
| 1 | §2.7 | Co-rank-1 §2.7 + merged §2.5 |
| 2 | §2.1+§2.5 merged | (same) |
| 3 | §2.2 defer | — |

---

## Cursor queue

| # | Task | Status |
|---|------|--------|
| 1 | DOF + §8 correction | ✅ |
| 2 | Sprint state + Phase III unblock handoff | ✅ |
| 3 | Ledger Ch 10 v5 sync | ✅ |
| 4 | Sky-coverage / n(z) ingest | ✅ v0.5 released | Jammer §2.7 unblocked |
| 6 | LoTSS exact mask (P0+) | **🟡 next** | Scratch §5.4 v0.2 geometry band; optional Phase IV sharpen |
| 7 | Phase IV Test A/C harness run | ✅ **harness** | v0.7; §2.7 vector integrated — **interpretation OPEN** (AC override G-A→G-D) |
| 5 | HEALPix footprint weights | ✅ **DONE** | `wagenveld_sprint_footprints_nside16.json` + FITS masks; astropy-healpix (healpy py313 blocked). Handoff: `Handoff_Cursor_to_Scratch_Jammer_HEALPix_P0_Complete_20260530.md` |

---

## Key files

| File | Role |
|------|------|
| `Working/Scratch_Wagenveld_Sprint_Phase_II_5_Input_v0_1.md` | Scratch II.5 (co-rank-1) |
| `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` | Phase II scoping; **(κ/κ₀)²≈42 superseded** by §5.2 (δκ/κ ≈ −0.54·δε) |
| `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_2_Closure_Linearisation_v0_1.md` | §5.2 verified — canonical perturbative response |
| `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_3_Hopf_Fibre_Mapping_v0_1.md` | §5.3 verified — n̂_pref **1 free direction** (CMB anchor favoured) |
| `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_4_v0_2_Catalogue_Refresh_Verification.md` | **§5.4 primary** — catalogue refresh on nside16 (Drive `1SdOh8HUlVJFHfsB3jxqWO4L3e4kUSp6suwbw5XKRTDI`) |
| `Working/Scratch_Wagenveld_Sprint_Candidate_2_5_Phase_III_5_4_Sky_Coverage_Integrals_v0_1.md` | §5.4 analytic arm — P_wag=0.32 northern proxy; superseded for Test A quant |
| `Working/NTE_Corpus_Sitrep_20260529.md` | Full programme sitrep |
| `Working/wagenveld_sprint_footprints_nside16.json` | HEALPix W(n) **primary** (Nside=16, LoTSS-DR2 + Galactic cuts) |
| `Working/wagenveld_sprint_footprints_nside8.json` | **Deprecated** — crude iso-latitude proxy (~3.1× artifact) |
| `Handoffs/Handoff_AC_to_Scratch_Jammer_Cursor_Greg_Phase_III_5_1_Verification_Verdict_20260530.md` | AC §5.1 accept + flags |

*Cursor coordinator v0.8 — Phase IV OPEN per AC override 2026-05-31.*
