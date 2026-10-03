---
title: "NTE Corpus Situation Report"
author: "G. White"
date: "2026-05-29 (Cursor autonomous sitrep)"
---

# NTE Corpus — Situation Report

**Prepared by:** Cursor (Desktop render lane, sprint coordinator)  
**Date:** 2026-05-29  
**Scope:** Progress, corpus state, consolidation / strengthening / extension pathways  
**Canonical log:** `NTE v10_6/Workflow/NTE_Stream_Notes_Cursor.md`  
**Greg-blocked register:** `NTE v10_6/Workflow/MB/Greg_Blocked_Register.md`

---

## 1. Executive summary

The programme is in a **deliberate consolidation phase** (Greg 2026-05-28) with one **active sprint exception**: the **Wagenveld / cosmic-dipole investigation**, which Greg elevated to full-stream priority when Branch I’s Wagenveld overshoot persisted.

**What is stable:** Four **Tier 1 standalone papers** at submission-ready draft state (pending CR-7 byline); master corpus at **v10.17.6** OneDrive-canonical; book chapters largely at v3–v7 with recent Ch 10 **v5** (t=0 vs N=0 fix); publication title-block YAML standard applied across active `Papers/Paper_*.md`.

**What is in flight:** Wagenveld sprint at **Phase II complete / Phase III scoping** (Scratch §2.5 shipped; AC provisional top-3; Jammer §2.7 + §2.3 parallel); Paper **S2** Phase I (Jammer/Scratch); Branch I numerics v0.4 partial; **Ch 16 “Strange Tests”** authorised but not yet drafted under ratified filename stem.

**What is paused (sprint priority):** AC consolidated-batch items — v10.17.7 corpus patches, S6 promote, external-clean-gates companion, pedagogical pivots, contraction reverse-pass remainder.

**Single Greg-blocked upload item:** **G-003** — arXiv joint P1 + P5 (HOLD until Greg sorts logistics).

---

## 2. Progress report (2026-05-25 → 2026-05-29)

### 2.1 Wagenveld sprint (dominant active arc)

| Phase | Status | Key deliverable |
|-------|--------|-----------------|
| Scoping | ✅ Ratified (Path A + 5 flags) | `AC_Wagenveld_Sprint_Architectural_Scoping_v0_1_20260528.md` |
| Phase I pattern | ✅ | `Wagenveld_Sprint_Phase_I_Pattern_Characterisation_v0_1.md` |
| Phase I.5 angular + DOF | ✅ | `Wagenveld_Sprint_Phase_I_5_Angular_Axis_v0_1.md`, `Wagenveld_Sprint_Joint_Fit_DOF_Accounting_v0_1.md` |
| Phase II adversarial | ✅ | `Scratch_Wagenveld_Sprint_Phase_II_Adversarial_Review_v0_1.md` |
| AC top-3 | ✅ Provisional | `Handoff_AC_to_Cursor_Jammer_Scratch_Wagenveld_Sprint_Phase_II_Top3_Ranking_20260529.md` |
| Scratch §2.5 scoping | ✅ | `Scratch_Wagenveld_Sprint_Candidate_2_5_Anisotropic_Kappa_v0_1.md` — **(κ/κ₀)² ≈ 42** amplification |
| Phase III derivations | ⏳ | Scratch ~3–4 sessions; Jammer §2.7 + §2.3 |
| Phase IV convergence | ⏳ | Cursor harness vs Branch I v0.5 |

**Stable empirical read:** Wagenveld **+3.28σ** amplitude outlier; **~6°** from Singal/CMB (direction-normal); shared-parameter fit cannot close without **survey-specific** nuisance DOF (Tier 2 fit → max|δσ| ≈ 0.42).

**Structural correction (Scratch):** §2.1 gauge-birth seed and §2.5 anisotropic κ are **one mechanism** (closure-step coupling), not independent candidates.

### 2.2 Book

| Item | State |
|------|--------|
| Ch 10 | **v5** canonical — PATCH-T (t=0 vs N=0 explicit) + PATCH-U (DM fringe strip); v3/v4 → `depreciated/` |
| Ch 13 | v5 canonical |
| Ch 11/12 | v3.1; epigraphs PC call ratified |
| Ch 14 | `Strange_Geometries_and_Structural_Rhymes_v1` (existing) |
| Ch 16 | Greg ratified **“Stranger and Stranger”** placement for *The Strange Tests*; stem `Chapter_16_Stranger_and_Stranger_v1.md` — **draft not yet on Desktop** (current `Chapter_16_The_Working_Bet_v1.md` is separate content) |
| Contraction / its-fix passes | Substantial progress Ch 1–15 + Popular; remainder queued |

### 2.3 Standalone papers (Tier 1)

| Paper | File | State |
|-------|------|--------|
| P1 / F1 | `Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md` | v0.2 submission-ready; pedagogical pivot v0.1 exists |
| P4 | `Paper_P4_Theta23_*_v0_2_20260526.md` | v0.2 submission-ready |
| P5 | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` | v0.2 arxiv-ready |
| κ₀ | `Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md` | v0.1 structural |
| PDF pipeline | `Documents/paper-build/` | YAML titles + centered header.tex; build from OneDrive canonical |

**Pending:** CR-7 affiliation/email/ORCID (Greg); joint P1+P5 upload (**G-003 HOLD**).

### 2.4 Programme S / empirical surface

| Item | State |
|------|--------|
| Paper S2 | v1.0 consolidation doc; Phase I item 1 PASS (Jammer D-operator); item 2 gate reconciliation in flight |
| Paper S1 | v0.4 in `Papers/` |
| S6 synthesis | Ratified for promote Working → Papers — **paused** (consolidated batch) |
| External empirical catalogue | `Compatibility_Catalogue_External_Empirical_Surface_Consolidated_v0_1` — companion note **not yet** in `Papers/` |
| Branch I void-bias | `lcdm_bao_void_bias.py` v0.5 sprint hooks (angular + DOF ladder) |
| CMB κ | Analytical v0.1 complete (Jammer); numerical v0.2 queued post-sprint |

### 2.5 Master corpus patches (authorized, not applied)

Three paste-ready patches batched for **v10.17.6 → v10.17.7**:

1. r ↔ BMV row (§17.5.12) + Charter §3.9 footnote  
2. CMB κ diagnostic (§17.5.12)  
3. §22.14 κ₀ → ξ_V rename (dimensional quantity only)

---

## 3. State of the corpus

### 3.1 Architecture (two publication arms)

| Arm | Purpose | Current state |
|-----|---------|---------------|
| **Standalone / Tier 1** | Credibility acquisition; framework-independent body | 4 papers ready; upload blocked on G-003 |
| **Companion + master** | Framework integrity; internal consistency | v10.17.6; eight-level Λ tier framing; patches queued |
| **Book** | Reader-facing *Shape of Time* | 16 chapter slots; strong mid-corpus (Ch 5–13); Ch 16 Strange Tests gap |
| **Working** | Sprint memos, scripts, adversarial reviews | High activity; Wagenveld cluster is load-bearing |

### 3.2 Version discipline

- **Live canonical:** `Papers/Paper_*.md` (no internal codes in filenames per register)  
- **Predecessors:** `Papers/depreciated/`, `Book/depreciated/` — partial hygiene done; ongoing  
- **Title blocks:** YAML frontmatter (`title`, `author`, `date`) — rule in `.cursor/rules/publication-title-blocks.mdc`  
- **Internal workflow notes:** belong in handoffs/register — **not** in PDF `date:` fields (CR-7 lesson applied)

### 3.3 Stream posture (2026-05-29)

| Stream | Posture |
|--------|---------|
| **Cursor** | Active — sprint coordinator + numerics + housekeeping |
| **AC** | Hold except sprint coordination; top-3 shipped |
| **Jammer** | Wagenveld §2.7 + §2.3 + S2 item 2 |
| **Scratch** | Wagenveld §2.5 Phase III; S2 triangle-review at reduced bandwidth |
| **PC** | Information only unless Phase V paper or book CR |

### 3.4 Health indicators

| Indicator | Assessment |
|-----------|------------|
| Adversarial loop | Strong — Scratch PASS + flags on scoping and Phase I |
| Empirical honesty | Strong — Wagenveld not dismissed; DOF accounting explicit |
| Fragmentation risk | Medium — sprint vs consolidated-batch pause creates patch backlog |
| Upload readiness | High content / low logistics — G-003 only hard block |
| Book–corpus coherence | Improving — Ch 10 t/N fix aligns with Wagenveld §2.1 mechanism language |

---

## 4. Next pathways to consolidation

Ordered by **dependency and Greg-facing impact**.

### 4.1 Close the Wagenveld sprint (consolidation through empirical arc)

1. **Phase II.5** — Scratch + Jammer reconcile AC vs Scratch top-3 ordering (~½ session).  
2. **Phase III** — mechanism v0.1 predictions on binding candidates.  
3. **Phase IV** — Cursor convergence vs Branch I; honest outcome memo.  
4. **Decision:** Tier 1 fifth paper (“cosmic dipole anomaly”) vs methodology note vs eliminate-and-document.

**Consolidation value:** Resolves the largest open empirical tension in Branch I; either closes watch-list item or defines falsifier surface for Charter §17.5.12.

### 4.2 Post-sprint corpus batch (v10.17.7)

Apply three AC patches as **single increment**; verify OneDrive sync; update Live Register §9.

**Consolidation value:** Closes Greg 2026-05-28 walkthrough items #3–#4; unifies r-BMV, CMB κ, and ξ_V naming.

### 4.3 Tier 1 publication hygiene

- Complete CR-7 bylines on F1, P4, P5, κ₀  
- F1 pedagogical pivot second pass (PC Option A sequencing)  
- Predecessor deprecation sweep (`Papers/` live-only canonical names)  
- PDF rebuild all four from `Documents/paper-build/`

**Consolidation value:** Removes upload friction the moment **G-003** clears.

### 4.4 Book consolidation

- Draft **Ch 16 Strange Tests** (`Chapter_16_Stranger_and_Stranger_v1.md`) from compatibility catalogue + BMV Case F  
- AC ledger: Ch 10 v5 row  
- Remaining contraction reverse-pass (Popular v6 + book grep-clean maintenance)  
- Resolve Ch 14 vs Ch 16 scope (Ch 14 exists; Ch 16 is new home for Strange Tests per G-101)

### 4.5 Programme S housekeeping

- Promote **Paper S6** to `Papers/`  
- S2 Phase II (Cursor a₀/a₂/a₄) after Jammer v0.2 + gates  
- Paper S2 item 2 closure (Jammer/Scratch lane assignment shipped)

### 4.6 External-facing companion artefacts

- **External-clean-gates** note in `Papers/` (pre-position for post-preprint reviewers)  
- Tier 1 weekend upload prep doc alignment with register v0.4

---

## 5. Pathways for strengthening the corpus

*Strengthen = tighter internal consistency, harder falsifiers, better adversarial discipline — not new physics claims.*

| Pathway | Action | Owner | Payoff |
|---------|--------|-------|--------|
| **A. Empirical falsifier surface** | Ship §17.5.12 expansions (r-BMV 2×2, CMB κ) via v10.17.7 | Cursor | Charter-linked watch-list → prediction surface |
| **B. Naming hygiene** | ξ_V vs κ₀ disambiguation in §22.14 | Cursor | Removes dimensional/dimensionless confusion |
| **C. Branch I numerics** | Catalogue-sourced directions + n(z); line-by-line script audit; v0.5 persistence test | Cursor | Wagenveld sprint + cosmic-dipole closure criterion |
| **D. κ mechanism depth** | Scratch Phase III: ε from bifurcation action; ∂κ/∂ε; Hopf-fibre sky map | Scratch | Tests merged §2.1+§2.5 with quantitative predictions |
| **E. Survey-geometry adjudication** | Jammer §2.7 non-perturbative δ₂ vs LoTSS geometry | Jammer | Proves or eliminates methodology vs physics for Wagenveld |
| **F. Adversarial cadence rule** | Codify major-version-only review (consolidated batch #5) | AC/Cursor | Stops per-increment review treadmill |
| **G. Publication presentation** | Centered PDF titles corpus-wide; sanitize.lua pipeline | Cursor/Greg | Professional standalone output |
| **H. Pedagogical pivot layer** | F1 pivot second pass + Tier-1 pivot sequencing | PC/Cursor | Outreach without diluting technical papers |
| **I. S2 heat-kernel closure** | Phase II numerical extraction after symbolic gates | Cursor/Jammer | Six-prediction single-computation programme credibility |
| **J. BMV / \|Φ_NTE\| Lagrangian** | Extract matter-coupling sources (deferred item) | Jammer/Cursor | Closes BMV gate item 1 from Greg batch |

---

## 6. Pathways for extending the corpus

*Extend = new reader-facing or specialist-facing surface area — new chapters, papers, empirical programmes.*

| Pathway | Description | Tier | Trigger |
|---------|-------------|------|---------|
| **1. Cosmic dipole standalone** | Fifth Tier 1 if Wagenveld sprint Phase IV converges | Tier 1 | Sprint success + external scrutiny path |
| **2. Ch 16 Strange Tests** | Empirical compatibility chapter (BMV Case F, catalogue A1/A2) | Book | PC brief + title triad ratified |
| **3. External-clean-gates paper** | Distinct NTE-vs-ΛCDM predictions without framework scaffolding | Companion / lay | Pre-arXiv reviewer landing |
| **4. Paper S6 promotion** | M_R heat-kernel theorem-grade Tier 2 | Programme S | Greg batch #4 |
| **5. CMB κ v0.2 numerical** | Gate 6 execution (Greg batch G-106) | Empirical | Post-sprint or parallel if resourced |
| **6. Branch II / III cosmic dipole** | If Wagenveld survives Phase IV as structural residual | Empirical | Sprint negative or partial outcome |
| **7. M_1 / n_s standalones** | Deferred per feasibility report | Tier 1 (future) | Separate Greg recognition gate |
| **8. Ch 14 evolution** | Strange Geometries v1 may complement or defer to Ch 16 | Book | PC/Greg placement call |
| **9. Popular v7 ↔ book sync** | Appendix A already rebuilt from v7; full edition v6 remains corpus lay paper | Outreach | Maintenance |
| **10. Expert outreach pool** | Individualized emails from Tier 1 prep doc | Outreach | G-003 fire |

---

## 7. Recommended sequencing (Cursor view)

### Now (sprint-active)

1. Cursor: catalogue ingest for Scratch §5.4 sky integrals + n(z) hook  
2. Scratch: Phase III §5.1–§5.3 (ε derivation chain)  
3. Jammer: §2.7 + §2.3 v0.1 predictions  
4. Scratch + Jammer: Phase II.5 top-3 reconciliation (implicit post-AC-lock)

### After sprint Phase IV outcome

5. v10.17.7 corpus patch batch  
6. S6 promote + external-clean-gates companion  
7. Ch 16 Strange Tests first draft  
8. F1 pedagogical pivot second pass  
9. CMB κ v0.2 numerical  
10. S2 Phase II (when gates clear)

### When Greg clears G-003

11. CR-7 populate → PDF final → arXiv P1+P5 joint upload  
12. P4 + κ₀ follow-on preprints  
13. External-clean-gates note live before reviewer traffic

---

## 8. Risks and watch items

| Risk | Mitigation |
|------|------------|
| Sprint vs patch backlog drift | Resume consolidated batch immediately after Phase IV |
| AC vs Scratch top-3 ordering | Phase II.5 explicit reconciliation |
| Ch 16 filename / content mismatch | Draft `Chapter_16_Stranger_and_Stranger_v1.md`; do not overwrite Working Bet without Greg call |
| Worksheet placeholders in Branch I | Phase I.5 catalogue ingest before publication claims |
| Over-claiming cosmic dipole resolution | Honest-scope envelope (AC §6, Scratch flags) |
| S2 bandwidth vs Wagenveld | Greg §2.5-only preserves reduced S2 triangle-review |

---

## 9. Key file index

| Purpose | Path |
|---------|------|
| Sprint coordination | `Working/Wagenveld_Sprint_Coordination_Register_v0_1.md` |
| Stream notes | `Workflow/NTE_Stream_Notes_Cursor.md` |
| Greg blocked | `Workflow/MB/Greg_Blocked_Register.md` |
| Standalone register | `Papers/NTE_Standalone_Papers_Register_v0_4.md` |
| Consolidated batch queue | `Handoffs/Handoff_AC_to_Cursor_Consolidated_Batch_Greg_Walkthrough_20260528.md` |
| Branch I numerics | `Working/lcdm_bao_void_bias.py` |
| PDF build | `Documents/paper-build/` |

---

*End sitrep — Cursor 2026-05-29.*
