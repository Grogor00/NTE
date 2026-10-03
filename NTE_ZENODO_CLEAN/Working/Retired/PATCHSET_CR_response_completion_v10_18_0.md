# Patch set — CR response completion (v10.18.0, pre-Zenodo)

**Author:** AC · **Date:** 2026-07-05 · **For:** CR re-verify (held 4 & 5) → Greg ratification → Cursor render
**Origin:** completes the CR ontology/falsifiability response. Patches 1–3 already sent to Cursor. This set carries the two CR held for revision (4, 5), CR's recommended point-3 residual, and the point-2 / distinctiveness positioning that Greg ratified in direction.
**Routing:** CR reserved re-verify on 4 and 5 — these go back to CR first. Patch 5 v2 also carries a corpus-consistency reconciliation (Part 2 + Part 3) that supersedes the withdrawn Patch 5 v1 (the Cayley–Dickson-flip assertion — pulled, it wasn't in the construction).

**Application rule (all):** match on distinctive prose, not whitespace; preserve each file's math style (Part 1 & Part 3 LaTeX `$…$`; Part 2 §8.5–8.6 unicode). **If any OLD block does not byte-match, stop and report — do not force.** Keep Core_Papers and paper-build/scratch-src copies in sync; re-render the touched files; confirm 29/29.

| # | CR pt | Target | Effect |
|---|-------|--------|--------|
| 4 v3 | 6 | Part 1 §III | de-bundle: μ–τ reflection gives θ₂₃/θ₁₃/δ; θ₁₂ separate & open |
| 5 v2a | 7 | Part 2 §8.5–8.6 | S³ forced via ℍ⊂𝕆 (not an S⁷/ℤ₂ involution) |
| 5 v2b | 7 | Part 3 §XVII | ledger line: S³ = unit sphere of surviving ℍ⊂𝕆 |
| R3 | 3 (resid.) | Part 1 §2.1.2 | surface-only is *spatial*; N-thickness is emergent-*temporal* |
| POS | 2 + distinct. | Part 3 falsifiability | honest distinctiveness: κ + w/CC-dissolution + Majorana |

---

## PATCH 4 v3 — Part 1 §III (neutrino sector: de-bundle θ₁₂)

Grounded in the mixing-sector paper (`NTE_Octonionic_Spine_Neutrino_Mixing_Sector`): μ–τ reflection on J₃(𝕆) fixes θ₂₃/θ₁₃/δ, not θ₁₂. Confirmed against Companion 13 and Part 3.

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §III (end of the "unresolved neutrino" paragraph)

**OLD:**
```
The "Majorana bridge" label from earlier drafts should be read in this light: the bridge is geometric, not a particle mechanism.
```
**NEW:**
```
The "Majorana bridge" label from earlier drafts should be read in this light: the bridge is geometric, not a particle mechanism. What this ontology forces is symmetry structure, and that is where its clean content sits: the Majorana character (a falsifier at neutrinoless double-beta decay) and, from the antilinear $\mu$–$\tau$ reflection on $J_3(\mathbb{O})$ (Jordan Hermiticity), the maximal atmospheric angle $\theta_{23} = \pi/4$, $\theta_{13} = 0$, and the maximal phase $|\delta_J| = \pi/2$ (matching observation). That reflection fixes $\theta_{23}$, $\theta_{13}$, and $\delta$ — but not the solar angle: $\sin^2\theta_{12} = 1/3$ is a separate leading-order value from a distinct, still-open route (currently $2.9\sigma$). The two are not one structure; the $\mu$–$\tau$ results do not depend on $\theta_{12}$, and its tension does not undercut them. Both are carried at their honest register (Part 3).
```

---

## PATCH 5 v2a — Part 2 §8.5–8.6 (S³ forced via ℍ⊂𝕆)

Grounded in the octonionic-origin standalone (§3.3): S³ is the unit sphere of the quaternionic subalgebra ℍ⊂𝕆 that survives the 𝕆→ℍ associativity transition (SO(4)⊂G₂ stabiliser; same ℍ as SU(2)_L). The standalone contains **no** S⁷/ℤ₂ involution, and G₂→SU(3) comes from the e₁ stabiliser, **not** a "quaternionic involution" — so the original parenthetical was doubly off. This replaces it with the construction's actual grounding.

**TARGET:** `NTE_v10_18_0_Part2_Structure.md`, §8.5–8.6 (the involution parenthetical). Unicode, not LaTeX.

**OLD:**
```
(The same quaternionic involution that gives G₂ → SU(3) also localises resolved fermions on the S³ fixed locus of S⁷/ℤ₂ while leaving the ℤ₂-even neutrino delocalised over S⁷ — the geometric basis for §IX. The orbifold does not independently derive three generations; that remains J₃(𝕆).)
```
**NEW:**
```
(S³ here is forced, not fitted: it is the unit sphere of the quaternionic subalgebra ℍ ⊂ 𝕆 that survives the 𝕆 → ℍ associativity transition — the same ℍ, stabilised by SO(4) ⊂ G₂, whose SU(2) factor is SU(2)_L. Resolved fermions localise on this S³ while the CPN-even neutrino stays delocalised over the full S⁷ — the geometric basis for §IX. This localisation does not independently derive three generations; that remains J₃(𝕆).)
```

---

## PATCH 5 v2b — Part 3 §XVII (ledger line: reconcile the S⁷/ℤ₂ phrasing)

Same reconciliation in the parameter ledger. Keeps the CPN Pin⁻ and Majorana-orbifold lines (grounded separately); only the "S³ as the S⁷/ℤ₂ fixed locus" phrase changes.

**TARGET:** `NTE_v10_18_0_Part3_Accounting.md`, §XVII "Derived within the framework (structural)"

**OLD:**
```
- CPN selection (Pin⁻ on the $\mathbb{Z}_2$ orbifold); the Majorana condition (forced by orbifold convergence $\kappa_0<1$); $S^3$ as the $S^7/\mathbb{Z}_2$ fixed locus.
```
**NEW:**
```
- CPN selection (Pin⁻ on the $\mathbb{Z}_2$ orbifold); the Majorana condition (forced by orbifold convergence $\kappa_0<1$); $S^3$ as the unit sphere of the surviving quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$ (the $\mathbb{O} \to \mathbb{H}$ associativity transition).
```

**Consistency flag for CR/Greg:** the deposit still says CPN is "Pin⁻ on the ℤ₂ orbifold." If the intent is that S³ *is* the geometric fixed locus of that CPN ℤ₂ (equivalent to the ℍ-unit-sphere iff the CPN involution is the ℍ-complement flip), that identification is **not** established in the standalone and should not be asserted. The ℍ-subalgebra grounding above is the established one and answers CR point 7 on its own. If Greg has a source that fixes the CPN involution as the ℍ-complement flip, the orbifold-fixed-locus phrasing can be restored with that citation.

---

## PATCH R3 — Part 1 §2.1.2 (point-3 residual: surface-only is spatial)

CR's recommended one-liner so the Hubble-scale N-thickness doesn't invite the spatial-bulk misreading. **Anchor is AC's reconstruction — verify and match-or-report; if §2.1.2's wording differs, place the added sentence wherever t = i·ΔN / the N-thickness orthogonality is introduced.**

**TARGET:** `NTE_v10_18_0_Part1_Foundations.md`, §2.1.2

**OLD (verify):**
```
the "i" encodes that orthogonality.
```
**NEW:**
```
the "i" encodes that orthogonality. "Surface-only" is accordingly a statement about the *spatial* ontology: the N-thickness is not a spatial bulk dimension but the emergent *temporal* extent — the accumulated proper time toward the CPN mirror — which is why it runs to $\ell(N) = 1/H(N)$ without contradicting the boundary-only spatial picture.
```

---

## POS — Part 3 falsifiability register (empirical distinctiveness)

Addresses CR point 2 and the distinctiveness meta-point. States the honest three-handle distinctiveness (correcting CR's "≈ one number"), with the CC-dissolution scoped so it doesn't overclaim. **Insert as a new paragraph in Part 3's falsifiability/predictions section — AC does not have that section's text verbatim; CR/Cursor to confirm placement (recommended: immediately after the predictions triage).**

**NEW paragraph:**
```
**Empirical distinctiveness.** NTE's near-term empirical content is not a single number. Three handles distinguish it from SM + ΛCDM: (i) $\kappa = 5.50$, a zero-parameter prediction testable at CMB-S4; (ii) $w = -1$ exactly, together with the surface-only boundary ontology's structural dissolution of the vacuum-energy problem — the $\sim 10^{120}$ mismatch between the naive QFT zero-point estimate and the observed $\Lambda$ that stands unresolved in SM + ΛCDM — via the absence of a gravitating 4-bulk vacuum and the $a_4 = 0$ suppression on $S^3\times S^1$; and (iii) the forced Majorana character, testable at neutrinoless double-beta decay. Two honest qualifications on (ii): the dissolution is explanatory and structural — NTE removes the naturalness catastrophe (why $\Lambda$ is not of order $M_{\mathrm{Pl}}^4$) but does not predict $\Lambda$'s numerical value, which remains open (§XVII); and dissolving the cosmological-constant problem is shared with other boundary/holographic programmes, so it distinguishes NTE from SM + ΛCDM without any claim to be its unique resolver. The framework's *time-emergence* sub-claim ($N$ primary, $t$ emergent) makes no post-lock observable distinct from a $t$-primary reading and is, on its own, not directly testable; its empirical purchase is carried entirely by the consequences above, which do descend from the boundary / $N$-emergent ontology.
```

---

## Summary for the ratification chain

- **CR re-verify:** Patches 4 v3 and 5 v2a/b were the two you held — confirm the θ₁₂ de-bundle lands (it now cites the construction, not TBM) and the S³/ℍ reconciliation is faithful (the standalone grounds S³ in ℍ⊂𝕆, no S⁷/ℤ₂ involution).
- **Point 3 residual (R3)** and **POS** are new; R3 is your recommended one-liner, POS is the point-2/distinctiveness positioning Greg ratified in direction.
- **Open flag:** the CPN-ℤ₂-fixed-locus identification (Patch 5 note) — keep-with-source or drop; defaulted to the ℍ grounding.
- After CR clears and Greg ratifies: second Cursor handoff, render, 29/29.
