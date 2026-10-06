# Handoff — AC: verification batch, items 2 and 4 complete. One new contradiction for Greg.

**From:** AC (Claude) · **To:** Greg, PC, Cursor, Scratch, Jammer · **Date:** 2026-09-24
**Sources read in full this session:** `Core_Papers\Companion_08_VNTE_Trajectory_v10_19_0.md`; `Core_Papers\Companion_05_StateSpace_v10_19_0.md`.
**Status:** 2 of 4 verifications complete. T1 matching scripts and P3 literature still outstanding. **Item (a) remains held.**

---

## Verification 2 — Companion 8 / the 63.4 figure. **CONFIRMED, and the error is one level deeper than reported.**

**Cursor's claim is correct.** Companion 8 §2 defines it exactly as claimed:

> Upstream of it is the Hartle-Hawking de Sitter sub-phase of roughly **N_e = −ln(β_NTE·M_Pl) ≈ 63.4 e-folds** at H ≈ M_Pl…

and names it explicitly as *"the **energy-scale ratio** N_e ≈ 63.4"*, distinguished in the same sentence from *"the locking span N_lock ≈ 0.1"*.

**But Companion 8 then commits the category slip itself.** §6 (F4) builds the spectral-index table with the column heading **"n_s at pivot (N_e ≈ 63.4)"** and evaluates every profile there — P3 (β = ½) and P4 (Starobinsky-form) both yielding 0.968.

So the conflation does **not** originate in Companion 17 importing a mislabelled number. **It originates in Companion 8, which defines 63.4 as an energy-scale ratio in §2 and uses it as the pivot horizon-exit count N_\* in §6.** Companion 17 inherited a slip already present in its source.

**This strengthens item (a) further and changes its scope.** The corrected patch set must fix the *use* in Companion 8 §6, not merely relabel the figure elsewhere. And the residual — keep 63.4 in Companions 8/9 as N_HH — needs care: Companion 8 is the very file where both uses sit side by side.

**One honest note in Companion 8's favour:** F4 already concludes that n_s is *"consistent with NTE structure but not derived from it"*, and that the natural constant-H instanton gives the wrong answer at ~8.4σ. The paper's scope honesty is intact. What is wrong is the pivot identification underneath the number, not the register attached to it.

---

## Verification 4 — Companion 5 / Ω_k. **AC's expectation was WRONG. This is a real contradiction, not a gloss.**

AC predicted the "Euler flatness" argument would turn out to be topological — χ(S³) = 0, true for any closed odd-dimensional manifold and carrying no implication for the density parameter — making the defect a category slip fixable by a gloss.

**That is not what Companion 5 says.** "Euler" means **Euler's identity**, and the argument is energetic:

> The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and **zero total energy requires zero spatial curvature, Ω_k = 0**. The universe is flat because the boundary condition demands it. NTE **derives flatness** both dynamically… and topologically (from Euler closure).

And §9 restates it as a falsifier: *"Spatial flatness Ω_k = 0 (**non-zero curvature would falsify the boundary identification**)."*

### Three consequences

**1. Direct contradiction with today's ratified Part 3 patch.** Part 3 now reads Ω_k → 0 with *"Exact Ω_k = 0 is not claimed."* Companion 5 claims it twice, as derived.

**2. Direct contradiction with falsifiability item 11 — and the two point opposite ways.** Item 11: NTE requires **Ω_k < 0 strictly**; a confirmed Ω_k > 0 falsifies. Companion 5 §9: **any** non-zero curvature falsifies. Under item 11 the framework *requires* non-zero curvature; under Companion 5 non-zero curvature kills it. **These cannot both stand**, and item 11 created the collision today.

**3. Companion 5's own argument is in tension with its own ontology.** In the Newtonian energy reading of Friedmann, zero total energy corresponds to k = 0 (flat, critical density); a **closed** universe, k = +1, corresponds to *negative* total energy. Companion 5 asserts both zero total energy *and* a closed S³. There may be a resolution — the Janus "zero total energy" is a bilateral sum across two sectors, which is a different quantity from the FRW energy of one sector — but if so, **the paper is using one phrase for two things**, and the flatness conclusion does not follow from the bilateral statement.

### Routing

**Not patchable by AC.** This is a derived-tier claim in a deposited companion, contradicting a same-day ratified correction and a same-day falsifier, with a physics question underneath it. It needs:

- **Greg** to rule on the claim; and
- **Scratch or Jammer** to settle whether the bilateral zero-energy condition implies anything about spatial curvature at all, or whether the two "zero energy" statements have been conflated.

**AC recommends** routing the physics first, then the wording, rather than patching Companion 5 to match Part 3 — because if the bilateral argument does not bear on curvature, the correct fix is to *withdraw the flatness derivation*, not to soften it.

**Interim:** item 11 and the Part 3 Ω_k → 0 wording stand as ratified. Companion 5 is the outlier and should not be cited for flatness until this closes.

---

## Still outstanding

- **Verification 1** — T1's matching scripts (N_* ≈ 55–56).
- **Verification 3** — P3 literature (Feldbrugge–Lehners–Turok vs Hartle–Hawking–Hertog) against primary sources.

**Item (a) stays held until both close.**

---

— AC, 2026-09-24.
