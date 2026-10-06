# Handoff — AC → PC (+ Cursor): G6/G7/G8 results. The ~40 Mpc figure is not in the corpus at all.

**From:** AC (Claude) · **To:** Claude_PC · **Cc:** Greg, Cursor, Scratch, Jammer · **Date:** 2026-09-25
**Basis:** `Handoff_Cursor_to_AC_G6_G7_G8_Reports_20260925.md`; raw dump `Working\_g6_g7_grep_20260925_OUT.txt`.

---

## G6 — **the answer is not "wrong register". The figure does not exist in the corpus.**

`Core_Papers\` contains **no** `40 Mpc`, no `forty megaparsec`, and no coherence *length*. What it deposits is a coherence **mass**:

> Part 2 §IX, under **Falsifiable prediction**: a mass-dependent DM:baryon variance σ(M) ∝ M^(−1/2) above the **neutrino free-streaming coherence mass M_c ~ 4 × 10¹⁴ M_☉**, with large scatter below it. *"The M^(−1/2) scaling is a generic CLT consequence; the NTE-specific content is its combination with the mean κ ≈ 5.50 and the coherence scale M_c."* Amplitude within one coherence volume: open.

Part 3 echoes it twice, and its falsifier is on **the scaling above M_c**, not on any length.

**So the Book converted a mass threshold into a length, and the corpus never did.** Three reasons that matters more than a tier fix:

1. **The conversion is convention-dependent.** M → R needs an assumed density. At mean matter density (Ω_m ≈ 0.31), 4 × 10¹⁴ M_☉ gives a comoving radius near 13 Mpc — about 27 Mpc across. **Neither is 40.**
2. **It does not match standard free-streaming either.** The neutrino free-streaming length at plausible masses runs to ~100 Mpc, not 40. So the figure reproduces from neither route.
3. **The corpus's own register split is cleaner than the Book's**, and the Book should simply mirror it: the M^(−1/2) scaling is generic CLT, the free-streaming scale is standard neutrino cosmology, and **the NTE-specific content is the combination** — that scaling, about a mean of κ ≈ 5.50, above M_c.

**AC's ruling for PC:** do not re-register the 40 Mpc figure. **Replace it with the coherence mass**, as the corpus states it, in `Chapter_10_The_Silvered_Boundary` §5 and §8 and `Chapter_15_The_Score` §4. If a chapter wants a length for the reader's intuition it must be given as an approximate conversion with the density convention named, and explicitly not as a framework output.

**This also strengthens Ch 10's three-part test rather than weakening it.** The corpus's version — scaling, mean, threshold — is fully falsifiable and survives intact. Only the Book's unit was wrong.

**PC was right to hold.** Had she patched the register and kept the number, the chapter would have carried a figure with no source at a tier that made it look sourced.

---

## G7 — **the corpus is clean, and explicitly so. PC's U1/U2 stand.**

Two deposited files **deny** mediation for the DM bridge, in terms:

- **Part 1 §III:** *"This bilateral support — **not a mediating role** — is the geometric structure on which the dark-matter cross-thickness coupling acts."*
- **Companion 5, abstract:** *"a geometric coupling, **not a particle mediator**."*

No load-bearing "neutrino mediates the coupling" sentence exists in `Core_Papers\` for the cross-thickness mechanism. **The Ch 10 defect is Book-only and not inherited.** U1 and U2 are correct and complete.

**One residual worth a light flag, not a patch.** Part 2 §XI carries *"neutrino-mediated boundary stiffening"* for the Li-7 / ⁷Be channel. Different mechanism, ordinary usage — **but it is the same word with the same subject**, sitting in the corpus while Ch 9 §3 disclaims that word emphatically for the neutrino. That is exactly the cross-file collapse pattern PC identified in §0 of her routing note, one step upstream. AC is **not** proposing a change: the physics is correct and the usage standard. Recording it so that if a future reader or chapter collapses the two, the origin is already on file.

---

## G8 — the Book render lane does not exist

Confirmed: `paper-build\` has no `Book\` configuration. Defaults and scripts hard-code `Core_Papers\`; a grep for `Book\` or `Chapter_` in `paper-build\` returns nothing. Eleven Book `.md` files have **no PDF currency path** once Ch 13, 9 and 10 land.

**AC's position:** this is infrastructure, not a corpus change, and it blocks any Book deposit. Cursor's scoping — a Book defaults file, a `Book\` → `pdf-out` prepare script, and a currency check — is the right shape. **Greg's nod to build it**, then Cursor proceeds; AC sees no reason to withhold.

**Note for whoever builds it:** the manifest's render-currency trap applies here too. "PASS" means built without error, **not** built from latest source. The currency check must compare `.md` and `.pdf` modification times, as the Core_Papers lane does.

---

## Also noted

Cursor re-rendered C17–C20, stale since 2026-09-05 against 2026-09-18 sources. All four now current. That was an unasked catch and a real one — four deposited companions had been carrying PDFs older than their markdown for three weeks.

---

— AC, 2026-09-25.
