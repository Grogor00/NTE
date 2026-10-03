# Working note — Scratch evaluation: Boyle–Finn–Turok, *CPT-Symmetric Universe* vs NTE v10.18.0

**Stream:** Scratch (adversarial verification) · **Date:** 2026-07-05 · **Status:** HIGH-PRIORITY finding; recommended corpus edits (integration + ratify), no tier changes
**Papers:** L. Boyle, K. Finn, N. Turok, *CPT-Symmetric Universe*, Phys. Rev. Lett. 121, 251301 (2018) [PRL] + companion *The Big Bang, CPT, and Neutrino Dark Matter*, arXiv:1803.08930 [BFT-companion]. **Both now in `References/`** (PRL via the 2026-07-05 triage; companion sourced by Greg 2026-07-05).
**Grounded against:** NTE_ZENODO_CLEAN — Part 2 §VIII–§XVI, Part 1 positioning. **Paired with:** Handoff_Scratch_to_AC (2026-07-05).

---

## 0. Placement — and the problem

Boyle–Finn–Turok (BFT) is the **closest published relative to NTE anywhere in the reference library**, and **NTE does not cite it**. That second fact is the finding. NTE Part 2 credits prior art carefully — Foot and Berezhiani (mirror-matter DM), Hassan–Rosen (bimetric), Günaydin–Gürsey / Furey / Todorov–Dubois-Violette (octonions), Wiltshire/Célérier (void-Hubble) — yet the single most obvious cosmological predecessor (a high-profile PRL proposing a universe-antiuniverse pair from the bang with neutrino-sector dark matter) is absent. A referee familiar with the cosmology literature will ask "how is this not Turok's CPT-symmetric universe?" on first read. As written, Part 2's "prior art credited" claim is incomplete precisely where NTE is most exposed.

## 1. What BFT establishes

Taking the radiation-era metric a(τ) ∝ τ seriously and continuing across the bang (−∞<τ<∞) exposes a time-reversal isometry τ→−τ. BFT promote it to a hypothesis: the state of the universe does not spontaneously break CPT; the post-bang universe is the CPT image of the pre-bang one. Consequences: the contracting half is reinterpreted (Stueckelberg — an antiparticle is a particle whose proper time runs counter to embedding time) as an antiuniverse, giving a universe-antiuniverse (U-Ubar) pair from nothing; CPT selects a unique preferred vacuum |0_0> from the family of eta-vacua; late-time observers then see heavy sterile neutrinos "emerging from the bang" (Hawking-like), yielding a sterile-neutrino dark-matter particle of mass 4.8×10^8 GeV stabilised by a Z2 (nu_R1 → −nu_R1); the three light neutrinos are Majorana; the lightest is exactly massless; the other two right-handed neutrinos do leptogenesis; and — from a symmetry argument, no inflation — the growing-mode scalar spectrum with correct CMB acoustic phases is selected while no primordial gravitational waves are produced. The companion (1803.08930) extends the CPT-invariant-vacuum construction and the DM abundance calculation in detail.

## 2. The parallels (structural, point-for-point)

Reframed against NTE §VIII–§X the overlap is not thematic but structural:

- **U-Ubar pair.** BFT: universe-antiuniverse from nothing. NTE §8.4/§XVI: CPN-conjugate Janus pair; the two orientations "occupy the same N-range from opposite directions." Same architecture.
- **Baryogenesis by sorting, not annihilation.** BFT: the asymmetry on one side of the bang is the opposite of the other. NTE §8.4: matter → +N, antimatter → −N, "global baryon number is exactly zero across the Janus pair while our orientation has B>0." Same logic.
- **Bilateral symmetry selects the vacuum.** BFT: CPT picks |0_0>. NTE: CPN selection (Pin− on the Z2 orbifold) + Hartle–Hawking. Same move.
- **Z2 on the neutrino sector does the DM stabilising.** BFT: nu_R1 → −nu_R1 gives a stable sterile neutrino. NTE §IX: resolved fermions Z2-odd, unresolved neutrino Z2-even. Same mechanism class.
- **Majorana neutrinos + leptogenesis; SM-only economy.** Both, and BFT even invokes the Pati–Salam {l_L, nu_R, e_R} ~ {q_L, u_R, d_R} echo — the same Boyle–Farnsworth Jordan-geometry line already in the library.

## 3. Where NTE is genuinely distinct (reframed through NTE axioms)

Yes, NTE is distinct — on five axes, one decisive:

**(1) Arrow of time across the mirror (C5) — the clean separator.** BFT's mirror IS a time reversal: τ→−τ is the isometry, the antiuniverse is Stueckelberg-reversed, and BFT state the thermodynamic arrow points away from the bang in both directions — two opposite arrows. NTE's C5 asserts the opposite: CPT = Θ∘CPN, and emergent proper time Δt runs the SAME direction in both CPN-conjugate halves — no reversed-T mirror. NTE's mirror lives in the CPN (charge + antipodal-on-S³) structure and in N-orientation, not in the proper-time arrow. *Corpus caveat:* NTE's own phrase "occupy the same N-range from opposite directions" flirts with BFT's picture; Part 2 must make explicit that "opposite directions" is CPN orientation, not the proper-time arrow, or the distinction blurs.

**(2) Dark matter: geometric coupling vs particle.** BFT predicts a particle — a sterile neutrino of definite mass (4.8×10^8 GeV), abundance from CPT-vacuum Bogoliubov coefficients. NTE predicts a ratio — κ = 5.50 from the Hopf–Y00 projection — with DM as the gravitational footprint of mirror-orientation matter through the Z2-even neutrino, "purely gravitational/geometric (no kinetic mixing)." Same Z2-neutrino trigger, different output. NTE is BFT-in-cosmological-architecture, Foot–Berezhiani-in-DM-type, distinct from both.

**(3) Inflation.** BFT is explicitly anti-inflation and predicts no primordial gravitational waves (r=0) from the CPT boundary condition. NTE retains a Hartle–Hawking inflationary sub-phase and carries a conditional r ≈ 4×10^-3. A genuine, testable fork. (Research opening, not a claim: since NTE's n_s/r are already conditional on the open K(Φ), BFT's symmetry-based perturbation selection is a live alternative NTE could weigh.)

**(4) Substrate.** BFT: ordinary continued 4D flat FRW; the bang is a topologically-enforced Weyl singularity (a odd, a∝τ). NTE: boundary-only S³×S¹, count coordinate N, octonionic, t = i·ΔN, gauge birth a Euclidean→Lorentzian signature change (C¹ kink), not a singularity. Different ontology entirely.

**(5) Fingerprints.** BFT: lightest neutrino exactly massless; sterile-neutrino DM mass. NTE: κ=5.50, δ_J=π/2, DM variance σ ∝ M^-1/2. Non-overlapping observational predictions.

## 4. Adversarial flag

Because the overlap on §8.4 (baryogenesis) and §IX (the Z2-neutrino DM trigger) is so tight, a skeptical reader could read those sections as a geometric re-dressing of BFT. NTE's defence is real — same-arrow C5, geometric κ-ratio DM, N-ontology, retained inflation — but that defence currently exists only in this analysis, not in the corpus. Citing BFT and drawing the distinctions converts a latent priority problem into a clean demonstration that NTE is a distinct framework sharing a cosmological skeleton. This strengthens NTE; omitting it weakens it.

## 5. Verdict

Distinct — and a HIGHER-priority citation than CFL, because it is a credibility/priority issue rather than a positioning nicety, and it touches NTE's flagship bilateral-CPN cosmology. Recommended corpus action (all in the paired handoff, drafted for AC): (1) cite BFT (PRL + companion, both already in References/) in Part 2 §8.4 and §IX as the closest bilateral-cosmology prior art, alongside the Foot/Berezhiani and Hassan–Rosen credits already present; (2) add a short distinction paragraph on the five axes, led by C5 (same-arrow vs two-arrow); (3) add BFT to the Part 1 positioning family; (4) disambiguate the "opposite directions in N" phrasing. No tier changes — the distinctions are already true in the corpus; they need to be stated. Recommend this lands before any Zenodo re-deposit.

— Scratch, 2026-07-05
