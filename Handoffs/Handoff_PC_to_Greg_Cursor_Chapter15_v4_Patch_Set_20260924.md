# Handoff — PC → Greg (ratify) → Cursor (apply): Chapter 15 v4 patch set

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-24
**Base file:** `Book\Chapter_15_The_Score_v3.md` (canonical, 20,167 B)
**Target:** `Book\Chapter_15_The_Score_v4.md` — v3 left in place
**Status:** PROPOSED — not ratified

---

## 0. Why this pass is larger than the Appendix C pass

Appendix C v1.3 was eighteen days old and mostly current. Chapter 15 v3 is dated 2026-07-05 and predates the corpus unify to v10.19.0. It is the Book's tier ledger, so every register drift in it is a §8 violation by construction — a standalone claim a tier above what the corpus grants.

Six of the eleven patches below are register corrections, not prose. Three of them are the chapter claiming more than the corpus does. One of them — the dark-energy entry — has the chapter offering a mitigation the corpus explicitly says does not exist.

Verified against `NTE_Workflow_Manifest_v10_18.md` §3 (2026-09-23), re-read this session. Part 3 wins on disagreement and PC has not read Part 3 this session; see F5.

---

## 1. Patches

### B1 — §2, T_GB entry: **derived → conditional**

The chapter grades T_GB "derived". §3 demotes it: *"T_GB = M_Pl/√(2π) **conditional** pending Companion 12 fibre-modulus grounding (raw-trace saddle ruled out)"* and *"T_GB demoted to conditional pending fibre-modulus close"*. Greg's own 2026-09-18 ratification of Ch 12 v4.1 authorised the v4.2 revision on exactly this basis ("T_GB → conditional"). Ch 15 must not sit a tier above Ch 12.

**OLD**

```
**T_GB = M_Pl/√(2π) (gauge-birth temperature) — derived.** When gauge symmetry and clocks switched on, the boundary field locked and post-temporal dynamics began. Standard cosmology treats that temperature as an initial condition; the framework derives T_GB ≈ 4.9 × 10¹⁸ GeV from the width of the Hartle–Hawking saddle on the Hopf fibre — the same single relation that fixes the temporal circle's size. No thermometer reaches the birth event; the commitment is structural, and its failure mode is structural too — the fibre relation threads the whole computation, so a wrong T_GB does not fail quietly.
```

**NEW**

```
**T_GB = M_Pl/√(2π) (gauge-birth temperature) — conditional.** When gauge symmetry and clocks switched on, the boundary field locked and post-temporal dynamics began. Standard cosmology treats that temperature as an initial condition; the framework places T_GB ≈ 4.9 × 10¹⁸ GeV at the width of the Hartle–Hawking Gaussian saddle on the Hopf fibre — the same single relation that fixes the temporal circle's size, with √(2π) the Gaussian normalisation rather than a number anyone chose. The register is the honest part. The raw-trace route to that saddle is ruled out, and the route that survives rests on identifying the fibre modulus from the spectral side — a step the framework has not independently grounded. The corpus therefore carries T_GB as *conditional*, and so does this chapter. No thermometer reaches the birth event; the commitment is structural, and its failure mode is structural too — the fibre relation threads the whole computation, so a wrong T_GB does not fail quietly.
```

---

### B2 — §2 closing: the accounting moved T_GB twice, not once

**OLD**

```
Notes from one calculation, none tuned to fit the sky — and no fixed tally: the count reflects where the mathematics has reached, and the framework's accounting has both removed a note (the spectral index, §3) and promoted one (T_GB) as the work matured. What cannot change without collective failure is the joint origin.
```

**NEW**

```
Notes from one calculation, none tuned to fit the sky — and no fixed tally: the count reflects where the mathematics has reached, and the accounting has moved notes in both directions as the work matured. It removed one outright (the spectral index, §3). It promoted another (T_GB) and then demoted it again, when the route to the saddle that carried it turned out to be conditional. A tally that only ever grows is a sales figure; this one is allowed to shrink. What cannot change without collective failure is the joint origin.
```

---

### B3 — §3, n_s entry: stale number, and the wrong open item named

Chapter carries `n_s = 0.9685` and names K(Φ) as the open input. §3 carries **(n_s, r) = (0.9692, 0.0053) at N_e = 63.4 from frame-closed K(Φ) (Companion 17, ξ = 1/6)**, with **anchors Planck 2018 and P-ACT-LB shown side by side**, and lists the open item as the **spectral origin of ξ**. K(Φ) is closed; ξ is not. The chapter is holding a superseded number *and* pointing the reader at the wrong gap.

Recomputed offset against Planck 2018: (0.9692 − 0.9649)/0.0042 = **1.0σ**, not 0.85σ.

**OLD**

```
**n_s = 0.9685 (CMB spectral index) — conditional on K(Φ).** Under the framework's slow-roll reading of the pre-temporal phase, the tilt is 1 − 2/N_e with the e-fold depth N_e ≈ 63.4 fixed by β_NTE — the same constant the central equation runs on, not tuned for the tilt. Planck measures 0.9649 ± 0.0042; the framework's value sits 0.85σ away. The register: the derivation depends on the *kinetic normalisation K(Φ)* — how the boundary field's energy actually varies — which the framework has not derived, and the slow-roll formula's applicability to the pre-temporal section is itself unestablished. The corpus therefore carries n_s as a *conditional survivor*: consistent under a named open assumption, holding reduced predictive credit, explicitly not advanced as a zero-parameter prediction.
```

**NEW**

```
**n_s = 0.9692 (CMB spectral index) — conditional on ξ.** Under the framework's slow-roll reading of the pre-temporal phase, the tilt is 1 − 2/N_e with the e-fold depth N_e = 63.4, fixed by the kinetic normalisation K(Φ) — and K(Φ) is now closed, in the frame the framework works in. Planck 2018 measures 0.9649 ± 0.0042, putting the framework's value 1.0σ away; the corpus deliberately shows the P-ACT-LB combination beside Planck rather than picking one anchor, because the two disagree about the tilt by more than the framework's own distance from either. The register: closing K(Φ) took a conformal coupling, ξ = 1/6, and the *spectral origin of ξ* is open — the framework selects that value on frame-closure grounds, not from the spectral triple. The slow-roll formula's applicability to the pre-temporal section is itself unestablished. So n_s stays a *conditional survivor*: consistent under a named open input, holding reduced predictive credit, explicitly not advanced as a zero-parameter prediction.
```

*(PC has not verified the P-ACT-LB central value and has not quoted one — see F6. If the chapter is to show both numerically, AC supplies the figure from Companion 17.)*

---

### B4 — §3, r entry: stale number

**OLD**

```
**r ≈ 4 × 10⁻³ (tensor-to-scalar ratio) — conditional on the same input.** The same sector, the same open normalisation, delivering a primordial gravitational-wave amplitude comfortably below current bounds.
```

**NEW**

```
**r = 0.0053 (tensor-to-scalar ratio) — conditional on the same input.** The same sector, the same open coupling, delivering a primordial gravitational-wave amplitude below every current bound — but not by much, and not for long.
```

---

### B5 — §3, the fuse paragraph: wrong condition, and it undersells the date

Two corrections. The fuse is lit by ξ, not K(Φ). And at r = 0.0053 the prediction sits *above* LiteBIRD's target sensitivity near 10⁻³ — so the instrument reaches it rather than merely approaching it. The v3 wording ("tighten toward sensitivity near r ≈ 10⁻³") leaves the reader thinking the test is marginal when it is the sharpest date in the tier.

**OLD**

```
The conditional tier is not a parking lot; it is a fuse. If the framework closes the derivation of K(Φ), both numbers convert overnight into hard zero-parameter tests — no escape hatch — precisely as CMB-S4 and LiteBIRD tighten toward sensitivity near r ≈ 10⁻³ and δn_s ≈ 0.001 in the early 2030s. A measurement of r far above the framework's value, even now, would mean the inflationary reading has missed something at the dynamics level. The test date depends on the framework's own homework, and Appendix C carries K(Φ) at the top of the open-work list for exactly that reason.
```

**NEW**

```
The conditional tier is not a parking lot; it is a fuse. If the framework derives ξ from the spectral side instead of selecting it, both numbers convert overnight into hard zero-parameter tests — no escape hatch — and the instruments are already coming for them. CMB-S4 and LiteBIRD reach sensitivity near r ≈ 10⁻³ and δn_s ≈ 0.001 in the early 2030s, which puts r = 0.0053 inside the window rather than below it: this is the nearest hard date the framework has. A measurement of r far above the framework's value, even now, would mean the inflationary reading has missed something at the dynamics level; a firm null well under 10⁻³ would do the same from the other side. The test date depends on the framework's own homework, and Appendix C carries the spectral origin of ξ at the top of the open-work list for exactly that reason.
```

---

### B6 — §4, dark energy: **the chapter offers a mitigation the corpus rules out**

This is the serious one. v3 reads DESI's low-redshift deviation as "void-enhancement signature" — i.e. as something the framework absorbs. §3 says the opposite, in terms:

> *"w = −1 naked prediction at ~3.1σ (DESI DR2 BAO+CMB SN-independent); void mechanism signed anti-DESI — **no internal mitigation**."*

The void mechanism is signed the wrong way. Reusing it here is the Hubble-tension move applied where it does not apply, and it converts the corpus's hardest live loss into a reassurance. It also understates 3.1σ as "hints". Both must go.

**OLD**

```
**The dark-energy equation of state w = −1, exactly.** A clean cosmological constant — structural quietness, not a dynamical field. The DESI hints of low-redshift deviation the framework reads as void-enhancement signature. Test: DESI's full survey. If w is genuinely time-varying after void corrections, the framework's reading requires substantial revision.
```

**NEW**

```
**The dark-energy equation of state w = −1, exactly — naked, and currently losing.** A clean cosmological constant: structural quietness, not a dynamical field, and no dial anywhere in the framework to turn. DESI DR2 — baryon acoustic oscillations with the CMB, supernova-independent — prefers evolving dark energy over w = −1 at about 3.1σ. The framework has no answer to that. The void mechanism that carries the Hubble tension is signed the wrong way here: it works *against* the DESI preference rather than explaining it, so it cannot be borrowed to soften this. w = −1 is exposed exactly as a prediction should be. Test: DESI's full survey and what follows it. If the preference firms up, w = −1 fails in the open, and the reading of Λ as structural quietness rather than dynamics fails with it.
```

---

### B7 — §5, CP phase: **the sign of the asymmetry is not the framework's to claim**

§3 fixes **|δ_J| = π/2** — magnitude only. The corpus records the δ_J sign as *free* (Manifest §10, the declined Companion 15 cross-reference, which turns on precisely that freedom). v3 has the geometry underwriting "the existence **and matter-favouring sign**" of the baryon asymmetry. It cannot underwrite a direction it does not fix.

**OLD**

```
The same geometry underwrites the *existence and matter-favouring sign* of the baryon asymmetry, which the sky already shows; the asymmetry's precise magnitude the framework carries only at order-one consistency (Appendix C).
```

**NEW**

```
What the geometry fixes is the magnitude, and only the magnitude: |δ_J| = π/2. The sign is free — nothing in the Janus construction selects it. So the framework underwrites maximal CP violation, and with it the *existence* of a baryon asymmetry; it does not underwrite the direction. That matter won rather than antimatter is a fact the framework accommodates, not one it predicts, and the distinction is worth keeping because the opposite sign would have been just as comfortable. The asymmetry's magnitude it carries only at order-one consistency (Appendix C).
```

---

### B8 — §5, θ₂₃: state what the reflection does *not* fix

The reflection's virtue is that it leaves θ₁₃ free. Saying so here is what makes Appendix C's sharpened solar-angle entry (A1, "the algebra does not choose") read as a considered position rather than a retreat.

**OLD**

```
Global fits: 45.0° ± 1.0° — consistent. The third of the three. Tightening octant data will eventually settle whether exact maximality holds.
```

**NEW**

```
Global fits: 45.0° ± 1.0° — consistent. The third of the three. What the reflection does *not* fix belongs in the same breath, because it is the reason the framework uses reflection rather than the simpler μ–τ permutation: reflection leaves θ₁₃ free, and θ₁₃ is measured nonzero, near 8.6°. A permutation symmetry would have forced θ₁₃ = 0 and been dead before it started. A symmetry that declines to fix an angle is doing work too. Tightening octant data will eventually settle whether exact maximality holds.
```

---

### B9 — §2, Λ: the dissolution is not NTE's alone

§3, empirical distinctiveness: the surface-only dissolution of the vacuum-energy catastrophe *"is not unique to NTE"*. The chapter should not let the reader infer priority.

**OLD**

```
The mechanism is the claim; the number is not — a previously circulated value was withdrawn when its route was found to be closed, and the numerical Λ sits in the open-work ledger.
```

**NEW**

```
The mechanism is the claim; the number is not — a previously circulated value was withdrawn when its route was found to be closed, and the numerical Λ sits in the open-work ledger. Nor is the mechanism NTE's alone: boundary-only ontologies and trace-free treatments of gravity remove the catastrophic term in other hands too. What the framework claims here is the combination and the company it keeps, not the discovery.
```

---

### B10 — §6, the grades paragraph: five corrections in one place

Inherits B1, B3, B4, B6, B7, and carries Appendix C's A1 into the score. The solar angle moves out of "currently losing" — it is not losing, it is **withdrawn**, and the difference is the whole point of keeping a ledger. This introduces a new grade line; **Greg to rule on whether the scorecard gains a "withdrawn" category** (F7).

**OLD**

```
**Passed, at the strictest tier:** κ within 0.83σ of Planck, zero parameters, now backed by the Janus action. **Consistent, at the strictest tier:** θ₂₃ maximal within current precision (inherited, credited); the baryon asymmetry's existence and sign. **Cross-checks passed:** M₁ within a factor 1.1 of the leptogenesis requirement; m_ν₂ within 0.7% of the solar scale on one branch of an open fork — with the branch and the atmospheric overshoot stated in the same breath. **Conditional, fuse lit:** n_s at 0.85σ and r below all bounds, both awaiting K(Φ). **By construction, not counted:** H₀ at the cosmic mean; standard BBN recovered (N_eff = 3.044, Y_p = 0.247). **Absences holding:** no WIMP, no fourth generation, no W_R, decade after decade. **Currently losing:** the atmospheric mass ratio, the solar angle at leading order, lithium-7, and the asymmetry's magnitude — catalogued honestly in Appendix C, at full volume, alongside the open gaps and the pathways under investigation.
```

**NEW**

```
**Passed, at the strictest tier:** κ within 0.83σ of Planck, zero parameters, now backed by the Janus action. **Consistent, at the strictest tier:** θ₂₃ maximal within current precision (inherited, credited); |δ_J| = π/2, with the sign free and the asymmetry's direction therefore not claimed. **Cross-checks passed:** M₁ within a factor 1.1 of the leptogenesis requirement; m_ν₂ within 0.7% of the solar scale on one branch of an open fork — with the branch and the atmospheric overshoot stated in the same breath. **Conditional, fuse lit:** n_s at 1.0σ and r = 0.0053 under every current bound, both resting on ξ = 1/6 with its spectral origin open; and T_GB, pending the fibre-modulus grounding. **By construction, not counted:** H₀ at the cosmic mean; standard BBN recovered (N_eff = 3.044, Y_p = 0.247). **Absences holding:** no WIMP, no fourth generation, no W_R, decade after decade. **Currently losing:** w = −1 against DESI DR2 at about 3.1σ, with nothing internal to absorb it; the atmospheric mass ratio; lithium-7; the asymmetry's magnitude. **Withdrawn — a gap, not a defeat:** the leading-order solar angle. The framework once offered sin²θ₁₂ = 1/3 and no longer does; the algebra does not choose between the candidate values, and on the present reading it does not determine the solar angle at all. That is a hole in the derivation, not a failed test, and a ledger that blurs the two is no use to anyone. All of it sits in Appendix C, at full volume, alongside the open gaps and the pathways under investigation.
```

---

### B11 — §1, tier preview: the conditional tier now has three members, not two

**OLD**

```
Below them sit the chord's structural results at their own registers; a conditional pair whose test date depends on the framework finishing a named piece of homework; consequences that follow by construction and are honestly not tests at all; and the open tensions — the places where the framework is currently *losing* — which have their own catalogue in Appendix C, because a scorecard that lists only wins is advertising, not accounting.
```

**NEW**

```
Below them sit the chord's structural results at their own registers; a conditional tier whose test dates depend on the framework finishing named pieces of homework; consequences that follow by construction and are honestly not tests at all; the claims the framework has withdrawn; and the open tensions — the places where it is currently *losing* — which have their own catalogue in Appendix C, because a scorecard that lists only wins is advertising, not accounting.
```

---

## 2. Flags

**F1 — RELEASED.** The Appendix C hold on the (n_s, r) anchors is lifted. Greg's 2026-09-18 ratification of Ch 12 v4.1 authorised the Book to carry *"(n_s, r) → 0.9692 / 0.0053 at N_e = 63.4 with dual anchors"*, and §3 records N_e = 63.4 as settled by Companion 17. The open item is ξ's spectral origin, which does not move the numbers. **Consequence for the pass already with you:** Appendix C v1.4 should gain a fifth patch, **A5**, updating its (n_s, r) row to 0.9692 / 0.0053 with dual anchors and re-pointing its open-work entry from K(Φ) to the spectral origin of ξ. PC will draft A5 on your word rather than assume it.

**F3 — half answered.** Chapter 15 must **not** mention the conformal reset or C21 at all, and v4 does not. C21 is ratified [SPECULATIVE and NON-LOADBEARING], and the deposit rule is that nothing in the set may lean on it. The score chapter is the single place where a speculative entry would corrupt the tier structure, because its whole function is to say what register each claim holds. So the Book-ledger question reduces to Appendix C alone: does the open-work list gain the interface question. Still yours to rule.

**F4 — JUNO currency, unverified.** §5 says the ordering verdict is "imminent" and "present data lean normal at modest significance"; §6 says "JUNO rules on the mass ordering". JUNO is now publishing oscillation results — the θ₁₂ withdrawal cites arXiv:2511.14593 — and PC has not checked what its current data say about ordering significance, or whether "imminent" is still the right word. Not patched. Recommend routing a literature-currency check (Scratch's lane) before the Book ships, covering JUNO ordering status, DESI DR2/DR3 as of now, and the LiteBIRD/CMB-S4 timeline the chapter quotes.

**F5 — the Manifest contradicts itself on T_GB.** §3 lists T_GB under **Derived / structural** — *"closed at the Hartle–Hawking Gaussian saddle-width (Companion 9), fibre-modulus identification β_GB·M_Pl = √(2π) from the spectral side (Companion 12)"* — and simultaneously under **Conditional** — *"conditional pending Companion 12 fibre-modulus grounding (raw-trace saddle ruled out)"* — and again in the chord paragraph as *"demoted to conditional"*. One says Companion 12 closed it; two say Companion 12 has not. PC wrote **conditional** (two of three, plus the Ch 12 v4.2 authorisation), but this is AC's to reconcile against Part 3, which wins. If Part 3 grades it derived, B1 and the T_GB clause in B10 come back out.

**F6 — P-ACT-LB value not quoted.** B3 says the corpus shows the anchor beside Planck but gives no number, because PC has not verified one and will not invent it. AC supplies it from Companion 17 if the chapter is to print both.

**F7 — new grade category, Greg's call.** B10 adds **"Withdrawn — a gap, not a defeat"** to the reckoning. It is the right distinction and it is an addition to the scorecard's structure, so it should not slide in as prose. If you decline it, the solar angle goes back under "currently losing" and the sentence about what the algebra does not determine still stands.

**No-patch notes.** β_NTE is quoted at 2.4 × 10⁻⁴⁷ GeV⁻¹ in §7 against §3's 2.38 × 10⁻⁴⁷; that is rounding, left alone. M_R sits at "pathway identified, not derived" in both the chapter and §3, so the Companion 10/13 repairs do not reach Ch 15. A9 photon-frame vocabulary does not appear in this chapter — checked; no instances of frame, perspective, or a photon vantage.

---

## 3. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*, as part of this delivery:

```
- **Book/ Chapter 15 v4 patch set** (`Handoff_PC_to_Greg_Cursor_Chapter15_v4_Patch_Set_20260924.md`, PC, 2026-09-24) — B1–B11 on `Chapter_15_The_Score_v3.md`. Register corrections: T_GB derived → conditional; (n_s, r) → 0.9692 / 0.0053 with the open item re-pointed from K(Φ) to the spectral origin of ξ; w = −1 restated as losing at ~3.1σ with the void mitigation removed (signed anti-DESI); δ_J sign freedom — baryon-asymmetry direction no longer claimed; solar angle moved from "losing" to "withdrawn". Flags F4 (JUNO/DESI/LiteBIRD currency, unverified), F5 (Manifest §3 self-contradiction on T_GB), F6 (P-ACT-LB value), F7 (new "withdrawn" grade category). **Status: PROPOSED, awaiting Greg.**
```

---

## 4. On ratification

Cursor applies B1–B11 byte-exact to a copy saved as `Chapter_15_The_Score_v4.md`; v3 left in place; match-or-report, never force. Then re-render and return the completion handoff.

PC then proceeds to **Chapter 4** with the A9 patch set and the emergence sweep folded in — the "Time and Expansion" retitle, the emergence register (*neither emergent from the other; intrinsically bound, possibly the same phenomenon*), and the framework-name sentence — followed by Ch 2 and Ch 5. Ch 1 v11 and Prelude v8 carry the same three items and can go in the same wave if you would rather have the emergence register land everywhere at once than chapter by chapter.
