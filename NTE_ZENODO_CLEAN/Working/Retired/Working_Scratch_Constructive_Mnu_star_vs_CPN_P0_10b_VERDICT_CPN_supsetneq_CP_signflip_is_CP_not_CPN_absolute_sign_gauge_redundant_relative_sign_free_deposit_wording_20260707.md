# Working — Scratch (constructive): is M_ν → M_ν* literally the CPN map (P0.10b)? VERDICT: CPN ⊋ CP. M_ν → M_ν* (within our sector) is ordinary CP (the C-part); the full CPN adds the N sector-swap, so CPN(M_ν) = M_ν* in the −N (mirror) sector, not in ours. The operation that flips sign(δ_J) is CP, not CPN. Convergent with Jammer; sharpened with the absolute-vs-relative-sign distinction that decides the deposit wording.

**Stream:** Scratch (constructive leg, per AC task (a) 2026-07-06 22:08Z).
**To:** AC (adjudicate; deposit wording held pending this); Cc: Greg (authorising), Jammer (adversarial — convergent), CR.
**Date:** 2026-07-07
**Priority:** P1 — deposit-blocking (decides the held δ_J wording).
**Sources:** P0.10b (Paper_Susskind_v0_4: CPN as modular conjugation of the Janus crossed product on A_F = 𝕆₊ ⊕ 𝕆₋), confirmed identical across the CPN fixed-locus joint note and Jammer's consolidated note: CPN(a,b) = (b̄, ā). The δ_J FORCED-UNCOMPUTED result (M_ν → M_ν* flips sign(δ_J) at fixed masses/ordering/|U|), AC-adjudicated. Jammer's adversarial (a) leg (CPN ⊋ CP).

---

## §0 — Verdict (one line)

**CPN ⊋ CP.** Under P0.10b, CPN = N ∘ CP: the C-part produces the complex conjugate (M_ν → M_ν*), the P-part acts trivially on the generation-space mass matrix (a spatial/Lorentz scalar), and the **N-part is the sector-swap 𝕆₊ ↔ 𝕆₋**. So CPN(M_ν) = M_ν* **in the −N (mirror) sector**, which is *not* M_ν* in our +N sector. The operation that flips sign(δ_J) — M_ν → M_ν* at fixed flavour basis, within our sector — is therefore **ordinary CP, not the full CPN.** Consequence for the deposit: the "two signs = two universes" framing is valid only as a *cross-sector bilateral correlation* (our sign ↔ the mirror's opposite sign), **not** as a determination of our sign. Ship the relational-not-absolute wording; do not ship "the two signs are the two universes" as a resolution of the sign.

---

## §1 — P0.10b and the C/P/N decomposition

P0.10b: on A_F = 𝕆₊ ⊕ 𝕆₋,

    CPN(a, b) = (b̄, ā),   a ∈ 𝕆₊, b ∈ 𝕆₋,  ¯ = octonion conjugation.

Antilinear (the bar), sector-swapping (positions exchanged), J² = 1, modular conjugation of the Janus crossed product. Decompose into the named pieces:

- **C** (charge conjugation) = the octonion conjugation (the bar). Antilinear. This is the piece that produces a complex conjugate.
- **N** (bilateral N-orientation reversal) = the sector-swap 𝕆₊ ↔ 𝕆₋, i.e. N → −N — the position-exchange (a,b) ↦ (b,a).
- **P** (spatial parity) = parity on the spatial S³ (the ℍ factor); acts on the spatial/spinor structure of the field.

As operators: **CPN = N ∘ (C∘P) = N ∘ CP.**

---

## §2 — Action on M_ν (the computation AC asked for)

M_ν is a 3×3 matrix in generation space; as a coupling in the Majorana mass term ν^T C M_ν ν it is a **Lorentz and spatial scalar**. Track each piece:

- **P on M_ν: trivial.** Parity acts on the spinor/spatial structure of the neutrino field (handedness, momentum), not on the entries of the generation-space coupling matrix. It contributes to the field-level CP transformation but adds nothing to M_ν beyond its standard role inside CP.
- **CP on M_ν: M_ν → M_ν\*.** In the charged-lepton-diagonal (flavour) basis, the standard CP transformation of a Majorana mass matrix is complex conjugation of the couplings, M_ν → M_ν* (up to phases absorbable into field redefinitions). This is exactly the operation that flipped sign(δ_J) in the sign-push (I conjugated the texture; masses, ordering, |U| unchanged; δ → −δ).
- **N on M_ν: sector-swap.** For M_ν localised in our +N sector — represented as (M_ν, 0) in A_F — the swap sends it to the −N slot.

Compose. Applying CPN to M_ν in +N:

    CPN((M_ν, 0)) = ( 0̄, M̄_ν ) = ( 0, M_ν* )   →   **M_ν\* sitting in the −N (mirror) sector.**

Compare with the sign-flip operation:

    CP(M_ν) = M_ν\*   **in the same +N sector.**

**CPN(M_ν) = M_ν\* in −N  ≠  M_ν\* in +N = CP(M_ν).** The two differ by exactly the N sector-swap. Answering AC's sub-question 3 precisely: the "*" comes from **C**; the piece that makes CPN ≠ CP is **N** (not P — P acts trivially on the scalar mass matrix). **CPN carries strictly more than CP: the extra piece is the bilateral N sector-swap.**

---

## §3 — What flips sign(δ_J) is CP, not CPN

The sign-push established sign(δ_J) flips under M_ν → M_ν* at fixed masses/ordering/|U|. §2 identifies that operation as **CP** (within-sector conjugation). It is *not* CPN: CPN would additionally move the conjugated matrix into the mirror sector. So:

- **Our sign(δ_J)** is set by which CP-parity texture (M_ν vs M_ν*) is realised **in our sector** — a free within-sector discrete datum (free spectral data, Companion 13). Unchanged by this analysis.
- **CPN** does not act within our sector at all; it maps our whole sector to the mirror.

---

## §4 — The bilateral correlation, and why it does not fix our sign

CPN relates the two sectors. For a CPN-symmetric bilateral state, the fixed-point condition is (from CPN((M_+,M_−)) = (M_−*, M_+*) = (M_+,M_−)):

    **M_− = M_+\*.**

So if our sector carries M_+ (with some sign(δ_J)), the CPN-mirror sector carries M_+* — the CP-conjugate texture, hence the **opposite** sign(δ_J). That is a genuine, distinctive bilateral correlation: **the CPN-conjugate universe carries the opposite δ_J sign.** True, and shippable.

But it does **not** determine *our* sign. Our sign is whichever M_+ nature realised; CPN only says the mirror is the conjugate. Moreover — strengthening — the N+/N− pair is a **discrete gauge redundancy** with no observable content (you cannot tell which member of the pair you inhabit; established this programme). CPN's entire content here is that cross-sector relation, i.e. the gauge-redundant part. **A gauge-redundant relation cannot fix a physical observable.** So CPN is structurally incapable of pinning our sign(δ_J); it names the (unobservable-from-inside) mirror partner and nothing more.

---

## §5 — The distinction that decides the wording: absolute vs relative sign

Two different "signs" must not be conflated:

1. **Absolute sign(δ_J)** (no reference): flips under the N+/N− relabelling (it is the CPN pair's label). **Gauge-redundant, unobservable from inside.** Greg's reading — "the two signs are the two universes, so the absolute sign is unobservable *by the bilateral symmetry itself*, a feature not a gap" — is **correct for the absolute sign.**

2. **Relative sign(δ_J) / sign(B)** (referenced to the baryon asymmetry, i.e. to our matter identity B > 0): **gauge-invariant and observable** — this is what an experiment with matter detectors actually measures. The sign-push proved this is **free**: the neutrino CP-parity is independent of the baryon sector, so sign(δ_J) flips relative to fixed B. **Not fixed by NTE — the genuine open gap.**

The crux: the bilateral "feature" resolves (1) but **not** (2). Making the *absolute* sign gauge-redundant does **not** close the physics, because the *observable relative* sign remains a free parameter. So the deposit must not present "two universes ⇒ sign unobservable" as *resolving* the δ_J sign question — it resolves only the unobservable absolute label, while the measurable relative sign stays FORCED-UNCOMPUTED.

---

## §6 — Deposit wording (refined; ready to cite; resolves the held wording)

Per AC's own mapping, CPN ⊋ CP ⇒ fall back from "the two signs are the two universes" to relational-not-absolute. Precise, distinctive, honest version:

> *"NTE forces θ₂₃ = π/4 and |δ_J| = π/2. The sign of δ_J is a within-sector CP-parity — the choice M_ν vs M_ν\* — which is free spectral data of the octonionic spectral triple (Companion 13) and is not fixed by NTE structure, the baryon asymmetry, the mass ordering, or leptogenesis. The bilateral CPN of P0.10b is cross-sector (CPN = N∘CP: it maps our sector's M_ν to M_ν\* in the −N mirror sector); it therefore correlates our sign with the opposite sign in the CPN-conjugate universe. This makes the **absolute** sign a gauge-redundant label of the N+/N− pair (unobservable from within — a feature of the bilateral symmetry), while the **physical** sign relative to our matter sector remains an open, well-posed prediction NTE does not yet fix. DUNE/Hyper-K decide the magnitude now; the (relative) sign is open."*

- **Ships** the distinctive bilateral content (CPN-conjugate universe carries the opposite sign; absolute sign gauge-redundant).
- **Avoids** the failure mode: does not claim CPN fixes or resolves our observable sign.
- **Preserves** the FORCED-UNCOMPUTED status of the observable sign.

---

## §7 — Convergence and routing

- **Convergent with Jammer's adversarial (a):** CPN ⊋ CP; M vs M* is within-sector CP; two-universes framing is cross-sector correlation, not within-sector determination.
- **Adds:** the explicit N∘CP operator decomposition with P shown to act trivially on the scalar M_ν (so the "extra piece" is precisely N, answering AC sub-question 3); the gauge-redundancy argument (CPN's content is the N+/N− redundancy, hence cannot fix an observable); and the **absolute-vs-relative-sign** distinction (§5) that pinpoints why the elegant framing is true but does not close the physics.
- **Deposit:** wording resolved — ship §6. This unblocks the held δ_J wording.
- **Routing:** AC → Greg. AC can verify §2 directly against P0.10b (it is a two-line operator computation).

— Scratch (constructive leg), 2026-07-07. CPN ⊋ CP; the δ_J sign-flip is CP not CPN; absolute sign gauge-redundant, observable relative sign free (open). Convergent with Jammer; deposit wording in §6.
