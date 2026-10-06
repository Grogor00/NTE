# AC → Greg: patch register, **Part 2** — mojibake in the canonical file, plus two live N-3 items. Pre-deposit.

**From:** AC (Claude) · **To:** Greg (ratification) · **Cc:** Cursor Main, PC, Scratch, Jammer · **Date:** 2026-09-28
**Source:** `Core_Papers\NTE_v10_19_0_Part2_Structure.md`, **read in full this session** — first systematic pass since Door B.
**Status: DRAFT. Nothing patched.** Item 1 is a **deposit blocker**.

---

## First, what is already correct — Part 2 came through Door B well

**§8.1's *"and the Higgs"* cut is applied.** **§8.2–8.3's T_GB regrade is applied**, with the T_max ≈ 2.2 × 10¹⁵ GeV cap and the open-sector pointer. **§XII's DESI language is corrected** — the 3.1σ figure is now stated as a frequentist DESI+CMB model preference, not a DESI-alone exclusion, with the Bayesian counterpoint. **§XVI** correctly marks the RT 1/4 coefficient as underived. **§IX's κ derivation** reads clean, with "one structural derivation followed by one algebraic closure" and the "two pathways" framing explicitly withdrawn.

---

## Item 1 — **MOJIBAKE in the canonical file. Deposit blocker.**

**§8.5–8.6 contains three corrupted octonion glyphs.** The character 𝕆 has been mis-decoded, appearing as `ð\u009d\u0095\u0086`:

> *"the unit sphere of the quaternionic subalgebra ℍ ⊂ **ð**𝕆-corrupt that survives the **ð**𝕆-corrupt → ℍ associativity transition"* … *"that remains J₃(**ð**𝕆-corrupt)"*

**Three instances, all in the parenthetical added by the S³-grounding patch.** The surrounding text uses `$\mathbb{O}$` correctly, so this passage was inserted as raw Unicode and lost its encoding somewhere in the apply chain.

**Why this blocks the deposit:** it is in `Core_Papers\`, in the paper that carries the gauge-group derivation, and it will render as garbage in the PDF. **A Zenodo deposit records the version as it stands.**

**Repair — replace the three corrupted glyphs with the LaTeX form used everywhere else in the section:**

```
OLD: it is the unit sphere of the quaternionic subalgebra ℍ ⊂ [corrupted] that survives the [corrupted] → ℍ associativity transition
NEW: it is the unit sphere of the quaternionic subalgebra $\mathbb{H} \subset \mathbb{O}$ that survives the $\mathbb{O} \to \mathbb{H}$ associativity transition
```
```
OLD: that remains J₃([corrupted]).
NEW: that remains $J_3(\mathbb{O})$.
```

**Cursor: read the actual bytes and match on them** — AC is reading through a decoding layer and cannot guarantee the on-disk byte sequence. **Match-or-report, and report the bytes found.**

**And sweep the whole corpus for the same corruption** — this passage was applied by the same chain as other patches, so `Core_Papers\`, `Book\` and `Popular_Editions\` should all be checked for mis-decoded 𝕆, ℍ, ℝ, ℂ, and the Greek and arrow glyphs.

## Item 2 — §XII contradicts §IX on the DM variance. **N-3 item, confirmed live.**

**§XII, live:** *"One mechanism, H(x,N)=β_NTE|Φ(x,N)|² with spatially varying |Φ|, still yields the Hubble-tension signature (§XIII) **and the DM variance (§IX)**."*

**§IX, live:** *"The M^{−1/2} scaling is a **generic CLT consequence**; the NTE-specific content is its combination with the mean κ ≈ 5.50 and the coherence scale M_c."*

**These attribute the same prediction to different origins** — spatial |Φ| variation versus the central limit theorem. §IX is correct; §XII's cross-attribution is the error.

```
OLD: One mechanism, $H(x,N)=\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$ with spatially varying $|\Phi|$, still yields the Hubble-tension signature (§XIII) and the DM variance (§IX); it does **not** reproduce DESI DR2's $(w_0>-1,\,w_a<0)$ pattern.
NEW: One mechanism, $H(x,N)=\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$ with spatially varying $|\Phi|$, still yields the Hubble-tension signature (§XIII); it does **not** reproduce DESI DR2's $(w_0>-1,\,w_a<0)$ pattern. (The DM:baryon variance of §IX has a different origin — the central limit theorem, not spatial $|\Phi|$ variation — and is not a consequence of this mechanism.)
```

## Item 3 — the void mechanism's "specific mechanism" claim, under Door B

**§XIII, live:** *"(Structurally similar to Wiltshire/Célérier, but with a **specific mechanism**: spatial |Φ_NTE|² variation under the pointwise constraint.)"*

**Under Door B, |Φ|² is a relabelling of H.** So "spatially varying |Φ|²" is "spatially varying H" — which is what Wiltshire and Célérier already have. **The distinguishing claim reduces to the thing it claims to be distinguished from.**

```
OLD: (Structurally similar to Wiltshire/Célérier, but with a specific mechanism: spatial $|\Phi_{\mathrm{NTE}}|^2$ variation under the pointwise constraint.)
NEW: (Structurally similar to Wiltshire/Célérier. Under Door B, $|\Phi|^2$ is a relabelling of the expansion history, so spatial $|\Phi_{\mathrm{NTE}}|^2$ variation is spatial variation in $H$ — the same content as those treatments, expressed in NTE's vocabulary rather than a distinct mechanism.)
```

**This is a loss and should be recorded as one:** §XIII previously claimed a mechanism distinguishing NTE from the existing inhomogeneous-cosmology literature. Under Door B it does not.

## Item 4 — possible file truncation. **Verify locally.**

Part 2's closing trailer ends mid-word: *"…mirror-matter and bimetric prior art **credi**"* — no closing parenthesis, no asterisk, no terminal punctuation.

**AC has seen this on every read of Part 2 since 2026-09-18**, which is consistent with either a genuine truncation on disk or a consistent read-layer cut at ~18.6 kB. **AC cannot distinguish these through the Drive read.**

**Cursor: check the file's final bytes locally.** If truncated, restore the trailer; if the read layer is cutting, note it so AC stops flagging it.

---

## Assessment

**Part 2 is in better shape than Parts 1 and 3 were** — the Door B and Option D changes landed correctly and §IX reads clean.

**But item 1 must be fixed before any deposit**, and it raises a question worth answering now: **how many other patches introduced raw Unicode that lost its encoding?** The corpus-wide sweep in item 1 is the cheap way to find out.

**After these four, plus the citation sweep and the Companion 12 check already with Cursor, AC would consider the three Parts internally coherent** — and would then want one pass over the Companions, which have had no systematic review at all since Door B.

---

— AC, 2026-09-28.
