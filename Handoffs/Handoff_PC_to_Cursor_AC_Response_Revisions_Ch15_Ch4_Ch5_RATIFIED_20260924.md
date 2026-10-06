# Handoff — PC → Cursor: revisions to three Book patch sets, following AC's Part 1 / Part 3 readings

**From:** PC
**To:** Cursor Main · **Cc:** Greg, AC
**Date:** 2026-09-24
**Greg ratified 2026-09-24, 18:15 NZST.**
**In response to:** `Handoff_AC_to_PC_Physics_Queries_Answered_N2_Closes_F5_Open_20260924.md` and `Handoff_AC_to_PC_F5_Closed_Ch15_Released_N1_Escalated_Part1_Part3_Disagree_20260924.md`

**Targets:** `Book\Chapter_15_The_Score_v3.md` (B3′, B10′ — **supersede** the same patches in the Ch 15 v4 set) · `Book\Chapter_04_Time_as_Expansion_v8.md` (C16 — **additional** patch) · `Book\Chapter_05_The_Eighth_Colour_v7.md` (D10, D11 — **additional** patches)

**Apply order:** B3′ and B10′ replace B3 and B10 inside the Chapter 15 apply — do not apply both versions. C16, D10 and D11 are additions to their sets, applied in the same pass.

Byte-exact match-or-report throughout. No numbers change except the two σ figures removed in B3′/B10′ and the one anchor value added.

---

## 0. Why

AC read Part 1 and Part 3 in full today and closed five of PC's six physics queries. Three answers require the Book to change, and one of them lands on a patch set that is already ratified and now released for apply.

- **F6.** AC supplied the P-ACT-LB value PC declined to invent — **n_s = 0.9743 ± 0.0034** — with a caveat: the σ figures in Part 3 are computed against (0.9692, 0.0053) at N_e = 63.4, and **if Greg ratifies the Companion 17 N_e change both anchors move**, Planck's offset shrinking toward +0.1σ and P-ACT-LB's growing toward −2.7σ. AC's instruction is to print the anchors and **not** the significance values. PC's B3 prints "1.0σ away" and B10 prints "n_s at 1.0σ". Both would be stale within the week. **B3′ and B10′ remove them.**
- **G5.** N_lock ≈ 0.1 is supported, but Part 3 carries it at **candidate** register — *"N_lock (candidate, pending closure)"* — and Part 1 §VII frames it as the **completion of a staged process** (quarks ~10⁻³, leptons ~10⁻², completion ~10⁻¹), not a single threshold. Chapter 4 reads it as a settled moment. **C16 fixes both, and the staging is better pedagogy than the threshold was.**
- **H1.** Part 1 does not name a potential V_NTE. It makes the stiffness argument through the SM Higgs potential's **curvature** instead. V_NTE does exist in Companion 9 eq. (1), but whether its form is derived or assumed is unverified — and that is precisely the distinction Ch 5's forced-addition argument turns on. **D10 rebuilds the argument on Part 1's own reasoning**, which needs no named potential and is stronger.
- **H2.** 10^8.5 is the corpus figure and stands. But Part 1 §2.3 frames the range as *"read off the expansion history, not predicted by it"* — a cross-check — and Ch 5 currently reads as though the framework produced it. **D11 corrects the register.**

Closed with no Book change: **N2** (Part 1 §V's R_H is the Hubble radius, and in the de Sitter limit it coincides with the event horizon, so no defect and no numbers move — Ch 3's M6 remains correct and necessary for the Book's general-cosmology passage), **F5** (T_GB conditional; B1 and the B10 clause stand), **N1** (Part 3 and the manifest patched by AC; Chapter 3 needs no change), **F2** (A5 correct; the "unobservable at the framework's heavy scale" caveat already travels with it).

**Falsifiability item 11 does not enter the Book in this pass.** Per AC's note, it is a new *exposure*, not a new prediction, and Chapter 15's scorecard must not gain a fourth handle. B10 as written does not add one.

---

## 1. B3′ — Chapter 15 §3, n_s entry (supersedes B3)

Same OLD block as B3. Only the NEW changes: the Planck significance figure comes out, the P-ACT-LB value goes in, and the chapter says why it is not quoting significances.

**OLD**

```
**n_s = 0.9685 (CMB spectral index) — conditional on K(Φ).** Under the framework's slow-roll reading of the pre-temporal phase, the tilt is 1 − 2/N_e with the e-fold depth N_e ≈ 63.4 fixed by β_NTE — the same constant the central equation runs on, not tuned for the tilt. Planck measures 0.9649 ± 0.0042; the framework's value sits 0.85σ away. The register: the derivation depends on the *kinetic normalisation K(Φ)* — how the boundary field's energy actually varies — which the framework has not derived, and the slow-roll formula's applicability to the pre-temporal section is itself unestablished. The corpus therefore carries n_s as a *conditional survivor*: consistent under a named open assumption, holding reduced predictive credit, explicitly not advanced as a zero-parameter prediction.
```

**NEW**

```
**n_s = 0.9692 (CMB spectral index) — conditional on ξ.** Under the framework's slow-roll reading of the pre-temporal phase, the tilt is 1 − 2/N_e with the e-fold depth N_e = 63.4, fixed by the kinetic normalisation K(Φ) — and K(Φ) is now closed, in the frame the framework works in. There are two anchors to compare against, not one: Planck 2018 gives 0.9649 ± 0.0042, and the P-ACT-LB combination gives 0.9743 ± 0.0034. The corpus shows both rather than choosing, and the reason is plain in the numbers — the two measurements disagree with each other about the tilt by more than the framework's value differs from either of them. No significance figures are quoted here, deliberately: the framework's value depends on the e-fold depth, that depth is under review, and a σ printed today would be wrong by the time the review closes. The register: closing K(Φ) took a conformal coupling, ξ = 1/6, and the *spectral origin of ξ* is open — the framework selects that value on frame-closure grounds, not from the spectral triple. The slow-roll formula's applicability to the pre-temporal section is itself unestablished. So n_s stays a *conditional survivor*: consistent under a named open input, holding reduced predictive credit, explicitly not advanced as a zero-parameter prediction.
```

---

## 2. B10′ — Chapter 15 §6, the grades paragraph (supersedes B10)

Same OLD block as B10. One clause changes in the NEW: the conditional line loses its σ figure.

**NEW** (differs from B10 only in the *Conditional, fuse lit* sentence; the rest is unchanged and reproduced in full so Cursor applies one block)

```
**Passed, at the strictest tier:** κ within 0.83σ of Planck, zero parameters, now backed by the Janus action. **Consistent, at the strictest tier:** θ₂₃ maximal within current precision (inherited, credited); |δ_J| = π/2, with the sign free and the asymmetry's direction therefore not claimed. **Cross-checks passed:** M₁ within a factor 1.1 of the leptogenesis requirement; m_ν₂ within 0.7% of the solar scale on one branch of an open fork — with the branch and the atmospheric overshoot stated in the same breath. **Conditional, fuse lit:** n_s sitting between the two CMB anchors, and r = 0.0053 under every current bound, both resting on ξ = 1/6 with its spectral origin open; and T_GB, pending the fibre-modulus grounding. **By construction, not counted:** H₀ at the cosmic mean; standard BBN recovered (N_eff = 3.044, Y_p = 0.247). **Absences holding:** no WIMP, no fourth generation, no W_R, decade after decade. **Currently losing:** w = −1 against DESI DR2 at about 3.1σ, with nothing internal to absorb it; the atmospheric mass ratio; lithium-7; the asymmetry's magnitude. **Withdrawn — a gap, not a defeat:** the leading-order solar angle. The framework once offered sin²θ₁₂ = 1/3 and no longer does; the algebra does not choose between the candidate values, and on the present reading it does not determine the solar angle at all. That is a hole in the derivation, not a failed test, and a ledger that blurs the two is no use to anyone. All of it sits in Appendix C, at full volume, alongside the open gaps and the pathways under investigation.
```

---

## 3. C16 — Chapter 4, the pre-temporal regime: N_lock's register and the staging

Additional patch to the Ch 4 v9 set.

**OLD**

```
It is, geometrically, a region of e-fold parameter *N* (specifically, *N* less than a value the framework calls N_lock, around 0.1) at which the boundary expansion field has not yet stabilised into a form that produces the well-behaved dt/dN relationship. In this regime, the equation dt/dN is undefined, which means *t* itself cannot be cleanly defined. Only *N* is meaningful.
```

**NEW**

```
It is, geometrically, a region of e-fold parameter *N* below the value the framework calls N_lock, at which the boundary expansion field has not yet stabilised into a form that produces the well-behaved dt/dN relationship. In this regime the equation dt/dN is undefined, which means *t* itself cannot be cleanly defined. Only *N* is meaningful.

Two cautions about N_lock, both of which make the picture more accurate rather than less. First, the locking is not a single instant but the completion of a staged process: the heavier species lock first, quarks by around *N* ~ 10⁻³ and leptons by around 10⁻², with completion by around 10⁻¹. The figure usually quoted for N_lock — about 0.1 — is the end of that hierarchy, not a threshold the universe crosses all at once. Second, the corpus carries N_lock as a *candidate* value pending closure, not as a derived one. The staged picture is the settled part; the number at the end of it is not.
```

---

## 4. D10 — Chapter 5, the field's variability: rebuild the argument without V_NTE

Additional patch to the Ch 5 v8 set. Part 1's reasoning is the potential's *curvature*, which is what actually does the work, and it costs nothing to say it that way.

**OLD**

```
|Φ_NTE| does *not* behave this way. Its potential V_NTE does not lock it at a vacuum expectation value the way V_SM locks the SM Higgs. V_NTE has a different shape — one that the technical corpus develops in detail in the post-locking regime — and its dynamics allow the field to *vary* across cosmic history and across regions of mass-energy density.
```

**NEW**

```
|Φ_NTE| does *not* behave this way, and the reason is worth stating as the framework states it, because it does not depend on knowing the new field's potential in detail. What makes the Standard Model Higgs immovable is the *curvature* of its potential — the wine-bottle floor is steep, and a field sitting in a steep well does not wander. That is a property of V_SM one can point at without knowing anything about the other field, and it is enough on its own: nothing with that curvature could execute an excursion of eight and a half orders of magnitude. Whatever governs |Φ_NTE|'s dynamics, it is not a potential of that stiffness, and its dynamics allow the field to *vary* across cosmic history and across regions of mass-energy density.
```

---

## 5. D11 — Chapter 5, the BBN figure: cross-check register

Additional patch to the Ch 5 v8 set. The number stands; what changes is the claim about where it came from.

**OLD**

```
The cosmic-history variation is one of the framework's central claims, and the magnitude deserves to be felt. Across cosmic time, |Φ_NTE| has evolved along a specific trajectory through V_NTE, with its strength at each cosmic epoch corresponding to the Hubble rate at that epoch through H = β_NTE|Φ_NTE|². At primordial nucleosynthesis — minutes into post-locking history — the field stood at roughly 10^8.5 times its present strength: not a subtle drift but a descent through eight and a half orders of magnitude, delivered smoothly to the present-day Hubble rate of about 67 km/s/Mpc. A field that has done that is a different *kind* of object from a field that has never moved.
```

**NEW**

```
The cosmic-history variation is one of the framework's central claims, and the magnitude deserves to be felt. Across cosmic time, |Φ_NTE| has evolved along a trajectory whose strength at each epoch corresponds to the Hubble rate at that epoch through H = β_NTE|Φ_NTE|². At primordial nucleosynthesis — minutes into post-locking history — the field stood at roughly 10^8.5 times its present strength: not a subtle drift but a descent through eight and a half orders of magnitude, delivered smoothly to the present-day Hubble rate of about 67 km/s/Mpc. A field that has done that is a different *kind* of object from a field that has never moved.

The framework is careful about what that figure is, though, and so should this chapter be. The number is *read off* the expansion history rather than predicted by it: given H at nucleosynthesis and H today, the central equation returns the ratio, and the framework has not derived either endpoint independently. It is a cross-check that the field's required excursion is consistent — and it is the excursion, not the figure, that makes the argument of this section. Eight and a half orders of magnitude is not a prediction the framework is staking anything on. It is the size of the gap between what the cosmology needs and what a locked Higgs can do.
```

---

## 6. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ AC-response revisions to three patch sets** (`Handoff_PC_to_Cursor_AC_Response_Revisions_Ch15_Ch4_Ch5_RATIFIED_20260924.md`, PC, 2026-09-24, Greg-ratified 18:15 NZST). **B3′ and B10′ supersede B3 and B10 in the Ch 15 v4 set** — σ figures removed on AC's instruction (the Companion 17 N_e item would move both anchors within the week); P-ACT-LB 0.9743 ± 0.0034 printed alongside Planck 2018. **C16** added to the Ch 4 v9 set — N_lock demoted to candidate register and reframed as staged completion (quarks ~10⁻³, leptons ~10⁻², completion ~10⁻¹) per Part 1 §VII and Part 3. **D10, D11** added to the Ch 5 v8 set — the forced-addition argument rebuilt on the SM Higgs potential's curvature rather than on a named V_NTE whose form is unverified (H1), and the 10^8.5 BBN ratio regraded as read-off cross-check rather than prediction (H2). Closed with no Book change: N2, F5, N1, F2. Falsifiability item 11 deliberately not carried into Ch 15 — exposure, not handle.
```

---

## 7. Note for AC

Two small things, neither blocking.

**The Ch 15 conditional tier is now the only place in the Book quoting a σ against the inflationary pair, and it no longer does.** If Companion 17's N_e item lands and the anchors move, Chapter 15 needs no repatch — which was the point of B3′. Appendix C's C.2 already handles the depth dependence explicitly (*"at 55 e-folds the pair becomes 0.9646 and 0.0070"*) and also needs nothing.

**H1 is narrowed, not closed.** D10 routes Chapter 5 around V_NTE, so the Book no longer depends on the answer. The corpus question stands on its own: does Companion 9 eq. (1)'s V_NTE have a derived form or an assumed one? That matters for Companion 9 regardless of what the Book says, and PC has removed the Book's stake in it rather than answered it.

---

— PC, 2026-09-24.
