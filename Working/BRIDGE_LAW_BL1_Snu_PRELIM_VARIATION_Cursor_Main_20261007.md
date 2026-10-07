# BL-1 preliminary — bilkinetic \(S_\nu\) variation (Cursor Main)

**Date:** 2026-10-07 · **Lane:** Cursor Main (not a substitute for Scratch/Jammer)  
**Status:** Preliminary constructive pass. Does **not** close BL-1. Lands **F-OPEN** with a clear lean to **F-LIN / hot-ν**, not F-AMP.

---

## 1. Action chosen (N1)

\[
\begin{aligned}
S_\nu
&= \frac{i}{2}\int d^4x\,\sqrt{-g^+}\,\bar\nu\,\gamma^\mu_+(x)\,D^+_\mu\nu
+ \frac{i}{2}\int d^4x\,\sqrt{-g^-}\,\bar\nu\,\gamma^\mu_-(x)\,D^-_\mu\nu \\
&\quad - \frac{1}{2}\int d^4x\,\Big(\sqrt{-g^+}+\sqrt{-g^-}\Big)\,M\,\bar\nu\nu .
\end{aligned}
\]

Assumptions (declared): one Majorana spinor; equal weight on both measures; mass \(M\) CPN-even; no \(T_b\) factors; no \(S_{\mathrm{cons}}\).

Full NTE action:

\[
S = S_{\mathrm{EH}}[g^+] + S_{\mathrm{EH}}[g^-] + S_m[g^+,\psi^+] + S_m[g^-,\psi^-] + S_\nu .
\]

---

## 2. Metric variation

\[
G^+_{\mu\nu} = 8\pi G\big(T_m^+ + T_\nu^+\big)_{\mu\nu},
\qquad
G^-_{\mu\nu} = 8\pi G\big(T_m^- + T_\nu^-\big)_{\mu\nu},
\]

where \(T_\nu^\pm\) is the canonical Hilbert stress of \(\nu\) computed with \(g^\pm\) (kinetic piece on that metric + half the mass piece for that measure).

**No term \(\kappa_0 G^\mp\) appears.** The Einstein tensors do not mix. Cross-talk is only through the shared field \(\nu(x)\) that solves a joint EOM.

---

## 3. Joint spinor equation (schematic)

Varying \(\nu\) (Majorana-consistent) yields schematically

\[
i\not D_+\nu + i\not D_-\nu - M\big(1 + \tfrac{\sqrt{-g^-}}{\sqrt{-g^+}}\text{-structure}\big)\nu = 0
\]

(exact measure factors depend on how the two volumes are weighted; under CPN \(g^+=g^-\) this collapses to a single Dirac/Majorana operator with mass \(M\)).

So: **coupled**, yes. **Amplifier on total gravity**, no.

---

## 4. FLRW + CPN

Set \(g^+=g^-=g\), \(T_m^+=T_m^-=T_b\). Then

\[
G_{\mu\nu} = 8\pi G\big(T_b + T_\nu\big)_{\mu\nu}.
\]

Background ratio:

\[
r_{\mathrm{bg}} = \frac{\rho_\nu}{\rho_b}.
\]

For light neutrinos, \(\rho_\nu\sim T^4\) (radiation / hot) after freeze-out, **not** \(\kappa_0/(1-\kappa_0)\rho_b\).  
κ₀ from Hopf/\(Y_{00}\) **does not enter this \(S_\nu\)** unless an extra overlap structure is added to the kinetic/mass terms (not present in N1).

---

## 5. Where κ₀ could re-enter (honest options — not used here)

| Add-on | Effect | Risk |
|---|---|---|
| Project twin baryon stress through \(Y_{00}\) into an effective source | Can recover **C1** with \(\alpha=\kappa_0\) | Must come from a scalar action, not by writing \(T_b\) in \(S\) |
| Einstein-tensor mixing / \(S_{\mathrm{cons}}\) | Recovers **C2** | Ghost / non-fundamental (Phase-0 quarantine) |
| HR potential between \(g^\pm\) | Track B | Separate; may not need \(\nu\) |

N1 alone: **κ₀ absent**; \(r_{\mathrm{bg}}=\rho_\nu/\rho_b\).

---

## 6. Perturbation character (BL-3 preview)

Under deposited CPN (equal temperature) and light \(M\), \(\nu\) is **hot / free-streaming**. Even if one normalised \(\rho_\nu/\rho_b\) to ~5 by hand (forbidden by no-f), it would not be Planck CDM. P2 stands.

---

## 7. Landing (Main preliminary)

- **Not F-AMP** from this \(S_\nu\).  
- Lean: **F-LIN** if a future overlap projects twin *bare* stress at strength κ₀; else **F-NU** as a hot bilateral sector with \(\Delta N_{\mathrm{eff}}\) exposure; Track B still open.  
- Programme fork remains **F-OPEN** until Scratch/Jammer file and AC arbitrates.

---

## 8. What Scratch should improve

1. Fix Majorana / vielbein technicalities on two metrics (spinor bundles).  
2. Decide measure weights from ontology, not convenience.  
3. Attempt an *action-level* Hopf overlap that yields C1 with \(\alpha=\kappa_0\) **without** \(T\)-in-\(S\).  
4. Do not smuggle \(S_{\mathrm{cons}}\).

— Cursor Main, 2026-10-07.
