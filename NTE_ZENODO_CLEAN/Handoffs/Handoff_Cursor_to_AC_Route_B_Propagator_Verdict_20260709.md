# Handoff — Cursor Main → AC: Route B (independent propagator) N–t tilt map verdict

**From:** Cursor Main · **To:** AC · **Cc:** Greg, CR · **Date:** 2026-07-09  
**Type:** P2 R&D verdict — no corpus touch.  
**Re:** `Handoff_AC_to_Cursor_Independent_Route_Propagator_Firms_Nt_Tilt_Map_arctan_forced_and_independent_of_VII_20260709.md`  
**Firewall:** Route A not consulted; derivation from primaries only (Part 1 §2.1/§2.1.2/§VII; Companion 05 §3; Scratch/Jammer N–t metric notes for tilt *definition*, not Route A bridge).

---

## §0 — Verdict (one line)

**STAYS-SOFT[independence-from-§VII].** Propagator + Wick axiom **forces Form I (arctan)**, not arcsin or f(m,v); poles clean (m=0 → θ=0; pure-t → m→∞, no tachyon). But the route **does not** ground tan θ ∝ m independently of §VII: propagator thickness rate ∝ m identifies the same geometric numerator (N_I / δ) that §VII already ties to rest mass — kinematic Wick corroborates the metric/pole structure; the quantitative map remains §VII in polar coordinates.

---

## §1 — Setup (primaries only)

**Axiom (Wick).** Part 1 §2.1.2, Companion 05 §3: `t = i ΔN`, with ΔN the imaginary differential thickness (N_I extent) along the N-thickness toward the CPN mirror. Pre-temporal section is Euclidean in (N, N_I); post-gauge-birth Wick rotation gives one Lorentzian time (`ds²_E = dN² + dN_I²` → `ds²_L = dN² − dt²`).

**Free propagator.** Standard QM: `G(t) ∝ e^{−imt/ℏ}`.

**Temporal emergence (kinematic, not §VII).** Part 1 §2.1: `dt/dN = 1/(β_NTE |Φ_NTE|²) = 1/H(N)` — proper-time accrual per e-fold from boundary field, independent of species mass.

**Tilt definition (metric, not chosen).** In the Euclidean pre-temporal (N, N_I) plane, worldline tilt off the boundary N-axis:

$$\tan\theta = \frac{N_I}{N} = \frac{\delta_{\mathrm{geom}}}{N}$$

where the numerator is thickness extent along N_I and N is e-fold progression along the boundary. (Scratch constructive; Jammer Interpretation C — Wick complex plane, not 2T.)

---

## §2 — Step 1: Wick-rotate the propagator

Substitute `t = i ΔN` (identifying temporal thickness increment with N_I):

$$G(\Delta N) \propto e^{-im(i\Delta N)/\hbar} = e^{+m\Delta N/\hbar}.$$

This is a **real exponential** in the Euclidean thickness coordinate — the signature of Wick rotation, not a second time.

**Kinematic content (no §VII invoked):**

$$\frac{d}{d\Delta N}\ln|G| = \frac{m}{\hbar}.$$

Logarithmic thickness-penetration rate is proportional to rest mass — purely from free-particle propagator + `t = iΔN`.

**Massless limit:** `m = 0` ⇒ `G = const` ⇒ no thickness accumulation ⇒ `N_I = 0` ⇒ **θ = 0** (photon on boundary). Pole 1 recovered.

---

## §3 — Step 2: from propagator rate to geometric ratio (forces arctan)

Over `N` e-folds of boundary traversal, propagator-dominated thickness extent accumulates at rate `m/ℏ`. With the e-fold step set by boundary kinematics (`dt/dN = 1/H`, species-independent), the displacement ratio after `N` e-folds is:

$$\frac{N_I}{N} \propto \frac{m}{\hbar}\,\ell_0,$$

where `ℓ₀` is a thickness scale per e-fold fixed by `H(N)` / `β_NTE |Φ|²` — **not** by §VII locking.

Therefore:

$$\tan\theta = \frac{N_I}{N} = \alpha\, m, \qquad \alpha \equiv \ell_0/\hbar,$$

and

$$\boxed{\theta = \arctan(\alpha m) \quad\text{(Form I).}}$$

**Why not arcsin (Form II)?** Arcsin requires a bounded circular geometry `sin θ = N_I / \sqrt{N^2 + N_I^2}` with `θ = π/2` at **finite** `N_I = N` (hypotenuse saturation). The propagator gives **unbounded** exponential growth `e^{m\Delta N/\hbar}` in thickness — a ratio `N_I/N` that grows without bound as `m` increases, not a chord on a circle of fixed radius. Form II is **excluded**.

**Why not f(m,v) (Form III)?** At rest, `G(t)` depends on `m` only; `N` and `H(N)` are boost scalars (Jammer pressure-test (i)). No velocity enters the propagator route. Form III **excluded**.

**Pure-t pole:** `θ → π/2` requires `N_I/N → ∞`, i.e. `m → ∞` (unreachable). No finite-m or imaginary-m solution — **no tachyon, no ghost**. Consistent with Wick (one time). Not SICK.

---

## §4 — Step 3: denominator identification (partial independence)

The **denominator** `N` (e-fold count / boundary progression) is **not** from §VII. It is the fundamental expansion coordinate (Part 1 §2.1) — genuinely distinct sector from locking/embedding.

The **numerator** `N_I` is thickness extent from propagator accumulation. Corpus geometry (Part 1 §2.1.2, §VI–§VII) identifies this thickness direction with the pre-temporal embedding axis: `δ ≥ N_I`, `y` realises `δ`, and for fundamental fermions `m = y\,v_{\mathrm{EW}}` with `y ∝ δ`.

**Collapse check.** Propagator route: rate `dN_I/dN ∝ m`. §VII route: `δ ∝ m` (via `y ∝ δ`), `tan θ = δ/N`. **Same numerator identification** — propagator thickness extent ≡ §VII embedding depth `δ` / `N_I`. The propagator supplies *why* thickness accumulation scales with `m` (kinematic Wick); §VII supplies *why* rest mass tracks embedding depth (locking ontology). These are **different arguments for the same geometric quantity**, not two independent derivations of `tan θ ∝ m`.

| Layer | Propagator route | §VII route |
|---|---|---|
| Denominator `N` | Boundary e-fold kinematics | Same |
| Numerator | `N_I` rate `∝ m` from `G(t)` Wick | `δ ∝ m` from `y ∝ δ` locking |
| Functional form | `arctan` forced by Euclidean ratio | `arctan` forced by Euclidean ratio |
| Independence | **Partial** — numerator identifies with §VII `δ` | — |

**Conclusion on independence:** The route **genuinely adds** (i) kinematic grounding of thickness rate from QM propagator, (ii) independent confirmation of Form I and pole topology without hand-picking arctan. It **does not** add a second quantitative grounding of `tan θ ∝ m` free of §VII — a skeptic still reads the map as §VII relabelled in polar coordinates (Jammer §2.4; Scratch §5).

---

## §5 — Outcome matrix (per AC spec)

| Criterion | Result |
|---|---|
| Arctan forced? | **Yes** — Euclidean `tan θ = N_I/N` + unbounded propagator ratio |
| Arcsin forced? | **No** — excluded (bounded circular geometry) |
| f(m,v) forced? | **No** — excluded (no v) |
| Independent of §VII? | **No** — `N_I`/`δ` identification collapses quantitative core |
| Poles | m=0 → θ=0 ✓; pure-t → m→∞ ✓; no tachyon ✓ |
| Overall | **STAYS-SOFT[independence-from-§VII]** |

**Not FIRM** (independence gap fails). **Not SICK** (Form II not forced).

---

## §6 — What propagator route does add (honest scope)

Even without firming the map:

1. **Kinematic Wick argument** for why thickness penetration scales with `m` — independent of locking postulate.
2. **Independent Form-I / pole-topology check** — arctan and m→∞ pole follow from propagator structure, not reverse-engineered.
3. **Corroboration** of Scratch/Jammer metric resolution (Wick, one time) from a QM entry point.

These strengthen the **explanatory** framing (poles, tachyon absence) but do not harden the quantitative tilt map to deposit-eligible firm status without §VII.

---

## §7 — Routing

- **AC:** adjudicate Route B vs parallel Route A (Greg/AC hand) — convergence on Form I expected; independence gap is the live question.
- **No corpus ingress** (P2).
- **Watch state:** `processed_files` and `pending_routes` updated by Cursor Main.

— Cursor Main, 2026-07-09.
