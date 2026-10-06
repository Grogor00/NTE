# Handoff — AC edit manifest: retire the strong emergence claim (residuals only) + δ_J cross-part fix caught in Part 2 sweep

**Stream:** AC (corpus edit — proposed diffs for ratification) · **To:** Greg (ratify) · **Cc:** CR, Cursor Main (apply on ratification).
**Date:** 2026-07-09
**Priority:** M1 deposit-relevant (δ_J §X fix); M2 recommended (§2.1.2); optional (§8.1, K(Φ) clause).
**Scope swept:** Part 1 (full), Part 2 (full), Part 3 (full). Companions NOT swept this pass.
**Finding in one line:** the strong emergence claim is *already retired* corpus-wide (O1 patch + v10.18.0 rebuild). Only one emergence residual needs an edit for internal consistency (§2.1.2); the Part 2 sweep additionally caught a stale δ_J sign claim (§X) that today's δ_J patch fixed in Parts 1/3 but missed in Part 2.

---

## §0 — What is already done (no edit needed)

The retirement is substantially complete in canonical text:
- **Part 3, "Empirical distinctiveness"**: the time-emergence sub-claim is already stated as *"a motivating frame, not a predictive mechanism… fixes nothing the geometry does not… the geometry, not the emergence, carries the physics."* (O1 patch, applied 2026-07-09.)
- **Part 1 §II.0**: t = iΔN already classed as *"Wick rotation plus Hartle–Hawking in NTE vocabulary… kept for the coherence they supply, not counted as postulate reductions… upgraded the moment it makes a distinguishing prediction."*
- **Part 1 abstract / §I**: H = β|Φ|² is *"a load-bearing constraint — not a causal claim that the field generates time"*; *"without asserting that the field dynamically creates time."*
- **Ledger / open-work**: n_s, r already conditional on open K(Φ); "determine K(Φ)" already open-problem #1.

This session's tilt-map result (STAYS-SOFT, three independent lines) *vindicates* the above rather than requiring new text. It stays in the Handoffs/adjudication record; it is **not** imported into the deposited trilogy (decontamination discipline — Parts are stripped of internal process by design).

---

## EDIT 1 (M2, recommended) — Part 1 §2.1.2: reconcile with §II.0

**Locus:** Part 1 (`NTE_v10_18_0_Part1_Foundations.md`), §2.1.2, final sentence.

**Current (exact):**
> This makes the no-boundary condition a consequence of the NTE axioms rather than a separate postulate.

**Proposed:**
> This expresses the no-boundary condition in NTE's vocabulary — a Wick rotation of the count coordinate. Consistent with §II.0, it is kept as a coherent reformulation within the unobservable pre-temporal regime, not a derivation of the no-boundary condition from the axioms.

**Rationale:** The current sentence asserts a postulate-*reduction* ("consequence… rather than a separate postulate") that §II.0 explicitly disowns for exactly this identification ("not counted as postulate reductions"). A live internal contradiction. This session's tilt-map result settles which side is right: the emergence reformulations do no derivational work, so §2.1.2 must match §II.0's demoted register. This is the one edit the emergence retirement genuinely requires.

---

## EDIT 2 (M1, deposit-relevant) — Part 2 §X: δ_J sign is stale, contradicts Part 3

**Locus:** Part 2 (`NTE_v10_18_0_Part2_Structure.md`), §X, "Honest scope" sentence.

**Current (exact):**
> Honest scope: the **existence and sign** of the asymmetry are zero-parameter (via $\delta_J = \pi/2$); the **magnitude** is a structural consistency at order unity, not a zero-parameter prediction — it inherits an O(1) residue in $M_1$, the atmospheric-ratio overshoot, and an underived washout efficiency.

**Proposed:**
> Honest scope: the **existence** of the asymmetry is zero-parameter (via $|\delta_J| = \pi/2 \neq 0$); its **sign** is *not* fixed — the sign of $\delta_J$ is a free within-sector CP-parity (Companion 13; §XVII), not locked to $B$; and the **magnitude** is a structural consistency at order unity, not a zero-parameter prediction — it inherits an O(1) residue in $M_1$, the atmospheric-ratio overshoot, and an underived washout efficiency.

**Also (same section, notation):** the derivation line "$\delta_J = \pi/2$ — **maximal CP violation, zero free parameters**, from the Janus geometry" should read "$|\delta_J| = \pi/2$ … (magnitude; the sign is free — §XVII)" to match Parts 1/3.

**Rationale:** The δ_J relational-wording patch (applied 2026-07-09: magnitude forced, sign free) updated Part 1 abstract ("the sign is a within-sector CP-parity NTE does not fix") and Part 3 (predictions (C): "its sign is not fixed — δ_J's sign is a free within-sector CP-parity, not locked to B"). **It missed Part 2 §X**, which still claims the *sign* of the asymmetry is zero-parameter. This is a direct Part 2 ↔ Part 3 contradiction on a headline (baryogenesis) claim — exactly what CR or an external referee would catch. Not an emergence issue; caught incidentally by the sweep. Highest priority in this manifest.

---

## EDIT 3 (optional, borderline) — Part 2 §8.1: register-consistency

**Locus:** Part 2, §8.1, final sentence.

**Current (exact):**
> This is a consequence of the NTE axioms, not a new postulate.

**Proposed:**
> This follows from the emergence picture once the frame is granted — not an independently added postulate.

**Rationale:** Same "consequence of the axioms, not a postulate" register as §2.1.2. The *substance* here is more defensible (gauge structure logically needs a timelike index, so gauge birth coincides with locking — a coherence consequence, and it makes no observable), so this is optional. Include only if aligning phrasing corpus-wide is wanted; the claim is sound as-is.

---

## EDIT 4 (optional) — Part 3 open-work: why K(Φ) is not closeable by the obvious route

**Locus:** Part 3, "Open work" list, first item.

**Current (exact):**
> determine $K(\Phi)$ (unlocks $n\_s$/$r$);

**Proposed:**
> determine $K(\Phi)$ (unlocks $n\_s$/$r$) — noting the natural geometric route via $\ell = 1/H$ is circular, inheriting $\beta|\Phi|^2$ from the $H = \beta|\Phi|^2$ constraint, so it does not fix $K(\Phi)$ independently;

**Rationale:** Adds honest content on *why* K(Φ) is open (Jammer FM1 circularity, this session), forecloses a route a referee might assume available. Optional — the corpus already lists K(Φ) as open.

---

## §5 — Routing

- **Ratify:** Greg. Recommended set = EDIT 1 + EDIT 2. EDIT 2 is the priority (live cross-part contradiction).
- **Apply on ratification:** AC (two-step Drive workaround when endpoint recovers) or Cursor Main. Byte-exact — current text quoted above verbatim.
- **Not done this pass:** Companion sweep for the same emergence phrasing and for any further stale δ_J sign statements. Given §X was stale, a δ_J-sign grep across Companions (esp. any baryogenesis/leptogenesis companion) is advisable before deposit. Flag if wanted.
- **No new physics; no claim added.** All four edits are honest-scope corrections or consistency fixes.

— AC, 2026-07-09. Emergence retirement already ~complete; residual = §2.1.2 (reconcile with §II.0). Sweep also caught §X δ_J sign stale vs Parts 1/3 — deposit-relevant, fix first. Two optional. Companion δ_J-sign grep recommended pre-deposit.
