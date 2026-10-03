# Companion 13 — δ_J-sign section (DRAFT for ratification) + apply instructions

**Author:** AC · **For:** Greg (ratify the drafted §6 below; the three repairs are pre-ratified) · **Cc:** CR, Cursor Main (apply on ratification) · **Date:** 2026-07-09
**Purpose:** backs the dangling citation — Parts 2 §X and 3 §XVII cite Companion 13 for "the sign of δ_J is a free within-sector CP-parity," but Companion 13 does not currently discuss it. This section supplies the grounding, in the paper's existing free-spectral-data register.

---

## PART 1 — DRAFTED CANONICAL CONTENT (read + ratify)

### Abstract addition (append to the existing abstract, final sentence)

> The same finite-Dirac openness that leaves the Dirac normalisation unfixed also leaves the sign of the Janus CP-phase δ_J free — a within-sector CP-parity, gauge-redundant across the twin pair. §6 grounds the citation Parts 2–3 make to this companion.

### New section — insert after §5, before the current §6 (Scope)

---

## 6. The sign of δ_J: a within-sector CP-parity, and free spectral data

Part 2 §X fixes the Janus Bogoliubov phase to its maximal magnitude, $|\delta_J| = \pi/2$, from the geometry of the Majorana boundary transformation: the exponential $(1 - e^{-M/\hbar H_{\mathrm{dS}}}) \to 1$ for any leptogenesis-scale mass, so the magnitude is forced with no free parameter. The *sign* of $\delta_J$ is not fixed by that geometry, and the reason is the same finite-Dirac openness that leaves the Dirac normalisation of §3 unfixed.

The magnitude of $\delta_J$ is geometric — it is the maximal Bogoliubov mixing angle of a Majorana mode at the boundary, and geometry supplies an angle, not an oriented one. The sign is a *branch*: it is set by whether the finite Dirac operator carries the neutrino mass matrix $M_\nu$ or its complex conjugate $M_\nu^*$. Under CP the mass matrix maps to its conjugate, so the two branches are CP-images and choosing between them is a within-sector CP-parity. NTE's finite geometry fixes the flux structure of the magnitudes (this paper) but does not select this parity: the operator phase is free spectral data in exactly the sense the absolute Yukawa normalisation is (§3, §6-now-§7). It is, in fact, the *phase*-analogue of the open magnitude — the finite-Dirac computation that would ground any Yukawa magnitude (corpus item 22.4) is the same computation that would fix the mass-matrix phase, and since that computation derives no magnitude, a fortiori it fixes no CP-parity. The sign of $\delta_J$ is not an independent unknown; it is the open finite-Dirac normalisation, read on the phase.

A distinction must be drawn between this within-sector CP-parity and the cross-sector symmetry relating the Janus twins. The pairing symmetry is bilateral CPN ($= N\circ CP$; Part 2 §IX–X), which is cross-sector and, because $\mathrm{CPN} \supsetneq \mathrm{CP}$, is *not* the within-sector CP whose parity is at issue. Bilateral CPN correlates the two twins to *opposite* branches: whichever mass-matrix orientation our sector realises, the conjugate twin realises the other. Two consequences follow, different in kind:

- The **relative** sign is fixed. The twins are opposite — matter sorted to $+N$, antimatter to $-N$ (Part 2 §8.4) — which is precisely the sorting-not-annihilation that lets a maximal asymmetry survive. This is physical, and it is what baryogenesis requires.
- The **absolute** sign is a gauge-redundant label. Which twin is "ours," the one with $B>0$, is a relabelling of the pair — a symmetry, not an observable. There is no fact internal to the framework about which side is matter; a matter-dominated observer is guaranteed to be able to call their side "ours."

The honest scope for the asymmetry is therefore layered. Its **existence and maximality** are zero-parameter: $|\delta_J| = \pi/2 \neq 0$ is forced, so a maximal CP asymmetry is guaranteed to exist. Its **relative** sign across the pair is fixed by bilateral CPN (the sorting mechanism). Its **absolute** sign — the direction of $B$ in our sector — is a free within-sector CP-parity, gauge-redundant across the pair, hence neither predicted nor physical. Its **magnitude** $\eta_B$ is a structural consistency at order unity, not a zero-parameter prediction, inheriting the $O(1)$ residue in $M_1$, the atmospheric-ratio overshoot, and an underived washout efficiency (Part 2 §X; Companion 10). This layered reading is what Parts 2 (§X) and 3 (§XVII) cite here: the sign of $\delta_J$ is a free within-sector CP-parity, not locked to $B$.

The result is falsifiable in one direction only, and correctly so. No measurement of "which side is matter" can bear on NTE, because that label is gauge-redundant — a would-be prediction of the absolute sign would be a category error. What *would* change the status is the finite-Dirac computation of item 22.4: were it to fix the mass-matrix phase, the $\delta_J$ sign would be upgraded from free to derived — by the very same computation that would fix the Yukawa magnitude. The sign of the Janus phase and the neutrino Yukawa normalisation share one open grounding, and they will close together or not at all.

---

### Reference addition (append to References)

> 6. NTE corpus, Part 2 §X (the Janus Bogoliubov phase and $|\delta_J|=\pi/2$) and §IX–X (bilateral CPN, $=N\circ CP$); Part 3 §XVII (the within-sector CP-parity ledger entry).

---

## PART 2 — APPLY INSTRUCTIONS FOR CURSOR (on Greg's ratification)

**Canonical target:** `Core_Papers/Companion_13_Yukawa_Nu2_v10_18_0.md` (Drive ID `1fMxwVY0cArYGNQSbgP2DkLy82v666Bz_`); keep `paper-build/scratch-src/` mirror hash-identical. Verify canonical path first.

**C13-A — insert §6.** Insert the "## 6. The sign of δ_J…" block above **after** the §5 block ("## 5. The first-generation Yukawa (open)" … ending "…not claimed here.") and **before** "## 6. Scope, and the open grounding".

**C13-B — renumber** (byte-exact):
- `## 6. Scope, and the open grounding` → `## 7. Scope, and the open grounding`
- `## 7. Falsifiability` → `## 8. Falsifiability`
- In the abstract/subtitle references and the §2 forward-pointer "the point made precisely in §4" is unaffected; no other in-text "§6"/"§7" cross-refs exist — confirm by grep before/after.

**C13-C — abstract sentence.** Append the abstract-addition sentence (Part 1 above) to the end of the existing Abstract paragraph.

**C13-D — reference.** Append the reference entry (Part 1 above) to the References list as item 6.

**REPAIR 2 (ratified) — Part 2 §X formula line, δ_J → |δ_J|.** In `Core_Papers/NTE_v10_18_0_Part2_Structure.md` §X:
Find: `geometric phase $\delta_J = (\pi/2)(1 - e^{-M/\hbar H_{\mathrm{dS}}})$`
Replace: `geometric phase of magnitude $|\delta_J| = (\pi/2)(1 - e^{-M/\hbar H_{\mathrm{dS}}})$`
(This makes the whole §X δ_J treatment magnitude-consistent; the sign is already handled in the honest-scope sentence.)

**REPAIR 3 (ratified) — Popular editions δ_J-sign pass.** In `Popular_Editions/Popular_Full_Edition_v10_18_0.md` (flagged L296, L358, L366, L390), `Popular_Editions/Popular_Reader_Edition_v10_18_0.md` (L191), and their `paper-build/scratch-src/` mirrors: grep for `existence and sign` and any statement that the sign of δ_J / the asymmetry is fixed, and apply the ratified correction — **existence zero-parameter via $|\delta_J|=\pi/2\neq0$; sign a free within-sector CP-parity, not locked to B** — matching the Part 2 §X honest-scope wording (register-appropriate to the Popular edition). Flag anything that does not map cleanly rather than force it.

**After all edits:** re-run `paper-build/render-all-clean.ps1`; expect PASS across Parts, Companions (incl. C13), and Popular editions. **File** `Handoff_Cursor_to_AC_C13_deltaJ_Section_plus_Repairs_Complete_20260709.md` reporting every string changed and the render result.

— AC, 2026-07-09. Drafted C13 §6 (δ_J sign = free within-sector CP-parity, gauge-redundant across the pair, shares 22.4's open grounding) to back the Parts 2/3 citation; bundled with the ratified §X formula fix and Popular-editions pass for Cursor.
