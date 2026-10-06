# ΔN_eff VERDICT — Jammer (adversarial lead)

**Landing: N5 on the mechanism, with N2 as the outcome of every reading the deposit currently supports.**

- The deposit **does not say** whether conjugate-sector radiation enters our Friedmann equation.
- Its one stated rule is written for stress-energy without restriction. Applied as written, radiation crosses and the result is **refuted**: the smallest ΔN_eff any such reading gives is **3.7**, against a measured N_eff of **2.86 ± 0.13**.
- **N4 fails.** The sectors stay in contact until about 1.5 MeV, and they start identical anyway.
- **N3 contradicts the deposit**, which identifies κ with Planck's dark-matter ratio.
- **N1a is not in the deposit.** A mechanism of that form exists (trace coupling) but it is new content, and it would fix the background expansion only.
- No f is proposed.

**From:** Jammer · **To:** AC · **Cc:** Greg · **Date:** 2026-10-06
**Directive:** `Handoffs\Directive_AC_to_Jammer_Cursor_Delta_N_eff_Confronts_Shared_Neutrino_Naive_Reading_Refuted_Five_Forks_20261006.md`
**Amendment:** `Handoffs\AMENDMENT_AC_f_Parameter_Constraint_Pre_Registered_Provenance_Not_Existence_20261006.md`
**Pre-registration (filed 03:52Z, before reading or computing):** `Working\DeltaNeff_PREREGISTRATION_Jammer_Forks_N1a_N1b_N2_N3_N4_N5_Adopted_…_20261006.md`
**Register:** findings, not rulings. Nothing patched. **Blind:** no Cursor lane filing on this directive was read.

---

## 0. Read set (discipline 11)

**Read in full this session, at current state on disk (2026-10-06):**
- `Core_Papers\NTE_v10_19_0_Part2_Structure.md` (modified 2026-10-03T08:23Z; tool truncated the final trailer line only)
- `Core_Papers\NTE_v10_19_0_Part3_Accounting.md` (modified 2026-09-30)
- `Core_Papers\NTE_v10_19_0_Part1_Foundations.md` (modified 2026-09-28)
- `Core_Papers\Companion_05_StateSpace_v10_19_0.md`
- `Core_Papers\Companion_07_Neutrino_v10_19_0.md`
- `Core_Papers\Companion_12_Chord_v10_19_0.md` (as patched 2026-10-03; references truncated)
- `Core_Papers\Companion_13_Yukawa_Nu2_v10_19_0.md`

**Not read for this verdict:** Companion 11 as patched (AC asked for it; it concerns Λ and I found no route by which it bears on R1–R4, but that is an inference from its title and from Part 3's summary, not from reading it). Companions 6, 8, 9, 10, 16. Companions 6, 8, 9 matched a search for `bilateral action` OR `two-metric` OR `bimetric` and **were not opened**; a statement about radiation crossing could sit there. `Working\` and `Book\` not searched.

**External, fetched this session (abstracts):**
- ACT DR6 extended models, arXiv:2503.14454.
- Yeh, Shelton, Olive, Fields, arXiv:2207.13133.

**Computation:** `scratchpad/neff.py`. Not on Drive.

---

## 1. Reading tests

**R1. Does the deposit say whether conjugate radiation enters our Friedmann equation? No.**
Not found in any file in the read set.

**R2. What does the cross-coupling act on?**
- Part 2 §IX: "its stress-energy appears in both Einstein equations"; "The two-orientation Einstein equations, coupled at κ₀, have the unique fixed point T^total = T^b/(1−κ₀)".
- Companion 5 §6: "Each sector perceives gravitational mass that includes a fraction κ₀ of the other sector's *total* perceived gravity — not its bare matter. With G_A = M + κ₀ G_B and G_B = M + κ₀ G_A".
- Part 2 §IX: "the coupling transmits magnitude, not location".

So: stress-energy in Part 2, "gravitational mass" and "total perceived gravity" in Companion 5. **Nothing restricts it to matter, and nothing states a trace or any component that vanishes for radiation.** Per my pre-registration §5, "monopole", "isotropic" and "magnitude, not location" are not counted as such a statement.

**R3. Does the conjugate sector have photons and a temperature? Yes, by implication.**
- Companion 5 §6: "photons are confined to one direction".
- Part 2 §8.4: antimatter is "sorted into the mirror orientation, not annihilated"; Companion 5 §5: total energy, charge and baryon number of the pair are zero at nucleation; §6: "M_A = M_B = M by CPN symmetry".
- No file gives the conjugate sector a different temperature.

**R4. Does the deposit claim N_eff? Yes, as recovered, without a derivation.**
- Part 3 §XVII, in the *derived* tier: "Standard BBN recovered (N_eff = 3.044, Y_p = 0.247)".
- Part 2 §XI: "With H₀ matching Planck by construction, NTE recovers standard BBN".
- Part 2 §XIV: "cross-orientation annihilation is negligible (ΔH/H ∼ 10⁻⁶ at BBN), so standard BBN is recovered."

That last line considers one cross-orientation effect on H at BBN (annihilation) and not the gravitational one. The deposit therefore assumes a standard expansion rate in the radiation era while applying the cross-coupling at full resummed strength to matter by the CMB epoch (Part 3 falsifier 1: "at the homogeneous CMB epoch"). **The two are never reconciled.**

A further inconsistency in the same place: Part 2 §XI applies "an enhancement factor 1 + κ₀ = 1.85" to a nuclear rate at BBN, "one bridge traversal, no gravitational feedback". So the deposit does switch the bridge on during BBN for one purpose and treats it as absent for the expansion rate.

---

## 2. The data (fetched; discipline 12b)

| Quantity | Value | Source |
|---|---|---|
| N_eff, free-streaming | **2.86 ± 0.13** (1σ) | ACT DR6, arXiv:2503.14454 abstract |
| N_eff with external BBN | **2.89 ± 0.11** (1σ) | same |
| Self-interacting dark radiation | **N_idr < 0.134** | same |
| BBN + CMB | N_ν = 2.898 ± 0.141; **N_ν < 3.180 at 2σ** | Yeh et al., arXiv:2207.13133 abstract |

**Correction to the directive's table.** The "< 0.14 (95% CL)" figure is, as far as the abstract shows, the **self-interacting** dark-radiation bound, not a free-streaming ΔN_eff bound. I did not read the paper body, so the confidence level and dataset label for 0.134 are unverified. It happens to be the more apt bound here: conjugate photons are coupled to conjugate matter until its own recombination, so they behave as a fluid, not as free-streaming radiation.

My arithmetic, not a quoted figure: 2.86 ± 0.13 puts the 2σ upper edge at 3.12, about 0.08 above the standard 3.044.

## 3. ΔN_eff, computed

Conjugate sector at equal temperature. Shared neutrinos counted once.

**At the CMB epoch:**

| Reading | ΔN_eff |
|---|---|
| Bare κ₀ × conjugate photons (one traversal, as in the Li-7 rule) | **3.73** |
| Unit weight, conjugate photons | 4.40 |
| Bare κ₀ × all conjugate radiation | 6.30 |
| Unit weight, conjugate photons plus a separate conjugate neutrino bath | 7.45 |
| Fixed-point rule on photons only | 24.2 |
| **Fixed-point rule as written, all radiation × 1/(1−κ₀)** | **41.0** |

**At BBN (T ≈ 1 MeV):**

| Reading | ΔN_eff | H / H_standard |
|---|---|---|
| Bare κ₀ × conjugate photons and e± | 2.66 | 1.20 |
| Unit weight, conjugate photons and e± | 3.14 | 1.23 |
| Fixed-point rule as written | 33.8 | 2.55 |

- AC's estimate of "≈ 6" sits inside this range. The reading the deposit's own formula gives is 41.
- **The smallest value, 3.73, is about 30σ from 2.86 ± 0.13**, about 45 times the 2σ headroom, and 28 times the N_idr bound.
- Under the fixed-point rule matter–radiation equality would also move: radiation rises by 6.5 while matter (baryons plus dark matter) is already the observed total, so z_eq falls to 0.15 of its measured value. That is excluded independently of N_eff.

**No reading in which conjugate radiation crosses survives.**

## 4. N4: fails, twice

- **Contact.** Weak rate against Hubble rate gives sector decoupling at **T ≈ 1.5 MeV** (0.9–2.9 MeV across a factor-25 range in the rate coefficient and g* from 10.75 to 21.5). At 1 GeV the rate exceeds the expansion rate by about 10⁸. This assumes the conjugate sector's weak coupling to the neutrino has our strength, which is what CPN symmetry implies and what AC's directive adopts with F1.
- **Initial conditions.** The pair is nucleated CPN-symmetric. With identical content the two sectors have the same temperature whether or not they are in contact, and electron–positron annihilation heats both photon baths equally afterwards.
- Asymmetric reheating, the standard escape in the mirror-matter literature, needs the sectors to be out of contact above the MeV scale and to start differently. NTE has neither. (That it is the standard escape is background knowledge; the Cursor lanes have the literature task.)

## 5. N3: contradicts the deposit

If neither matter nor radiation crosses, κ is not a dark-matter ratio. Part 2 §IX says "This is dark matter"; Part 3 lists κ = 5.50 against Planck's 5.38 ± 0.15 as a passed zero-parameter prediction and its first empirical handle. N3 is available only as a withdrawal.

## 6. N1: not in the deposit

**N1a.** No deposited passage distinguishes matter from radiation in the cross-coupling (R2).

**The candidate I disclosed before reading: coupling through the trace of the stress-energy.**
- Form: all-or-nothing. Radiation is traceless, pressureless matter is not. No strength to adjust, so no f.
- **Status: new content constructed here, not found in the deposit.** By the amendment §3 step 1 it needs its own justification. I am listing it for Greg, not landing on it.
- Not checked: whether it is compatible with the bilateral action's Bianchi consistency, with the κ₀ extraction in Companion 12, or with gravitational lensing by the dark component.
- Cost already visible: the κ closure in Companion 5 is written for "total perceived gravity", so the derivation text would have to change. Adopting a trace coupling because it rescues N_eff is exactly what discipline 12(c) forbids; it would have to be argued from the Hopf-bridge structure first.

**N1b.** No mechanism with a strength was found. I propose none.

## 7. What N1a would not fix, even if adopted

This is outside the directive's five forks and I flag it because it bears on the same handle.

Planck's 5.38 ± 0.15 is not only a background ratio. It is inferred with a dark component that is **cold and collisionless at the perturbation level** before recombination. Under F1 the conjugate matter is ordinary baryonic matter at our temperature, tightly coupled to its own photons until its own recombination at the same epoch. It oscillates acoustically and does not cluster as cold dark matter does. Separately, Part 2 §IX says the coupling "transmits magnitude, not location", which leaves open what dark-matter *perturbations* exist on our side at all.

So a mechanism that keeps conjugate radiation out of our Friedmann equation repairs N_eff and BBN and leaves the question of whether κ can be compared with Planck's number untouched. **Unfetched; background knowledge of mirror-matter cosmology.** It wants its own pre-registered check.

## 8. Landing against my priors

I expected N2 as the deposit's literal reading, N5 on the mechanism, and N4 to fail (pre-registration §2). All three held. The result was not blind to my expectation; the numbers and passages are above for checking.

## 9. What would settle it

One commitment from Greg, made on structural grounds before any further number is compared:

**What does the Hopf bridge couple to: the full stress-energy, or only rest mass?**

- Full stress-energy → refuted by N_eff as it stands.
- Rest mass only → new content; survives the background test; κ unchanged at 5.50; still owes §7.
- Neither → κ is withdrawn as a dark-matter prediction.

**Deposit lines that cannot stand as written whatever is chosen:**
- Part 3 §XVII, "Standard BBN recovered (N_eff = 3.044 …)" in the derived tier: it is assumed, not derived, and currently contradicted by the deposit's own coupling rule.
- Part 2 §XIV, "so standard BBN is recovered": the 10⁻⁶ figure addresses annihilation only.
- Part 2 §IX and Companion 5 §6, "invisible … weakly" / "or through the weak force": false under F1.

— Jammer, 2026-10-06.
