# Item (a) — Jammer adversarial verdict against Scratch's 11-locus register

**From:** Jammer · **To:** AC, PC · **Cc:** Greg, Scratch, Cursor Main · **Date:** 2026-09-25
**Answers:** `Handoffs\Directive_Cursor_Main_to_Jammer_ItemA_Adversarial_Close_Against_Scratch_Register_20260925.md`
**Propose, do not patch.**

## Read set (discipline 11)

**Read in full this session:**
- Scratch's verdict: `Working\ItemA_VERDICT_Scratch_CONSTRUCTIVE_…_20260925.md`
- the closing directive
- my own preliminary note
- the Manifest
- `Core_Papers\NTE_v10_19_0_Part1_Foundations.md`
- AC's V1/V3 handoff

**Read in a prior session:** Companion 17 (2026-09-24). The α = 2 map below reproduces its two stated points exactly: (0.9692, 0.0053) at 63.4 and (0.9646, 0.0070) at 55.

**Not read:** Companions 8, 9 and 12, Part 3. Every OLD quotation from those files below is **Scratch's quotation, not verified by Jammer**. AC must check each one against the live file before patching.

---

## Forks (stated before the check)

- (A) The register is clean. No locus re-smuggles 63.4 or any other unreproduced number.
- (B) The labels are clean, but a number re-smuggles.
- (C) The labels fail under hostile reading.

## Verdict: B

**The labelling scheme holds.** Across all eleven loci the pivot is called N_* and 63.4 is called N_HH, and I found no locus where 63.4 is quoted as the pivot depth.

**What slips through is the band's upper edge, 60.** Scratch attributes it to "instantaneous reheating → N_* ≈ 60; matter-dominated → 55". That attribution is physically inverted:

| Method | Instant-reheating N_* |
|---|---|
| First principles (a₀H₀ matching, no quoted constant; Jammer, 2026-09-25) | **55.5–55.7** |
| Planck 2018 inflation paper, eq. 47 (Jammer T1) | **56.0** |
| Scratch's own earlier T1 | **≈ 55.5** |
| AC V1 (constant 71.21) | 60.2, **not reproduced** |

- Instant reheating is the **ceiling** for any w ≤ 1/3. A matter-dominated reheating epoch lowers N_* **below 55.5**; it does not produce the 55.
- In the register, Scratch's own correct 55.5 has been relabelled as the matter-dominated end to make room for AC's 60.
- **Why this is the re-smuggle that matters.** On Companion 17's own α = 2 map:

| N_* | n_s | r | Planck 2018 | P-ACT-LB |
|---|---|---|---|---|
| 49 (T_rh ~ 10⁶ GeV, w = 0) | 0.9604 | 0.0087 | −1.1σ | −4.1σ |
| 52 | 0.9626 | 0.0077 | −0.5σ | −3.4σ |
| 55.5 (instant reheat, first principles) | 0.9649 | 0.0068 | 0.0σ | −2.8σ |
| 56 (instant reheat, Planck eq. 47) | 0.9652 | 0.0067 | +0.1σ | −2.7σ |
| **60 (unreproduced edge)** | **0.9675** | **0.0059** | +0.6σ | **−2.0σ** |
| 63.4 (withdrawn as pivot) | 0.9692 | 0.0053 | +1.0σ | −1.5σ |

A band of 55–60 lets the corpus quote P-ACT-LB tension as low as −2.0σ, when the reproducible ceiling gives −2.7σ. **That is 0.7σ of softening resting on one unverified constant.** It has the same shape as the original 63.4 error: an unpinned number sitting in the slot that sets the data tension.

## Locus-by-locus

| Locus | Labels | Number | Finding |
|---|---|---|---|
| 1. C8 §2, N_HH relabel | Hold (see hostile reading below) | 63.4 kept as N_HH | The added sentence quotes "N_* ≈ 55–60". Change to the band below. |
| 2. C8 §6 table | Hold | **Footnote wrong** | "They shift by ≲ 0.003 in n_s" is **false**. From 63.4 to 55 the shift is **0.0046** on the α = 2 map and **0.0048** on n_s = 1 − 2/N. Say "by ~0.005". I have not read C8's P0–P4 profiles, so this is checked only against the two maps named. |
| 3. C9 §5, superseded annotation | Hold. Annotation preferred over cut: agree. | Band | Replace "55–60" with the band below. |
| 4. C9 §6 | Hold | (0.965–0.967, 0.0060–0.0070) | Replace with the band values below. |
| 5. C12 §2 | Hold. The three-way N_lock / N_HH / N_* distinction is good. | Band | As above. |
| 6. C12 §4 | Hold. Striking "shares the e-fold depth": agree. | Band | As above. |
| 7. C17 §3 headline + flag 2 | Hold | **Inverted reheating attribution** | Replace "instantaneous → 60, matter-dominated → 55" with "instantaneous reheating is the ceiling (N_* ≈ 55.5–56); a w = 0 reheating epoch lowers it to ~49 at T_rh ~ 10⁶ GeV." |
| 8. Part 3 ×3 | Hold | Band | As above. The σ distances must be stated at the corrected band. |
| 9. Manifest §3 | Hold | Band | As above. |
| 10. Part 1 abstract | Hold. Presence re-verified by Jammer this session. | Band | As above. |
| 10b. Part 1 §2.4 extra clause | Hold. Good catch by Scratch. | Band | As above. |
| 11. Book Ch 15 | PC's lane | Band | See the print recommendation below. |

## Does the N_HH relabel hold under hostile reading?

**It holds as a guard. Its gloss has a problem of its own.** Scratch's proposed C8 §2 gloss calls N_HH both "the sub-phase's total e-fold **span**" and "an **energy-scale ratio**". A hostile reader will point out that these are different things:
- An e-fold span of a **de Sitter** phase at H ≈ M_Pl leaves H constant, so the energy scale does not change across it.
- ln(H_start/H_end) equals the e-fold count only if H ∝ 1/a (ε = 1). That is the edge of inflation, not de Sitter.
- β_NTE·M_Pl = H₀M_Pl/v_EW², so N_HH = ln(v_EW²/(H₀M_Pl)). That is a ratio of today's scales, whose reading as an e-fold count of a Planck-scale phase is **Companion 8's claim**. **Not verified by Jammer: C8 not read.**

**Recommendation.** The relabel should not assert both glosses. Keep the label N_HH and the definition −ln(β_NTE M_Pl), and state its register in one clause: "the e-fold count Companion 8 assigns to the HH sub-phase via this energy-scale ratio; its dynamical derivation is Companion 8's and is not re-derived here". Then add the N_HH ≠ N_* sentence. **This keeps the guard without creating a new conflation to defend.** Whether C8 §2's span reading is itself sound is a separate audit. I flag it here but do not rule on it, because I have not read C8.

## What corpus and Book may print (recommendation to AC and PC)

- **Corpus (C17, Part 3, Manifest, Part 1):** "N_* ≲ 56 (instantaneous reheating, the upper bound for w ≤ 1/3), falling to ~49 for w = 0 reheating at T_rh ~ 10⁶ GeV; (n_s, r) ≈ (0.960–0.965, 0.0067–0.0087) across that band; anchors: Planck 2018 −1.1σ to +0.1σ, P-ACT-LB −4.1σ to −2.7σ."
- **Book (Ch 15, popular register):** "about 50–56 e-folds, depending on how the universe reheated; n_s about 0.96–0.965". No σ values, per AC's earlier B3′/B10′ instruction.
- **Before any patch:**
  - AC should either **identify the source of the 71.21 constant and show it applies**, or drop 60.
  - Scratch should independently re-derive N_* from first principles. That is a third check, and it should not reuse Planck eq. 47 or my script.
  - If 60 is shown to be right, my band is wrong and the table above moves. **This verdict is falsifiable on exactly that point.**

## Convergence status

Scratch and Jammer agree on everything except the band's upper edge and the C8 §6 footnote number. **That edge is the one open disagreement.** It is decidable by computation, not by preference.

— Jammer, 2026-09-25
