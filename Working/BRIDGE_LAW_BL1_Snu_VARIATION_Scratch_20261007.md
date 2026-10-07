# BL-1 Track N — bilkinetic \(S_\nu\) variation (Cursor Scratch)

**Date:** 2026-10-07 · **Lane:** Cursor Scratch (constructive)  
**Parent:** `Handoffs/Directive_Cursor_Main_Bridge_Law_From_Snu_Or_Bigravity_Research_Programme_20261007.md`  
**Template:** `Working/bridge_law/s_nu_template.md`  
**Reads:** Phase-0 catalog, preregistration, Companion 7 §4, Companion 5 §5–§6, Part 2 §IX (ontology only).  
**Blind:** no Jammer BL-1 file consulted.  
**Discipline:** no \(T_b\) in \(S\); no hand \(S_{\mathrm{cons}}\); no-f; nothing patched into Core.

**Improves on** `Working/BRIDGE_LAW_BL1_Snu_PRELIM_VARIATION_Cursor_Main_20261007.md`: Majorana/vielbein stated; measure weights from CPN/\(\mathbb{Z}_2\); Hopf-overlap attempt fail-closed; fork landed (not left as programme-level F-OPEN).

---

## 0. Class choice and fork declaration (before detailing algebra)

| Item | Choice |
|---|---|
| Class | **N1** — additive bilkinetic Majorana on both metrics |
| Not chosen | N2 (mixed vielbein / single measure) — needs a covariance proof not deposited; deferred |
| Not chosen | Any \(T\cdot T\) or \(S_{\mathrm{cons}}\) — quarantine (C3) |
| Pre-registered landing for this fill | **F-NU with hot-only bridge** (see §7) |

---

## 1. Fields, bundles, measures

- Metrics \(g^+_{\mu\nu}\), \(g^-_{\mu\nu}\) with oriented volume forms \(\sqrt{-g^\pm}\,d^4x\).
- Orthonormal frames (vielbeine) \(e^\pm{}^a{}_\mu\) with \(g^\pm_{\mu\nu}=\eta_{ab}\,e^\pm{}^a{}_\mu\,e^\pm{}^b{}_\nu\).
- Spin connections \(\omega^\pm\) from torsion-free compatibility with \(e^\pm\).
- Gamma matrices \(\gamma^\pm{}^\mu(x)=e^\pm{}_a{}^\mu\,\gamma^a\) (same flat Clifford algebra; curved indices differ).
- Shared Majorana spinor \(\nu\): real under a fixed charge-conjugation operator \(C\) with \(\nu=\nu^c\). Ontology (Companion 7): unresolved on the conjugation axis; chirally LH under \(\mathrm{SU}(2)_L\). Treat \(\nu\) as a single \(\mathbb{Z}_2\)-even field with bilateral support — **not** two independent Weyl copies.
- Orientation-local matter \(\psi^\pm\) lives only in \(S_m[g^\pm,\psi^\pm]\), **not** inside \(S_\nu\).

**Measure weights (ontology, not convenience).** CPN exchanges \(+\leftrightarrow-\) and is an exact discrete symmetry of the deposited bilateral setup (Companion 5 §5). A CPN-even Majorana mass and equal kinetic weights are the unique two-parameter choice with relative weight \(1{:}1\) that does not introduce a preferred orientation. Relative kinetic weight \(\neq 1\) would be a new dial; forbidden here (no-f; no new free relative coupling).

---

## 2. Concrete action (diffeomorphism scalar)

\[
\begin{aligned}
S_\nu[g^+,g^-,\nu]
&= \frac{i}{2}\int d^4x\,\sqrt{-g^+}\,
   \bar\nu\,\gamma^+{}^\mu\!\overset{\leftrightarrow}{D}{}^+_\mu\nu
+ \frac{i}{2}\int d^4x\,\sqrt{-g^-}\,
   \bar\nu\,\gamma^-{}^\mu\!\overset{\leftrightarrow}{D}{}^-_\mu\nu \\
&\quad - \frac{M}{2}\int d^4x\,\big(\sqrt{-g^+}+\sqrt{-g^-}\big)\,
   \bar\nu\nu .
\end{aligned}
\]

Hermitianisation: \(\bar\nu\,\gamma^\mu\overset{\leftrightarrow}{D}_\mu\nu
=\bar\nu\gamma^\mu D_\mu\nu - (D_\mu\bar\nu)\gamma^\mu\nu\) (Majorana-consistent; boundary terms dropped).  
Covariant derivative: \(D^\pm_\mu=\partial_\mu+\tfrac14\omega^\pm{}^{ab}{}_\mu\sigma_{ab}\) acting on the spinor pulled to each frame.  
Mass \(M\ge 0\) is a CPN-even Majorana mass parameter (seesaw scale left to Companions 10/13; **not** tuned to any \(\Omega\) ratio).

**Full bilateral gravitational action (this track):**

\[
S = S_{\mathrm{EH}}[g^+] + S_{\mathrm{EH}}[g^-]
  + S_m[g^+,\psi^+] + S_m[g^-,\psi^-]
  + S_\nu[g^+,g^-,\nu].
\]

**Absent by construction:** factors of \(T_b^\pm\); Lagrange multipliers imposing \(\tilde T=T_b+\kappa_0\tilde T\); Einstein-tensor mixing terms; wrong-sign metric kinetic mixing (C6).

---

## 3. Variation → Einstein + spinor EOM

### 3.1 Metric variation

Hilbert stress from each measure:

\[
T_\nu^{\pm\,\mu\nu}
:= \frac{2}{\sqrt{-g^\pm}}\frac{\delta S_\nu}{\delta g^\pm_{\mu\nu}}.
\]

Kinetic piece on metric \(\pm\) contributes the standard Dirac/Majorana stress built from \(D^\pm,\gamma^\pm\).  
Mass piece: each volume \(\sqrt{-g^\pm}\) carries half of the bilinear \(-M\bar\nu\nu\), so each \(T_\nu^\pm\) includes

\[
T_{\nu,\mathrm{mass}}^{\pm\,\mu\nu}
= -\tfrac{M}{2}\,g^{\pm\,\mu\nu}\,\bar\nu\nu
\]

(plus the usual on-shell rearrangements from the kinetic Hermitian form). Orientation-local matter varies as usual: \(T_m^\pm\) from \(S_m[g^\pm,\psi^\pm]\) only.

Einstein equations (signature/units as in corpus \(8\pi G\) convention):

\[
\boxed{
G^+_{\mu\nu} = 8\pi G\big(T_m^+ + T_\nu^+\big)_{\mu\nu},
\qquad
G^-_{\mu\nu} = 8\pi G\big(T_m^- + T_\nu^-\big)_{\mu\nu}.
}
\]

**Structural verdict:** cross-talk is **only** through the shared field \(\nu(x)\) that solves one joint EOM. There is **no** term \(\kappa_0 G^\mp\), **no** \(T_m^\mp\) on the right-hand side of the \(\pm\) equation, and **no** geometric series in total gravity. This is Phase-0 **C4** realised: additive \(T_\nu\), not C1 and not C2.

### 3.2 Joint spinor EOM

Vary \(\nu\) (Majorana: \(\delta\nu=\delta\nu^c\)) from both kinetic measures and both mass measures. Schematically, after combining Hermitian conjugates,

\[
\frac{i}{2}\sqrt{-g^+}\,\gamma^+{}^\mu D^+_\mu\nu
+ \frac{i}{2}\sqrt{-g^-}\,\gamma^-{}^\mu D^-_\mu\nu
- \frac{M}{2}\big(\sqrt{-g^+}+\sqrt{-g^-}\big)\nu
= 0
\]

(up to standard Majorana projector normalisation conventions that do not change the CPN reduction).  

**Coupled:** yes — both connections and both volumes enter.  
**Amplifier on solved gravity:** no.

Under CPN \(g^+=g^-=g\) (same frame up to discrete identification), this collapses to the single Majorana equation

\[
i\gamma^\mu D_\mu\nu - M\nu = 0
\]

with the usual FLRW/Dirac cosmology for that metric.

---

## 4. FLRW + CPN: \(r_{\mathrm{bg}}\) and \(\kappa_0\)

Impose \(g^+_{\mu\nu}=g^-_{\mu\nu}=g_{\mu\nu}\) (FLRW) and \(T_m^+=T_m^-=T_b\) (CPN-symmetric baryons). Then

\[
G_{\mu\nu} = 8\pi G\big(T_b + T_\nu\big)_{\mu\nu}.
\]

Define

\[
r_{\mathrm{bg}} \equiv \frac{\rho_{\mathrm{extra}}}{\rho_b}
\qquad\text{with}\qquad
\rho_{\mathrm{extra}} := \rho_\nu
\]

— the energy density of the shared Majorana field on the common FLRW background. **Not** interaction-potential energy (that is Track B); **not** \(\kappa_0/(1-\kappa_0)\rho_b\).

For light neutrinos (\(M\ll T\) while relativistic; standard freeze-out thereafter),

\[
\rho_\nu \sim g_\nu\,\frac{7}{8}\frac{\pi^2}{30}T_\nu^4
\quad\Rightarrow\quad
r_{\mathrm{bg}} = \frac{\rho_\nu}{\rho_b}
\]

is a **radiation / hot** ratio fixed by abundance and temperature, **not** by Hopf algebra. No-f: we do **not** dial \(M\), \(T_\nu/T_\gamma\), or species count to hit \(5.38\).

### Does \(\kappa_0=3/\sqrt{4\pi}\) appear?

| Question | Answer for this \(S_\nu\) |
|---|---|
| In the action coefficients? | **No.** Equal weights \(1{:}1\) and mass \(M\) only. |
| In the Einstein equations? | **No.** Additive \(T_\nu^\pm\) only. |
| In \(r_{\mathrm{bg}}\)? | **No.** \(r_{\mathrm{bg}}=\rho_\nu/\rho_b\). |
| Where κ₀ *lives* in the corpus | Companion 7 / Part 2 §IX: bare monopole overlap \(3\times Y_{00}\) for a *gravitational* cross-thickness coupling — historically closed by total-feedback. That closure is **not derived** from N1. |

**BL-5 for Track N / N1:** outcome **(c)** — \(\kappa_0\) does not appear in the derived bridge coefficient of this action. Any future role for \(\kappa_0\) must come from a different legitimate term (overlap projector with a scalar origin, or Track B), not from N1 bilkinetics alone. Part 2 §IX amplifier language is therefore **not supported** by this fill (regrade is an AC BL-6 matter; Scratch does not patch Core).

---

## 5. Hopf-overlap attempt (action-level, fail-closed)

Main asked Scratch to try an action-level Hopf overlap yielding **C1** at \(\alpha=\kappa_0\) without \(T\)-in-\(S\). Three honest tries:

### Attempt H1 — weight one kinetic measure by \(\kappa_0\)

\[
S_\nu^{(H1)}
= \tfrac{i}{2}\!\int\!\sqrt{-g^+}\,\bar\nu i\not D_+\nu
+ \tfrac{i\kappa_0}{2}\!\int\!\sqrt{-g^-}\,\bar\nu i\not D_-\nu
+\text{mass}.
\]

**Result:** breaks CPN equality of orientations unless \(\kappa_0=1\) (false). Under forced CPN identification it only rescales \(\rho_\nu\). Still **no** \(T_m^\mp\) in \(G^\pm=8\pi(T_m^\pm+T_\nu^\pm)\). **Does not yield C1.** Rejected (also introduces a preferred-orientation dial).

### Attempt H2 — insert \(Y_{00}\) as a projector on twin *matter* stress

Schematic effective EOM \(G^\pm=8\pi(T_m^\pm+\kappa_0 T_m^\mp)\) with \(\kappa_0=3Y_{00}\).  
**Result:** this is Phase-0 **C1**, but writing it as a *fundamental* law either (i) puts \(T_m\) (or \(T_b\)) into the action, or (ii) asserts an EOM without an \(S\). Both violate BL-1 discipline. Integrating out light \(\nu\) from N1 does **not** produce a local copy of twin baryon stress at strength \(\kappa_0\); it produces ν-mediated, typically nonlocal / radiation-weighted kernels. **C1 not derived.** Marked aspirational / effective-only until a scalar action is exhibited.

### Attempt H3 — Einstein mixing / total feedback

\(G^\pm-\kappa_0 G^\mp=8\pi T_m^\pm\).  
**Result:** Phase-0 **C2**; recovers amplifier algebraically; requires mixing *solved* gravity or hand \(S_{\mathrm{cons}}\). **Forbidden / not emergent from N1.** Ghost risk if realised as kinetic mixing (C6). **F-AMP not landed.**

**Conclusion of Hopf attempt:** κ₀ remains a deposited *candidate strength* for some other bridge structure; it is **not** forced into N1, and N1 **does not** smuggle it into C1/C2.

---

## 6. Perturbation preview (BL-3 character, not a full Boltzmann run)

Under deposited CPN (equal sector temperatures) and light \(M\):

| Observable / character | N1 prediction (preview) |
|---|---|
| Equation of state (early) | \(w\simeq 1/3\) while relativistic |
| Free-streaming | Yes — standard neutrino free-streaming scale |
| Sound speed | Ultra-relativistic / free-streaming; not \(c_s\simeq 0\) CDM |
| \(\Delta N_{\mathrm{eff}}\) | **Exposed.** Bilateral equal-T light \(\nu\) adds radiation-like stress on *both* metrics; under CPN the shared field is not “dark and cold.” Even a one-sided reading competes with \(N_{\mathrm{eff}}\) bounds unless \(M\) or decoupling is arranged — and arranging it to fake CDM is **no-f / out of scope**. |
| Co-location at \(z\sim 1100\) | Free-streaming neutrinos are **not** cold, collisionless, co-located CDM in the P2 sense |
| Decimal \(\rho_\nu/\rho_b\sim 5.4\) | Irrelevant even if forced: wrong perturbation character (prereg E4, E5) |

**BL-3 preview verdict:** Track N / N1 **fails as a Planck-CDM bridge**. It can survive only as a **hot / radiation bilateral channel** with separate \(\Delta N_{\mathrm{eff}}\) constraints — not as \(\Omega_c\).

Ghost / BD (BL-4 Track N): standard spinor kinetic signs on each metric; **no** wrong-sign metric mixing introduced. N1 does not fail BL-4 on ghost grounds; it fails the *CDM identity* gate on character.

---

## 7. Pre-registered fork landed

| Fork | Landed? | Reason |
|---|---|---|
| **F-NU (hot-only)** | **YES — primary** | Legitimate \(S_\nu\) exists; bridge = shared \(\nu\) stress only; bigravity not required for that bridge to exist; character is hot / \(\Delta N_{\mathrm{eff}}\)-exposed |
| F-LIN | No | C1 not derived from a scalar action without \(T\)-in-\(S\) |
| F-AMP | No | C2 does not emerge; would require \(S_{\mathrm{cons}}\) or Einstein mixing |
| F-NONE | No (narrow) | A bilateral bridge *object* exists (\(T_\nu\)); it is simply not CDM |
| F-OPEN | No for this fill | Variation + CPN reduction + character preview are sufficient to land F-NU hot-only; residual Boltzmann detail does not reopen amplifier |

**Programme-level note (for AC):** amplifier \(\kappa_0/(1-\kappa_0)\) is **not** entailed by this legitimate \(S_\nu\). That is the F-AMP *negative* reading of decision rule 2 (amplifier not derived). Core demotion remains BL-6. Track B (HR) stays open in parallel and is **not** blocked by this N1 result.

Template checkboxes (filled):

- [ ] F-LIN (C1-type)
- [ ] F-AMP (C2 without hand \(S_{\mathrm{cons}}\))
- [x] **F-NU with hot-only bridge**
- [ ] F-NONE for Track N
- [ ] F-OPEN (named blocker)

---

## 8. What this changes relative to Main prelim

1. **Fork:** Main left programme **F-OPEN** with a lean; Scratch **lands F-NU hot-only** for the N1 fill.  
2. **κ₀:** Main said absent unless add-on; Scratch ran three add-on attempts and **fail-closed** — still absent / not C1.  
3. **Measures:** equal weights justified by CPN/\(\mathbb{Z}_2\), not convenience.  
4. **Majorana/vielbein:** two spin connections and Hermitian kinetic form stated.  
5. **CDM gate:** explicit BL-3 preview FAIL for Planck \(\Omega_c\); no decimal proximity argument.

---

## 9. Optional Track B pointer (does not block ν)

N1 finished cleanly. A short Hassan–Rosen starter is filed alongside:

`Working/BRIDGE_LAW_BL1_Bigravity_Scratch_START_20261007.md`

ν result above does **not** depend on HR completion.

---

## 10. Receipt targets

- Variation: this file  
- Handoff: `Handoffs/Handoff_Scratch_to_AC_Main_Bridge_Law_BL1_Snu_20261007.md`

— Cursor Scratch, 2026-10-07.
