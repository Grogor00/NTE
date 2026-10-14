# Publication readiness: C1, C2, C3 and C6 against the minimal set. VERDICT

Lane: Claude Jammer (lead, adversarial)
Directive: Handoffs\Directive_AC_Publication_Readiness_C1_C2_C3_C6_Against_The_Minimal_Set_20261015.md
Pre-registration: Working\Publication_Readiness_C1_C2_C3_C6_PREREGISTRATION_Claude_Jammer_20261015.md (filed before the reads below)
Blind: I have not read any other lane's readiness filing.
Stake: as declared in the pre-registration. Two of my priors were wrong: C3 (I leaned PF at 0.6) and C2 (I expected the defect to sit at the n=2 non-contextuality gap; it is worse than that). Both are recorded below.

## 0. Read set (full reads this session, current state)

- Core_Papers\Companion_01_Entanglement_v10_19_0.md: modified 2026-10-06; read in full today.
- Core_Papers\Companion_02_BornRule_Hopf_v10_19_0.md: modified 2026-10-06; read in full today.
- Core_Papers\Companion_03_Quantisation_v10_19_0.md: modified 2026-10-06; read in full today. The byte count of my decoded copy (15132) matches Drive.
- Core_Papers\Companion_06_BornRule_GaugeBirth_v10_19_0.md: modified 2026-10-06; read in full today. The byte count matches (20334).
- Cross-checks, also read this session:
  - Companion 16 §1 and §3 (grep plus the earlier full read);
  - Part 1 line 43 (the "earned simplifications" paragraph);
  - closure record v2 (earlier full read).

Minimal set used: M1, the spin-½ state space is S³⊂ℂ²; M2, global U(1) phase is unobservable; M3, SU(2) covariance. Named external inputs: A1 (emergent time / e-fold depth), A5 (the state space is the physical S³ boundary), the Cayley–Dickson descent (graded W-3 in my why-complex-S³ verdict), and the cosmological sector.

Literature I cite from my own knowledge, not read this session, and marked [unverified-session] where used:
- Busch 2003 (PRL 91, 120403): a Gleason-type theorem for POVMs that also holds at d=2.
- Hensen et al. 2015 (Nature 526, 682): electron spins in NV centres.
- Dubois-Violette & Todorov (2018–19): Standard Model group from F₄ ⊃ J₃(𝕆) structure.
- Manning et al. 2015: atom delayed-choice experiment.

---

## C2: "The Born rule is the Hopf fibration". Grade: NOT PUBLISHABLE

This is the hardest test the directive set. §6 grades itself on "inputs already in the standard formalism", and the abstract claims a uniqueness result. The uniqueness claim is false as stated.

**T5-1 (fatal). The qubit uniqueness claim is false.** The abstract says: "the only smooth function from S³ to [0,1] that is simultaneously U(1)-invariant, SU(2)-equivariant, and correctly normalised … is |z|²."
- Counterexample: P(ψ,φ) = sin²(π|⟨φ|ψ⟩|²/2). It is smooth on S³, global-U(1)-invariant and invariant under joint SU(2) rotation of state and axis. It is normalised for every qubit basis, since f(r)+f(1−r) = sin²+cos² = 1. I checked this numerically today.
- A whole family passes, for example f(r) = r + ε·sin(2πr) with small ε.
- The paper names sin²(πr/2) itself (§3.3 Step 2). It then claims the counterexample fails "additivity over higher-dimensional partitions, or … consistency when SU(2) rotates the basis".
  - The second clause is false. P = f(|⟨φ|ψ⟩|²) uses the same f in every basis, so it is identical in all rotated bases.
  - Only the first clause bites. "Higher-dimensional partitions" means leaving the qubit, which is the paper's own subject.
- At n=3, three-outcome additivity forces f linear: f(r₁)+f(r₂)+f(1−r₁−r₂)=1 is Cauchy's equation, and continuity then gives linearity. For sin², r=(0.2, 0.3, 0.5) gives 0.80, not 1.

So the exponent is not selected on S³, nor by the Hopf map. It is selected on S^{2n−1}, n≥3, by non-contextual additivity. That input is not in M1–M3.

**T5-2 (fatal to the title). Non-contextuality is assumed, not emergent.** §6 says: "Non-contextuality emerges as a consequence of the Hopf projection rather than being assumed."
- The step that does the work assumes P depends only on the outcome vector's overlap, through the same f, whatever basis completes it. That is non-contextuality.
- With that assumption added, the argument is Gleason restricted to pure states with the functional form assumed. That is weaker than Gleason, not "less in one respect".
- At d=2 the Gleason-type result needs POVMs (Busch 2003 [unverified-session]). C2 does not use POVMs.

**T5-3. "The exponent is the topological signature of the Hopf map" is wrong.**
- The quadratic comes from the Hermitian norm, which is M1. It does not come from the topology of the bundle.
- §3.4 says "|z₁| fails normalisation … |z₁|² satisfies it". That excludes f = √, not f = sin². Normalisation does not force exponent 2.

**T5-4. Fact 3 is misstated.** It says: "The unique non-trivial principal U(1) bundle over S²". Principal U(1) bundles over S² are classified by c₁∈ℤ. Hopf is c₁=±1, the generator and the only one whose total space is S³. Fix the wording.

**T5-5. The §4 extension uses SU(2j+1), not SU(2).** Full unitary invariance on ℂ^{2j+1} is not M3. The spin-j extension rests on a symmetry larger than rotational covariance.

**T2. Registers.**
- The abstract says the Born rule "has been an axiom without derivation since 1926". §1 says "never been derived". §6 cites Gleason 1957. The paper contradicts itself.
- Part 1 line 43 already classes this result as "Gleason's theorem read on an imported qubit geometry … reformulation". C2 should not claim more than Part 1 grants it.

**T3/T4. Citations and dependencies.**
- §7.2 offers the Cayley–Dickson descent as "the wider framework addresses this". That descent is W-3: circular and selected by observation.
- §7.2 also asserts that G₂ "breaks … to deliver SU(3)_C × SU(2)_L × U(1)_Y". G₂ has rank 2, while the SM group has rank 4. No subgroup of G₂ is isomorphic to the SM group. See §G below.
- §7.2 cites C6 for the "physical mechanism". C6 is graded NP below.

**What survives on M1–M3.** The Layer-1 plus Layer-2 reduction (§3.3) is correct, clean and the paper's best piece. Global phase together with the stabiliser of the measurement axis reduces P to f(|z₁|²). That reduction is valid. Nothing after it is.

**Salvage.** It would be a different paper: a short expository note. Its content would be: "the phase-stabiliser symmetry reduces any qubit rule to f(|⟨φ|ψ⟩|²); at n=2 f is undetermined (a family of counterexamples); at n≥3 non-contextual additivity plus continuity gives f(r)=r".
- Retitle.
- Delete §7.2's descent and G₂ material.
- Delete the C6 dependency.
- Cite Gleason and Busch as the real results.

I expect a referee to judge the novelty near zero. The grade stands: NOT PUBLISHABLE as a research paper.

Prior check: F2b (NP, 0.6) holds, but for a stronger reason than I pre-registered. The qubit claim is not merely incomplete at n=2. It is false at n=2, and the paper's own example shows it.

---

## C1: "There is no pair". Grade: NOT PUBLISHABLE

**T5-1 (fatal). There is no photon frame, and the two detections are spacelike.**
- §1.1 says: "from a photon's own frame, emission and absorption … are the same event."
  - No inertial frame exists at c. Part 1 §I says exactly this (read this session).
  - A null interval separates two distinct events. It does not identify them.
- §2.1 says: "no temporal separation between emission and either detection, nor between the two detections."
  - Two photons emitted back to back reach detectors 2L apart, and those detection events are spacelike separated.
  - No null curve joins them. The "single zero-interval object" is two null segments meeting at the source.
  - The geometry the conclusion needs does not exist.

**T5-2 (fatal). The paper contradicts itself on hidden variables.**
- §2.3 and §3 say outcomes are "jointly fixed by the object's geometry and the detector orientations", with the geometry "fixed at creation".
- Two readings are possible, and both fail:
  - If geometry fixed at creation plus the local setting fixes each outcome, the model is a local hidden-variable model, which Bell excludes.
  - If both settings jointly fix it, the model is a non-local deterministic hidden-variable model, which contradicts "no hidden variables".
- §2.2's "conservation" yields perfect anticorrelation on equal axes only. Local models reproduce that (Bell's own example). Conservation fixes nothing at unequal axes, and the violation lives there.
- "One object" renames non-locality. It does not explain it.

**T5-3 (fatal to the evidence base). The paper's flagship test refutes its own selection rule.**
- Hensen 2015 measured Bell correlations on electron spins in NV centres [unverified-session; widely known]. Electrons are massive, with nonzero proper time.
- The paper cites Hensen as confirming a picture in which entanglement is "natural and robust for zero-proper-time particles and fragile for matter".
- The path-integral argument in §1.2 rests on electron g−2. The electron is again massive, and has a timeline.
- Delayed choice has also been done with atoms (Manning et al. 2015 [unverified-session]).
- The zero-proper-time premise is not what any of the cited evidence depends on.

**T5-4. Formula mismatch.**
- The ontology is photonic, while the formula quoted is the spin-½ singlet's cos²(θ/2).
- Photon polarisation Bell tests follow cos²θ (correlation cos 2θ). Neither formula is derived (§4 item 1 concedes this).
- The twistor claim ("an entangled pair is a single holomorphic line … Bell violations from non-factorisability") is unsourced and unsupported.

**T5-5. Internal inconsistency (minor).** g−2 agreement is given as "one part in 10¹²" in one sentence and "fifteen significant figures" in the next.

**T2. Registers.**
- The "standalone" banner sits beside §5. §5 rests on A1 (e-fold depth as time) and A5 (the universe as a closed S³ boundary).
- §4.4 defers the Born rule to C6.
- "The detection problem dissolves" and "the mystery is self-inflicted" are interpretive claims stated in the register of results.
- There is no engagement with the obvious prior art: transactional and retrocausal interpretations, which share the photon-zero-interval intuition. A referee will ask about it at once.

**M1–M3 trace.** Nothing in C1 uses M1–M3. It is special relativity plus an interpretation. The interpretation's load-bearing premises are T5-1 and T5-2, and both fail.

**Salvage.** None as a physics paper. A popular essay would need T5-1 to T5-3 removed, and those are the argument.

Prior check: F1b (0.55) holds.

---

## C3: "Quantisation is compactness". Grade: NOT PUBLISHABLE (my PF prior is overturned)

**T5-1 (fatal). The thesis is a category error.** It says the spectrum is discrete "because the state space is compact".
- (i) The qubit's state space is the set of points of S³. Laplacian eigenfunctions on S³ are functions on S³, which form L²(S³). That is a different Hilbert space: by Peter–Weyl, the sum over spin-j blocks. §2 Theorem 2 identifies the eigenfunctions correctly as SU(2) matrix elements and then treats them as the qubit's observables.
- (ii) Spectra belong to operators, not to the unit sphere of the Hilbert space.
  - Hydrogen and a free particle share the same Hilbert space L²(ℝ³), with the same unit sphere. Yet one Hamiltonian has a discrete spectrum and the other a continuous one.
  - The unit sphere of an infinite-dimensional Hilbert space is not compact at all. Discreteness cannot come from its compactness.
- §4 "Energy" concedes the mechanism is the potential and normalisability ("effective state space compact"). That is the standard account restated. Known defect (c) is confirmed, and it is worse than "heuristic": it contradicts the thesis.

**T5-2. The oscillator sentence (known defect b) is confirmed, with three errors in it.**
- Unitary equivalence preserves spectra. Ĥ has spectrum ℏω(n+½), while −d²/dθ² on S¹ has n², doubly degenerate, so they cannot be unitarily equivalent.
- n² is not equally spaced.
- S¹ has no intrinsic curvature.
- The true statement: under Bargmann, N̂ = z d/dz. Its spectrum ℕ is that of −i∂_θ restricted to holomorphic modes.

**T5-3. The CCR claim is false.** §5 says: "[x̂,p̂]=iℏ is the operator expression of the symplectic structure of a compact phase space."
- On a finite-dimensional space, tr[x̂,p̂]=0, while tr(iℏ·1)≠0.
- The CCR has no representation on a compact phase space. A compact phase space (for example a torus) gives finite Weyl/clock-and-shift relations, not [x̂,p̂]=iℏ.
- Kostant–Souriau does not say what §5 attributes to it.

**T5-4. §6 makes a false claim and contradicts C2.** §6 says: "the Hopf fibration S³→S² … exists only for S³ among spheres with non-trivial fibrations".
- Hopf fibrations also exist for S⁷→S⁴ and S¹⁵→S⁸.
- Every odd sphere fibres S^{2n+1}→ℂPⁿ with fibre U(1).
- C2 §4 uses exactly S^{4j+1}→ℂP^{2j}.

**T5-5. §6 uniqueness proves too much.** The four criteria (Lie group, parallelisable, associative, 3-dimensional) exclude the state space of every system that is not a qubit. The qutrit's S⁵ is neither a Lie group nor parallelisable. Spin-1 would be forbidden.
- Criterion 4 is stipulated.
- Criterion 3 rests on reading quantum-state composition as octonion multiplication, which nothing in quantum mechanics does.
- Among compact manifolds generally, SO(3), Tⁿ and SU(3) pass criteria 1–3.

**Known defects.**
- (a) Confirmed at §8 ("like Companion 2 it addresses this via the Cayley–Dickson cosmic-phase descent"). The same claim recurs in §6.3, §9 and the correspondence line. All four occurrences are W-3.
- §8's ℏ–radius sentence ("depends on the relation between the S³ radius and the observer's units — cosmological input") needs A5. Taken literally, it implies a time-varying ℏ under expansion; that is not computed and is excluded by prior.
- §3 repeats C2's false uniqueness claim verbatim ("the unique smooth, U(1)-invariant, SU(2)-equivariant map").

**What survives on M1–M3 (plus mathematics).**
- Theorems 1 and 2 are textbook results.
- Angular-momentum spectra from su(2) representation theory are standard. The su(2) structure constants are M3, and the spectrum is rep theory, not compactness of the qubit sphere.
- Neither is new.

**Salvage.** None as stated. With defects (a)–(c) fixed, the thesis itself (T5-1) remains, and fixing T5-1 removes the paper.

Prior check: I pre-registered F3a (PF) at 0.6. The current-state read refutes it. T5-1, T5-3 and T5-4 were not on the known-defect list.

---

## C6: "The Born rule activates at the gauge birth". Grade: NOT PUBLISHABLE

**T5-1 (fatal). It identifies spin with weak isospin.** §3 says: "the stabiliser U(1) is the residual symmetry of the measurement-axis frame within SU(2)_L."
- C2's Layer 2 is the stabiliser of a spin axis. It sits in spatial-rotation SU(2), the Spin(3) of the Lorentz group.
- SU(2)_L is an internal gauge group acting on weak isospin. They are different groups acting on different indices.
- SU(2)_L is also broken by EWSB, yet the Born rule holds today for spin measurements.

**T5-2 (fatal). It identifies global phase with hypercharge.** §3 and §6 say the global U(1) "is U(1)_Y".
- Global phase unobservability (M2) holds for neutral systems (Y=0) and for any state of definite charge, whatever the gauge structure.
- A hypercharge rotation multiplies sectors by e^{iYξ}. That is a uniform phase only within a superselection sector of fixed Y.
- U(1)_Y is broken at EWSB, while M2 is unaffected.
- The thesis "the Hopf fibre is the gauge fibre" is false as stated. Without it, "activation at gauge birth" has no mechanism.

**T5-3. The §8 G₂ claim is false by rank.**
- §8 says: "SM gauge group is therefore forced by 𝕆 plus Janus plus temporal emergence".
- §8 also says U(1)_Y "arises from the complex direction the VEV selects".
- The SU(3) that stabilises e₁ fixes span{1,e₁}. No U(1) inside G₂ commutes with that SU(3).
- See §G.
- The Higgs VEV selecting a direction at gauge birth also places EWSB at the gauge-birth epoch. That is the two-epoch placement already noted for C16.

**T5-4.** §7 says "every Bell experiment" tests cos²(θ/2), and "every confirmation of S=2√2".
- Photon Bell tests test polarisation, which follows cos²θ.
- Measured S values sit below 2√2.
- §7 "Universality" says gauge symmetry "acts identically on all representations". Hypercharge assignments differ between representations, and neutral states carry none.

**Known defect (d) confirmed.** §6 carries "κ = κ₀/(1 − κ₀) = 5.50" and "the measurement-probability rule and the dark-matter ratio share a common geometric origin". §9 repeats "the dark-matter ratio". κ as dark matter is withdrawn in closure record v2. §6's "the neutrino, with minimal coupling, … unresolved" rests on the unresolved-neutrino ontology, which grounds nothing (closure record v2; my U-4 verdict).

**Dependencies.**
- The entire mechanism needs A1 (N_lock ~ 0.1, emergent t) and A5 ("the inner product is computed on the physical S³ boundary").
- §4 imports C1's single-object picture (C1 is NP).
- The pre-temporal claim in §2 ("global phase is not unobservable … a physical operation that changes the state") cannot be tested by construction.

**What survives on M1–M3.**
- §4–5's cos²(θ/2) from d^{1/2}(θ) is textbook, given the Born rule.
- The Dirac spectrum on S³ (±(n+3/2)/r, degeneracy (n+1)(n+2)) is a correct standard result.
- Neither is new.

**Salvage.** None. The thesis depends on T5-1 and T5-2, which are false, and on A1/A5, which are not in M1–M3.

Prior check: F6b (0.8) holds.

---

## Global answer: is there a spine? Yes, and it carries errors, not only assumptions

**1. An internal citation chain.**
- C2's false uniqueness sentence is reproduced verbatim in C3 §3, C6 §3 and C6 §9.
- C3 §6 builds on "exponent 2 is a property of the Hopf fibration, which exists only for S³".
- C6 imports C1's single-object Bell account.
- C1 §4.4 defers the Born rule to C6.
- C2 §7.2 defers mechanism to C6.

None of the four is independent. A referee who breaks C2 §3.3 breaks C3 §3 and C6 §3 with the same counterexample.

**2. An external spine.**
- The Cayley–Dickson descent (W-3) is cited as the answer to "why ℂ" in:
  - C2 §7.2 and §8;
  - C3 §6.3, §8, §9 and the correspondence line;
  - C6 §8.
- A1/A5 carry C1 §5, C3 §8 and all of C6.
- The axiom audit found the quantum core and the cosmology joined only by A5. The four papers are where that join is written into the text.

**3. On M1–M3 alone, the surviving content of all four is standard material:**
- the phase-stabiliser reduction;
- Laplacian spectra;
- su(2) rep theory;
- d-matrix overlaps.

The novel claims are false (C1 T5-1/2; C2 T5-1/2; C3 T5-1/3/4; C6 T5-1/2/3) or rest outside M1–M3.

Grades: C1 NP · C2 NP · C3 NP · C6 NP. The best-placed candidate for a rewrite into a short honest note is C2's phase-stabiliser reduction plus the n=2 counterexample family. I expect it to be judged not novel; I did not run a literature search to confirm that, and it is flagged as the open check.

---

## §G. New finding outside the four papers: the G₂ rank obstruction (flag for AC; not ruled here)

- G₂ = Aut(𝕆) has rank 2 and dimension 14 (standard). SU(3)×SU(2)×U(1) has rank 4.
- No subgroup of G₂ is isomorphic to the SM group, or to SU(3)×SU(2).
- Companion 16 §3 assembles the SM group from factors of two different maximal subgroups:
  - SU(3) = Stab(e₁);
  - SO(4) = Stab(ℍ).
- Their intersection is U(2) (contained in SU(3)), not a commuting product.
- The literature lineage that C16 credits obtains the SM group by different routes:
  - Dubois-Violette–Todorov: via F₄ = Aut(J₃(𝕆)) and S(U(2)×U(3)) [unverified-session];
  - Furey: via ℂ⊗𝕆 / Cl(6) [unverified-session].
- Part 1 line 43 lists "the gauge group from G₂" as a simplification that "earned its place". That entry needs the same test.

Recommendation: AC commissions a dedicated C16 §3 retest. I have not re-read C16 §3 in full today; the excerpt I grepped is quoted above in substance. The rank arithmetic alone settles that "G₂ → SM" as subgroup breaking is impossible. Whether C16 has a defensible non-subgroup reading (for example via J₃(𝕆)/F₄) is the open question.

## Fix list, if Greg wants rewrite stubs rather than withdrawal
- C2:
  - retitle;
  - strike the qubit-uniqueness claims (abstract, §3.3 last paragraph, §3.4 final sentences, §6 "non-contextuality emerges");
  - add the n=2 counterexample family;
  - state non-contextual additivity at n≥3 as an input;
  - fix Fact 3's wording;
  - strike the §7.2 descent and G₂ material;
  - strike "since 1926 / never derived";
  - cite Gleason and Busch.
- C3: withdraw. Optionally keep §2 and §4 "Angular momentum" as background in another paper.
- C1: withdraw.
- C6: withdraw. Under closure record v2, §6 must go regardless.
- C16 §3 / Part 1 line 43: retest (§G).
