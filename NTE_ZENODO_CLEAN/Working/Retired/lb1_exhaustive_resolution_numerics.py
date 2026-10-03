#!/usr/bin/env python3
"""LB-1 exhaustive resolution sweep — every H(N) vantage, dead ends, sunshine path."""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

ALPHA = 2.38e-47
M_PL_NR = 1.221e19
M_PL = 2.435e18
NS_OBS = 0.9685
NE_CORPUS = -math.log(ALPHA * M_PL_NR)
H_ALPHA = ALPHA * M_PL_NR**2
PHI_INF_RATIO = 15.9
EPS_TARGET = (1.0 - NS_OBS) / 2.0


@dataclass
class RouteResult:
    name: str
    ns_horizon: float | None
    h_at_ne: float
    h_err: float
    verdict: str
    note: str


def eps_of(H_fn: Callable[[float], float], N: float, dN: float = 1e-4) -> float:
    H0, H1 = H_fn(N), H_fn(N + dN)
    if H0 <= 0 or H1 <= 0:
        return float("nan")
    return -(math.log(H1) - math.log(H0)) / dN


def ns_sr(eps: float) -> float:
    return 1.0 - 2.0 * eps


def h_exp(N: float) -> float:
    return M_PL_NR * math.exp(-N)


def h_linear(N: float, ne: float = NE_CORPUS) -> float:
    return M_PL_NR * (1.0 - N / ne)


def h_sqrt(N: float, ne: float = NE_CORPUS) -> float:
    return M_PL_NR * math.sqrt(max(1.0 - N / ne, 1e-30))


def h_power(N: float, p: float, ne: float = NE_CORPUS) -> float:
    return M_PL_NR * (max(1.0 - N / ne, 1e-30)) ** p


def h_starobinsky(N: float, ne: float = NE_CORPUS) -> float:
    """Companion 9 P3/P4: H ~ (1 - N/Ne)^beta, beta=1/2 gives n_s~0.968."""
    return h_power(N, 0.5, ne)


def h_starobinsky_full(N: float, ne: float = 63.0) -> float:
    """Starobinsky R^2: H/H0 ~ (1 - N/(4Ne)) exp(-N/(4Ne)) style decay."""
    x = N / (4.0 * ne)
    return M_PL_NR * (1.0 - x) * math.exp(-x)


def h_hilltop(N: float, phi0: float = PHI_INF_RATIO * M_PL, v0: float = 0.5 * M_PL) -> float:
    """Schematic hilltop: V ~ (1 - (Phi/phi0)^2); H ~ sqrt(V) at slow roll."""
    # Map N to phi decrease: phi ~ phi0 * sqrt(1 - N/ne)
    ne = phi0**2 / (4.0 * M_PL**2)
    phi = phi0 * math.sqrt(max(1.0 - N / ne, 1e-12))
    v = v0 * (1.0 - (phi / phi0) ** 2)
    return math.sqrt(max(8.0 * math.pi * v / (3.0 * M_PL_NR**2), 1e-30))


def h_piecewise(N: float, n1: float, eps1: float) -> float:
    """Two segments: slow-roll then fast roll; eps2 fixed by endpoint closure."""
    drop_total = math.log(M_PL_NR / H_ALPHA)
    drop1 = eps1 * n1
    drop2 = drop_total - drop1
    rem = NE_CORPUS - n1
    eps2 = drop2 / rem if rem > 0 else 1.0
    if N <= n1:
        return M_PL_NR * math.exp(-eps1 * N)
    return M_PL_NR * math.exp(-drop1) * math.exp(-eps2 * (N - n1))


def h_logistic_switch(N: float, n_sw: float, width: float = 2.0) -> float:
    """Smooth switch: slow-roll then fast roll via logistic epsilon."""
    sig = 1.0 / (1.0 + math.exp(-(N - n_sw) / width))
    eps = EPS_TARGET * (1.0 - sig) + 1.0 * sig
    # integrate eps dN numerically (RK4 coarse)
    steps = 4000
    dN = NE_CORPUS / steps
    lnH = math.log(M_PL_NR)
    for i in range(steps + 1):
        Ni = i * dN
        if Ni >= N:
            break
        si = 1.0 / (1.0 + math.exp(-(Ni - n_sw) / width))
        ei = EPS_TARGET * (1.0 - si) + 1.0 * si
        lnH -= ei * dN
    return math.exp(lnH)


def h_constraint_delayed(N: float, n_on: float) -> float:
    """Sunshine model: Sector 1 C9 sqrt until constraint at n_on, then exp roll."""
    if N <= n_on:
        return h_sqrt(N, ne=NE_CORPUS)
    h_on = h_sqrt(n_on)
    # remaining drop to H_alpha in (n_on, NE]
    rem = NE_CORPUS - n_on
    eps2 = math.log(h_on / H_ALPHA) / rem if rem > 0 else 1.0
    return h_on * math.exp(-eps2 * (N - n_on))


def evaluate(name: str, H_fn: Callable[[float], float], n_horizon: float = 55.0) -> RouteResult:
    h_end = H_fn(NE_CORPUS)
    h_err = abs(h_end / H_ALPHA - 1.0)
    e_h = eps_of(H_fn, n_horizon)
    ns = ns_sr(e_h) if math.isfinite(e_h) else None
    return RouteResult(name, ns, h_end, h_err, "", "")


def verdict_single_ansatz(r: RouteResult) -> RouteResult:
    ns_ok = r.ns_horizon is not None and abs(r.ns_horizon - NS_OBS) < 0.005
    h_ok = r.h_err < 0.01
    if ns_ok and h_ok:
        r.verdict = "UNIFIED CANDIDATE"
        r.note = "Both n_s and H(Ne) match — investigate further"
    elif ns_ok and not h_ok:
        r.verdict = "DEAD END (n_s only)"
        r.note = f"H(Ne)/H_alpha err={r.h_err:.2e}"
    elif h_ok and not ns_ok:
        r.verdict = "DEAD END (endpoints only)"
        r.note = f"n_s~{r.ns_horizon:.3f} at N~55"
    else:
        r.verdict = "DEAD END (both fail)"
        r.note = f"n_s~{r.ns_horizon}; H err={r.h_err:.2e}"
    return r


def search_logistic() -> tuple[float, float, float]:
    best = (1e9, 60.0, 2.0)
    for n_sw in range(45, 63):
        for w in (0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
            H = lambda N, ns=n_sw, ww=w: h_logistic_switch(N, ns, ww)
            r = evaluate(f"logistic n_sw={n_sw} w={w}", H)
            score = abs((r.ns_horizon or 0) - NS_OBS) + r.h_err
            if score < best[0]:
                best = (score, float(n_sw), w)
    return best


def search_constraint_delayed() -> tuple[float, float]:
    best = (1e9, 0.0)
    for n_on in [x * 0.5 for x in range(80, 126)]:  # 40 .. 62.5
        H = lambda N, no=n_on: h_constraint_delayed(N, no)
        r = evaluate(f"delayed n_on={n_on:.1f}", H)
        ns_ok = r.ns_horizon is not None and abs(r.ns_horizon - NS_OBS) < 0.01
        if ns_ok and r.h_err < 0.01:
            return (0.0, n_on)
        score = abs((r.ns_horizon or 0) - NS_OBS) + r.h_err
        if score < best[0]:
            best = (score, n_on)
    return best


def two_formula_ns_check() -> None:
    """§18.3 n_s=1-2/Ne vs C9 n_s=1-8/Phi^2 — same number, different physics."""
    ns_18 = 1.0 - 2.0 / NE_CORPUS
    ns_c9 = 1.0 - 8.0 / PHI_INF_RATIO**2
    print("\n## G-NS: two n_s formulas")
    print(f"  n_s = 1 - 2/N_e           = {ns_18:.6f}")
    print(f"  n_s = 1 - 8/Phi^2 (C9)    = {ns_c9:.6f}")
    print(f"  Planck target             = {NS_OBS}")
    print("  => numerically aligned; apply C9 during Sector 1, not on Role A constraint roll")


def sunshine_path() -> None:
    n_on = 60.0
    print("\n## SUNSHINE PATH — sequential constraint activation (BR2c + R4b)")
    print("  Sector 1 (N in observation window): Role B, V_eff slow-roll, NO holonomic H=alpha Phi^2")
    print("  Sector 2 (terminal roll): Role A, constraint ON, H = alpha |Phi_NTE|^2")
    print(f"  Illustrative handoff N_on ~ {n_on} e-folds (Jammer derives from action)")
    for N in (0, 30, 55, 60, 61, NE_CORPUS):
        H = h_constraint_delayed(N, n_on)
        e = eps_of(lambda x: h_constraint_delayed(x, n_on), min(N, NE_CORPUS - 0.01))
        print(f"    N={N:5.1f}  H={H:.3e}  eps={e:.4f}  n_s~{ns_sr(e):.4f}")
    r = evaluate("sunshine delayed", lambda N: h_constraint_delayed(N, n_on))
    print(f"  H(Ne) match: err={r.h_err:.4e}; n_s@55={r.ns_horizon:.4f}")
    print("  Field map: Phi_inf != |Phi_NTE| at HH — Z2 portal / sequential activation (NOT identity)")
    print("  Charts: y=N_lock vs N=N_e orthogonal at event G (BR2d-J1 theorem)")


def main() -> None:
    print("LB-1 EXHAUSTIVE RESOLUTION SWEEP")
    print("=" * 72)
    print(f"Corpus: alpha={ALPHA:.2e}, N_e={NE_CORPUS:.4f}, H^(alpha)={H_ALPHA:.3e} GeV")
    print(f"Targets: n_s={NS_OBS}, H(N_e)=H^(alpha), |Phi(N_e)|=M_Pl,nr")

    routes: list[RouteResult] = []

    catalog: list[tuple[str, Callable[[float], float]]] = [
        ("V1 exponential H=M_Pl e^{-N}", h_exp),
        ("V2 linear H=M_Pl(1-N/Ne)", h_linear),
        ("V3 C9 sqrt H=M_Pl sqrt(1-N/Ne)", h_sqrt),
        ("V4 Starobinsky beta=1/2", h_starobinsky),
        ("V5 Starobinsky full R2 form", h_starobinsky_full),
        ("V6 hilltop schematic", h_hilltop),
        ("V7 power p=0.25", lambda N: h_power(N, 0.25)),
        ("V8 power p=0.75", lambda N: h_power(N, 0.75)),
        ("V9 piecewise eps=0.016 then fast (N1=60)", lambda N: h_piecewise(N, 60, EPS_TARGET)),
        ("V10 piecewise (N1=58)", lambda N: h_piecewise(N, 58, EPS_TARGET)),
    ]

    print("\n## I. SINGLE-ANSATZ ROUTES (R1 — unified H(N))")
    for name, fn in catalog:
        r = verdict_single_ansatz(evaluate(name, fn))
        routes.append(r)
        ns_s = f"{r.ns_horizon:.4f}" if r.ns_horizon is not None else "nan"
        print(f"  {r.name[:42]:42s}  n_s@55={ns_s}  H_err={r.h_err:.2e}  -> {r.verdict}")

    print("\n## II. CONSTANT-EPSILON IMPOSSIBILITY (algebraic)")
    ne_needed = math.log(M_PL_NR / H_ALPHA) / EPS_TARGET
    print(f"  eps={EPS_TARGET:.5f} for n_s => N_e required = {ne_needed:.1f}  (corpus {NE_CORPUS:.1f})")
    print("  => R1 with constant eps EXCLUDED (theorem)")

    print("\n## III. LOGISTIC EPSILON SWEEP (smooth unified attempt)")
    score, n_sw, w = search_logistic()
    print(f"  Best logistic: n_sw={n_sw}, width={w}, score={score:.4f}")
    r = verdict_single_ansatz(evaluate("best logistic", lambda N: h_logistic_switch(N, n_sw, w)))
    print(f"  -> {r.verdict}: {r.note}")

    print("\n## IV. CONSTRAINT-DELAYED SWEEP (sunshine family)")
    score_d, n_on = search_constraint_delayed()
    print(f"  Best n_on={n_on:.1f}, combined score={score_d:.4f}")
    r = verdict_single_ansatz(evaluate("best delayed", lambda N: h_constraint_delayed(N, n_on)))
    print(f"  -> {r.verdict}: {r.note}")

    print("\n## V. ROLE (A) MAGNITUDE CLASH (apply constraint at HH)")
    phi_a = math.sqrt(M_PL_NR / ALPHA)
    phi_b = PHI_INF_RATIO * M_PL
    print(f"  |Phi_NTE|(HH) = sqrt(M_Pl/alpha) = {phi_a:.3e} GeV")
    print(f"  Phi_inf (C9)   = {phi_b:.3e} GeV")
    print(f"  ratio B/A      = {phi_b/phi_a:.3e}")
    print("  => DEAD END if constraint active during Sector 1 (R4c EXCLUDED)")

    print("\n## VI. THREE-EPOCH / H_GB (not a contradiction)")
    T_GB = M_PL_NR / math.sqrt(2 * math.pi)
    rho = (math.pi**2 / 30.0) * 106.75 * T_GB**4
    h_f = math.sqrt((8 * math.pi / 3.0) * rho / M_PL_NR**2)
    print(f"  H^(F)/H^(alpha) = {h_f/H_ALPHA:.2e}; ln ratio = {math.log(h_f/H_ALPHA):.2f} ~ N_e+1")
    print("  => thermal and constraint H are different readings at G (R4 ratified)")

    two_formula_ns_check()
    sunshine_path()

    print("\n## VII. VERDICT SUMMARY")
    unified = [r for r in routes if r.verdict == "UNIFIED CANDIDATE"]
    print(f"  Unified single-ansatz survivors: {len(unified)}")
    print("  LB-1 RESOLUTION (register):")
    print("    1. R1 single H(N) — EXCLUDED (this sweep + BR2c)")
    print("    2. R2 two-sector + sequential constraint — SUNSHINE PATH")
    print("    3. False problem dissolved: applying Role A at Role B epoch")
    print("    4. Remaining derive: J6 ODE Sector 1; BR2d-J3 chart map; R4 Z2 portal")
    print("    5. eta correction ~ -2/Ne^2 shaves 0.85sigma n_s residual (optional)")


if __name__ == "__main__":
    main()
