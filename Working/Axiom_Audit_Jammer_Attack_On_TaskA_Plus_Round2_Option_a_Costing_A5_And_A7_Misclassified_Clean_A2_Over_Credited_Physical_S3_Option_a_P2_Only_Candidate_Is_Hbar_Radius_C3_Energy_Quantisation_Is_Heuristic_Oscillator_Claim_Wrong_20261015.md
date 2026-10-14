# Axiom audit — Jammer's attack on Task A, and round-2 costing of option (a) — VERDICT (Claude Jammer)

**Date:** 2026-10-15
**Targets:**
- Scratch's Task A, `Working\Axiom_Audit_TaskA_SPECIFICATION_Scratch_nine_axioms_three_fields_each_…_20261015.md` (read in full).
- Round-2 directive, `Handoffs\Directive_AC_Axiom_Audit_Round2_Extract_The_Minimal_Set_From_What_Works_20261015.md` (read in full).

**Pre-registrations:**
- `Working\Axiom_Audit_Task_B_PREREGISTRATION_Claude_Jammer_…_20261015.md`
- `Working\Axiom_Audit_Round2_PREREGISTRATION_Claude_Jammer_Option_a_Physical_S3_Costing_…_20261015.md`

**Read in full at current state:** C1, C2 and C3 (C3 decoded today); C5 (2026-10-11, unchanged since); Parts 1–3.
**Scratch's round-2 minimal set is not yet filed.** Part C below is the attack plan, ready to apply when it is.

---

## Part A — attack on Task A's "licenses / does not license" columns

**Overall:** I agree with A1 (S), A6 (W), the A8 false clause, A3 (clean, with a redundancy candidate) and A9 (hybrid). **I disagree on three classifications**, and in each case the column credits an axiom with work it does not do.

**A5 ("state space IS the physical S³"), classed C, licensing "the Born rule …; quantisation …; entanglement …": wrong.**
- C2 uses S³ as *"the state space of a spin-½ system … This is a definition, not an analogy"*. Its §6 lists its inputs as *"inputs already in the standard formalism"*.
- C3 uses the same unit state space.
- C1 *"requires none of the framework's machinery"*.
- **None of the three uses the identification as a step.** Its working dependents are cosmological (my Task B verdict).
- **Correct class: R for the quantum core, or interpretive.** "Licenses" should list only the closed S³ / Ω_k sign, κ₀ on the physical Hopf base, C6's activation-at-gauge-birth, and C21.
- AC has accepted this in the round-2 directive (§3). Scratch's VERIFY on C5 would have caught it, and it is the reason the verify step exists.

**A7 ("c = boundary expansion velocity"), classed C: wrong.**
- **Zero dependents** in the files read. "Exceeding c is geometrically undefined" is a restatement, not a derivation.
- Its **literal** reading contradicts the deposit: a closed S³ with radius a grows at ȧ = aH, so ȧ/c = a/R_H, and near-flatness needs a ≫ R_H (≳ 20c on Planck's bound; my arithmetic).
- Its **generous** reading (the Hubble sphere) is true by definition.
- Self-scoping disclaimers ("not a speed budget") do not make an axiom clean if it licenses nothing. **Class: R, with a literal-reading inconsistency.**

**A2 (H = β|Φ|²), "licenses … w and Ω_k → 0 as structural consequences; the tie to v_EW": over-credited.**
- **w = −1** rests on the **adopted unimodular treatment** (Part 2 §XIII: *"its support is adopted, not derived"*; C11), not on H = β|Φ|².
- **Ω_k < 0 (sign)** rests on the **closed-S³ topology**, i.e. the physical-S³ / boundary ontology, not on the relation.
- **"Ω_k → 0"** is withdrawn as derived (the flatness explanation, closure record §2.7).
- **The "tie to v_EW"** is a normalisation **chosen** in §2.3 (|Φ|² = v²H/H₀, so that |Φ| = v today by construction).
- **What A2 actually licenses:** the definition of t(N) and H₀ = βv² by construction. **Class: closer to R than U.** The U label suggests a sound law missing a scope line. It is an identity with no independent content, as §2.3 says.

**A8, "licenses … the arrow of time at locking":** the locking criterion y_eff²/(β|Φ|) ≥ 1 is a **rule stated at the point of use**, not a consequence of "embedding ∝ rest energy" (Task B, B2 table). It also uses Φ outside Door B's identity reading. **The column should list the criterion as an adoption, not a licensed derivation.**

**A10 (entanglement as null-time geometry), deferred by Scratch:** C1 states it is standalone and *"adds nothing to this evidence"*. On test (a) it is an interpretation of standard quantum mechanics, not an axiom: removing it breaks no derivation. **Not an axiom.**

## Part B — costing option (a): does any quantum result need *physical* S³?

**Landing: P-2, leaning P-1.**
- **No deposited quantum result needs it.**
- **One deposited sentence implies a consequence that would need it.** C3 §8: ℏ *"depends on the relation between the S³ radius and the observer's units — cosmological input beyond this paper."* A **unit** state-space sphere has no radius, so the sentence only has content under the physical identification.
- **That is the only candidate in the files read.** As written it is a non-derivation (C3 says so).

**Cost of making it a derivation.**
- It would tie the quantum scale to the universe's radius, which grows by e^N, so it predicts a cosmologically varying quantum scale.
- Dimensionless constants that contain ℏ (α = e²/ħc, for example) are bounded very tightly in the laboratory. *I have not computed this or sourced the bounds today.*
- **My prior is that this route is already excluded unless the "observer's units" co-vary.** If they do co-vary, the consequence becomes unobservable, and the identification goes back to being interpretive.
- **Either way it does not obviously deliver the "more than a reformulation" result AC hopes for.** It is worth one pre-registered computation if Greg wants option (a) tested. It is not a lead.

**A structural cost to the identification as worded** (C2 §4–§5):
- "The state space is S³" is true only for a single spin-½ system. Spin-j states live on S^{4j+1} (projectively ℂP^{2j}); a general system lives on S^∞ (ℂP^∞).
- So the physical universe cannot be "the" state space in general, only the state space of one qubit. **Any version of option (a) has to say which state space is identified with physical space, and why that one.** The deposit does not.

## Part C — a caution for extracting the minimal set "from what works"

**C3 is on the "what works" list, but what survives of it is narrower than its title.**
- **Survives (inherited):** angular-momentum spectra from SU(2) representation theory (C3 §4). That is standard; the geometric reading adds no step.
- **Heuristic, not derived:** energy quantisation of bound systems "because the effective state space is compact" (C3 §4). Standard bound-state discreteness is a property of the Hamiltonian on L²(ℝ³). The configuration space is not compact, and C3's own §8 concedes that the spectrum needs the potential and boundary conditions.
- **Wrong as stated:** C3 §4 says the oscillator Hamiltonian *"is unitarily equivalent (via the Bargmann transform) to the Laplacian on a circle S¹, whose eigenvalues n² give the oscillator levels as a shifted version; the equal spacing reflects the constant curvature of S¹."* The S¹ Laplacian's eigenvalues n² are **not** equally spaced. Equal spacing belongs to the first-order generator −i∂_θ (eigenvalues n), restricted to n ≥ 0, i.e. the number operator. *My reading; flag for Scratch to check independently.*
- **Implication for round 2:** extract the minimal set from what C3 actually derives (angular momentum via SU(2), inherited), not from its headline ("quantisation is compactness"). Otherwise the minimal set inherits an unearned commitment.

**Attack plan for Scratch's set, when filed:**
- test (a) on every item;
- the background inheritances (complex Hilbert space, bilinearity, unitarity, SU(2) rotations) must be listed as **inherited**, per C2 §7.1–7.2's own words;
- no mass-sector rule may appear as background (test b).

## Summary for AC and Greg
- **Task A disagreements:** A5 → R / interpretive (in the quantum core); A7 → R with an inconsistency; A2 → identity with no independent content (w and Ω_k sign come from elsewhere); A8's locking criterion → an adoption; A10 → not an axiom.
- **Option (a): P-2.** The only candidate is C3's ℏ–radius sentence, and if derived it predicts a varying quantum scale (prior: excluded). "No quantum result needs physical S³" stands as the expected outcome.
- **C3's surviving content is SU(2) angular momentum (inherited).** Its energy-quantisation argument is heuristic, and its oscillator sentence is wrong as stated.

No f. Nothing patched. Does not reopen the closure.

— Claude Jammer, 2026-10-15.
