# AC → Greg: patch register — **§2.1 now contradicts itself in adjacent paragraphs.** Three items, pre-deposit.

**From:** AC (Claude) · **To:** Greg (ratification) · **Cc:** Cursor Main, PC, Scratch, Jammer · **Date:** 2026-09-28
**Source:** `Core_Papers\NTE_v10_19_0_Part1_Foundations.md`, **read in full this session, post-apply.**
**Context:** Greg wants the corpus coherent and stable before PC updates the Book, for a Zenodo deposit.
**Status: DRAFT. Nothing patched.**

---

## Item 1 — **The patch created a contradiction in adjacent paragraphs.** This is the reserved item, and it is now urgent.

**§2.1, patched sentence (P1-2, applied):**
> *"Gravitational time dilation is **inherited (General Relativity)**… β_NTE|Φ(x)|² is a local expansion rate, **not the lapse** √g₀₀ that sources the Schwarzschild factor."*

**§2.1, the very next paragraph, unpatched:**
> *"**It is a lapse** on the N-foliation… **the Schwarzschild recovery above** is the static-observer statement… **NTE's derived content here is the gravitational piece alone — the identification of the lapse with** β_NTE|Φ(x,N)|²."*

**Two defects, one visible on a single screen:**
1. *"not the lapse"* against *"it is a lapse"*, and *"inherited, not derived"* against *"NTE's derived content here is the gravitational piece alone."*
2. *"the Schwarzschild recovery above"* is now a **dangling reference** — the sentence it points to no longer contains one.

**The physics, stated precisely so the repair is right rather than merely consistent.** β_NTE|Φ|² *is* the inverse lapse on the N-foliation: with N as time coordinate, dt = dN/(β|Φ|²), so the cosmological lapse is 1/(β|Φ|²). **That much is correct and should be kept.** What fails is treating its *spatial* variation as the source of the Schwarzschild factor — the N-foliation lapse is a function of the *cosmological* slicing, and **a bound system has no local Hubble flow**, so |Φ(x)| does not vary across a gravitational well in the way the claim needs. **The cosmological reading survives; the gravitational-well reading does not.**

```
OLD: **What $\beta_{\mathrm{NTE}}|\Phi|^2$ is, in standard terms.** It is a *lapse* on the $N$-foliation. Accordingly $t(N)$ is the proper time of an observer at rest in the comoving frame at $x$ — cosmic time — not proper time simpliciter, and the Schwarzschild recovery above is the static-observer statement. Velocity-dependent dilation is then the ordinary tilt of a worldline relative to the foliation, $d\tau/dt = \sqrt{1-v^2/c^2}$ locally, and is **inherited, not derived**: once the emergent metric is Lorentzian, local special relativity applies unmodified. NTE's derived content here is the *gravitational* piece alone — the identification of the lapse with $\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$. Two observers at the same $x$ with different velocities share a local $|\Phi|$ and are separated by the tilt, not by the field. The preferred foliation is a global slicing, as the comoving frame is in standard cosmology, and introduces no locally preferred frame: the tangent-space metric remains Minkowski and local Lorentz invariance is exact.

NEW: **What $\beta_{\mathrm{NTE}}|\Phi|^2$ is, in standard terms.** It is the *inverse lapse* of the $N$-foliation: taking $N$ as time coordinate, $dt = dN/(\beta_{\mathrm{NTE}}|\Phi|^2)$. Accordingly $t(N)$ is the proper time of an observer at rest in the **comoving** frame — cosmic time — not proper time simpliciter. This is a **cosmological** statement and does not extend to bound systems: the $N$-foliation lapse belongs to the cosmological slicing, and a gravitationally bound region has no local Hubble flow, so gravitational time dilation is **inherited from General Relativity** and not obtained here from spatial variation of $|\Phi|$ (regraded 2026-09-27). Velocity-dependent dilation is likewise the ordinary tilt of a worldline relative to the foliation, $d\tau/dt = \sqrt{1-v^2/c^2}$ locally, **inherited, not derived**: once the emergent metric is Lorentzian, local special relativity applies unmodified. Two observers at the same $x$ with different velocities share a local $|\Phi|$ and are separated by the tilt, not by the field. The preferred foliation is a global slicing, as the comoving frame is in standard cosmology, and introduces no locally preferred frame: the tangent-space metric remains Minkowski and local Lorentz invariance is exact.
```

**What this keeps and what it gives up.** Keeps: the lapse identification as a *cosmological* statement, which is correct and load-bearing for t(N); the velocity-dilation passage; the local-Lorentz-invariance paragraph. Gives up: the claim that NTE *derives* the gravitational piece. **That was already surrendered by P1-2 and P3-2; this makes the two paragraphs agree.**

## Item 2 — **§VI carries the same withdrawn claim, unpatched**

**Live text:** *"The thickness varies pointwise with local |Φ_NTE|: **gravitational time dilation is the time-side measure of N-thickness variation**."*

Same claim as Item 1, one section later, and missed by both registers.

```
OLD: The thickness varies pointwise with local $|\Phi_{\mathrm{NTE}}|$: gravitational time dilation is the time-side measure of N-thickness variation.
NEW: The thickness varies pointwise with local $|\Phi_{\mathrm{NTE}}|$. (Earlier drafts read gravitational time dilation as the time-side measure of this variation; that reading is withdrawn — see §2.1 — and gravitational dilation is inherited from General Relativity.)
```

## Item 3 — **Apply defect in P1-3: a broken sentence in §VI**

The applied text reads: *"…§V's reset trigger uses $\ell$. **the** apparent "trans-Planckian" field value…"* — lowercase after a full stop. **AC's own drafting error**, carried through byte-exact apply as drafted.

```
OLD: §V's reset trigger uses $\ell$. the apparent "trans-Planckian" field value
NEW: §V's reset trigger uses $\ell$. The apparent "trans-Planckian" field value
```

---

## Assessment for the deposit

**These three close the gravitational-time-dilation regrade completely.** After them, AC knows of no remaining internal contradiction in Part 1 or Part 3.

**Still open before AC would call the corpus deposit-ready**, none of which is drafted here:
- **Part 2's N-3 items** — §XII's DM-variance attribution to |Φ| variation (contradicts §IX's CLT origin), the voids "specific mechanism", and §VII's locking criterion y_eff²/(β|Φ|) ≥ 1 which no lane has recomputed under Door B. **AC has not re-read Part 2 post-Door-B.**
- **The citation sweep**, still open after two confirmed misattributions.
- **Companion 12's fibre modulus** — whether the T_GB regrade reaches it.

**AC's recommendation on sequencing:** apply these three, then **re-read Part 2 in full** before declaring the corpus stable. Part 2 has had no systematic pass since Door B, and it is the paper carrying §IX (κ), §XII (voids/variance) and §8.1–8.6 (gauge birth) — the three areas every ruling this week has touched.

---

— AC, 2026-09-28.
