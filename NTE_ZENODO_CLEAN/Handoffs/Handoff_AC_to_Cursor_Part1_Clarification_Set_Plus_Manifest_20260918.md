# Handoff — AC → Cursor: Part 1 clarification set + manifest corrections

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-18
**Status:** READY TO APPLY. Greg has ratified the manifest §3 correction. All other items are clarifications — no tier movement, no new claims.
**Targets:** `Core_Papers/NTE_v10_19_0_Part1_Foundations.md` (patches 1–8); `NTE_Workflow_Manifest_v10_18.md` (patches M1–M3).
**Render:** Part 1 only, after patches 1–8.

---

## Standing caveat for this run

OLD blocks below were reconstructed into raw markdown from a `read_file_content` call, which returns markdown **escaped**. Apply **byte-exact match-or-report**. If any OLD fails to match, report that block and apply the remainder — do not force, do not fuzzy-match, do not normalise whitespace.

---

## Part 1 — patch 1 (§I, insert after the question sentence)

```
OLD:
This is standard relativity, but it raises a question standard physics leaves unanswered: *what distinguishes entities that accumulate proper time from those that do not?*

NEW:
This is standard relativity, but it raises a question standard physics leaves unanswered: *what distinguishes entities that accumulate proper time from those that do not?*

Two clarifications, since this is routinely mis-stated. First, $ds^2 = 0$ is an invariant we compute about the photon's worldline, not a description of anything the photon undergoes; there is no inertial frame at $c$, so "from the photon's perspective" is undefined rather than degenerate — the limit does not converge. Second, the photon has no four-velocity at all: $u^\mu = dx^\mu/d\tau$ is $0/0$ when $d\tau = 0$, and its four-momentum is null, $k \cdot k = 0$. The photon is not the extreme case of proper-time accumulation; it is the case outside the construction.
```

## Part 1 — patch 2 (§2.2, append new paragraph)

```
OLD:
Exceeding $c$ is not forbidden but geometrically undefined: there is no manifold ahead of the boundary.

NEW:
Exceeding $c$ is not forbidden but geometrically undefined: there is no manifold ahead of the boundary.

**The two uses of c.** The boundary expansion velocity and the four-velocity normalisation share a numerical value but are structurally different statements. A photon's $c$ is a coordinate speed, $dx/dt$. The popular claim that every entity "moves through spacetime at $c$" is the normalisation $|u| = c$ of $u^\mu = dx^\mu/d\tau$ — an identity that follows from choosing $\tau$ as the parameter, and a units convention besides: parameterising by $c\tau$ makes the norm unity. NTE asserts neither as a budget. The "spacetime speed budget" framing, in which spatial motion is traded against motion through time, is not NTE's claim and must not be read into §I or §VII: its trade-off is velocity-dependent and frame-dependent, whereas embedding depth is set by rest energy and is frame-invariant.
```

## Part 1 — patch 3 (§III, append to the zero-coupling paragraph)

```
OLD:
"Null-time" is null *from* time (a saturated value of an existing proper-time measure), not existence in the absence of time.

NEW:
"Null-time" is null *from* time (a saturated value of an existing proper-time measure), not existence in the absence of time. The structural content of null-time is reparameterisation freedom: a massive worldline carries an intrinsic scale along it, whereas a null worldline carries only an affine parameter, fixed up to affine rescaling, so nothing along it is metrically marked. This is the relativistic reading of zero e-fold embedding depth — no embedding, no intrinsic parameter. The two are one fact in different vocabularies.
```

## Part 1 — patch 4 (§III, θ₁₂ currency — Part 3 alignment)

```
OLD:
but not the solar angle: $\sin^2\theta_{12} = 1/3$ is a separate leading-order value from a distinct, still-open route (currently $2.9\sigma$). The two are not one structure; the $\mu$–$\tau$ results do not depend on $\theta_{12}$, and its tension does not undercut them.

NEW:
but not the solar angle: $\sin^2\theta_{12} = 1/3$ was **withdrawn in 2026-08** — its basis was generation democracy assumed in the $\mu$–$\tau$-even plane (TM2 default), not a derivation from deposited $\sigma$-structure, and JUNO's first measurement, $\sin^2\theta_{12} = 0.3092 \pm 0.0087$ (arXiv:2511.14593), excludes it at $3.5$–$3.8\sigma$. Solar mixing is open, gated on the $\sigma\leftrightarrow$generation dictionary. The two are not one structure; the $\mu$–$\tau$ results do not depend on $\theta_{12}$, and its withdrawal does not undercut them.
```

## Part 1 — patch 5 (closing trailer)

```
OLD:
physics faithful to canonical v10.17.7, decontaminated and audit-corrected (β_NTE characterisation withdrawn; n_s/r conditional; octonion gauge group credited as imported; κ as single derivation + closure; positioning + no-numerology embedded).

NEW:
physics current to canonical v10.19.0, decontaminated and audit-corrected (β_NTE characterisation withdrawn; n_s/r conditional on frame-closed K(Φ), Companion 17; $\sin^2\theta_{12} = 1/3$ withdrawn 2026-08 per JUNO; octonion gauge group credited as imported; κ as single derivation + closure; positioning + no-numerology embedded).
```

## Part 1 — patch 6 (§2.1, append after the Schwarzschild sentence)

Closes the velocity-dilation gap. Names the lapse explicitly; velocity dilation enters as **inherited, not derived**.

```
OLD:
Where $|\Phi|^2$ is reduced (a gravitational well), less proper time accrues per e-fold — gravitational time dilation as $|\Phi_{\mathrm{NTE}}|^2$ variation, recovering the Schwarzschild factor $\tau(x)/\tau(\infty) = 1 - GM/rc^2$ to first post-Newtonian order.

NEW:
Where $|\Phi|^2$ is reduced (a gravitational well), less proper time accrues per e-fold — gravitational time dilation as $|\Phi_{\mathrm{NTE}}|^2$ variation, recovering the Schwarzschild factor $\tau(x)/\tau(\infty) = 1 - GM/rc^2$ to first post-Newtonian order.

**What $\beta_{\mathrm{NTE}}|\Phi|^2$ is, in standard terms.** It is a *lapse* on the $N$-foliation. Accordingly $t(N)$ is the proper time of an observer at rest in the comoving frame at $x$ — cosmic time — not proper time simpliciter, and the Schwarzschild recovery above is the static-observer statement. Velocity-dependent dilation is then the ordinary tilt of a worldline relative to the foliation, $d\tau/dt = \sqrt{1-v^2/c^2}$ locally, and is **inherited, not derived**: once the emergent metric is Lorentzian, local special relativity applies unmodified. NTE's derived content here is the *gravitational* piece alone — the identification of the lapse with $\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$. Two observers at the same $x$ with different velocities share a local $|\Phi|$ and are separated by the tilt, not by the field. The preferred foliation is a global slicing, as the comoving frame is in standard cosmology, and introduces no locally preferred frame: the tangent-space metric remains Minkowski and local Lorentz invariance is exact.
```

## Part 1 — patch 7 (§VI, N-thickness frame)

Required by patch 6: with proper time observer-dependent, the thickness must be pinned to the comoving frame or the Janus architecture becomes frame-dependent.

```
OLD:
with thickness at $x$ given by $\int dN/(\beta_{\mathrm{NTE}}|\Phi(x,N)|^2)$ — the same integral that yields proper time.

NEW:
with thickness at $x$ given by $\int dN/(\beta_{\mathrm{NTE}}|\Phi(x,N)|^2)$ — the same integral that yields proper time, evaluated in the comoving frame. The thickness is therefore a property of the geometry at $x$, not of any observer's worldline: a boosted observer's proper time differs by the tilt factor of §2.1, while the thickness traversed does not.
```

## Part 1 — patch 8 (header date)

```
OLD: date: "2026-06 (NTE Corpus v10.19.0)"
NEW: date: "2026-09 (NTE Corpus v10.19.0)"
```

---

## Manifest — patch M1 (§3 Neutrino mixing) — RATIFIED BY GREG 2026-09-18

Part 3 contains no θ₁₃ = 0 claim; its only θ₁₃ entry is the withdrawn `arcsin√(m_μ/3m_τ)` formula. Part 1 §III is correct: μ–τ **reflection** leaves θ₁₃ free; μ–τ **permutation** is what forces θ₁₃ = 0. The snapshot stated the permutation result under the reflection label.

```
OLD: μ–τ reflection fixes θ₂₃ = π/4, θ₁₃ = 0, |δ_J| = π/2 — clean.
NEW: μ–τ reflection fixes θ₂₃ = π/4 and |δ_J| = π/2, and leaves θ₁₃ free (nonzero, ≈8.6° observed) — this is the reflection's advantage over μ–τ permutation, which would force θ₁₃ = 0. Clean.
```

## Manifest — patch M2 (§10, κ-appendix watch-item closure)

Verified 2026-09-18 by direct read of the canonical note: the appendix is present in full.

```
OLD:
**Drafted — application NOT yet verified (check next session):**
- **κ-appendix** ("coefficient survives the variation") for the Kappa_AB note — drafted (`PATCH_KappaNote_appendix_...`); CR called it the top pre-Zenodo item. Not confirmed applied to the canonical Kappa_AB note — verify.

NEW:
**Closed 2026-09-18:**
- **κ-appendix** ("coefficient survives the variation") — **verified present** in canonical `Paper_Kappa_AB_Pedagogical_Note_v10_19_0.md` as "Appendix: the cross-source coefficient survives the variation" (bilateral action; variation to G⁺; the three no-renormalisation facts — fixed internal base, Jacobian cancellation, projector idempotency; averaged s-wave scope paragraph). CR's top pre-Zenodo item is satisfied. No patch required.
```

## Manifest — patch M3 (Last updated line)

```
OLD:
**Last updated.** 2026-08-09 — rev 10.4. Deposit set filename+stamp unify to **v10.19.0** (Core / Popular / Pedagogical; Book deferred). Prior: rev 10.3 (2026-08-03) Session edit manifest + Drive root retarget.

NEW:
**Last updated.** 2026-09-18 — rev 10.5. Part 1 clarification set (lapse / velocity dilation; four-velocity and the two uses of c; null-time as reparameterisation freedom; θ₁₂ currency; trailer and header date). §3 μ–τ reflection θ₁₃ correction (Greg-ratified). κ-appendix watch-item closed — verified applied. Prior: rev 10.4 (2026-08-09) deposit set unify to **v10.19.0**.
```

---

## Notes for Cursor

- **Stale folder IDs.** Manifest §4 lists pre-rebuild IDs for both `Core_Papers/` and `Handoffs/`. The live tree is the one under `NTE_ZENODO_CLEAN`; the superseded `Core_Papers` still holds the `v10_18_0` set. Use the live tree.
- **Today's bulk mtime refresh** across `Handoffs/` and the deposit tree is a Drive sync touch, not content — already confirmed in your own 2026-09-18 scan. Part 2 is unmodified.
- **Part 2 carries the same two defects Part 1 had** (`date: "2026-06"` header and the `physics faithful to canonical v10.17.7` trailer). **Not** in this run — awaiting Greg's word.
- **Not in this run:** the Companion 15 cross-reference proposed in your 2026-09-05 C13 handoff (Step 2). AC recommends declining it; awaiting Greg's ratification either way.

---

— AC, 2026-09-18.
