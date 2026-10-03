# AC Wagenveld Sprint — Phase IV Integration Framework (v0.1)

**Author:** AC (Phase IV integration role per binding II.5 §9)
**Date:** 2026-05-30
**Status:** **Pre-registered / advisory.** Written *before* Phase III v0.1 predictions land, deliberately — pre-registering the discrimination tests avoids post-hoc fitting and fixes the acceptance bar in advance. Becomes operative when §5.2/§5.3/§5.4 (Scratch) and §2.7/§2.3 v0.1 (Jammer) arrive. Not a gate on any stream; it tells the lanes what Phase IV will ask of their outputs so they produce the right things.

**Inputs grounding this:** binding co-rank-1 (`Scratch_Jammer_..._Phase_II_5_Adversarial_Review_v0_1.md`); §5.1 seed (`Scratch_..._Phase_III_5_1_Seed_Amplitude_v0_1.md`, A~0.1–0.8, c_A-soft to ~few — AC verdict `1AxaQSr5...`); Cursor DOF memo + HEALPix scaffold (`wagenveld_sprint_footprints_nside8.json`, Nside=8 projection proxy).

---

## §1 — What Phase IV must decide

The binding II.5 left §2.7 and merged §2.5 observationally degenerate at the Phase I + I.5 vantage and deferred discrimination here. Phase IV must answer, in order:

1. Do the Phase III v0.1 predictions **break the §2.7 ↔ merged §2.5 degeneracy**, or do they remain co-equal?
2. Is the resolution **single-mechanism** (one candidate carries Wagenveld) or **multi-mechanism** (a coherent §2.7 + §2.5 combination, which II.5 promoted to primary framing)?
3. Where does §2.3 (frame mismatch, rank-2 alive-but-watching) land after catalogue directions?
4. What honest-scope tier does the outcome support (§6)?

---

## §2 — Required inputs from each lane (so Phase IV can actually run)

| Lane | Deliverable | Phase IV needs, in this form |
|------|-------------|------------------------------|
| Scratch §5.2 | ∂κ/∂ε normalisation | The **δκ → observed-dipole transfer**: how δκ(n̂) maps to a number-count dipole D_S (the [2+x(1+α)] count-slope factor), and the fractional-vs-absolute convention. Without this, A~0.1–0.8 is not yet a dipole amplitude. |
| Scratch §5.4 | per-survey ΔD_S | ΔD_S = A·∫W_S(n̂)(n̂·n̂_pref)dΩ / ∫W_S dΩ for all four surveys, as a **band** in A (not a point — see §3 Test C). |
| Scratch §5.3 | Hopf-fibre direction | Is n̂_pref **structurally forced** near CMB apex, or a **fit parameter**? Binary output with justification — this sets whether direction is a prediction or a free knob (DOF, §4). |
| Jammer §2.7 v0.1 | δ₂ survey-geometry | Per-survey predicted amplitude pattern from LoTSS source-distribution geometry — and explicitly **whether the pattern is Wagenveld-unique or shared** with CatWISE/Quaia geometry. |
| Jammer §2.3 v0.1 | frame-amplitude F(Δθ) | Per-survey amplitude + the direction-consistency cross-check vs catalogue ingest. |
| Cursor | catalogue LoTSS footprint (P0) + directions | Replaces the analytic scaffold; supplies catalogue directions for the ratio + direction tests. DOF accounting (shared vs per-survey nuisance params). |

---

## §3 — Discrimination tests (pre-registered)

### Test A — inter-survey amplitude **ratio** (primary; A-independent, hence c_A-independent)

The single most useful discriminator, and it sidesteps the c_A uncertainty I flagged in the §5.1 verdict. Merged §2.5 predicts δκ(n̂)=A·(n̂·n̂_pref), so each survey's dipole contribution scales as A·⟨n̂·n̂_pref⟩_S. **A cancels in any ratio between surveys.**

**Amended 2026-05-30 (AC handoff post-§5.4 verification):** The specific **"≈3.1× Wagenveld/full-sky"** value from Cursor's crude iso-latitude Nside=8 proxy is **superseded** — a pixelisation artifact (spurious uniform floor P≈0.0096; proper HEALPix gives uniform surveys **P=0 exactly**). The robust content is **qualitative**: Wagenveld's asymmetric northern footprint → large positive projection (**P ≈ 0.32** proper HEALPix); genuinely near-full-sky surveys → **P ≈ 0**. The quantitative inter-survey ratio is **not pinnable until catalogue-grade footprints land** (Cursor P0); discriminating power lives in real footprint asymmetries (CatWISE/Quaia/Singal masks, Galactic cut, true f_sky).

§2.7 predicts a *different* inter-survey pattern — enhancement tied to LoTSS source-distribution/flux geometry, not to a universal n̂_pref projection — so its ratio set need not track the footprint-projection ratios. **Test A:** compute observed per-survey amplitude ratios; compare against (i) the §2.5 projection-ratio vector and (ii) the §2.7 geometry-derived vector. Whichever the observed ratios track is favoured; if observed ratios sit between, multi-mechanism (§5).

### Test B — direction consistency (catalogue-sourced)

Per Jammer's binding §2.3 threshold: catalogue inter-survey direction separation **<5°** → §2.3 elevates and merged-§2.5/§2.3 frame picture strengthens; **>10°** → §2.3 demotes. Independently: do all surveys' directions cluster near a common n̂_pref (favours §2.5 universal-axis) or scatter with survey geometry (favours §2.7)? Gated on Cursor catalogue directions (Quaia priority).

### Test C — absolute amplitude (feasibility, A-band-dependent → softer)

Only here does A (hence c_A) enter. ΔD_wagenveld ≈ A·0.0296 with A~0.1–0.8 (→ ~few if c_A runs high). Feasibility question: does ΔD_wagenveld, after the §5.2 transfer, **reach the observed Wagenveld excess**, or is there a residual gap that only the §2.7 contribution (multi-mechanism) closes? **Do not dial c_A to close it** (Greg directive); report the gap honestly as a band. Because this test is A-soft, Test A is primary and Test C is corroborating.

---

## §4 — DOF-fair comparison

Each candidate is scored on fit **net of free parameters**, using Cursor's DOF memo (shared vs per-survey nuisance). Parameter ledger to fill at Phase IV:

- **Merged §2.5:** A (1, c_A-set — or 0 free if Test A uses ratios only); n̂_pref (**1 free direction** per §5.3 — CMB dipole favoured anchor, not structurally forced at v0.1). Best case for Test A: ratio test remains A-independent; direction adds **1 DOF**.
- **§2.7:** survey-specific activation strength — count whether it needs one parameter per survey (worse DOF) or one geometry rule (better).
- **§2.3:** frame direction + F(Δθ) normalisation.

A candidate that fits with fewer free parameters wins on the DOF-fair metric even at equal raw agreement. The §5.3 structural-vs-fit verdict on n̂_pref is therefore load-bearing for §2.5's DOF score.

---

## §5 — Multi-mechanism adjudication

II.5 made a coherent §2.7 + §2.5 combination the primary framing, not a fallback. Rules to keep it honest:

- A combined fit must use a **single shared n̂_pref** where both invoke a direction (no independent direction knobs per mechanism — that would be double-counting the angular DOF).
- The combination is only preferred over the best single mechanism if it improves DOF-fair fit by more than the added parameters justify (no overfitting reward).
- If §2.7 alone passes Test A and Test C with adequate DOF, single-mechanism §2.7 is the parsimonious outcome and merged §2.5 becomes a sub-dominant contributor, not a co-anchor — and vice-versa. Co-rank-1 is the *entry* condition to Phase IV, not a guaranteed *exit* state.

---

## §6 — Honest-scope acceptance bar (pre-set)

| Outcome | What it requires | Claim permitted |
|---------|------------------|-----------------|
| **Testable predictions produced** | Phase III v0.1 predictions exist with discriminating tests defined | "NTE produced candidate mechanisms with discriminating predictions" — the sprint's stated bar |
| **Anomaly addressed** | One mechanism (or the combination) passes Tests A+B at DOF-fair parity with ΛCDM-systematic baselines | "NTE offers a viable mechanism for the Wagenveld excess, pending external scrutiny" |
| **Tier-1 standalone** | Above + Test C absolute amplitude reached without number-dialing + survives post-sprint adversarial review | Tier-1 paper — **contingent on Phase IV convergence, not pre-ordained** |

A clean §2.7 resolution may be a methodology note rather than new physics; that outcome is valuable and must not be skewed by reward-seeking (carried from top-3 §7).

---

## §7 — Open dependencies

- **Test A (ratios):** **runnable** on catalogue footprints (Scratch §5.4 v0.2, 2026-05-30). §2.5 projection-ratio vector at Nside=16: P_wag=0.222 (LoTSS two-cap), P_cat/quaia/singal≈0 (symmetric Galactic cuts). Compare against Jammer §2.7 geometry-derived vector when it lands.
- **Test B (directions):** runnable on `wagenveld_sprint_surveys.json` v0.4 literature anchors; Quaia direction TBD (highest leverage).
- **Test C (absolute):** runnable via Cursor void-bias harness v0.6; merged §2.5 mid-band ~13% of Wagenveld observed excess (sub-dominant).
- **DOF score:** needs §5.3 (n̂_pref structural-vs-fit) + Cursor DOF memo.

**Addendum (2026-05-30, Cursor integration of Scratch §5.4 v0.2):** Catalogue-grade HEALPix input is `wagenveld_sprint_footprints_nside16.json`. The v0.1 northern-hemisphere proxy (P≈0.32) is superseded for quantitative Test A by LoTSS cap geometry (P≈0.22). Symmetric-cut full-sky surveys still project to P≈0 at ring-centre — robust qualitative pattern unchanged.

AC remains in integration role; this framework is the adjudication spec the Phase III outputs feed into. No stream action required beyond producing the §2 inputs in the stated form.

— AC, 2026-05-30. Phase IV integration framework pre-registered; Test A (A-independent ratio) is the primary, c_A-robust discriminator.
