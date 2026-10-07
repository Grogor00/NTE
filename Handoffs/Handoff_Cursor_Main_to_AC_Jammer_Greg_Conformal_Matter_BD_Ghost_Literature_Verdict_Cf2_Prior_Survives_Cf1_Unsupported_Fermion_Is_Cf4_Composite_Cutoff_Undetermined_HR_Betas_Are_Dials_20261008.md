# Handoff — Cursor Main → AC, Jammer, Greg: **conformal-matter BD-ghost literature verdict**

**From:** Cursor Main (literature lane) · **To:** AC, Claude Jammer (attacks), Greg · **Cc:** Scratch, PC · **Date:** 2026-10-08
**Directive:** `Handoffs\Directive_AC_to_Cursor_Conformal_Matter_BD_Ghost_Literature_Check_Jammers_Request_Routed_Late_20261008.md`
**Pre-registration:** `Working\ConformalNeutrino_Lead_PREREGISTRATION_…_Forks_Cf1_Cf4_…_20261008.md`
**Register: literature check. Nothing patched. Sourced. Not a route to κ.**

---

## Verdict against Cf1–Cf4 (as written)

| Fork | Landing | One line |
|---|---|---|
| **Cf1** | **Unsupported** | No fetched paper shows that conformally invariant matter escapes the doubly-coupled BD ghost on a class wide enough for cosmological perturbations. |
| **Cf2** | **Analogy only — not support for the conformal/spinor lead** | 1408.0487 §III.1.2 shows a *scalar* subclass that looks safe on FLRW and ghosts on anisotropic backgrounds. That subclass is **not** conformally invariant. **Nobody in the fetched set analysed conformal matter (or a spinor) under relative shear.** Citing §III.1.2 as support for Cf2 on the lead is **analogy, not support**. |
| **Cf3** | **Partial for scalars; false as written for fermions/conformal** | The paper kills *scalar* double-kinetic coupling. It does **not** already cover fermions or conformal weight. |
| **Cf4** | **Where the lead sits** | Whether a Majorana / first-order Dirac kinetic on two orientation-metrics (or tetrads) is ghost-safe is **not settled in the literature**; needs an original constraint analysis. |

**Amendment (AC R4 / Jammer, 2026-10-08–09):** Earlier draft overstated Cf2 as “best-supported reading.” **Struck.** Cf2 remains Jammer’s *prior*; literature does not *support* it for the conformal/spinor claim. **Cf4 is the correct landing for the lead.** Cf1 is not earned.

---

## Task 1 — arXiv:1408.0487 (Yamashita, De Felice, Tanaka), read in full via ar5iv

**Title:** *Appearance of Boulware-Deser ghost in bigravity with doubly coupled matter*

**What the derivation depends on.** Not conformal weight. The Hamiltonian argument (§III open): when matter has **two kinetic terms** coupled to respective metrics, the conjugate momentum depends on **both lapses**, the kinetic Hamiltonian becomes **nonlinear in both lapses**, and the constraint \(\mathcal{C}\) that removes the BD ghost is lost. Singly-coupled matter is absorbed into a redefinition of \(R_0^{(g)}\) / \(R_i^{(g)}\) and the proof survives.

**Safe exception (proved, §IV).**  
\[\mathcal{L}_m = \sqrt{-g}\,P(X,\phi) + \sqrt{-f}\,\tilde{P}(\phi)\]  
— kinetic on **one** metric only; the second metric sees only a **non-derivative** potential \(\tilde{P}(\phi)\). Hamiltonian remains linear in both lapses.

**Scalar choice: essential to their calculation, not merely illustrative of a general theorem.** The body works exclusively with k-essence scalars \(P(X,\phi)\), \(X = -\tfrac12 g^{\alpha\beta}\partial_\alpha\phi\partial_\beta\phi\). There is **no fermion, spinor, Dirac, Majorana, or conformal-weight** discussion anywhere in the paper. **Struck (AC R4):** earlier draft said *“the spirit of the two-kinetic / two-lapse argument is field-type agnostic.”* That claim is **unsourced** and is **withdrawn**. The paper proves a scalar result; it does not license generalisation to first-order fields.

**FLRW vs anisotropic — analogy for Cf2, not support for the lead.**  
- §III.1.1 FLRW linear: \(\det(\mathcal{A}_{ij})\) can vanish for subclasses including \(\tilde{P}=\tilde{P}(\phi)\) and a spurious \(\tilde{P}=F_1\sqrt{\tilde{X}}+F_2\).  
- §III.1.2 Bianchi-I axial: that subclass has a **non-vanishing** kinetic determinant with **one negative eigenvalue** — BD ghost present.  
- Conclusion (§III.1.2 end): **only** \(\tilde{P}=\tilde{P}(\phi)\) survives in their class.  
- **Scope limit (Jammer):** the §III.1.2 counterexample field is **not** conformally invariant. It does not analyse conformal matter or a spinor under shear.

**Implication for Greg’s option 3.** The conformal-absorption identification is **not in 1408.0487**. Jammer’s later point (adopted by AC): the operative question for a neutrino may be **first-order Dirac structure** (lapse cancellation), not conformal invariance — and that is **outside** this paper’s scope → **Cf4**.

---

## Task 2 — Doubly-coupled fermions

**No paper found that establishes ghost-freedom for independent minimal kinetic couplings of a Dirac/Majorana field to both metrics.**

What exists instead:

| Paper | What it does with fermions |
|---|---|
| **arXiv:1511.01485** (Noller & Melville, *Generalised matter couplings in massive bigravity*) | Treats a **Dirac** field in **mini-superspace** for **composite / effective-vielbein** (rank-2) couplings — not independent double minimal coupling. Finds only rank-2 constructions can be simultaneously healthy for scalars, Yang–Mills **and** Dirac. Rank-0 (overall conformal factor × rank-2) couplings require **traceless \(T_{\mu\nu}\)** / conformal matter and break universal coupling. |
| **arXiv:1505.02616** | Uniqueness of the **composite-metric** non-minimal coupling below the strong-coupling scale — scalars/general matter, not a fermion double-kinetic theorem. |
| **arXiv:1408.0487** | Scalars only. |

**So: fermion double-kinetic on two independent metrics = Cf4.** Composite coupling of a Dirac to one effective metric is a different object and does not answer the lead.

---

## Task 3 — Composite-metric route: 1409.3146 and 1409.3834

### arXiv:1409.3146 (Schmidt-May et al.)
*Mass eigenstates in bimetric theory with matter coupling.*

- **Is it that construction?** **Yes.** Matter couples through the composite effective metric  
  \(G_{\mu\nu} = a^2 g_{\mu\nu} + ab\,(g\sqrt{g^{-1}f}+\cdots)_{\mu\nu} + b^2 f_{\mu\nu}\)  
  (de Rham–Heisenberg–Ribeiro form; \(a,b\) constants).
- Content: EOM trick; proportional backgrounds \(f=c^2 g\) (requires **fixing one parameter**); quadratic spectrum — matter sees the **massless** mode.
- **Cutoff:** not the subject of this paper.

### arXiv:1409.3834 (de Rham, Heisenberg, Ribeiro)
*Ghosts & Matter Couplings in Massive (bi-&multi-)Gravity.*

- **Is it that construction?** **Yes** — same \(g_{\rm eff}\).
- **Ghost status:** On **generic** backgrounds the standard lapse constraint is lost after integrating out the shift → **BD ghost reappears**. Decoupling-limit analysis: **no ghost at the strong-coupling scale** \(\Lambda_3 = (M_{\rm Pl}\,m^2)^{1/3}\).
- **Cutoff:** identified as the scale where the ghost enters; **higher than \(\Lambda_3\)**, **below \(M_{\rm Pl}\)**. Quote (sourced): *“The exact value of the cut-off has not yet been fully determined and it should be established with care…”*
- **Derived value or free?** **Not a derived fixed number.** It is bounded between \(\Lambda_3\) and \(M_{\rm Pl}\) and left undetermined. **For NTE: a free/undetermined cutoff used to keep a construction viable is a dial → no-f / discipline 12(c). Not available as deposit content.**

### Also noted (Jammer’s unread list)
**arXiv:1404.0006** (Akrami, Koivisto, Solomon) — conceptual: double *minimal* coupling → no universal effective Riemannian metric; Finsler quasimetric for point particles. Cites Yamashita / de Rham that minimal double coupling revives the ghost. Does **not** rescue the conformal lead. (Interesting aside: a *massless* scalar *does* admit an effective metric of the form \(\sqrt{-h}\,h^{\mu\nu}=\alpha_g\sqrt{-g}\,g^{\mu\nu}+\alpha_f\sqrt{-f}\,f^{\mu\nu}\); a massive scalar generally does not — parallel to kill criterion 4.)

---

## Task 4 — Hassan–Rosen uniqueness (sourced)

**Source:** S. F. Hassan & R. A. Rosen, *Bimetric Gravity from Ghost-free Massive Gravity*, JHEP 02 (2012) 126, **arXiv:1109.3515**.

- Uniqueness claim (their wording): given earlier dRGT arguments, **“the mass term (4) is the unique interaction term that avoids the Boulware-Deser ghost in the \(g\)-sector with a non-dynamical \(f\).”** They then show the same structure protects the \(f\)-sector when \(g\) is frozen, motivating dynamical bimetric theory with two Einstein–Hilbert kinetics.
- Secondary-constraint completion: **arXiv:1111.2070** (Hassan & Rosen) — explicit secondary constraint; BD ghost absent in that class.
- **Parameters are free:** action has **five \(\beta_n\)** (incl. graviton mass and cosmological constants for both metrics) plus Planck masses \(M_g, M_f\) and mass scale \(m\). Quote: *“The resulting theory has five free parameters, including the graviton mass and the cosmological constants for both \(g_{\mu\nu}\) and \(f_{\mu\nu}\).”*
- **Discipline 12(c):** any NTE use that **fixes** \(m\) or \(\beta_n\) to obtain a desired cosmological / ghost outcome is a dial. The *form* of the potential is unique (up to those coefficients); the *values* are not derived.

---

## Kill criteria from the pre-registration — literature status

| # | Criterion | Literature status |
|---|---|---|
| 1 | Metrics cannot be restricted to a conformal pair without new assumption | **Open threat.** Deposit does not force \(g^-=\Omega^2 g^+\). Hassan–Rosen backgrounds that *are* proportional require parameter fixing (1409.3146). |
| 2 | Relative non-conformal perturbation reintroduces double kinetic | **Supported by 1408.0487 §III.1.2** (anisotropic counterexample). Aligns with Cf2. |
| 3 | Mass on both measures ≠ scalar exception \(\tilde{P}(\phi)\) on one | **Supported.** Exception is kinetic-on-one + potential-on-other. Bilateral \(m\bar\psi\psi\) weighted on both measures is **not** that object; not analysed. |
| 4 | Needs exact masslessness; NTE has massive Majorana | **Open threat.** Conformal invariance of the kinetic survives with mass; the *absorption* argument does not automatically. 1404.0006: massive scalar loses effective-metric description that massless scalar has. |
| 5 | Tunable quantity / no-f | **Composite cutoff undetermined (1409.3834); HR \(m,\beta_n\) free (1109.3515).** Both dials if used to force safety. |

---

## Gate 0 implication (no κ drift)

Greg’s option 3 is **not rescued to Cf1** by the literature.  
**Correct landing for the lead: Cf4.** Cf2 is Jammer’s prior and an *analogy* from a scalar counterexample, not support.  
**Composite route** does not close Gate 0 for deposit: ghost above an **undetermined** cutoff.  
**Hassan–Rosen** supplies the unique *form* of the interaction potential; its **mass scale and \(\beta_n\) are dials**.

Jammer’s trilemma first row is **undetermined for a spinor** (AC R1), not settled by this literature check.

**Next (constructive lane, Scratch; Jammer attacks):** ADM analysis for a Dirac/Majorana with kinetic terms on **two tetrads** — primary lapse-linearity vs secondary constraint / relative Lorentz (openings 1–3). See amend handoff of 2026-10-09 for prior-art status.

---

— Cursor Main, 2026-10-08
