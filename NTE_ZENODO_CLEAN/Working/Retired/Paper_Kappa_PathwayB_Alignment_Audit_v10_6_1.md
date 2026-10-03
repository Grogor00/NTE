# Paper_Kappa_PathwayB Alignment Audit — v10.6 → v10.6.1

**From:** AC
**To:** AC (own execution, next session) / Greg (manual application alternative)
**Re:** PC flagged in `Chapter_9_outline_v2.md` (§"Tier 3 alignment debt"): `Paper_Kappa_PathwayB_v10_6.md` lines 235, 258, 263, 292, 331 propose the finite-y_ν correction to "the effective S² radius" as the most likely source of the κ residual — directly contradicting master corpus `NTE_v10_6.md` §9.3 (PC's pointer: lines 1249, 1412, 1440), which closes that candidate by extending the topological protection of κ₁ to κ₀ as a whole.
**Corpus baseline:** v10.6 (canonical; shipped 2026-05-03).
**Status:** Audit complete. Five surgical edits identified. Mathematical content untouched throughout. Workflow lesson #18 (full-file replacement) deferred: AC has not seen the full current paper end-to-end via project search; the diff format below lets Greg apply manually in Drive *or* sets up a follow-up session for AC to produce the full updated file. Either path is clean.

---

## 0. Headline finding

The internal contradiction is real and pre-dates the v10.6 ship rather than being introduced by it. Pathway B v10.6's §4 ("Mode-Independence: The Key Result") established the topological protection of κ₁ — κ₁ = Y₀₀ for *any* normalised mode on S² by the constancy of Y₀₀. §4.2 Third consequence then explicitly states that the 0.84σ discrepancy "cannot originate from corrections to κ₁."

But §4.3 ("What the Coupling Does Depend On") leaves a loophole: "The S² has a different effective radius than that set by the unit-S³ Hopf projection." §6.(a) then exploits this loophole: a finite Yukawa y_ν shifts r_eff from 1 to (1 − ε), inflating Y₀₀(r_eff) and shifting κ₀. §6 Assessment, §7.(iv), and §9 Summary point 6 all rest on this candidate.

Master corpus §9.3 closes the loophole. The Hopf projection is from *unit S³* to *unit S²* — a fixed geometric structure determined by the boundary's intrinsic curvature, not by the source field's Yukawa. Finite y_ν changes which Dirac mode the unresolved neutrino occupies; it does not change the projection target's geometry. Combined with §4's mode-independence, this makes ε(y_ν) exactly zero by mathematical identity. The framework's current position (per `Chapter_9_outline_v2.md` §"A note on the residual"): "the framework does not currently identify a positive candidate explanation for the residual."

The five edits below remove the §4.3 loophole and propagate the closure through §6, §7, §9. The paper's main mathematical content (§2 Killing-spinor projection, §3 Gaunt calculation, §4 mode-independence proof, §5 parity selection) is unchanged — those sections already establish the result that closes the loophole.

---

## 1. The five edits

### Edit 1 — §4.3 third bullet ("What the Coupling Does Depend On")

**Current** (third bullet in the "if-then" list):

> *The coupling would be modified if:*
> *— The CPN parity rule is violated (some odd-l coupling leaks through)*
> *— The gravitational coupling has anisotropic corrections (non-zero l=2, l=4 components)*
> *— **The S² has a different effective radius than that set by the unit-S³ Hopf projection***

**Proposed replacement** (drop the third bullet; add a closing sentence):

> *The coupling would be modified if:*
> *— The CPN parity rule is violated (some odd-l coupling leaks through)*
> *— The gravitational coupling has anisotropic corrections (non-zero l=2, l=4 components)*
>
> *The Hopf projection target — unit S² as the base of the unit-S³ Hopf fibration — is fixed by the boundary's intrinsic geometry and is independent of the source field's Yukawa coupling or any internal-mode parameter. Combined with the mode-independence of §4.2, this means the topological protection of κ₁ extends to κ₀ as a whole: finite-Yukawa effects on the unresolved neutrino's S³ wavefunction change which Dirac mode is occupied but do not change the geometric projection or the monopole component of any normalised density on S². The 0.84σ discrepancy must therefore originate in one of the two effects above (parity violation or anisotropic gravitational coupling) or in the observational inputs (§6).*

**Why:** removes the v10.5-era loophole that §6.(a) was exploiting. The loophole conflated two things — the projection target (a fixed geometric S²) and the source field's effective domain (which can shift but doesn't move the projection) — and the v10.6 master corpus §9.3 has resolved the conflation. The new closing sentence states the closure explicitly so that §6 can refer back to it.

---

### Edit 2 — §6 candidate (a) "Finite-y_ν correction" (around line 235)

**Current** (the full §6.(a) paragraph):

> *(a) **Finite-Yukawa correction to the effective S² radius:***
> *This means the neutrino is not completely unresolved — it has a tiny engagement with the Hopf projection. The S² cross-section is not exactly the unit S², but an S² with an effective radius slightly reduced by the Higgs coupling:*
>
> *r_eff = 1 − ε(y_ν)*
>
> *where ε(y_ν) is small. The correction to Y₀₀(S²(r_eff)) relative to Y₀₀(S²(unit)):*
>
> *Y₀₀(r_eff) = 1/√(4π r_eff²) ≈ (1/√(4π)) × (1 − ε)*
>
> *This would reduce κ₀ from 3/√(4π) to 3/√(4π) × (1 − ε), which in the right direction (negative correction). The magnitude of ε from y_ν ~ 10⁻¹² is not computed here but is parametrically small.*

**Proposed replacement** (full paragraph replacement):

> *(a) **Finite-Yukawa correction (closed in v10.6).***
> *Earlier versions of this paper proposed that finite Yukawa coupling shifts an "effective S² radius" r_eff = 1 − ε(y_ν) and thereby corrects κ₀. Master corpus §9.3 (v10.6) closes this candidate: the Hopf projection target is a fixed geometric S² determined by the unit-S³ Hopf fibration, independent of the source field's Yukawa coupling. Combined with §4's mode-independence, ε(y_ν) ≡ 0 as a mathematical identity. Finite-Yukawa effects change which Dirac mode the unresolved neutrino occupies; they do not change the projection geometry or the monopole component of the projected density. Candidate (a) is closed; remaining candidates are (b)–(d) below.*

**Why:** removes the active overclaim. Reframes the candidate as historical-and-closed rather than live future work, preserving the audit trail (§II.0 symmetric-tracking discipline applies).

---

### Edit 3 — §6 Assessment (around line 263)

**Current:**

> ***Assessment:** The most likely source is a combination of (a) (finite y_ν) and (d) (measurement uncertainty). The correction is in the right direction and the right magnitude. A precise computation of ε(y_ν) from the neutrino's partial engagement with the Hopf projection would provide a testable prediction for the residual correction.*

**Proposed replacement:**

> ***Assessment:** Of the four candidates above, (a) is closed by the v10.6 extension of the topological protection (see §4.3 close and §6.(a)). Candidate (b) gives corrections suppressed by m_ν / M_Pl ~ 10⁻²⁸ and is negligible. Candidate (c) contributes at the 10⁻³ level on CMB scales — comparable to the 0.36% κ₀-level discrepancy at the order-of-magnitude level, but no calculation has demonstrated that the contribution carries the right sign or specific magnitude. Candidate (d), measurement uncertainty, has Planck systematic errors at the ~1% level on Ω_b h² and Ω_DM h² from foreground modelling and calibration; this is consistent with the observed 0.83σ (κ-level) discrepancy being measurement noise rather than a structural shortfall. The framework does not currently identify a positive candidate explanation for the residual that survives corpus checks. CMB-S4 will provide ~2× Planck's precision and will resolve whether the residual is a genuine puzzle or measurement noise.*

**Why:** brings the assessment into alignment with the corpus's hardened position (per `Chapter_9_outline_v2.md` §"A note on the residual"). The framework is now honest about not having a positive candidate; (d) is the remaining quiet hypothesis but not asserted as "most likely."

---

### Edit 4 — §7.(iv) "Finite-y_ν correction" (around line 292)

**Current:**

> ***(iv) Finite-y_ν correction:** Compute ε(y_ν) — the correction to the effective S² radius from the neutrino's small but nonzero Higgs coupling. This would predict the residual 0.36% discrepancy in κ if it comes from source (a) of §6.*

**Proposed replacement:**

> ***(iv) [Closed in v10.6]** Earlier versions of this paper named the finite-Yukawa correction ε(y_ν) to an "effective S² radius" as a candidate residual mechanism and a future-work item. Master corpus §9.3 (v10.6) closes this candidate by extending the topological protection of κ₁ (§4) to κ₀ as a whole: the Hopf projection target is a fixed geometric S², not modified by the source field's Yukawa coupling. ε(y_ν) ≡ 0 as a mathematical identity, and (iv) is no longer a live future-work item. Items (i)–(iii) above remain valid future work and are independent of (iv)'s closure.*

**Why:** preserves the audit trail (the framework had this candidate; it has been closed and we say so explicitly) and preserves the §II.0 symmetric-tracking discipline. Items (i)–(iii) — one-loop renormalisation, Majorana propagator on S³ in two backgrounds, parity rule from propagator symmetry — are unaffected and remain genuinely open.

---

### Edit 5 — §9 Summary point 6 (around line 331)

**Current:**

> ***6.** The 0.36% discrepancy cannot be from mode corrections to κ₁ (which is exact). The most likely source is the finite y_ν correction to the effective S² radius, which remains to be computed.*

**Proposed replacement:**

> ***6.** The 0.36% κ₀-level (0.83σ at the κ level) discrepancy is not from mode corrections to κ₁ (exact, §4.2) and is not from finite-Yukawa corrections to the projection geometry (closed in v10.6 by extending the topological protection of §4 to κ₀; see §4.3 close, §6.(a), §7.(iv)). The framework does not currently identify a positive candidate explanation for the residual. CMB-S4's ~2× Planck precision will resolve whether the residual is a genuine puzzle for the framework or measurement noise.*

**Why:** brings the paper's headline summary into alignment with the rest of the post-edit text and with the master corpus position.

---

## 2. What is NOT being changed

For the audit trail:

- **§1 (Setup), §2 (Killing Spinor and Hopf Projection), §3 (Gaunt calculation), §4.1–§4.2 (mode-independence proof and consequences), §5 (parity selection rule):** mathematical content untouched. The result κ₀ = 3/√(4π) and the topological-protection argument are the basis for the closure that this audit propagates; they don't need editing.
- **§6 candidates (b), (c), (d):** unchanged. (b) and (c) are still genuine subleading effects; (d) is still genuine measurement uncertainty. Their relative weights are recalibrated in the §6 Assessment edit (Edit 3) but the candidates themselves stay.
- **§7 items (i), (ii), (iii):** unchanged. One-loop renormalisation, Majorana propagator on S³, parity selection from propagator symmetry — all still genuine future work, untouched by the closure of (iv).
- **§8 Comparison table and conclusion:** unchanged. The post-2026-05-03 framing edit (sequential steps; mode-independence as protection for input/closure structure) is current and correct.
- **Abstract:** unchanged. The corollary in the abstract — "the 0.84σ discrepancy ... cannot originate from corrections to κ₁ — the value Y₀₀ is protected by the triviality of the Gaunt coefficient. The discrepancy must come from elsewhere. Candidate sources are discussed." — is consistent with the post-edit reading. The abstract leaves the candidates open-ended, which is honest under the corrected reading where (a) is closed and (b)/(c)/(d) remain.

---

## 3. Version stamping and changelog

**Recommendation:** the post-edit paper ships at the same `_v10_6` filename (no version increment), with a new preface line recording the alignment patch:

> *v10.6.1 alignment patch (2026-05-06): §4.3 third bullet retired; §6.(a) closed; §6 Assessment recalibrated; §7.(iv) closed; §9 Summary point 6 updated. Closure follows master corpus §9.3 (v10.6) extension of topological protection of κ₁ to κ₀. Mathematical content unchanged.*

The paper still ships as `Paper_Kappa_PathwayB_v10_6.md`. The patch is internal alignment, not a new corpus version, and PC's "alignment debt indicator" reading is satisfied by the in-place edit. (If Greg prefers a `_v10_6_1` filename for cleanliness, that's also fine; AC's call is the in-place option matches the v10.6 ship-history.)

---

## 4. Estimated impact

**Cost (under in-place patch):** Five surgical edits in one paper. ~1 page of total prose touched. No mathematical content modified. Estimated execution time: ~20 minutes including verification of paragraph boundaries.

**Outcome:**
- Paper's §6 / §7 / §9 brought into agreement with §4.2's own topological-protection result and with master corpus §9.3.
- PC's flagged alignment debt closed.
- Chapter 9 prose draft (when authorised) can cite Pathway B v10.6.1 without inheriting the contradiction.
- §II.0 symmetric-tracking discipline preserved (the closed candidate is recorded as closed, not deleted).

**Risk:** Very low. The edits remove an internal contradiction; they don't introduce new commitments. The math is unchanged. The §II.0 symmetric-tracking layer is preserved by recording the candidate-and-its-closure rather than silently deleting the candidate.

---

## 5. Awaiting

Two paths forward; Greg's preference:

**Path A (AC executes next session):** Greg confirms the audit; next AC-active session, AC produces the full updated `Paper_Kappa_PathwayB_v10_6.md` with the five edits applied and the preface alignment-patch line added. Drive replacement; old version deleted by Greg.

**Path B (Greg manual):** Greg applies the five edits manually in the Drive copy. Saves a round-trip; suitable if Greg is at a keyboard and the diffs above are clear enough. The diffs are written for direct copy-paste.

Either path closes the same alignment debt. AC has no preference; the audit memo is the substance.

---

## END-OF-AUDIT FILE OPERATIONS

```
ADD TO PROJECT (new files):
  - Paper_Kappa_PathwayB_Alignment_Audit_v10_6_1.md
    (this audit; specifies the five edits;
     queued for either AC execution next session or Greg manual application)

REPLACE IN PROJECT:
  - None this turn.
  - Paper_Kappa_PathwayB_v10_6.md will be replaced after Path A or Path B executes.

DELETE FROM PROJECT:
  - None.
```

— End audit. AC, 2026-05-06.
