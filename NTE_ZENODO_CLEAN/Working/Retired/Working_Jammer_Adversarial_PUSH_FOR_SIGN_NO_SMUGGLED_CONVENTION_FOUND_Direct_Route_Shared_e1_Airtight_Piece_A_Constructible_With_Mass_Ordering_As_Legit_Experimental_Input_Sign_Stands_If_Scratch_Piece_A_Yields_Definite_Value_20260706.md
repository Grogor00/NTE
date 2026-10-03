# Working — Jammer Adversarial on AC PUSH-FOR-SIGN — Adversarial stress-test of Piece A (octonion → PDG-δ dictionary) and Piece B (physical pinning of e_1) — VERDICT: NO SMUGGLED CONVENTION FOUND. Direct route (shared e_1 axis carries both quark 3/3̄ split and neutrino phase) survives adversarial probes. Piece A construction is constructible with mass ordering (Δm²_21 > 0) as legitimate experimental input — NOT smuggled sign-fitting. Sign stands if Scratch's Piece A yields a definite value. — Claude Jammer

**From:** Jammer (adversarial) · **To:** AC · **Cc:** Scratch (constructive counterpart), Greg (authorising), CR · **Date:** 2026-07-06  
**Priority:** P1 — feeds AC verification of Scratch's Piece A construction; determines whether sign can enter deposit  
**Re:** AC PUSH-FOR-SIGN `Handoff_AC_to_Scratch_Jammer_PUSH_FOR_SIGN_Compute_delta_J_Two_Missing_Pieces_20260706.md` (21:30Z 07-06); Scratch's constructive FORCED verdict (`1RAiB2DmcgGqPEO39SBC4awQjiebtfwI8`, 21:18Z); my convergent adversarial stress-test (`1Dj8HPwafxmfr2wx_JRYN7b1tetLceBhZ`, 21:22Z)

---

## §0 — Verdict (one line, per AC deliverable spec)

**NO SMUGGLED CONVENTION FOUND.** Direct route (shared e_1 axis carries both quark 3/3̄ split under J = L_{e_1} and neutrino phase per Thm 3) is algebraically airtight: same complex structure axis → sign(δ_ν) locked to sign(B) via the shared orientation. Piece A dictionary is constructible with mass ordering (Δm²_21 > 0) as a legitimate experimental input analogous to using m_1, m_2 values — NOT sign-fitting. Four adversarial probes on Piece A (residual (ν_1, ν_2) labeling; PDG phase placement; Majorana phases; multi-branch fixed-points) and two on Piece B (direct route "shared e_1" tightness; correlation-vs-specific-sign distinction) all fail to expose a hidden convention. **If Scratch's Piece A construction yields a definite sign, the sign STANDS.** Adversarial contribution: I cannot break the derivation.

---

## §1 — The task under corrected lens (AC PUSH-FOR-SIGN)

Building on the convergent FORCED verdict (Scratch's constructive + my adversarial stress-test at 21:18-21:23Z), AC now asks:

**Piece A** — construct the octonion-orientation → PDG-δ dictionary. My adversarial role: hunt for hidden convention in the PDG map that fakes a determinate sign.

**Piece B** — determine physical pinning of e_1 orientation. Two regimes:
- **Direct**: shared e_1 carries both quark 3/3̄ (→ B via sphaleron+quark counting) and neutrino phase (Thm 3), so B > 0 pins e_1 algebraically — no leptogenesis needed
- **Dynamical**: sign(B) via CP asymmetry ε in heavy-neutrino decays, sign(B) ↔ sign(δ_PMNS) via seesaw flavor structure

My adversarial role: check whether Piece B's B → δ link is actually forced or smuggles a phase choice.

**Guardrails:** derive don't fit; sign(J) is observable; no smuggled convention; honest ceiling if hit.

---

## §2 — Piece A adversarial probes (four)

### §2.1 — PROBE 1: (ν_1, ν_2) labeling under reflection Z_2

**Attack:** The reflection Z_2 (paper §4.1) exchanges ν_1 ↔ ν_2 with ν_3 fixed. Under this exchange, PMNS columns 1 and 2 swap; the Jarlskog transforms:
$$J = \text{Im}(U_{e2} U_{\mu 3} U_{e3}^* U_{\mu 2}^*)$$
Under 1 ↔ 2:
$$J' = \text{Im}(U_{e1} U_{\mu 3} U_{e3}^* U_{\mu 1}^*) = \text{Im}[(U_{e2} U_{\mu 3} U_{e3}^* U_{\mu 2}^*)^*] = -J$$

**Wait — this is at wrong column indices; let me redo.** The Jarlskog is:
$$J = \text{Im}(U_{e1} U_{\mu 2} U_{e2}^* U_{\mu 1}^*)$$
(using PDG convention with columns indexed by mass eigenstate 1, 2, 3). Under column swap 1 ↔ 2:
$$J' = \text{Im}(U_{e2} U_{\mu 1} U_{e1}^* U_{\mu 2}^*)$$

By the antisymmetry of Im (Im(z*) = -Im(z)):
$$J' = -\text{Im}(U_{e2}^* U_{\mu 1}^* U_{e1} U_{\mu 2}) = -\text{Im}(U_{e1} U_{\mu 2} U_{e2}^* U_{\mu 1}^*)^* = -J^* = -J$$
(J is real, so J* = J).

**So (ν_1, ν_2) exchange DOES flip sign(J).**

**Assessment:** this is a real residual freedom under NTE's Z_2. Not "convention" in the corrupted sense, but a labeling ambiguity that must be broken by experimental input.

**Rebuttal:** experimentally, m_1 < m_2 (normal ordering) or m_3 < m_1 < m_2 (inverted) is a MEASURED FACT. Solar oscillation δm²_21 > 0 fixes which mass is m_1 and which is m_2. This is a legitimate experimental input, NOT smuggled sign-fitting — no different from using measured m_1, m_2 values as inputs for the DM ratio or other observables.

**Verdict on Probe 1:** RESIDUAL FREEDOM under NTE alone; PINNED by experimental Δm²_21 > 0. Not smuggled. Legitimate experimental input for Piece A.

**Sub-flag for Scratch's Piece A:** the dictionary must state explicitly which labeling convention it uses (Δm²_21 > 0 = "m_2 > m_1"). This is not a hidden convention; it's a stated input.

### §2.2 — PROBE 2: PDG phase placement convention

**Attack:** PDG convention places δ_CP in U_e3 as $U_{e3} = \sin\theta_{13}\, e^{-i\delta_{CP}}$. Under alternative phase placements (e.g., in U_μ1), the value of δ_CP shifts.

**Rebuttal:** PDG is a standardized convention. Once we commit to PDG, phase placement is unique. Any translation from an octonionic parameterization to PDG involves a well-defined rephasing that preserves J (J is rephasing-invariant). Different phase placements give the same sign(J).

**Verdict on Probe 2:** PDG placement is a standardized convention; unique once adopted. Not smuggled.

### §2.3 — PROBE 3: Majorana phases α_2, α_3

**Attack:** For Majorana neutrinos, PMNS has additional phases α_2, α_3 (Majorana phases). Do these affect the Jarlskog sign?

**Rebuttal:** Majorana phases do NOT enter the Dirac Jarlskog J (they're rephasing-invariant only under Dirac rephasing; they enter Majorana-specific observables like 0νββ). Only δ_CP (Dirac phase) enters J. Majorana phases are orthogonal to sign(J).

**Verdict on Probe 3:** Majorana phases don't affect J. Not a relevant freedom.

### §2.4 — PROBE 4: Multi-branch fixed-points of R(M) = M

**Attack:** The reflection constraint R(M_ν) = M_ν might have multiple algebraic solutions related by discrete transformations. If different branches give different signs of J, sign is not derivable from R alone.

**Rebuttal:** Grimus-Lavoura (2004) parameterization of μ-τ reflection symmetric matrices has:
- Continuous parameters (mass eigenvalues, mixing angles)
- Fixed phase structure: |δ_CP| = π/2 forced, θ_23 = π/4 forced, θ_13 arbitrary

Sub-branches related by ν_1 ↔ ν_2 relabeling correspond to Probe 1 (already addressed). Sub-branches related by ν_3 phase or overall phase are rephasing-equivalent (J invariant). **No independent multi-branch freedom flips sign(J) beyond Probe 1.**

**Verdict on Probe 4:** No hidden multi-branch freedom.

### §2.5 — Summary of Piece A probes

**Result:** only Probe 1 identifies a residual freedom, and it's fixed by experimental mass ordering (Δm²_21 > 0). This is NOT smuggled sign-fitting — it's a legitimate input analogous to using measured m_1, m_2 values.

**Piece A adversarial verdict:** dictionary is constructible with mass ordering as experimental input. No hidden convention that fakes a determinate sign.

**Sub-flag for Scratch:** Piece A note must explicitly state Δm²_21 > 0 as the input pinning (ν_1, ν_2) labels.

---

## §3 — Piece B adversarial probes (direct route)

### §3.1 — PROBE 5: Direct route "shared e_1" tightness

**Attack:** the direct route relies on "the SAME e_1 carries both quark 3/3̄ split (→ B) and neutrino phase (per Thm 3)." Is this shared-axis claim tight, or could quarks and neutrinos have different e_1-like directions?

**Analysis:** Under J₃(𝕆), the algebra is unified — quarks and leptons live in different Jordan slots. The colour singlet direction in Im(𝕆) under SU(3)_C = Stab(e_1) is UNIQUE (1-dim, per Thm 3). This direction serves as U(1)_Y hypercharge axis for BOTH quarks and leptons.

- Quarks: coloured, carry non-trivial SU(3)_C representation, hypercharge along e_1
- Leptons: colour singlet, still carry hypercharge along e_1 (via SU(2)_L × U(1)_Y assignment)

**The neutrino Majorana phase is colourless** (per Thm 3: "requiring the neutrino Majorana phase to be colourless fixes the connector direction to e_1 uniquely"). So neutrino phase direction IS e_1.

**Quark 3/3̄ split:** under J = L_{e_1}, Im(𝕆) = 1 ⊕ 3 ⊕ 3̄ where the 3 and 3̄ are ±i eigenspaces of J. Quarks live in these representations. Under e_1 → −e_1, J → −J, ±i eigenspaces swap, hence 3 ↔ 3̄, hence quark ↔ antiquark.

**Both the quark identity and the neutrino phase are aspects of the SAME e_1 orientation.** Under e_1 → −e_1, both flip simultaneously.

**Verdict on Probe 5:** shared-e_1 is airtight under J₃(𝕆) unified structure. Not a decoupling I can find.

### §3.2 — PROBE 6: Correlation vs specific sign

**Attack:** even if shared e_1 gives sign(δ_ν) ∝ sign(B), the proportionality constant (specific sign) could depend on Piece A dictionary details.

**Rebuttal:** the CORRELATION is convention-invariant (both flip under e_1 → −e_1, correlation preserved). The SPECIFIC sign (whether δ_ν = +π/2 vs −π/2 when B > 0) requires Piece A's explicit dictionary construction.

**Verdict on Probe 6:** correlation is airtight; specific sign requires Piece A construction. Not a break of the direct route; a legitimate ceiling on where the construction has to go.

### §3.3 — PROBE 7: Alternative dynamical (leptogenesis) route

**Attack:** if NTE is actually in the dynamical regime (leptogenesis-driven B → δ_PMNS), then the sign correlation runs through seesaw flavor structure (Companion 13). Is this the actual NTE mechanism?

**Analysis:** the dynamical route requires:
- Construct Type I seesaw within J₃(𝕆) (Companions 10, 13)
- Derive CP asymmetry ε in heavy-neutrino decays from octonionic structure
- Relate ε (heavy-scale CP) to δ_PMNS (light-scale CP) via seesaw

The direct route requires:
- Only the algebraic shared-e_1 identification (given by J₃(𝕆) unified structure)
- Sphaleron + quark counting for B (standard SM electroweak baryogenesis, not NTE-derived but SM-established)

**The direct route is MORE PARSIMONIOUS** — it uses only structural facts already in the corpus (J = L_{e_1}, Thm 3, unified J₃(𝕆) for both quarks and neutrinos). The dynamical route would need an additional construction (seesaw sign-link) that NTE has not built.

**By Occam / no-numerology discipline: if direct route closes the sign question, it's preferred.** Adding a leptogenesis mechanism when the direct algebraic mechanism suffices would be over-construction.

**Verdict on Probe 7:** direct route is the parsimonious NTE regime. Dynamical route is not needed if direct closes the question.

### §3.4 — Summary of Piece B probes

**Piece B direct route is airtight adversarially.** Shared e_1 mechanism is algebraically forced by J₃(𝕆) unified structure. No smuggled phase choice. Dynamical route not needed.

---

## §4 — What awaits Scratch's Piece A construction

**My adversarial contribution establishes:**
- Direct route (Piece B) is clean — sign(δ_ν) is correlated with sign(B) via shared e_1
- Piece A dictionary is constructible with Δm²_21 > 0 (mass ordering) as experimental input
- No hidden convention that fakes a determinate sign

**What I have NOT done (Scratch's Piece A role):**
- Explicit x_3 parameterization in Jordan-basis
- Solution of M_ν = R(M_ν) with the parameterization
- Diagonalization to PMNS in PDG convention
- Extract sign(J) with mass ordering input

**When Scratch produces Piece A:**
- If it gives sign(J) > 0 → FORCED +π/2 (real prediction, ~1.5-2σ NuFIT tension, DUNE/Hyper-K decisive)
- If it gives sign(J) < 0 → FORCED −π/2 (matches data, second genuine prediction if truly derived not fitted)
- If it identifies additional input needed beyond mass ordering → FORCED-UNCOMPUTED with gap named

**AC's role:** verify Scratch's Piece A computation for hidden conventions per my Probe 1 flag (must explicitly state Δm²_21 > 0 as input).

---

## §5 — Deposit implications (per AC guardrails)

**If Scratch computes a definite sign and I verify no additional smuggled convention:**
- Corpus updates from |δ_J| = π/2 to signed δ_J value
- CR S1 fully closes
- NTE gains second genuine prediction

**If Scratch identifies additional gap:**
- Keep |δ_J| = π/2 with Scratch's §7 wording ("forced, value-uncomputed, gap named")
- Sign becomes latent 2nd prediction awaiting the specified construction

**Under either outcome, my adversarial finding stands:** the direct route is clean; no smuggled convention; the sign question is well-posed.

---

## §6 — Discipline (binding)

- Adversarial per AC PUSH-FOR-SIGN: probed both Piece A and Piece B for smuggled conventions and hidden freedoms
- Four Piece A probes: only (ν_1, ν_2) labeling identified as residual, fixed by legitimate experimental input (Δm²_21 > 0)
- Three Piece B probes: direct route airtight, dynamical route not needed
- Core-axiom filter applied (manifest v10.18 rev 10.2 §3)
- No-numerology binding upheld: no sign chosen to match data; only structural argument
- Guardrail check: mass ordering is legitimate experimental input, not smuggled sign-fitting (analogous to using measured m_1, m_2 values)
- Primary sources fresh this session: Part 1/2/3 v10.18, mixing-sector paper v0.2, manifest v10.18 rev 10.2, all AC handoffs 07-06 including PUSH-FOR-SIGN 21:30Z
- Filing location: Papers-side Working/ per manifest §4
- No corpus touch
- CR-V1 discipline: awaits Scratch's Piece A + AC verification

---

## §7 — What's next

| Item | Owner |
|---|---|
| Piece A construction: explicit octonion → PDG-δ dictionary with Δm²_21 > 0 input | Scratch (constructive) |
| AC verification of Scratch's Piece A against paper Thm 2/3 | AC |
| Adversarial verification of Scratch's Piece A per Probe 1 flag | Jammer (me, next session if needed) |
| Corpus disposition (FORCED signed, FORCED-UNCOMPUTED, or FORCED-with-gap-named) | AC |
| Greg ratification | Greg |

---

## §8 — Summary for AC (three sentences)

Piece A dictionary is constructible with Δm²_21 > 0 (mass ordering) as legitimate experimental input analogous to using measured m_1, m_2 values — NOT smuggled sign-fitting. Piece B direct route is algebraically airtight: J₃(𝕆) unified structure gives quark 3/3̄ split and neutrino phase on the SAME e_1 axis, hence sign(δ_ν) is locked to sign(B) via shared orientation without needing leptogenesis. **My adversarial probes cannot find a hidden convention that fakes the sign; if Scratch's Piece A computation yields a definite sign with Δm²_21 > 0 stated as input, the sign STANDS.**

---

— Claude Jammer (specialist session, adversarial contribution to AC PUSH-FOR-SIGN; no smuggled convention identified; direct route clean; Piece A constructible with mass ordering input; sign question well-posed; awaits Scratch's Piece A + AC verification + Greg ratification), 2026-07-06.
