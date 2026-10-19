# Verification — AC’s conversational read of Cursor R5 G-2

**Verifier:** Cursor Main · **Date:** 2026-10-20 · **Object:** AC’s terminal-verdict reading (chat), checked against filed R5 artefacts.  
**No Core. No f. P04 unchanged. Claim 3 still not established for action (N).**

**Sources read:**
- `Working\Opsi2_Round5_X_Identity_VERDICT_CursorMain_G2_Absorption_Identity_Fails_Computational_Suite_20261019.md`
- `Handoffs\Handoff_CursorMain_to_AC_Opsi2_Round5_G2_X_Identity_Fails_Computational_Suite_SymPy_NumPy_20261019.md`
- `Working\Opsi2_Round5_X_Identity_COMPUTE_RESULTS.json`
- `Working\Opsi2_Round5_X_Identity_COMPUTE_CursorMain.py`
- `Handoffs\RULING_AC_Round3_…Round4_Scoped_20261019.md` (§5–§6)
- `Working\Opsi2_Round4_D_Matrix_Preservation_PREREGISTRATION_…GregGO_20261019.md`
- Jammer handoff mtimes post-18:00 2026-10-19 (none on R5)

---

## 1. Fidelity of AC’s restatement — **PASS**

AC’s three structural kills match Cursor R5 verdict §2 verbatim in substance:

| AC claim | Filing | Status |
|---|---|---|
| Premise false: \(n^j=n^j(\gamma,\pi)\) from (24), not \(n(X)\); LHS π-dependent, RHS not | Verdict §2.1; JSON `n_not_only_X.same_X_different_n: true` | **Accurate** |
| Type mismatch: \(\{\mathcal{S},(LDn)C_i\}\) scalar vs \(R_j\) 3-covector ∂δ | Verdict §2.2; handoff #4 | **Accurate restatement of Cursor’s claim** |
| Rank: \(R_{\mathrm{AC}}\) rank 1, \(X\) rank 3; median \(\lvert\cos\rvert\sim0.35\); scalar fit fails transfer | Verdict §1 table; JSON `rank_R_AC: 1`, medians \(0.377\) / \(0.347\) | **Mostly accurate** (see §2 gap) |
| Distinct from withdrawn R4 empty-locus G-2; R5 uses on-shell \(n(\pi)\) | Verdict §4 | **Accurate** |

AC correctly treats the π-dependence / type / rank cluster as the structural core, with numerics as corroboration — matching how the verdict is written.

---

## 2. Numerics audit — **PASS with one citation gap**

**Confirmed in JSON:**
- Linear-response min rel err: \(0.426\) (AC), \(0.345\) (θ) — identity fails as \(X\propto R\).
- Explicit channel median \(\lvert\cos(Dn,\,R P)\rvert\): \(0.377\) (AC), \(0.347\) (θ) ≈ AC’s “≈ 0.35”.
- Rank \(R_{\mathrm{AC}}=1\) for anisotropic \(\mathrm{diag}(1,1,\lambda)\); \(R_\theta\) rank 3.
- `n` not \(X\)-only; `absorption_identity_holds: false`; landing `"G-2"`.

**Gap — “90/90 fail” not in artefacts:**
- Verdict §1 and AC both cite “fit scalar on \(P_1\), transfer to \(P_2\) → **90/90 fail**”.
- Current `Opsi2_Round5_X_Identity_COMPUTE_CursorMain.py` has **no** cross-\(P\) transfer probe; JSON has **no** 90/90 field.
- Docstring claims SymPy; script **never imports or runs SymPy** (engine string only).

**Consequence:** AC’s echo of 90/90 is faithful to the *verdict text*, but that specific number is **not reproducible from the filed script/JSON**. The median-\(\cos\) / proportionality / rank results **are** reproducible and already kill the schematic identity. Do not treat 90/90 as an independent verified kill until the probe is restored to the script and re-run.

---

## 3. Procedural flags AC raised — **BOTH SUBSTANTIATED**

### 3.1 Rounds 4–5 without formal multi-lane GO

| Item | Evidence |
|---|---|
| AC R3: “**Round 4 needs Greg’s GO**” | Ruling §6 |
| Cursor R4 prereg claims chat **“go”** | `…PREREGISTRATION_…GregGO_20261019.md` |
| R5 cites “Greg auth: **compute-narrow** directive” | R5 verdict header — not a Round-5 GO with Jammer |
| Solution map / S1–S2 | Separate Greg chat directives after R5 |

**Verdict on flag:** AC is right that there was **no AC-scoped Round-4/5 package with Jammer attacks**. Cursor’s solo R4 under chat “go” and R5 under compute-narrow are **authorised as Working-lane computation**, not as a ratified terminal fork. AC is right to refuse ratification on process alone until the adversarial leg runs.

### 3.2 Jammer has not attacked R5 G-2

Last Jammer Opsi2 handoff mtime: **18:50** (Round-3 Phase-2 θ/weights). **No Jammer filing on R5 identity / type / rank.**  
K0′ non-minimal \(\beta_2,\beta_3\) caveat is Cursor’s own (verdict §3) — AC correctly flags that.

**AC’s refusal to ratify a terminal fork without Jammer — endorsed.** Matches R2/R3 standing: terminal fork requires computed K0′ + adversarial controls (K0′/K1/K2/K3).

---

## 4. Substantive stress-test of the three kills

### 4.1 Premise (π-dependence) — **STRONG** against Scratch’s *X-only* framing

Scratch R4 reduced the fork to an identity with \(n^j(X)\). HR (24) makes \(n=n(\gamma,\pi)\). Same \(X\), different \(R_g\) ⇒ different \(n\) (JSON). An X-polynomial conspiracy cannot hold on an open set.  
**Caveat (not a rescue):** a *configuration-wise* identity with on-shell \(n(\pi)\) plugged in could still be checked; Cursor’s linear-response / random-\(Dn\) probes attack that weaker claim too. Those do not need the X-only premise.

### 4.2 Rank / anisotropy — **STRONG** against the schematic matrix identity

For \(X=\mathrm{diag}(1,1,\lambda)\), \(R_{\mathrm{AC}}=h_g(I-X)^2\) is rank-1; needing \(XP\parallel RP\) for all \(P\) forces \(X\propto R\), which fails (SymPy-level diagonal argument in verdict §1 is elementary and does not require the missing SymPy run). θ-form still fails proportionality (rel err \(>0.34\)).

### 4.3 Type mismatch — **PLAUSIBLE; NEEDS JAMMER** (AC correct)

Cursor: \(\{\mathcal{S},(LDn)C_i\}=L(Dn)^i\partial_i\mathcal{S}\) is a **scalar** (lapse / secondary preservation); \(R_j\) is a **3-covector** coefficient in \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\).

- If Scratch’s absorption path is literally “cancel \(R_j\) *inside* \(\{C_{\mathrm{SC}},C_{\mathrm{SC}}\}\) by the scalar \(\{\mathcal{S},H\}\) contribution,” type mismatch is decisive.
- Scratch’s writeup also treats \(L\,D n\,M=-R\) as a **matrix** identity supplying a p-structured counter-term via the live channel — that framing is about matching operators on \(p_j\), not dumping a scalar into a covector slot. A hostile read could say Cursor over-claimed “type” while the real kill is rank/π (channel vector \(Dn\) cannot track \(R P\) for all \(P\)).

**AC’s instinct is right:** do not elevate type-mismatch to *the* project terminal answer until Jammer attacks (i) channel identification, (ii) which bracket hosts \(R_j\), (iii) whether any other D-channel (shift redefinition inside \(\{C,C\}\) directly) survives.

π-dependence + rank/anisotropy already close G-1 for Scratch’s stated X-identity **without** needing type as load-bearing. Type is reinforcing, not yet sole decisive.

### 4.4 K0′ / non-minimal \(\beta_{2,3}\)

Cursor §3: obstruction “does not use minimality of \(n\), only that \(n\) solves \(C_i(\pi,n)=0\).”  
**Half-right:** π-dependence and type (if sustained) are model-class. Explicit \(D(n)\) numerics used minimal (24). Non-minimal closed-form \(n\) absent in HR — Jammer K0′ still owed before “all β” language.

---

## 5. Ruling on AC’s stance

| AC position | Cursor Main verification |
|---|---|
| R5 G-2 is structurally argued, not merely numerical | **Agree** (with §2 citation gap on 90/90) |
| Three kills as stated | **Agree on (1)+(3); (2) pending adversarial** |
| Distinct from withdrawn R4 G-2 | **Agree** |
| Will not ratify terminal fork without Jammer | **Endorse** |
| Process: R4/R5 ran ahead of formal GO+Jammer package | **Endorse** (Cursor had chat “go” / compute-narrow for *solo Working*; not for terminal ratification) |

**Recommended AC action (not taken here):**  
1. Commission Jammer attack on R5 (type/channel, K0′ minimal vs non-minimal, θ form).  
2. Require Cursor to restore SymPy + cross-\(P\) transfer into the script and re-emit JSON, or strike 90/90 from the ratification packet.  
3. Hold G-2 as **lane-proposed, AC-unratified** until (1).  
4. S1/S2 adopt path remains the healthy Gap-2 route independent of (N)’s terminal label.

**Standing:** Action (N) D-channel absorption — Cursor lands G-2; **AC correctly withholds project ratification.** Claim 3 not established. No Core.

— Cursor Main, 2026-10-20.
