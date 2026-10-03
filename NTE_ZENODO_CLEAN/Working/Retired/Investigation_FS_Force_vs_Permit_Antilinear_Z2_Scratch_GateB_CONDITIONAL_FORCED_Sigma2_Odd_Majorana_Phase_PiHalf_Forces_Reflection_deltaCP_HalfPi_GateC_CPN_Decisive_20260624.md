# Investigation: FS Force-vs-Permit antilinear θ₂₃ Z₂ — GATE B VERDICT: CONDITIONAL-FORCED. The Majorana condition on the σ₂-polarised mode forces a π/2 relative phase (σ₂ is conjugation-odd), which makes the LINEAR swap inconsistent and the ANTILINEAR (reflection) swap the consistent one → δ_CP = ±π/2 — **conditional on P4's chirality-superposition identification**, which Gate C (CPN) must lock.

**From:** Scratch (lead, Claude model)
**To:** AC; Cc: Greg, Jammer, PC, Cursor
**Date:** 2026-06-24
**Charter:** `CHARTER_FS_Force_vs_Permit_...`. Builds on Gate A (PASS: det = −1 obstruction, antiunitary-only at spinor level). No corpus touch; P4 unedited; nothing adopted.

**GATE B: CONDITIONAL-FORCED.** Under P4's own chirality-superposition premise, the Majorana phase structure forces the antilinear swap and δ_CP = ±π/2. Premise-free strict forcing routes to Gate C.

---

## What Gate B computed
Built the neutrino Majorana mass matrix M_ν under each candidate symmetry and diagonalised:
- **μτ-EXCHANGE (P4's LINEAR Z₂):** impose P M P = M with M real. ⇒ θ₂₃ = π/4, θ₁₃ → 0, **Jarlskog J = 0** (CP-conserving, δ undetermined). This is P4's exchange — and it is **CP-blind**.
- **μτ-REFLECTION (antilinear):** impose P M\* P = M. ⇒ θ₂₃ = π/4, **θ₁₃ ≠ 0 allowed, |J| maximal ⇒ δ_CP = ±π/2.** (Verified by diagonalisation; standard Harrison–Scott.)

So the two implementations are observationally distinct: exchange ⇒ CP-conserving; reflection ⇒ maximal CP violation. The question is which the Majorana/chirality structure selects.

## The forcing mechanism (the new content — ties Gate A's hook to a real phase)
Charge conjugation acts on the polarisations as established in Gate A: **σ₁ → +σ₁ (even), σ₂ → −σ₂ (ODD), σ₃ → +σ₃ (even).** Imposing the Majorana condition ψ = ψ^c on a σ_a-polarised mode fixes its intrinsic Majorana phase by self-conjugacy:
- σ₁-polarised (conjugation-even): intrinsic phase **real** (Majorana phase 0).
- σ₂-polarised (conjugation-**odd**): self-conjugacy ⇒ intrinsic phase **imaginary** (Majorana phase π/2, factor i).

So **σ₁ and σ₂ Majorana modes are forced to differ by a relative phase of π/2** — set by σ₂\* = −σ₂, not inserted by hand. The σ₁↔σ₂ swap therefore relates a real mode to an i-phased mode:
- the **linear** swap ignores the i ⇒ inconsistent with the forced Majorana phase (it relates the modes as if both real);
- the **antilinear** swap carries the conjugation that supplies the i ⇒ consistent.

The forced π/2 relative phase is exactly δ_CP = ±π/2 in the mixing — matching the reflection diagonalisation. The same σ₂\* = −σ₂ fact drives **both** gates: in Gate A it is the det = −1 obstruction; in Gate B it is the forced Majorana phase. One structural fact, two consequences, converging on antilinear.

## Honest conditionality (why CONDITIONAL, not unconditional FORCED)
Both P M P = M (linear) and P M\* P = M (antilinear) are **mathematically valid symmetries to impose** — at the bare matrix level, this is PERMIT, and it is exactly why P4 could adopt the linear one and still get θ₂₃ = π/4 (its derivation worked at the flavor-permutation level and never tested the Majorana phase). The **forcing appears only if the swapped σ-polarisation IS the charge-conjugation structure** — i.e. P4's chirality-superposition identification is a *rigid identity*, not a suggestive label. Under that identification the σ₂-odd Majorana phase is forced and the linear swap is inconsistent ⇒ reflection forced ⇒ δ_CP = ±π/2. Whether the identification is rigid is **not** settled by Gate B.

## Verdict + next
- **GATE B: CONDITIONAL-FORCED.** The Majorana phase structure forces the antilinear swap (δ_CP = ±π/2) **given** P4's chirality-superposition premise. Within P4's own framework, that premise is granted — so within P4, this is forced. For a premise-free claim, the identification must be derived from ratified structure.
- **Gate C is now the whole ballgame:** does the ratified antilinear **CPN** actually implement (or contain) the σ₁↔σ₂ swap on the chirality-superposed sector? If yes, the identification is canon, the conditionality discharges, and FORCED locks (δ_CP = ±π/2 becomes an NTE prediction tied to ratified CPN). If CPN does not implement the swap, the verdict settles at PERMITTED-ONLY (attractive, not forced) and P4 stands as-is.
- Discipline check: I did not upgrade CONDITIONAL to FORCED. Both gates lean antilinear hard, but the premise-free forcing genuinely depends on Gate C, and PERMITTED-ONLY remains a live, acceptable outcome.

— Scratch, 2026-06-24. Gate B: σ₂ is conjugation-odd, so a σ₂-polarised Majorana mode is forced to carry a relative i — a π/2 phase that is δ_CP = ±π/2, and that the linear swap can't honour. The same σ₂\*=−σ₂ that was Gate A's det wall is Gate B's forced phase. It forces the reflection **under P4's chirality identification** — and whether that identification is canon or label is exactly what CPN (Gate C) decides. Strong, conditional, not yet closed.
