# PC → Greg (ratify) + Cursor (apply on GO) · Cc AC, Jammer: **C21 v0.8 — eight blocks.** AC's three items; an answer to Jammer's §3 question from the paper's own text; one consequence neither AC nor Jammer stated; and **one live κ-withdrawal site in §7 that PC's first sweep missed and first draft declared absent.**

**From:** PC · **To:** Greg (ratification), Cursor Main (apply on GO) · **Cc:** AC, Claude Jammer, Scratch · **Date:** 2026-10-07
**Arises from:** `Handoffs\AC_to_PC_C21_v0_8_Relic_Neutrino_Repair_First_Occurrence_Plus_Jammer_Boundary_Question_20261007.md`
**Target:** `Core_Papers\Companion_21_ConformalReset_SeedPhoton_v10_19_0.md`, **read in full this session**
**Register unchanged: [SPECULATIVE and NON-LOADBEARING]. Not urgent.**
**Status: DRAFT. Nothing patched.** C21 is now a Core artefact; PC drafts, Cursor applies on GO. The Working `v0_7` path is superseded and carries a do-not-edit banner, so there is no v0.8 Working draft to cut.

---

## 0. Jammer's §3 question — answerable from the text for the first two readings

AC asked Jammer: *does a Hubble cube containing a photon and no relic neutrino satisfy C21's trigger as the paper defines it?* The part that is a question about **what C21 says** is PC's to answer, and it is answerable.

**C21 defines the trigger as a photon count and nothing else.** §3's convention block:

> *n_γ · V_H = 1, with **V_H ≡ R_H³ = (c/H_dS)³**, and n_γ = (2ζ(3)/π²)(kT/ħc)³*

There is **no massive-content condition in the criterion**. So of AC's three readings, the paper as written is **reading one — "one photon per Hubble volume" simpliciter.** It is not reading two; the paper never requires the volume to be free of massive content.

**And §10 already shows how C21 handles massive content: through its photon output, not its presence.** §10 item 2 excludes black holes from the trigger patch not because they are massive but because any hole below ~3 × 10²¹ M_☉ *radiates hotter than the reset bath and floods the volume with photons*, violating n_γ·V_H = 1. That is the paper's own method, applied already and ratified. **Relic neutrinos radiate nothing.** Three cold Majorana neutrinos in a cube do not add photons, so a cube holding one photon and three relics satisfies the criterion as stated.

**Consequence for item (a): Greg's repair is not a replacement of the premise. It is the deletion of a clause that was never part of the criterion.** §3's opening sentence — *"Matter decays to photons; photon density thins; at one photon per Hubble volume…"* — is narrative preamble explaining how the density gets low. The criterion below it never used the decay. So the repair removes a false global claim that carried no load, which is exactly what Greg said and is stronger ground than "the premise is not needed": the premise was **never invoked**.

**What remains genuinely for Jammer** is AC's third reading: whether conformal invariance requires the *boundary* rather than the cube to be free of massive content, since the relics are still on the same S³. C21 does not address it at any version, and PC cannot settle it from the paper. **The blocks below are written so that items (a), (b) and (c) stand whichever way the third reading goes**, and §12.2 gains the question by name rather than having it resolved in the paper's favour.

---

## 1. Item (b) first, because (a) depends on its numbers — **all three figures confirmed wrong, arithmetic re-run independently**

PC re-derived from the paper's own T_reset rather than accepting AC's or Jammer's figures.

| Quantity | Value | Source |
|---|---|---|
| T_reset | 2.213 × 10⁻²⁹ K | C21 §3 |
| T today | 2.725 K | — |
| ratio | 1.231 × 10²⁹ | computed |
| **e-folds, ln(ratio)** | **67.0** | computed |
| ℓ_dS | 1.4 × 10²⁶ m | C21 §2 |
| H_dS = c/ℓ_dS | 2.141 × 10⁻¹⁸ s⁻¹ | computed |
| **t at that epoch** | **9.9 × 10¹¹ yr ≈ 1 × 10¹² yr** | computed |
| **Ht at that epoch** | **67.0** (de Sitter: Ht = N identically) | computed |

**AC's diagnosis of the "200" is confirmed exactly.** 3 × 67.0 = **200.9**, and the photon density goes as T³ — so "200 e-folds" is the natural logarithm of the **photon-density** ratio, mistaken for the e-fold count. A factor of three, not a factor of ten.

**And Ht ≈ 5.7 × 10¹¹ is confirmed as the 10²² yr figure carried through:** 10²² yr × H_dS = 6.8 × 10¹¹. It is the same error one step downstream. AC's note that she verified the multiplication twice without checking its input is correct, and PC supplied the 10²² figure in the first place — the input was PC's.

**Residue:** e^(−3 × 67) = 10^(−87.3), confirming Jammer's ~10⁻⁸⁷ against the paper's 10^(−10¹¹).

### 1a. **The consequence neither AC nor Jammer stated — and it runs the wrong way for §10**

Under item (a) the trigger is a **first occurrence**, which is **earlier** than the homogeneous-density crossing. Earlier means **smaller Ht**, and smaller Ht means a **larger** no-hair residue. So 10⁻⁸⁷ is not the residue — it is the residue *at the mean-field epoch*, which is now an optimistic bound rather than the operative one. The honest statement is a residue of order e^(−3Ht_first) with t_first not estimated.

**§10's conclusion still survives, and the reason matters.** Item 1's argument is **causal severance** — permanent disconnection beyond the de Sitter event horizon — which is in-principle and holds at any anchor, as §10 already says of §2's open anchor question. The no-hair residue is the *qualification*, not the argument. But the old wording leaned the in-principle claim partly on the residue's size (*"in-principle unobservable, which blocks the objection that 'effectively' is not 'actually'"*), and at 10⁻⁸⁷-or-larger that lean is no longer available. The block below moves the in-principle weight entirely onto severance, where it belongs, and states the residue as a bound rather than a number.

**This is a loss of 10¹¹ orders of magnitude in a figure the paper published twice with AC's verification on it. It is recorded as such and not smoothed.**

---

## 2. The blocks

### Block 1 — §3's opening sentence *(item (a), the criterion)*

```
OLD: Matter decays to photons; photon density thins; at one photon per Hubble volume the null-time exchange structure that sustains causal coherence can no longer close.

NEW: Photon density thins as the boundary expands; where a Hubble volume holds one photon, the null-time exchange structure that sustains causal coherence can no longer close there. The criterion is **local and per-volume**, which is what §5's discrete nucleation already assumes: it is satisfied by the **first** Hubble cube to reach it, not by the universe as a whole.

Earlier versions opened this section *"matter decays to photons"*. That clause is **withdrawn.** It was never part of the criterion below — which counts photons and nothing else — and as a global statement it is false: the three massive Majorana neutrinos the framework requires do not decay, and at any epoch under discussion there remains on average of order one relic neutrino per Hubble volume. The criterion does not ask about them. §10's exclusion of black holes from the trigger patch shows the paper's method on massive content and has always shown it: a black hole is excluded because it *radiates photons* into the volume, not because it has mass.
```

### Block 2 — §3, new paragraph after the convention block *(item (a), what the locality buys)*

```
NEW (insert after the "Solving:" display and its Register paragraph):

**Locality, and why the trigger is a first occurrence rather than an epoch.** Nothing in n_γ·V_H = 1 is a statement about the universe. It is a statement about a volume, and the boundary is inhomogeneous, so different volumes reach it at different times. The trigger is therefore the **first** Hubble cube to satisfy it — which occurs earlier than the homogeneous-density crossing, and earlier by an amount set by the inhomogeneity statistics and the number of cubes available. Once one such cube exists, one reset occurs; uncountably many follow, across a distribution of times set by local density. **That distribution is not a cost of the mechanism; it is the mechanism.** §5's nucleation is already discrete and local — *each photon resets once isolated in its own Hubble volume, each seeding its own Janus pair* — and the fractal structure of §8 is what a distribution of trigger times looks like. A single reset epoch was never this paper's claim, and where earlier versions implied one, the implication came from the withdrawn global premise rather than from the mechanism.
```

### Block 3 — §2's timescale paragraph *(item (b))*

```
OLD: **Timescale, and an open item that is not load-bearing.** The one-photon-per-Hubble-cube crossing sits at roughly 10²²–10²³ years (Adams & Laughlin 1997; Krauss & Scherrer 2007), about 200 e-folds past today — much earlier than the ~10¹⁰⁰-year black-hole-evaporation horizon that anchors Penrose's version. Which moment NTE's foam transition should anchor on is open work (§12.2).

NEW: **Timescale — three published figures withdrawn, and what replaces them.** Earlier versions of this section gave the crossing as *"roughly 10²²–10²³ years, about 200 e-folds past today"*, and §10 carried *Ht ≈ 5.7 × 10¹¹* downstream of it. **All three are withdrawn.** From this paper's own T_reset = 2.213 × 10⁻²⁹ K against 2.725 K today, the temperature ratio is 1.23 × 10²⁹ and the e-fold count is its logarithm, **67**, not 200 — the 200 is the logarithm of the *photon-density* ratio, which goes as T³, mistaken for the e-fold count. At ℓ_dS = 1.4 × 10²⁶ m that is **≈ 1 × 10¹² years**, and Ht at that epoch is **67**, since Ht = N identically in de Sitter.

**And under §3's local criterion none of these is quite the right quantity.** 67 e-folds is when the *homogeneous* photon density reaches one per Hubble volume. The trigger is the **first** volume to reach it, which is earlier, by an amount this paper does not estimate: it depends on inhomogeneity statistics the framework does not supply, and a figure chosen to be convenient would be a fitted parameter in another costume. **So the honest statement is that the trigger time is a distribution whose earliest member precedes 67 e-folds, with 67 e-folds / ~10¹² years carried as the homogeneous reference point and not as the trigger.** Either way it is far earlier than the ~10¹⁰⁰-year black-hole-evaporation horizon that anchors Penrose's version, which is the only use this paper makes of the comparison. Which moment NTE's foam transition should anchor on remains open work (§12.2).
```

### Block 4 — §10's no-hair qualification *(item (b) downstream, and §1a)*

```
OLD: One qualification, stated so a referee does not find it first: what left the horizon earlier leaves static Weyl curvature behind, and cosmic no-hair (Wald 1983) erases it as roughly e^(−3Ht) rather than exactly. At the trigger epoch Ht ≈ 5.7 × 10¹¹, so the residue is of order one part in 10^(10¹¹). **Erased, not zero** — and in-principle unobservable, which blocks the objection that "effectively" is not "actually". A completeness remark only: in CCC the Hawking-point channel is concentrated Hawking radiation, not Weyl curvature.

NEW: One qualification, stated so a referee does not find it first: what left the horizon earlier leaves static Weyl curvature behind, and cosmic no-hair (Wald 1983) erases it as roughly e^(−3Ht) rather than exactly. **The figure this paper previously gave here is withdrawn.** It read *Ht ≈ 5.7 × 10¹¹*, residue of order 10^(−10¹¹), and it was carried from §2's withdrawn 10²²-year timescale. At the corrected homogeneous crossing, Ht = 67 and the residue is of order **10⁻⁸⁷** — a correction of some 10¹¹ orders of magnitude in a published figure, and it is recorded rather than quietly replaced.

**The bound is weaker still under §3's local criterion**, because the first volume to trigger does so *earlier*, at smaller Ht, leaving a *larger* residue. So the defensible statement is a residue of order e^(−3Ht) evaluated at a first-occurrence time this paper does not estimate, bounded above by nothing the paper derives and below by 10⁻⁸⁷. **Erased, not zero**, and the erasure is no longer the load-bearing part of the argument.

**What carries the argument is causal severance, in principle rather than in magnitude.** Anything beyond the de Sitter event horizon is *permanently* disconnected from the photon and from the daughter — not faintly connected, disconnected — and that holds at every anchor, which is why §2's open anchor question does not reach this section. The earlier wording let the in-principle claim rest partly on the residue being unimaginably small; it no longer needs to and no longer does. A completeness remark only: in CCC the Hawking-point channel is concentrated Hawking radiation, not Weyl curvature.
```

### Block 5 — §5's "no scale to lose" *(item (c))*

```
OLD: The reason the map works is the reason the whole paper exists: ds² = 0 is preserved under Ω² multiplication. A universe of purely massless content has no scale to lose.

NEW: The reason the map works is the reason the whole paper exists: ds² = 0 is preserved under Ω² multiplication. The second half of that sentence, as earlier versions put it — *"a universe of purely massless content has no scale to lose"* — needs scoping on two counts, because as written it says something the paper does not hold.

**It is not a claim that no scales exist.** They plainly do, and this paper uses them: §2's plateau fixes a finite |Φ_NTE|²  → v_EW²√Ω_Λ and a finite ℓ_dS, and the map's own conformal factor is *defined* as the ratio of two scales, Ω ≡ R_H/ℓ_P. The claim is narrower and is about what the rescaling **preserves**: a massless worldline has no proper time, so its dynamics is a statement about the metric's conformal class alone, and the absolute scales drop out of it. A massive worldline does carry proper time, which Ω² multiplication does not preserve — which is why the content that crosses matters and the content that stays behind does not.

**And the trigger patch is not purely massless either**, now that §3's global decay premise is withdrawn: the framework's three massive relic neutrinos persist, and the criterion does not exclude them from the volume. What crosses is a photon and, by §7, a scalar and topological datum. So the defensible statement is that **the content that crosses is massless and therefore carries no absolute scale across**, not that the parent contains none. Whether massive content elsewhere on the same S³ bears on the conformal step at all is a separate question and is open — §12.2.
```

### Block 6 — §12.2, two new open items

```
NEW (append to §12.2's list):

- Whether conformal invariance at the crossover constrains the **S³ boundary's** massive content or only the **trigger volume's**. C21's criterion is a photon count in a volume (§3) and excludes massive content only through its photon emission (§10 item 2); the framework's three massive relic neutrinos therefore satisfy it while remaining on the same S³. If the conformal step requires the boundary rather than the cube to be free of massive content, locality does not suffice and §5's step needs a condition the paper does not currently state. **Raised by AC on Jammer's read, 2026-10-07; not settled from the deposit.**
- The **first-occurrence time** of the trigger (§§2, 3). The homogeneous crossing is at 67 e-folds; the first volume to satisfy the criterion precedes it by an amount set by inhomogeneity statistics the framework does not supply. No estimate is offered, and §10's no-hair residue inherits the same indeterminacy.
```

### Block 7 — status header and front matter

```
Status line → v0.8, 2026-10-07.

Front matter, new paragraph:

**Changes in v0.8 — Greg's relic-neutrino repair, and a timescale that was wrong at three places.** §3's global premise *"matter decays to photons"* is **withdrawn**: the framework's three massive Majorana neutrinos falsify it, and the criterion below it never used it — it counts photons and nothing else. The trigger is restated as what §5's nucleation always assumed, the **first** Hubble volume to satisfy n_γ·V_H = 1, with uncountably many resets following across a distribution of local times. §2's *10²²–10²³ years / about 200 e-folds* and §10's *Ht ≈ 5.7 × 10¹¹* are **withdrawn and replaced**: from this paper's own T_reset the homogeneous crossing is at **67 e-folds ≈ 10¹² years**, the 200 being the logarithm of the photon-density ratio mistaken for the e-fold count, and the no-hair residue moves from 10^(−10¹¹) to of order 10⁻⁸⁷ — weaker still at a first-occurrence trigger. §10's conclusion survives on **causal severance**, which is in-principle and anchor-independent; the earlier wording let it lean partly on the residue's magnitude and no longer does. §5's *"no scale to lose"* is scoped to the content that crosses. Two items are added to §12.2, including AC's boundary question, which is **not** resolved here.

**Provenance, recorded.** The 10²²-year figure was PC's and entered at v0.2. AC verified Ht ≈ 5.7 × 10¹¹ at v0.6 and again at v0.7 by checking the multiplication rather than its input, and has stated so. Jammer found all three figures on an adversarial read with his forks pre-registered; Greg supplied the repair. **The error survived two verifications because both checked the step and neither checked the premise.**
```

---

## 3. Abstract sweep — AC's standing correction, applied to C21. **It found a site, and it found it on the second pass.**

AC's register note of today: *every withdrawal register must include the abstract of every paper it touches*, and the κ sweep must cover **Part 2, Part 3, C5 and C21**. C21 is PC's.

**First pass.** Searched `Core_Papers\Companion_21_ConformalReset_SeedPhoton_v10_19_0.md` in full for `5.38`, `0.83`, `Ω_DM`, `Omega_DM`, `dark matter`, `dark-matter`, `passed`. **Zero hits on all seven.** C21 has no abstract section as such; the front matter and §1 carry the register and both state **[SPECULATIVE and NON-LOADBEARING]** explicitly.

**PC's first draft of this register said, on that basis, that C21 was clean and needed no patch. That was wrong, and the error is instructive enough to leave in rather than delete.** The seven terms were the *match claim's* vocabulary. The κ withdrawal is not only a match claim — it also removes an endorsement — and searching for the one does not find the other. A second pass on `demonstrated`, `handle`, `channel`, `observational`, `zero-parameter` found the site immediately.

**§7, line 196 — one live endorsement of the withdrawn status:**

> *"The same arbitration found that κ **survives and is demonstrated**, but that its **ontological support has migrated** …"*

Written 2026-09-27 under the N-thickness arbitration, when κ *was* a passed observational handle. Read today, **"demonstrated" asserts exactly what 2026-10-06 withdrew** — that κ has a shown referent. A reader meets it in the section that exists to quarantine κ from this paper, with no mention of the withdrawal. The firewall paragraph is the worst possible place for it: it is where a careful reader goes to check what C21 is and is not claiming about κ.

**Nothing else leaked.** §7's operative firewall sentences (line 194, *"κ does not depend on this paper … no cross-reference may create an apparent dependency in the other direction"*) are unaffected and are if anything strengthened by the withdrawal. Line 258's "handle" is C21's own Hawking-point discriminator, not κ. **Block 8 below is the patch.**

**The generalisation, offered to all streams.** A withdrawal sweep run on the withdrawn claim's own wording will miss every place the claim was *endorsed* in other words. The sweep needs both vocabularies: the claim's, and the grading language the corpus uses to approve claims — demonstrated, passed, handle, channel, confirmed, zero-parameter. **PC ran the first kind, published a negative finding on it, and caught it only because AC's standing correction says to re-examine the class rather than the instance.**

### Block 8 — §7's firewall note *(the κ endorsement)*

```
OLD: *A note on why that firewall now matters more than when it was written.* The same arbitration found that κ **survives and is demonstrated**, but that its **ontological support has migrated** — from the N-thickness to the bilateral two-metric action, whose completion Part 3 lists as open. A speculative paper standing next to a handle whose grounding has just moved is exactly the configuration in which an apparent dependency does damage. The firewall is the thing preventing it.

NEW: *A note on why that firewall now matters more than when it was written.* The N-thickness arbitration (2026-09-27) found that κ's **derivation** survives while its **ontological support migrated** — from the N-thickness to the bilateral two-metric action, whose completion Part 3 lists as open. That note originally read *"κ survives and is demonstrated"*; the second half is **withdrawn (2026-10-07)**. On 2026-10-06 the identification of κ with the observed dark-matter ratio was withdrawn and the observed cold dark matter was deposited OPEN (Part 3, Open work), so κ is derived and zero-parameter with **no established observational referent** — not demonstrated. A speculative paper standing next to a derived number whose grounding has moved *and* whose referent is now open is a sharper version of the configuration this firewall was built for, not a milder one. The firewall is the thing preventing an apparent dependency in either direction, and nothing in this paper may be read as supplying κ a referent.
```

## 4. What PC did not do

- **Did not edit `Core_Papers\`.** C21 is a Core artefact now; these are blocks for Cursor on GO.
- **Did not estimate the first-occurrence time.** It would require inhomogeneity statistics the framework does not supply, and a number chosen to land conveniently is discipline 12's fitted parameter in structural dress.
- **Did not resolve AC's third reading.** It is in §12.2 by name.
- **The Honest Path proposal** (`Handoffs\AC_The_Honest_Path_Deposit_Restructure_Two_Registers_20261007.md`) asks PC for a matching Book split. It is a DRAFT awaiting Greg's ratification and PC has not started it. When it is ratified, PC's reading is that it affects Chapters 9, 10, 12 and 15 and Appendix C — the five artefacts rewritten yesterday — and that the rewrite already moved them most of the way, since every one of them now states the cosmological sector's claims at the open register. **Awaiting GO.**
- **Yesterday's Book rulings 5.1 and 5.2 are still open** (Chapter 9's title and filename; the variance scaling's register in C5 §9, where Core and Book now disagree). Ruling 5.3 is answered — AC has adopted the Bullet Cluster finding as a named Part 3 open-work entry.
- **BA1 remains unapplied in Chapter 7** — eleven days. The missing blank line fuses item 4 of the "Four at Once" list into the preceding paragraph, and it will render that way in any PDF built from the live tip.

— PC, 2026-10-07
