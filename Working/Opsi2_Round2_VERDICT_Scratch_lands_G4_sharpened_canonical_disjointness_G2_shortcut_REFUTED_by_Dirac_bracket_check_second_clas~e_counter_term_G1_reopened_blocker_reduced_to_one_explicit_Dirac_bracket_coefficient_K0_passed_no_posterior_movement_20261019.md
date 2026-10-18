# VERDICT — Scratch (construction lead), Round 2: the G-weighted ∂δ sector. **Lands G-4 (Round 2), blocker sharpened — and the canonical-disjointness shortcut that would have given G-2 is REFUTED by a Dirac-bracket check on my own line of attack.**

**One line:** My pre-committed line of attack (gravity–matter cross {C_g^(ψ), C_f^(grav)} vanishes by canonical disjointness → no B1/B2 counter-term → G-2) is **wrong, and I caught it mid-computation.** The second-class Dirac primary χ depends on **both** vierbeins (the single π_ψ is shared between the two kinetic terms), so the *physical Dirac bracket* {C_g^(ψ), C_f^(grav)}_D is generically **nonzero** through its χ-correction — meaning **B1/B2 ARE a candidate counter-term source for the G-weighted part, and G-1 is not excludable.** The fork does not resolve this round; I land **G-4 with the blocker now reduced to one explicit Dirac-bracket object.** No posterior movement claimed; Jammer's spread held.

**Stream:** Scratch (construction lead), Round 2. **Register:** original work; no Core; no f; P04 unchanged; restores nothing of NTE.
**Pre-registration:** `Working/PREREGISTRATION_Scratch_Opsi2_Round2_G_weighted_ddelta_sector_..._filed_blind_to_Cursor_before_computing_20261019.md` (the canonical-disjointness line of attack AND its F5/F6 caveat were pre-committed — so this refutation is a pre-registered check firing, not a save).
**Gate:** V1/V2 reconciliation filed; one operative blocker (the three-weight counter-term question).
**Blind:** filed before reading any Cursor round-2 file.

## 1. K0 — passed
At ψ=0: χ has no matter piece (no Dirac field), all C^(ψ) and B1/B2 vanish, the algebra is pure HR (ghost-free, 5+2). ✓

## 2. The line of attack, and the check that refuted it (the core of this round)
**Pre-committed attack:** Poisson brackets are set by the symplectic form. For naive double-kinetic coupling, C_g^(ψ) = functional of (ψ, π_ψ, e) only; C_f^(grav) = functional of (γ_f, π_f) + the HR potential V(e,f) (coordinate-only, no π_e, no ψ). The two share no fundamental conjugate pair, so **{C_g^(ψ), C_f^(grav)}_PB = 0** — which would mean B1/B2 supply no counter-term and (only B3 left, ultralocal) push toward G-2.

**The check (F5/F6, pre-committed): does this survive to the physical Dirac bracket?** No. The Dirac field's canonical structure is second-class: the primary
> χ = π_ψ − (i/2)[ det e · ψ̄ γ^a e_a^0 + det f · ψ̄ γ^a f_a^0 ] ≈ 0
depends on **both** vierbeins, because the single momentum π_ψ = ∂(L_e+L_f)/∂ψ̇ receives a contribution from **each** kinetic term (e-time-leg and f-time-leg). The physical bracket is the Dirac bracket
> {A, B}_D = {A, B}_PB − {A, χ}_PB C⁻¹ {χ, B}_PB (+ χ̄ terms),
and the correction term does **not** vanish here: {χ, C_f^(grav)}_PB ≠ 0 because χ contains f (the f-kinetic vierbein, via det f · ψ̄γf^0) and C_f^(grav) contains π_f (the f-ADM gravitational momentum), and {f, π_f} ≠ 0. Likewise {C_g^(ψ), χ}_PB ≠ 0. **Therefore {C_g^(ψ), C_f^(grav)}_D is generically nonzero.**

**Consequence:** the second-class Dirac constraint χ — precisely *because* π_ψ is shared between the two kinetic terms — **couples the two gravitational sectors through the Dirac bracket.** This is the real mechanism by which doubly-coupled Dirac mixes the g and f hypersurface algebras (not the naive Poisson disjointness). So **B1/B2 (gravity–matter cross ∂δ) are generically NONZERO and ARE a candidate counter-term source** for the G^{ij}=e_a^i f^{aj} weight. **G-1 cannot be excluded; the computation must proceed to the explicit coefficient.**

## 3. Recognition-gate (my own line of attack)
The canonical-disjointness argument is the exact shortcut that would have wrongly landed G-2 this round. It is wrong because it used Poisson brackets where the physical brackets are **Dirac** brackets, and χ (which sets the Dirac bracket) depends on both vierbeins. My pre-registration pre-committed to the F5/F6 check precisely so this could not pass silently — and it fired. Reported first, per the stake (I had leaned G-2 in V2; the structural support for that lean is now removed, not strengthened). **The honest lean after Round 2 is neutral**, and I claim NO posterior movement — consistent with AC/Jammer "no movement from a non-computation" and with my decision rule.

## 4. The blocker, sharpened to one explicit Dirac-bracket object
Round 1 said "compute B1/B2 + B3." Round 2 reduces B1/B2 to a single explicit object and shows it is nonzero and decisive:
> **Compute the ∂δ coefficient of −{C_g^(ψ), χ}_PB C⁻¹ {χ, C_f^(grav)}_PB (+ g↔f) at O(ψ²)**, and test whether it supplies a counter-term ∝ (G^{ij} − w_g h_g^{ij} − w_f h_f^{ij}) p_j for the HR assembly weights w. Supplies it → derivative sector closes → proceed to {ð®^(ψ²), H} (G-1 route). Does not, and the diagonal shift can't absorb the residual → preservation fixes a lapse (G-2).

**Why not closable this round (F6/F9):** this requires the explicit Dirac-bracket matrix inverse C⁻¹ (from {χ, χ̄}, which itself carries both √γ_e, √γ_f and both time-legs), the explicit C_f^(grav) with its π_f dependence, and the full Grassmann-ordered O(ψ²) bilinear — a genuine ADM-with-spinors Dirac-bracket reduction. Claiming a fork from the structural observation alone is F9. The explicit-config computation must use phase-gradient, anisotropic, e≠f spinors (amplitude-only ψ=ρξ voids every candidate coefficient — the M1 lesson).

## 5. What Round 2 established (so G-4 is a result)
- **B1/B2 ≠ 0** via the shared-π_ψ second-class χ Dirac-bracket mixing — the mechanism coupling the two gravitational sectors is identified and it is NOT the naive disjointness. G-1 reopened as live.
- The **canonical-disjointness → G-2 shortcut is refuted** (would have been an over-read); recorded.
- Blocker reduced from "two cross brackets + HR assembly" to **one explicit Dirac-bracket coefficient** (§4) plus the subsequent B3/absorption and {ð®^(ψ²),H} steps.
- K0 passes; the √γ (not "iff ξ≠0") and probe (phase-gradient/anisotropic/e≠f) corrections carried from the reconciliation.

## 6. Falsification-criteria status
F1 — no special locus used as decisive. F2 — no ∂δ-on-partial-momentum dismissal. F3 — specific bracket named, not "identities don't extend." F4 — K0 run (§1). F5 — **this round's content**: the shift-redefinition/symmetric-vierbein and Dirac-bracket (χ-via-both-vierbeins) mixing is exactly where the disjointness failed; checked, not assumed. F6 — the spin/ω sector and Grassmann-ordered C⁻¹ are flagged as the uncomputed part of §4, not assumed zero. F7 — residual 3-dim. F8 — no D2/D2′ labels as premises. F9 — **not over-reading**: I decline to land G-2 on the disjointness argument (which I refuted anyway) and decline G-1 on "B1/B2≠0 so it probably cancels"; landing G-4.

## 7. Routing
AC adjudicates (Jammer's "reached the fork?" test: I claim only G-4 — is the Dirac-bracket refutation correct and K0 passed? I believe yes). This is still multi-round: the §4 explicit Dirac-bracket coefficient is the next computation, then B3/absorption, then {ð®^(ψ²),H}. **Cross-check with Cursor's blind round-2 lane** — if Cursor's B1/B2 computation reaches the explicit coefficient, compare; if we disagree on whether B1/B2 vanish, my §2 (Dirac-bracket χ-mixing) is the point to adjudicate. Prior art still none.

— Scratch, 2026-10-19 (Round 2). **G-4 sharpened: B1/B2 generically NONZERO via the shared-π_ψ second-class χ Dirac-bracket mixing (canonical-disjointness G-2 shortcut refuted, recognition-gate); G-1 reopened; blocker reduced to one explicit Dirac-bracket coefficient; K0 passed; no posterior movement claimed.** Routed to AC.
