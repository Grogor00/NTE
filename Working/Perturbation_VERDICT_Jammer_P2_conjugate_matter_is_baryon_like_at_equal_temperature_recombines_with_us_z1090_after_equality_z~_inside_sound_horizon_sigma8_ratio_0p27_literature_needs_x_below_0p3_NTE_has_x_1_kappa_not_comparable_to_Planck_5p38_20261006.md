# Perturbation-level VERDICT — Jammer (adversarial lead)

**Landing: P2.** Under the shared-neutrino reading with CPN-symmetric initial conditions, the conjugate sector's matter is baryon-like through the whole epoch in which Planck's dark-matter ratio is fixed. **κ = 5.50 is not comparable with Planck's 5.38 ± 0.15, whatever the bridge carries.**

- The conjugate sector recombines when we do, at z ≈ 1090. Matter–radiation equality is at z ≈ 3490. So its matter is pressure-supported for the entire interval in which cold dark matter does its growing.
- Inside the sound horizon at recombination the matter density contrast is **2% to 12%** of the cold-dark-matter reference, and the gravitational potential likewise. The implied σ₈ is about **0.27** of the reference.
- The mirror-matter literature (fetched) allows mirror baryons to be all the dark matter only for a temperature ratio x ≲ 0.3 and excludes x > 0.5 even for a small mirror fraction. NTE under this reading has **x = 1**.
- There is a P4 component (what "magnitude, not location" means), but **it does not change the landing**: the alternative reading is further from cold dark matter, not closer.
- No f introduced.

**From:** Jammer · **To:** AC · **Cc:** Greg · **Date:** 2026-10-06
**Directive:** `Handoffs\Directive_AC_Perturbation_Level_Check_Does_Conjugate_Sector_Supply_What_Planck_Measures_Four_Forks_20261006.md`
**Pre-registration (filed 04:05Z, before reading or computing):** `Working\Perturbation_PREREGISTRATION_Jammer_Forks_P1_P2_P3_P4_Adopted_Model_And_Quantities_Declared_Before_Reading_Or_Computing_Prior_P2_Disclosed_20261006.md`
**Register:** findings, not rulings. Nothing patched. **Blind:** no Cursor lane filing on this directive read.

---

## 0. Read set (discipline 11)

**Read in full this session, at current state (2026-10-06):**
- `Core_Papers\Companion_11_Lambda_v10_19_0.md` (as patched; final reference line truncated by the tool)
- `Core_Papers\Companion_06_BornRule_GaugeBirth_v10_19_0.md` (final sentence truncated)
- `Core_Papers\Companion_08_VNTE_Trajectory_v10_19_0.md`
- `Core_Papers\Companion_09_VNTE_Stage3_v10_19_0.md`
- Earlier today, unchanged since: Parts 1, 2, 3; Companions 5, 7, 12, 13.

**Not read:** Companions 1–4, 10, 14–18, 20, 21. `Working\` and `Book\` not searched.

**External, fetched this session:** Berezhiani, Ciarcelluti, Comelli, Villante, *Structure formation with mirror dark matter: CMB and LSS*, arXiv:astro-ph/0312605, PDF through a summarising fetch. Quotations below are as that tool returned them; **not read line by line.** The paper is from 2003; later data can only have tightened its limits, but I did not fetch a later bound.

**Computation:** `scratchpad/pert.py`. Not on Drive.

---

## 1. Reading tests (pre-registration §5)

**S1. What the bridge carries.** No statement in Companions 6, 8, 9 or 11.
- Companion 9 §1: the Hubble rate is fixed "from the Einstein equation with ordinary stress-energy", and "⋯ denotes bilateral / portal structure deposited elsewhere that does **not** replace Einstein–Hilbert gravity".
- Companion 6 §6: κ's closure rests "on the bilateral two-metric action whose completion Part 3 lists as open".
- So the companions that matched my bilateral/bimetric search point back to Part 2 §IX and say the action is incomplete. They add nothing on matter versus radiation. **The ΔN_eff landing (N5 on mechanism) is unchanged.**

**S2. Perturbations or only homogeneous magnitude.** Only two passages bear on it, both read earlier today:
- Part 2 §IX: "the coupling transmits magnitude, not location", with the two structures decorrelating "to ∼10⁻³ by z∼0".
- Companion 5 §6: "Both sectors share the same Janus seed … but their large-scale structures do not stay correlated".
- "Do not stay" and "by z∼0" imply they begin correlated. Neither passage says what our metric sees of conjugate perturbations at the linear stage.

**S3. Conjugate temperature, recombination, clustering.** Not stated anywhere in the read set.

**Companion 11 as patched.** Confirms what AC reported: adopted, CCM as candidate. Reference 4 still reads "Mimetic dark matter arises automatically with that construction". Nothing in it bears on this question.

---

## 2. Conjugate thermal history

CPN-symmetric start, same microphysics, same baryon-to-photon ratio in magnitude, equal temperature (ΔN_eff verdict §4).

| Quantity | Conjugate sector | Note |
|---|---|---|
| Recombination | z ≈ 1090, same as ours | Source formula: "1 + z′_dec ≃ x⁻¹(1 + z_dec)"; x = 1 |
| Matter–radiation equality | z ≈ 3490 | from κ = 5.50 and standard radiation |
| Pressureless by equality? | **No.** Coupled to its photons until z ≈ 1090 | |
| Sound horizon at recombination | ≈ 144 Mpc (k ≈ 0.022 Mpc⁻¹) | computed |
| Silk damping scale | k_D ≈ 0.2 Mpc⁻¹ (crude; ours is about 0.14 from background knowledge) | same as ours by symmetry |

**Answers to the directive's four specifics:**
- *Acoustic oscillation instead of cold collapse:* yes, on all scales inside 144 Mpc.
- *Silk damping:* yes; it erases the conjugate footprint below roughly 30 Mpc.
- *Early enough recombination to be cold:* no. It would need to recombine well before equality, which requires x ≲ 0.3. Here x = 1.
- *Visible in our acoustic peaks, already excluded:* see §4.

---

## 3. The computation

**Setup, as pre-registered.** Two universes with identical backgrounds (Ω_b h² = 0.0224, total matter 6.5 × baryons, standard radiation). Reference: dark part cold and collisionless. Model: dark part is a copy of the baryon–photon fluid with the same initial perturbation, released at z = 1090. Conjugate photons do **not** gravitate here (that is the rest-mass-only assumption, the most favourable case).

| k (Mpc⁻¹) | Matter contrast at decoupling, model ÷ reference | Potential at decoupling, model ÷ reference |
|---|---|---|
| 0.005 | 0.99 | 1.00 |
| 0.01 | 0.94 | 0.98 |
| 0.02 | 0.59 | 0.77 |
| 0.05 | −0.12 | −0.20 |
| 0.1 | 0.02 | 0.02 |
| 0.2 | 0.06 | 0.09 |
| 0.5 | 0.04 | 0.06 |
| 1.0 | −0.02 | −0.03 |

Negative entries are oscillation phase, not error. **σ₈, model ÷ reference: 0.27.**

**Against the decision rule fixed in advance:**
- P1 needed all ratios within 10% of 1. Fails from k ≈ 0.02 upward.
- P3 needed the departure confined to k above about 0.3. It starts at 0.02.
- **P2** needed ratios below one half inside the sound horizon. Met by a wide margin.

**Method limits.** Tight-coupling fluid, neutrinos lumped with radiation, no anisotropic stress, Silk damping applied as a factor and not evolved. The σ₈ figure and the individual ratios are good to a factor of order two at best; the late-time transfer at k above 0.2 is unreliable and I have not tabulated it. The size of the effect is a factor of ten to fifty, so the discrimination between P1 and P2 does not depend on that precision. **This is not a likelihood against Planck and I do not claim one.**

---

## 4. Literature (fetched)

From arXiv:astro-ph/0312605, as returned by the fetch:
- "the assumption that DM is entirely due to mirror baryons is evidently not compatible with present LSS data unless the value of x is enough small: x ≤ x_eq ≈ 0.3"
- "High values of x, x > 0.5, can be excluded even for a relatively small amount of mirror baryons."
- "For small values of x, say x < 0.3, neither the linear LSS power spectrum nor the CMB angular power spectrum can distinguish the MBDM from the CDM."
- BBN: "the conservative bound ΔN_ν < 1 implies that x < 0.64".

So the case NTE lands in, all of the dark matter as mirror baryons at x = 1, is inside the region that paper excludes on 2003 data. That matches my own calculation in direction and in order of magnitude.

---

## 5. The P4 component, and why it does not rescue P1

The deposit does not say whether our metric sees conjugate perturbations or only the conjugate mean density. The two readings:

- **Perturbations cross (the model above).** Baryon-like footprint. P2.
- **Only the homogeneous magnitude crosses.** Then the dark component on our side is smooth and does not cluster at all. Our baryons are 15% of the matter, and with the rest unclustered the growth law weakens from δ ∝ a to about δ ∝ a^0.29. That is further from cold dark matter than the first reading. P2, more strongly.

A third possibility, that conjugate matter clusters *independently* and cold, has no support: nothing in the deposit makes it cold, and §2 shows it is not.

**The commitment the deposit has not made** (the P4 item, for the record): what the bridge transmits at the linear stage. It should be stated, but neither answer gives P1.

---

## 6. Consequences

1. **κ's Planck comparison does not stand.** Part 3 lists "κ = 5.50 vs observed 5.38 ± 0.15 — 0.83σ, passed" as a zero-parameter prediction and as empirical handle (i). The observed number is extracted assuming a component that is cold and collisionless before recombination. Under the shared-neutrino reading the conjugate matter is not that component. The 0.83σ is a comparison of unlike quantities.
2. **This holds for both of Greg's bridge options.** Rest-mass-only repairs N_eff and leaves this untouched; I assumed it in §3 and still land on P2.
3. **What would have to be true for P1.** The conjugate sector would have to be much colder than ours (x ≲ 0.3), or its matter would have to be non-baryonic and collisionless. The first is closed by the ΔN_eff verdict §4 (thermal contact to 1.5 MeV and a symmetric start). The second contradicts CPN symmetry and Part 2 §8.4.
4. **What survives.** κ₀ = 3/√(4π) and the closure κ₀/(1−κ₀) as mathematics. What is lost under this reading is the identification of that number with Ω_DM/Ω_b as measured.

**Under discipline 12(a) and (c):** the response to this is to restate or withdraw the handle, not to look for reasons to doubt the mirror-matter literature or to add a mechanism that cools the conjugate sector by the amount needed.

## 7. Where the pressure actually sits

Both today's verdicts trace to one step: reading the Z₂-even neutrino as a field the conjugate sector's weak force couples to at our strength (F1), with a CPN-symmetric conjugate sector made of ordinary matter. If that step is right, κ is neither a viable radiation history nor a cold-dark-matter ratio. The steps upstream of it are the deposit's own (Part 2 §IX, §8.4, §8.5; Companion 5 §5–6; Companion 7 §7), so I do not see a place to stand inside the current text. Greg's structural choice is therefore larger than "what does the bridge carry": it is **what the conjugate sector is made of and whether it is a thermal copy of ours at all.**

## 8. Landing against my prior

I expected P2 with a P4 component (pre-registration §2). Both held. Not blind; numbers and passages are above.

— Jammer, 2026-10-06.
