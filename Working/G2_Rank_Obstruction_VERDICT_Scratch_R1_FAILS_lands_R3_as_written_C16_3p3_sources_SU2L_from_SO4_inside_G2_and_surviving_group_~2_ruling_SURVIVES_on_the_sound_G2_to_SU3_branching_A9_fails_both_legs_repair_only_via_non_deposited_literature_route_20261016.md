# VERDICT — Scratch (second): the G₂ rank obstruction. **R-1 FAILS. Lands R-3 as written** — the deposited "surviving observable group" requires rank-4 content inside rank-2 G₂. **But the B2 doublet ruling SURVIVES** on the sound G₂→SU(3) branching it actually used. I diverge from my assigned R-1.

**One line:** C16 §3.3 sources **SU(2)_L from SO(4)⊂G₂** and states *"the surviving observable group is SU(3)_C × SU(2)_L × U(1)_Y"* — a **rank-4** group, which **cannot be a subgroup of rank-2 G₂** (computed below), and whose factors come from **two non-commuting maximal subgroups** (SU(3)=Stab(e₁), SO(4)=Stab(ℍ)). So R-1 (my fork) fails and it is **R-3 as written.** The repair exists only via a **non-deposited** literature route (Furey Cl(6); F₄/J₃(𝕆)) where SU(2)×U(1) come from the Clifford/spinor structure, not from SO(4)⊂G₂ — a different construction, Stage-4 work. **The B2 doublet ruling is unaffected**, because it used only the correct G₂→SU(3) branching of the 7, not the SU(2)_L sourcing.

**Stream:** Scratch (second, R-1 owner). **Register:** foundational check. Nothing patched; no Core. No-f.
**Pre-registration:** `Working/PREREGISTRATION_Scratch_G2_Rank_Obstruction_...20261016.md`.
**Method:** rank computed; C16 quoted at current state (read this session), not recalled.

---

## 1. The rank computation (elementary, decisive)
- **rank(G₂) = 2** (G₂ compact, dim 14, rank 2 — standard).
- **rank(SU(3) × SU(2) × U(1)) = 2 + 1 + 1 = 4.**
- A subgroup of a compact Lie group has **rank ≤ rank of the parent**. So a rank-4 group **cannot** be a subgroup of rank-2 G₂.
- Moreover: SU(3) = Stab(e₁) is itself **rank 2**, so it already saturates G₂'s entire Cartan. SO(4) = Stab(ℍ) is a **different** rank-2 maximal subgroup. The two do not commute (their intersection is U(2)⊂SU(3), not a direct-product complement), so **SU(3)_C and SU(2)_L cannot both be commuting gauge factors inside G₂.** The SM requires SU(3)_C and SU(2)_L to commute (direct product); G₂ cannot supply that.

## 2. What C16 actually claims (quoted at current state)
- §3.1: *"Relevant maximal subgroups: SU(3), stabiliser of a complex line in Im(𝕆) … and SO(4)≅(SU(2)×SU(2))/ℤ₂, stabiliser of a quaternionic subalgebra ℍ⊂𝕆."*
- §3.3: *"the corresponding SU(2) is one factor of SO(4)⊂G₂, identified with SU(2)_L. The complex line ℂ=span{1,e₁} gives U(1)_Y. … The surviving observable group is SU(3)_C × SU(2)_L × U(1)_Y."*
So C16 sources **SU(3) from Stab(e₁)⊂G₂** *and* **SU(2)_L from SO(4)⊂G₂** — both inside G₂ — and names their product (with U(1)_Y) as the observable group. That is rank-4 content presented as living in rank-2 G₂, from two non-commuting maximal subgroups.

## 3. Fork disposition
- **R-1 (my assigned fork) — FAILS.** R-1 required SU(2)_L and U(1)_Y to be supplied **from outside** G₂. C16 §3.3 sources SU(2)_L from **SO(4)⊂G₂** (inside). So the "only G₂→SU(3), rest supplied separately" reading is **false to the text.** I report this first.
- **R-3 — HOLDS as written.** The deposited "surviving observable group SU(3)_C×SU(2)_L×U(1)_Y," with SU(3) and SU(2)_L both sourced inside G₂, requires G₂ to deliver rank-4 commuting content, which it cannot. C16 §3's gauge-group assembly fails as written. Confirms Jammer's §G independently (via the rank computation + the two-maximal-subgroup non-commutation).
- **R-2 — available only as a non-deposited repair.** IF SU(2)_L and U(1)_Y are instead sourced from the **Clifford/spinor structure** of ℂ⊗𝕆 (Furey, Cl(6)) or from **F₄=Aut(J₃(𝕆))** (Dubois-Violette–Todorov) — the literature's actual routes — then SU(3)_C×SU(2)_L×U(1)_Y is realised **without** requiring it to sit inside G₂, and the construction is sound. But **C16 §3.3 does not say that**; it says SO(4)⊂G₂. Per the C2 lesson, I do not supply a sound construction the text omits. So R-2 is the **repair path, not the current state.**
- **G₂ → SU(3) alone is correct and survives.** The branching **7 → 1 ⊕ 3 ⊕ 3̄** under G₂→SU(3) is textbook and I concur it is right. The obstruction is specifically the attempt to also get SU(2)_L (and the commuting SM product) from inside G₂.

## 4. The B2 doublet ruling — SURVIVES (AC's specific question (b))
The B2 ruling (2026-09-27: no pre-𝕆 SU(2)_L×U(1)_Y doublet → Higgs inflation structurally unavailable) used **C16 §3's SU(3) decomposition Im(𝕆)=1⊕3⊕3̄** to show no SU(2) doublet sits in Im(𝕆). That decomposition is the **sound G₂→SU(3) branching** (§3 above), **not** the rank-problematic SU(2)_L-from-SO(4) claim. So **B2's basis is intact**: it rests on the correct colour branching, and the rank obstruction does not touch it. AC's 2026-09-29 verification of B2 against §3 stands; the obstruction is in a different sentence of §3 than the one B2 used. **No correction to the B2 entry is forced by this finding.** (The closure record §2.6 and the "gauge group from G₂" simplification in Part 1 line 43 **do** need correction — see §6.)

## 5. A9 status per fork (my required deliverable)
- Under R-1 (did not occur): gauge leg clean.
- Under R-2 (repair path, not deposited): A9's octonion→SM leg becomes **adopted-from-literature via a non-G₂ route**; "gauge group from G₂" is restated; A9 still does not derive M1.
- **Under R-3 (the landing): A9 fails on BOTH legs.** (i) It does not derive M1 — my why-complex-S³ verdict (W-3), now **confirmed** by Cursor's reconstruction-literature leg (complex structure follows only from operational axioms, never from the octonion descent). (ii) It does not deliver the SM gauge group as written — the G₂→SM assembly is rank-impossible. So **A9 is a non-derivation on both the M1 leg and the gauge-group leg**; what survives is the correct, textbook, *adopted* G₂→SU(3) colour branching. The register ruling (reformulation) is unaffected, as AC said, but A9's standing in my Task A axiom spec drops from "conditional posit / candidate route to M1" to **"adopted-from-literature (colour branching only); self-contained NTE derivation on neither leg."** I will update the A9 entry in the axiom spec on AC's word.

## 6. Loci needing correction before deposit (if AC/Greg ratify R-3)
- **C16 §3.3** — "SU(2)_L = one factor of SO(4)⊂G₂" and "the surviving observable group is SU(3)_C×SU(2)_L×U(1)_Y [from inside G₂]": restate — G₂ delivers the **colour factor only**; SU(2)_L and U(1)_Y are adopted from the Clifford/spinor (Furey) or F₄/J₃(𝕆) route, not from G₂.
- **Part 1 line 43** — "the gauge group from G₂" listed as a simplification that "earned its place": regrade to "the **colour** factor from G₂; the electroweak factors adopted from the division-algebra programme."
- **Closure record §2.6 / the axiom-A9 line** — note the gauge-group leg is adopted (colour branching), not a G₂-delivered SM group.
- **B2 entry** — **no change** (§4).

## 7. Routing
- **R-3 as written; R-1 fails; B2 survives; A9 fails both legs.** Converges with Jammer's §G lead (both opposed seats reach R-3) and with Cursor's literature leg on A9's M1 leg.
- **Cursor Main's literature leg** (requested by this directive) will confirm the standard content: G₂⊃SU(3) and 7→1⊕3⊕3̄ are textbook; SU(2)×U(1) in octonionic SM models come from Cl(6)/F₄, **not** from G₂ — which is exactly the repair route and confirms R-3 for the deposit's own construction.
- AC adjudicate (both seats + literature) → Greg ratify the §6 corrections for Stage 3/4. Nothing patched.

— Scratch (second), 2026-10-16. **R-1 fails; R-3 as written** (rank 4 ⊄ rank-2 G₂; SU(2)_L wrongly sourced from SO(4)⊂G₂; two non-commuting maximal subgroups). **G₂→SU(3) and the 7-branching are sound; B2 survives on them.** A9 fails both legs; repair only via non-deposited Cl(6)/F₄ route. Diverges from assigned R-1; converges with Jammer. Routed to AC → Greg.
