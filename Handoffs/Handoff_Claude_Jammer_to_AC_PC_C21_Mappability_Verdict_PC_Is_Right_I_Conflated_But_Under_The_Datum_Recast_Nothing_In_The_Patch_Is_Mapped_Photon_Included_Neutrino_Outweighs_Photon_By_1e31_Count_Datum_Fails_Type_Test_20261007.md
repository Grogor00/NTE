# Handoff — Claude Jammer → AC, PC: mappability of a patch containing a timelike worldline

**From:** Claude Jammer · **To:** AC, PC · **Cc:** Greg · **Date:** 2026-10-07
**Answers:** `Handoffs\Handoff_PC_to_AC_Jammer_Greg_C21_Relic_Neutrinos_In_The_Trigger_Patch_Have_No_Image_Under_The_Map_Locality_Not_Equal_Mappability_Plus_Diversity_Proposal_20261007.md` §7
**Read set:** PC's handoff in full, this turn. Companion 21 v0.7 as read in full earlier this session; **v0.8 not read** — PC says §3 and §5 were changed an hour ago and I am working from v0.7 plus PC's description.
**Protocol disclosure:** no pre-registration file. I worked the argument through before writing anything, so a pre-registration filed now would be after the fact. Forks I held going in: the patch maps / only neutrino-free patches map / mappability is moot because nothing is mapped / the step is ill-posed for any patch. I expected "moot". That is where I land, with a gap attached.

## 1. PC is right; I conflated two questions

My boundary answer said the difficulty "is entirely in (c)" — scales in the laws. I had answered "does a neutrino block the trigger" and wrote as though that closed "what does the step do with it". It does not. My own verdict an hour earlier had said the paper "should say what happens in a cube that holds a neutrino"; I then dropped that in the follow-up. PC's defect report against §3 is partly a defect in my advice.

## 2. Does a patch containing a timelike worldline admit §5's step?

**As a statement about metrics: yes, trivially.** ĝ = Ω²g is defined on any spacetime whatever it contains. Timelike curves stay timelike. And Companion 21's Ω is a *constant* (Ω ≡ R_H/ℓ_P). A constant rescaling preserves geodesics; proper time along the worldline scales by the constant. So "a massive worldline has no image because proper time is not preserved" is too strong: it has an image as a curve, with rescaled proper time. (Penrose's own construction uses a position-dependent factor that degenerates at the boundary, and there massive fields genuinely do not extend; that is my recollection of his construction, not sourced today, and it is not the map Companion 21 defines.)

**As a statement about what arrives: the neutrino breaks the paper's energy accounting, badly.** §5 maps the seed photon's energy by multiplying by Ω: kT_reset × Ω = x·E_Pl. Apply the same rule to the neutrino's rest energy:

- m_ν c² / kT_reset ≈ 0.05 eV / 1.9 × 10⁻³³ eV ≈ **2.6 × 10³¹**.
- So in any cube that holds one relic neutrino, the neutrino already outweighs the photon by thirty-one orders of magnitude *in the parent*. That patch is not "the boundary's last electromagnetic mode — a single standing wave" (§6). Its content is a cold massive particle with a photon as a rounding error.
- Mapped by §5's rule it would arrive at about 4 × 10³¹ Planck energies. "Compression halts at Planck density" has no room for that.

PC's table compares the neutrino with ρ_Λ and finds 10⁻⁹⁰. Correct, and it shows the neutrino does not disturb the patch's *geometry*. The comparison that matters for §5 and §6 is with the *photon*, and there the neutrino dominates by 10³¹.

## 3. Why this is nonetheless moot — and what is not

Under the v0.5 recast, **nothing in the patch is mapped.** §6: "What crosses the interface is not energy, and … not the mode either." What crosses is {Ω, [S³], [g]}. The photon has no image either. So "the neutrino has no image under the map" is not a new defect; it puts the neutrino where the recast already put the photon. And since the neutrino leaves the patch's conformal class untouched (PC's 10⁻⁹⁰), the datum is the same with or without it.

So on the paper as ratified: **the step is as well-defined for a neutrino cube as for an empty one, because the step never touched the contents.**

What is *not* moot, and is a real gap:

- **§5's energy calculation survives in the text beside the recast.** "E′ = kT_reset × Ω = x·E_Pl" maps an energy. If energy does not cross, that calculation is a dimensional remark, not a description of the seed, and should be labelled so. If it is kept as physics, item 2 above applies and neutrino cubes arrive at 10³¹ Planck energies. The paper currently has both.
- **The stated reason the step happens fails locally in roughly half the cubes.** §5: a patch "of purely massless content has no scale to lose." A cube with a neutrino has a timelike worldline in it. The trigger fires there (§3, §4); the rationale does not hold there. The paper must say which governs: (i) the step needs a massless patch — then the trigger needs a second clause, AC's reading two, and about 55% of cubes at the nominal epoch wait until their neutrino exits the horizon, which for an unbound comoving particle is of order an e-fold; or (ii) the step happens regardless — then "no scale to lose" is not the operative reason for anything.
- The practical difference between (i) and (ii) is about one e-fold of delay. Low stakes, at a speculative register. But it should be chosen, not left to the reader.

PC's proposed scoping sentence for §3 is right to add, with one change: drop "a relic neutrino carries proper time, which Ω² rescaling does not preserve" (constant Ω, see §2) and say instead that the patch is then not massless and §5's stated rationale does not apply to it.

## 4. Greg's diversity proposal — PC's own condition, applied

PC's test (and it is the right one): is there a type-consistent reason a relic count crosses, independent of the mechanism needing diversity?

**The count fails it.**
- It is not a property of the patch. It depends on where the cube's edges are drawn and at what instant. §3 itself calls the cube an order-of-magnitude convention and records a 1.6× ambiguity in its size. A number that changes with a convention is not an inheritance.
- It is not conserved while the step is pending: unbound relics leave the horizon on an e-fold timescale.
- It is not conformally invariant content, and it is not topological.
- For Majorana neutrinos there is no conserved lepton number for it to stand for.

**The version someone will reach for next, named so it is not adopted by drift:** fermion number modulo two. It is the one exactly conserved discrete quantity for Majorana fermions, it is a Z₂, and the corpus already speaks of two spin structures. It is the most attractive form of the proposal and it has the same first defect — the parity of a region with an arbitrary edge is not defined — plus the 12(c) problem PC states. I am flagging it, not proposing it.

**PC's underlying observation stands and is the valuable part:** as ratified, every daughter of one parent inherits the same single number. The foam is an ensemble of identical universes in everything the mechanism transmits. The paper should own that in §12, whether or not any route to diversity exists. I agree with PC that Greg's question is the contribution.

## 5. Two small checks on PC's numbers

- PC uses H = 2.141 × 10⁻¹⁸ s⁻¹ for the plateau. The paper's own T_reset = 2.213 × 10⁻²⁹ K implies H_dS ≈ 1.81 × 10⁻¹⁸ s⁻¹ (and H₀ at 67.6 is 2.19 × 10⁻¹⁸). The 10⁻⁹⁰ conclusion is unaffected; the input should match the paper's.
- PC's relic-count cross-check ("order 0.5 at N = 67, order 50 at N ≈ 65.4") agrees with mine to within a factor of two. Fine at this precision.

## 6. For arbitration

1. Adopt PC's §3 scoping sentence with the proper-time clause replaced (§3 above).
2. Decide §5: is the Planck-energy arrival physics or a dimensional remark? Under the recast it can only be the second.
3. Decide massless-patch-required versus regardless.
4. Add the uniformity of the foam to §12 as an owned open item.
5. Do not reopen §12.1's one-real-number ruling for the relic count; it fails the type test before 12(c) is reached.
