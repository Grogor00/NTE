#!/usr/bin/env python3
"""Apply PC Package E2 + E3 patches (Cursor PC)."""
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop")
CH12 = ROOT / "Book/Chapter_12_The_Chord_v3_1.md"
CH15 = ROOT / "Book/Chapter_15_The_Score_v2.md"
CH9 = ROOT / "Book/Chapter_9_The_Number_That_Could_Have_Failed_v3.md"

E2_1_OLD = """## The Fifth Note: The Spectral Index

The fifth note of the chord is the strangest to introduce, because what it describes is hard to see and easy to misstate, but it's also one of the framework's sharpest empirical commitments. The note is called the *spectral index*. It's a single number — measured to be 0.9649, with an uncertainty of ±0.0042, by the Planck satellite's observations of the cosmic microwave background. The framework predicts it lands at 0.9685, with no parameters tuned. The match is within roughly one standard deviation of the measurement.

What is the spectral index?

The early universe was not perfectly smooth. If it had been, every part of it would have evolved the same way, and the universe today would be a uniform soup of particles with no galaxies, no stars, no structure. What allowed structure to form was the presence of tiny ripples — small variations in density from place to place that, after enough cosmic expansion, gravity amplified into the cosmic web of galaxies and clusters we observe. The cosmic microwave background, the oldest light in the universe, carries the imprint of these ripples directly.

The ripples have a pattern. At larger physical scales — across vast stretches of the early universe — the variations have a slightly different amplitude than at smaller scales. The spectral index measures this difference. A spectral index of exactly 1 would mean the ripple amplitudes are the same at every scale, large or small — a perfectly "scale-invariant" pattern. The observed universe has a spectral index slightly below 1, meaning larger scales carry slightly more power than smaller scales. The exact value — how far below 1 — is what cosmologists measure and what theories of the early universe try to predict.

For most theories of the early universe, the value of the spectral index is something to be fit. You adjust the parameters of your model until the prediction matches the observation, and you call the model successful when the fit is good. The framework doesn't have this freedom. The number 0.9685 emerges from a specific count.

The count is the number of e-folds — the number of doublings of cosmic radius — during the universe's pre-temporal phase, the regime Chapter 4 introduced as the time before time. During this phase, the universe's expansion was already underway, but the structure that allows time to emerge had not yet settled into the form that gives rise to ordinary physics. The framework's mathematics says that the spectral index depends on how many e-folds this phase ran for, through a simple relationship: the spectral index equals one minus two divided by the count. The framework's broader programme has previously identified the count: about 63.4 e-folds, set by the same constant β_NTE that fixes the boundary expansion field's relationship to the Planck mass. The same β_NTE that appears in the central equation H = β_NTE|Φ_NTE|² also fixes the spectral index. One number does double duty. The result, plugged into the formula, is 0.9685.

A careful reader may notice that the gauge birth — the moment Chapter 7 develops — carries its own e-fold language: a holographic width of about one-tenth of an e-fold at locking, quite separate from the sixty-three used here. The framework's resolution is that the pre-temporal epoch is not one story told in one register. The ripple pattern that sets n_s is counted in one register — the slow roll where the dominant pattern resolves. The constraint lock that connects the Planck-scale configuration to gauge birth is another. Confusing the two created a false tension; keeping them distinct is part of the honest account. **About sixty-three e-folds is not about one-tenth of an e-fold.** The long count sets the tilt; the short count is the width of the locking transition itself — the chord's attack, not the song's length.

The note has two pieces of honesty attached to it.

The first is the structural one. The framework's prediction is that the dominant pattern in the pre-temporal action delivers 0.9685 — and two independent routes now land on the same formula: a long pre-temporal slow-roll phase and a separate e-fold count from the same depth. One tilt, one geometry, read two ways. The match with Planck (roughly 0.85 standard deviations) is unchanged. What remains open is precision cosmology tightening the observation further — not a free parameter hiding in the framework.

The second is the falsification one. If future cosmological surveys — CMB-S4 ground-based observations, the LiteBIRD satellite — tighten the spectral index measurement to about ±0.001 while keeping the central value near 0.9649, the framework's 0.9685 prediction would sit more than two standard deviations from observation, and the note would be wrong. The framework would have to either revise the dominant pattern of the pre-temporal phase or accept that the spectral index, unlike κ, is not derivable from the universe-instrument's geometry without further parameter input.

This makes the spectral index the closest sibling κ has in the chord. Both are zero-parameter cosmological predictions that the geometry produces and observation has so far confirmed. κ at 0.83 standard deviations; the spectral index at roughly one. Both are exposed; both could fail; neither has been adjusted to match. The instrument plays both notes, and so far observation has registered both notes at the pitches the geometry sets."""

E2_1_NEW = """## The Fifth Note: The Spectral Index

The fifth note of the chord is the strangest to introduce, because what it describes is hard to see and easy to misstate, but it's also where the framework's honest scope earns its keep. The note is called the *spectral index*. It's a single number — measured to be 0.9649, with an uncertainty of ±0.0042, by the Planck satellite's observations of the cosmic microwave background. The framework's structural reading lands at 0.9685 under a specific assumption about the pre-temporal phase that the section will name plainly. The match with Planck sits within roughly one standard deviation; the assumption — and what it means that the assumption is open — is the work of the section.

What is the spectral index?

The early universe was not perfectly smooth. If it had been, every part of it would have evolved the same way, and the universe today would be a uniform soup of particles with no galaxies, no stars, no structure. What allowed structure to form was the presence of tiny ripples — small variations in density from place to place that, after enough cosmic expansion, gravity amplified into the cosmic web of galaxies and clusters we observe. The cosmic microwave background, the oldest light in the universe, carries the imprint of these ripples directly.

The ripples have a pattern. At larger physical scales — across vast stretches of the early universe — the variations have a slightly different amplitude than at smaller scales. The spectral index measures this difference. A spectral index of exactly 1 would mean the ripple amplitudes are the same at every scale, large or small — a perfectly "scale-invariant" pattern. The observed universe has a spectral index slightly below 1, meaning larger scales carry slightly more power than smaller scales. The exact value — how far below 1 — is what cosmologists measure and what theories of the early universe try to predict.

For most theories of the early universe, the value of the spectral index is something to be fit. You adjust the parameters of your model until the prediction matches the observation, and you call the model successful when the fit is good. The framework's reading doesn't have this freedom in the usual sense — no parameter has been tuned to make 0.9685 come out. But the framework's reading does rest on a specific structural choice about the pre-temporal phase that, at the current state of the corpus, is not itself derived from first principles. The 0.9685 number depends on that choice; under a different choice, the framework's natural pre-geometry would deliver a spectral index of exactly 1 — badly off from observation. Naming the choice honestly is part of what the chapter owes the reader.

The structural choice is the *slow-roll reading of the dominant pre-temporal pattern* — a specific identification of how the boundary expansion field's energy varies across the pre-temporal epoch, in which the dominant ripple pattern resolves slowly across many e-folds rather than rapidly. Under that reading, the framework's mathematics gives a simple relationship: the spectral index equals one minus two divided by the e-fold count of the slow-roll phase. The framework's broader programme has identified the count: about 63.4 e-folds, set by the same constant β_NTE that fixes the boundary expansion field's relationship to the Planck mass. The same β_NTE that appears in the central equation H = β_NTE|Φ_NTE|² also fixes the count. Plugged into the formula under the slow-roll reading, the result is 0.9685. The question the framework can answer cleanly is *given the slow-roll reading*, what does the e-fold count produce. The question the framework cannot yet answer is whether the slow-roll reading is forced by deeper geometric structure — that derivation is open work the broader programme continues.

A careful reader may notice that the gauge birth — the moment Chapter 7 develops — carries its own e-fold language: a holographic width of about one-tenth of an e-fold at locking, quite separate from the sixty-three used here. The framework's resolution is that the pre-temporal epoch is not one story told in one register. The ripple pattern that sets n_s is counted in one register — the slow roll where the dominant pattern resolves. The constraint lock that connects the Planck-scale configuration to gauge birth is another. Confusing the two created a false tension; keeping them distinct is part of the honest account. **About sixty-three e-folds is not about one-tenth of an e-fold.** The long count sets the tilt; the short count is the width of the locking transition itself — the chord's attack, not the song's length.

The note has two pieces of honesty attached to it.

The first is the structural one. *Within* the slow-roll reading, the framework's account is clean: no parameter has been tuned to make 0.9685 come out, the e-fold count comes from β_NTE which appears already in the central equation, and the match with Planck (roughly 0.85 standard deviations) is not the result of fitting. The cleanness of the *match* is real. What is not yet clean is the *derivation* of the slow-roll reading itself — the framework currently identifies it as the natural reading the pre-temporal phase invites, but a first-principles geometric forcing of that reading remains open. The note is, in the framework's honest scope, consistent at clean tier without yet being derived from first principles.

The second is the falsification one. If future cosmological surveys — CMB-S4 ground-based observations, the LiteBIRD satellite — tighten the spectral index measurement to about ±0.001 while keeping the central value near 0.9649, the framework's 0.9685 reading would sit more than two standard deviations from observation, and the note would be wrong. The framework would have to either revise its identification of the dominant pattern in the pre-temporal phase or accept that the spectral index is not derivable from the universe-instrument's geometry under the framework's current reading. Either outcome is a structural admission, and the precise nature of the open assumption — the slow-roll identification — makes the failure mode specific rather than vague.

This is what distinguishes the spectral-index note from the dark-matter note in the chord's structure. The dark-matter ratio's derivation in Chapter 9 runs from the framework's geometry to a definite number through algebraic steps each of which is structurally exact at its register. The spectral-index note runs from the framework's geometry to a definite number through a structural identification — the slow-roll reading — which the framework has not yet derived. Both notes are at clean tier in the same calibration sense: no observational input fed either derivation chain. Both sit within their measurement's stated uncertainty. The dark-matter note is closer to derived; the spectral-index note is closer to consistent. The chord plays both notes at the pitches the framework's geometry produces; whether one of them turns out to depend on an assumption the framework can later derive, or remains an open structural choice that observation eventually settles, is among the things the next decade will reveal."""

REPLACEMENTS = [
    (CH12, E2_1_OLD, E2_1_NEW, "E2-1"),
    (CH12,
     "The spectral index sits at its specific value because the count of pre-temporal e-folds the geometry demands fixes it.",
     "The spectral index sits at its specific value because the count of pre-temporal e-folds, set by β_NTE, fixes it under the framework's slow-roll reading of the pre-temporal phase.",
     "E2-2"),
    (CH15,
     "On scope: six chord slots — κ, gauge-birth temperature, inflation tilt, leptogenesis and Majorana scales, Λ, and the comoving-volume audit — read from one heat-kernel computation on the spectral triple. κ, n_s, and m_{ν₂} are clean-tier: no observational input in the derivation chain. Λ now stands as structural quietness — the framework's account of why empty space is not catastrophically loud — but its specific numeric route was retired during the framework's 2026 internal review; Chapter 13 explains why, and what the closure now claims and does not claim at the present register. The rest of the chapter is the scorecard.",
     "On scope: six chord slots — κ, gauge-birth temperature, inflation tilt, leptogenesis and Majorana scales, Λ, and the comoving-volume audit — read from one heat-kernel computation on the spectral triple. The clean-tier label — no observational input fed into the derivation chain — applies cleanly to κ and m_{ν₂}. n_s sits at clean tier in the same calibration sense (no feedback from observation into the derivation) but its 0.9685 value depends on a structural choice — the slow-roll reading of the pre-temporal phase — that the framework has not yet derived from first principles; Chapter 12 develops the distinction between clean (in the calibration sense) and derived (in the first-principles sense). Λ now stands as structural quietness — the framework's account of why empty space is not catastrophically loud — but its specific numeric route was retired during the framework's 2026 internal review; Chapter 13 explains why, and what the closure now claims and does not claim at the present register. The rest of the chapter is the scorecard.",
     "E2-3"),
    (CH15,
     "**n_s = 0.9685 (CMB spectral index).** Chapter 12's ripple register: pre-temporal pattern resolution plus the e-fold depth from β_NTE, not a post-hoc fit. Planck: 0.9649 ± 0.0042 (0.85σ). Clean tier — no observational input in the chain. CMB-S4 sharpens the test.",
     "**n_s = 0.9685 (CMB spectral index — consistent at clean tier, slow-roll reading open).** Chapter 12's ripple register: pre-temporal pattern resolution plus the e-fold depth from β_NTE delivers 0.9685 under the framework's slow-roll reading of the pre-temporal phase. No post-hoc fit — β_NTE is already fixed by the central equation H = β_NTE|Φ_NTE|², not tuned for the tilt. Planck: 0.9649 ± 0.0042 (0.85σ). Honest scope: the slow-roll reading is itself an open structural identification — the framework has not yet derived it from first principles, and under a different reading the natural pre-geometry would deliver n_s = 1, badly off from observation. So n_s is consistent at clean tier (no calibration feedback) but not yet derived (profile-contingent on the slow-roll identification). CMB-S4 sharpens the empirical test; a successful first-principles derivation of the slow-roll reading would promote n_s from consistent to derived.",
     "E2-4"),
    (CH15,
     "The CMB spectral index and **m_{ν₂}** sit in the clean zero-parameter tier.",
     "**m_{ν₂}** sits in the clean derived tier — the framework's calculation produces 0.0086 eV from geometry alone, matching the solar oscillation scale within sub-percent precision. The CMB spectral index **n_s** sits at clean tier in the calibration sense (no observational input fed the derivation) but its specific value of 0.9685 depends on the framework's slow-roll reading of the pre-temporal phase, which is an open structural identification rather than a first-principles derivation; the match with Planck at 0.85σ is real but the underlying assumption is named honestly in Chapter 12.",
     "E2-5"),
    (CH15,
     "**The tensor-to-scalar ratio r ≈ 4 × 10⁻³ (hilltop reading).** A measure of how strongly primordial gravitational waves contribute to the CMB compared to the density fluctuations. Standard inflationary models leave this as a free parameter that depends on the inflaton potential's shape. The framework's hilltop reading of the pre-temporal sector — the same inflation slot that delivers n_s in §2 — gives **r ~ 4×10⁻³**, comfortably below current bounds. *Consistent so far; the test is CMB-S4 / LiteBIRD in the early 2030s*, with sensitivity approaching r ≈ 10⁻³. If r is measured far above the hilltop value, the framework's inflationary reading has missed something.",
     "**The tensor-to-scalar ratio r ≈ 4 × 10⁻³ (hilltop reading — conditional survivor).** A measure of how strongly primordial gravitational waves contribute to the CMB compared to the density fluctuations. Standard inflationary models leave this as a free parameter that depends on the inflaton potential's shape. The framework's hilltop reading of the pre-temporal sector — the same inflation slot that delivers n_s in §2 — gives **r ~ 4×10⁻³**, comfortably below current bounds. *Honest scope:* r's value depends on a specific assumption about the boundary expansion field's kinetic energy — the simplest assumption (the standard \"canonical\" form natural to a minimally-coupled constraint-bound real scalar) is what the framework currently uses, but the framework has not yet derived that this is the form deeper geometry requires; that derivation is open work the broader programme continues. So r is a *conditional survivor* — consistent at clean tier with no observational input feeding the derivation, but conditional on the open kinetic-term default. *Test: CMB-S4 / LiteBIRD in the early 2030s*, with sensitivity approaching r ≈ 10⁻³. Two pathways to failure: r measured far above the hilltop value would mean the framework's inflationary reading has missed something at the dynamics level; a different kinetic-term default derived from deeper geometry would shift the r prediction without breaking the framework's structural reading.",
     "E2-6"),
    (CH9,
     "The second fact. Why is there only one factor of 1/√(4π), or three, or some other count? Because the unresolved neutrino has *three* mass eigenmodes. This was developed in Chapter 8 as the source of flavour oscillation: the unresolved species decomposes into three eigenmodes corresponding to the three independent generators of the algebra called su(2), the algebra that organises the manifold's S³ structure and which the reader has met as the algebra underlying spin in quantum mechanics. The factor of three in the bare coupling comes from this dimensional count: three eigenmodes, each contributing the same monopole projection independently. For the κ₀ derivation specifically, only the count dim(su(2)) = 3 is load-bearing; the further structural question of how the three eigenmodes correspond to the three observed neutrino flavours is a separate corpus claim the framework reads as kin to this one but structurally distinct.",
     """The second fact. Why is there only one factor of 1/√(4π), or three, or some other count? Because the gauge structure that organises the cross-thickness coupling — the SU(2) algebra at the heart of the framework's manifold geometry — has exactly *three* independent generators. The reader has met this algebra in earlier chapters as the algebra underlying spin in quantum mechanics, and as the structure that organises the manifold's S³. What matters for the bare coupling is that this algebra has three independent gauge-field components — three independent ways the coupling can direct itself within the gauge sector — and each contributes the same monopole projection from §4 independently. The factor of three in the bare coupling counts these gauge-field components. The number three has, structurally, a single home: it counts the dimension of the adjoint representation of SU(2), the count of independent generators the framework's gauge algebra carries.

A related fact worth distinguishing carefully. The unresolved neutrino also has three mass eigenmodes (developed in Chapter 8 as the source of flavour oscillation), and the three is the same three — the eigenmodes live in the same su(2) algebra whose dimensional count fixes the gauge components. But the κ₀ derivation does not load-bear on the neutrino's eigenmodes; it loads on the gauge-field components. The neutrino's three flavours and the gauge sector's three independent directions share their *count* because they share their underlying algebra, not because one is the source of the other. The framework's broader programme treats these as structurally related — the algebra is one, the three appears wherever the algebra acts — but for the κ₀ derivation specifically, the load-bearing claim is about gauge-field components.""",
     "E3-1"),
    (CH9, "The three-eigenmode count is topological.", "The three-gauge-component count is fixed by the dimension of the adjoint representation of SU(2) — a topological-algebraic fact, not an empirical fit.", "E3-3a"),
    (CH9,
     "- The three-eigenmode count is set by the dimension of the unresolved neutrino's su(2) mass-eigenmode structure. This is a topological count, not a phenomenological fit.",
     "- The factor of three in the bare coupling counts the gauge-field components of the SU(2) algebra — dim(adj SU(2)) = 3. This is a structural fact about the framework's gauge sector, not a fit. The neutrino's three flavours share the same count for the same algebraic reason (they live in the same su(2)), but the κ₀ derivation loads on the gauge-field components, not on the neutrino's flavour structure — the distinction matters for what the prediction stands or falls on.",
     "E3-4"),
]

E3_2_INSERT = """

Worth one independent check on the count of three before moving on. In an unrelated branch of theoretical physics — work on monopole couplings in field theory contexts unrelated to dark matter or cosmology — the same factor of three appears naturally, for the same reason: it counts the dimension of the adjoint representation of SU(2), the algebraic content the framework's gauge sector lives in. The match is not an independent derivation of κ₀ within this framework (the underlying algebraic content is the same), but it tells us something useful: the framework's identification of dim(adj SU(2)) = 3 as the load-bearing count is structurally well-grounded rather than peculiar to NTE's specific construction. The factor of three has a single structural home in the gauge algebra; multiple physical contexts find it there independently.

"""

E3_3b_INSERT = """

Worth being plain about the leverage in this derivation. The closure step amplifies wobbles: the 0.36 percent adjustment at the bare-coupling level corresponds to the 2.3 percent residual at the resummed-coupling level, an amplification of about a factor of six. This is the same factor of six that turned κ₀ ≈ 0.846 into κ ≈ 5.50 in the first place — the closure step's geometric series, which amplifies the bare coupling into the cosmological ratio, also amplifies any imprecision in the bare coupling into a larger imprecision at the headline number. The framework's structural confidence sits most cleanly at the bare-coupling level — κ₀ = 3/√(4π) is structurally exact at its derivation register — and the headline 5.50 is the algebraic consequence the closure step produces from that bare coupling. The match at 0.83σ is the joint reading: the bare-coupling derivation lands at a structural value that the closure step turns into a number sitting within Planck's measurement uncertainty. Tightening Planck's measurement, which CMB-S4 will do in the early 2030s, will either confirm that the bare-coupling derivation is structurally correct or surface a residual the framework's current corpus cannot account for.

"""

E3_5_INSERT = """

Worth a brief note on where the framework's confidence sits structurally. The geometric-series step amplifies wobbles — the closure formula κ = κ₀/(1 − κ₀) turns small variations in the bare coupling into larger variations in the headline ratio. The bare coupling κ₀ ≈ 0.846 carries the framework's strongest structural-derivation confidence; the headline 5.50 is what the algebraic closure step produces from that bare coupling. The match at 0.83 standard deviations from Planck is the joint reading: bare-coupling derivation plus closure-step algebra, both landing within the measurement's uncertainty. Chapter 9 carries the technical detail; what matters here is that the chord's first note has a structural confidence level that lives at the bare-coupling derivation, with the headline 5.50 as its algebraic consequence.

"""


def main():
    log = []
    for path, old, new, tag in REPLACEMENTS:
        text = path.read_text(encoding="utf-8")
        if old not in text:
            log.append(f"FAIL {tag}: OLD not found in {path.name}")
            continue
        path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
        log.append(f"OK {tag} {path.name}")

    ch9 = CH9.read_text(encoding="utf-8")
    anchor = "This is the framework's distinctive claim about this number, and the reason this chapter exists."
    if anchor in ch9 and E3_2_INSERT.strip() not in ch9:
        ch9 = ch9.replace(anchor, E3_2_INSERT + anchor, 1)
        log.append("OK E3-2 Ch9")
    else:
        log.append("SKIP/FAIL E3-2")

    residual_end = "The framework, on its current corpus, does not identify a positive candidate explanation for the residual."
    if residual_end in ch9 and "factor of six" not in ch9:
        ch9 = ch9.replace(
            residual_end + "\n\nThis is worth being clear about.",
            residual_end + E3_3b_INSERT + "\nThis is worth being clear about.",
            1,
        )
        log.append("OK E3-3b Ch9")
    else:
        log.append("SKIP/FAIL E3-3b")

    ch12 = CH12.read_text(encoding="utf-8")
    first_note_close = "The note exists at 5.50 because the instrument is shaped the way it's shaped."
    if first_note_close in ch12 and "structural confidence level" not in ch12:
        ch12 = ch12.replace(
            first_note_close + "\n\n---",
            first_note_close + E3_5_INSERT + "\n---",
            1,
        )
        log.append("OK E3-5 Ch12")
    else:
        log.append("SKIP/FAIL E3-5")

    CH9.write_text(ch9, encoding="utf-8", newline="\n")
    CH12.write_text(ch12, encoding="utf-8", newline="\n")

    out = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6\Working\_pc_e2_e3_apply_log.txt")
    out.write_text("\n".join(log), encoding="utf-8")
    print("\n".join(log))


if __name__ == "__main__":
    main()
