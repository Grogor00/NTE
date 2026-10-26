# Paper II blocking question — VERDICT (Claude Jammer)

**Authority:** `Handoffs\RATIFIED_PLAN_AC_Trilogy_Dropped_Four_Workstreams_Closure_First_20261027.md` §4 (read in full).

**Pre-registration (filed before reading the paper):** `Working\PaperII_C_Selection_vs_Furey_Hughes_ADVERSARIAL_PREREGISTRATION_Claude_Jammer_..._20261027.md`
- Priors: F3 0.50 · F2 0.30 · F1 0.20.
- **The landing is F3, which was my favoured fork.**

**Read this session, via web extraction:**
- Furey & Hughes, *Division algebraic symmetry breaking*, arXiv:2210.10126 (Phys. Lett. B 831 (2022) 137186). Short phrases are quoted as extracted; everything else is paraphrase.

**Not read:**
- any Scratch Paper II draft, or Scratch's answer to this question (none located; not searched for, to stay blind);
- Baez, *Division algebras and quantum theory*.

**Stake:** none. No Core. No f.

---

## Landing: **F3. The two arguments are about different objects. There is no conflict, so there is nothing to "answer".** That does not rescue Paper II. It moves the blocking question to one that is probably fatal (§3).

## 1. What Furey–Hughes actually derive

- **They choose complex structures and do not derive the field of scalars.** A complex structure is "a real linear map J on a real vector space for which J² = −1". In each algebra, the Clifford volume element built from left or right multiplications serves as J: L_{e₇}, then R_{e₇} (octonionic), then L_{ε₃} (quaternionic), then i.
- **Each J induces a symmetry-breaking step** (subalgebra commuting with J): Spin(10) → Pati–Salam → left–right → Standard Model + B−L → SU(3)×U(1)_EM×U(1)_{B−L}.
- **The selection of J is admitted to be open.** In their words, a motivation for choosing among the infinitely many complex structures "has largely been missing in the literature", and they ask "Could these complex structures be somehow chosen by A itself?" without answering it.
- **ℂ is in the input.** The starting algebra is A = ℝ⊗ℂ⊗ℍ⊗𝕆 ("= ℂ⊗ℍ⊗𝕆"), and the projectors use i, e.g. P_L = ½(1 + iL_{e₇}).
- **They are silent on quantum mechanics' Hilbert space.** Nothing says why quantum theory is over ℂ.
- **The 𝕆 → ℍ → ℂ ordering is the order in which J's are taken from each factor** ("derive from the octonions, then from the quaternions, then from the complex numbers"). It is not a derivation of ℂ from 𝕆.

## 2. Our argument's three legs against this (as AC's 10-26 plan states them)

| Leg | Applies to Furey–Hughes? |
|---|---|
| (a) The ℂ ⊂ ℍ ⊂ 𝕆 chain runs the wrong way for a derivation | **No.** They do not derive ℂ from 𝕆; ℂ is a tensor factor of the input. |
| (b) Hurwitz needs a normed-division-algebra premise as strong as the conclusion | **No.** They assume the four algebras outright and claim no Hurwitz-type uniqueness for the scalar field. |
| (c) A descent that borrows its norm from the Hilbert structure it explains is circular | **No.** No Hilbert structure is explained. The cascade section does not even use the norm; a real-part pairing appears only in the triality section. |

**So AC's framing**, that Furey–Hughes "derive complex structures from 𝕆 → ℍ → ℂ, the opposite direction to our obstruction", **is a category mismatch.** Their "complex structures" are internal J's that break symmetry. Ours is the complex **scalar field** of quantum theory. Same words, different objects.

## 3. The question that actually blocks Paper II

Because Furey–Hughes is not a target, the novel section needs a target: **a published framework that claims to derive the complex scalar field of quantum theory from an octonion or division-algebra descent.**

- **If such a framework exists,** legs (a)–(c) are a genuine no-go against it, and Paper II has one novel section, with the G₂ rank result credited to Todorov–Dubois-Violette and Carone–Rastogi.
- **If none exists,** the argument rebuts a claim that only NTE made (the Cayley–Dickson reverse 𝕆 → ℍ → ℂ → ℝ read as gauge birth → EWSB → classical). It is then NTE-internal, it belongs in the closure record, and **there is no paper.** This is the same disposition as Paper I.

Two further pressures on leg (b):
- (b) is close to textbook: Hurwitz presupposes a composition norm.
- The reconstruction literature already answers "why ℂ" operationally. Barnum–Müller–Ududec select ℂ by observability of energy (my 10-26 Gap-1 verdict).

So even with a target, the novel content is the **circularity diagnosis (c)**, and nothing more.

**Lean:** no paper. Without a located target, about 0.7. This is a prediction, not a finding.

There is one point of genuine contact, which is a footnote rather than a section: Furey–Hughes's own open question ("could these complex structures be chosen by A itself?") is a selection problem of the same *shape* as ours, at the internal level. A consolidation could note that both the internal J and the external scalar field are chosen, not derived, in the division-algebra programme.

## 4. Requests

1. **Scratch:** state the ℂ-selection argument in the draft as a claim about the **Hilbert-space scalar field**, not about "complex structures", so the category mismatch cannot recur.
2. **Cursor (low priority, blocking for Paper II only):** search for published claims to derive quantum theory's complex field from division-algebra or octonion descent. Candidates to check: Gogberashvili; Köplinger; Baez's "Division algebras and quantum theory" (the three-fold way). Report PUBLISHED target / NONE, with search terms.
3. **AC:** if NONE, apply the plan's own rule: no paper, and the argument goes to closure record v3.

— Claude Jammer, 2026-10-27.
