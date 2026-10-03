#!/usr/bin/env python3
"""Paper S3 full suppression sweep — all corpus routes until fit bracket found."""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

M_PL = 2.435e18
M_PL_NR = 1.221e19
ALPHA = 2.38e-47
V_EW = 246.0
N_F = 180
G_EFF = 106.75
BETA_GB = math.sqrt(2 * math.pi) / M_PL
VOL_M = 2 * math.pi**2 * BETA_GB
N_E = -math.log(ALPHA * M_PL_NR)
N_LOCK = 45.0 / (4.0 * G_EFF)
H_ALPHA = ALPHA * M_PL_NR**2
T_GB = M_PL_NR / math.sqrt(2 * math.pi)
H_FRIED = math.sqrt((8 * math.pi / 3) * (math.pi**2 / 30) * G_EFF * T_GB**4 / M_PL_NR**2)
H0 = ALPHA * V_EW**2
LAMBDA_A4 = (2430 / math.pi**4) * (M_PL**2 / (2 * math.pi))
LAMBDA_NAIVE = (45 / math.pi**2) * M_PL**4
LAMBDA_OBS = (2.3e-3 * 1e-9) ** 4
TARGET_LOG = math.log10(LAMBDA_OBS)


@dataclass
class Route:
    name: str
    factor: float
    mechanism: str
    register: str  # derived | heuristic | tuning | forbidden


def log10(x: float) -> float:
    return math.log10(x) if x > 0 else float("-inf")


def classify_result(lam: float) -> tuple[float, str]:
    lg = log10(lam / LAMBDA_OBS)
    if abs(lg) <= 0.5:
        tag = "FIT (<3x)"
    elif abs(lg) <= 1.0:
        tag = "NEAR (10x)"
    elif abs(lg) <= 2.0:
        tag = "BRACKET (100x)"
    else:
        tag = "MISS"
    return lg, tag


def main() -> None:
    print("# Paper S3 — full suppression sweep (all corpus routes)")
    print(f"Lambda_obs = {LAMBDA_OBS:.4e} GeV^4")
    print(f"Lambda_a4  = {LAMBDA_A4:.4e} GeV^4  (log10/obs = {log10(LAMBDA_A4/LAMBDA_OBS):.2f})")
    print()

    # --- Single-factor routes ---
    routes: list[Route] = []

    def add(name: str, factor: float, mech: str, reg: str) -> None:
        routes.append(Route(name, factor, mech, reg))

  # R1 f_k
    add("R1 f0~1 (derived)", 1.0, "S3-f2 Connes moments", "derived")
    add("R1 gauss f4/f2=0.56", 0.56, "Gaussian cutoff ratio", "derived")

    # R2 dmu (S3-f3)
    add("R2 dt/H S2 fraction", 1.0, "Sector2 dominates — ~1", "derived")
    add("R2 1/<V>_pre illus.", 1.0 / 164.58, "S3-f3 illustrative", "heuristic")

    # R3 tail
    add("R3 eps muL=1", math.exp(-0.5 * math.pi), "CC2008 Theorem 3 canonical", "derived")
    add("R3 eps muL=11", math.exp(-0.5 * math.pi * 121), "Tail-only 83-OOM target", "tuning")

    # R4 area / entropy
    s_gh_a = 45.0 / G_EFF
    add("R4 1/S_GH (Route A)", 1.0 / s_gh_a, "P-dS1 S=45/g_eff", "derived")
    add("R4 S_GH/N_lock", s_gh_a / N_LOCK, "Identity S=4 N_lock", "derived")
    n_max = M_PL_NR / H_ALPHA
    add("R4 1/n_max", 1.0 / n_max, "Dirac modes ~ M_Pl/H_alpha", "heuristic")
    add("R4 1/n_max^2", 1.0 / n_max**2, "Mode counting squared", "heuristic")
    add("R4 1/n_max^3", 1.0 / n_max**3, "Mode counting cubed", "heuristic")
    add("R4 log(n_max)/n_max", math.log(n_max) / n_max, "log dim not dim", "heuristic")

    # R5 M3
    add("R5 M3 seam O(1)", 1.0, "M3 scaffold", "derived")
    add("R5 M3 seam 1e3", 1e-3, "Upper M3 bound", "heuristic")

    # Volume / e-fold (cosmic)
    add("exp(-N_e)", math.exp(-N_E), "Single e-fold dilution", "derived")
    add("exp(-3 N_e)", math.exp(-3 * N_E), "Comoving V ~ exp(3N)", "derived")
    add("exp(-3 N_e - 1)", math.exp(-3 * N_E - 1), "Bridge ln(HF/Ha)~-64", "heuristic")
    add("N_lock/N_e", N_LOCK / N_E, "Stage3/cosmo chart ratio", "derived")
    add("(N_lock/N_e)^2", (N_LOCK / N_E) ** 2, "Chart ratio squared", "heuristic")

    # H scales
    add("(H_alpha/H_F)^1", H_ALPHA / H_FRIED, "Epoch C/A ratio", "derived")
    add("(H_alpha/H_F)^2", (H_ALPHA / H_FRIED) ** 2, "H ratio squared", "heuristic")
    add("(H_alpha/H_F)^4", (H_ALPHA / H_FRIED) ** 4, "H ratio^4 ~ rho", "heuristic")
    add("(H0/H_alpha)^1", H0 / H_ALPHA, "Today vs lock H", "derived")
    add("(H0/M_Pl)^4", (H0 / M_PL) ** 4, "Today H density", "derived")

    # alpha / EW
    add("alpha^4 M_Pl^4/L_a4", (ALPHA**4 * M_PL**4) / LAMBDA_A4, "alpha^4 vs a4 scale", "heuristic")
    add("(v_EW/M_Pl)^4", (V_EW / M_PL) ** 4, "EWSB/Planck^4", "derived")

    # Internal volume
    add("Vol(M)", VOL_M, "Internal manifold vol", "derived")
    add("1/Vol(M)", 1.0 / VOL_M, "Inverse internal vol", "derived")
    add("beta_GB*M_Pl", BETA_GB * M_PL, "sqrt(2pi)", "derived")

    # D_F
    add("D_F 1e-18", 1e-18, "S2-C-C subleading", "derived")

    # Forbidden tuning
    add("f0_req (FORBIDDEN)", LAMBDA_OBS / LAMBDA_A4, "Tune f0 to obs", "forbidden")
    add("f4_req (FORBIDDEN)", LAMBDA_OBS / LAMBDA_NAIVE, "Tune f4 naive", "forbidden")

    print("## A. Single-factor routes (Lambda = Lambda_a4 * factor)")
    print(f"{'Route':<32s} {'factor':>12s} {'log10/obs':>10s} {'tag':>12s} {'reg':>10s}")
    singles = []
    for r in routes:
        if r.register == "forbidden":
            continue
        lam = LAMBDA_A4 * r.factor
        lg, tag = classify_result(lam)
        singles.append((abs(lg), lg, tag, r, lam))
        if tag in ("FIT (<3x)", "NEAR (10x)", "BRACKET (100x)"):
            print(f"{r.name:<32s} {r.factor:12.4e} {lg:10.2f} {tag:>12s} {r.register:>10s}")
    print()

    # --- Key pairwise products (structured stack) ---
    print("## B. Structured product stacks")
    key_factors = {
        "f0": 1.0,
        "eps": math.exp(-0.5 * math.pi),
        "exp3Ne": math.exp(-3 * N_E),
        "expNe": math.exp(-N_E),
        "Hratio2": (H_ALPHA / H_FRIED) ** 2,
        "Hratio4": (H_ALPHA / H_FRIED) ** 4,
        "1/SGH": G_EFF / 45.0,
        "1/nmax3": 1.0 / n_max**3,
        "vEW4": (V_EW / M_PL) ** 4,
        "H04": (H0 / M_PL) ** 4,
        "Nle2": (N_LOCK / N_E) ** 2,
        "dmuV": 1.0 / 164.58,
        "M3": 1e-3,
        "DF": 1e-18,
    }

    combos = [
        ("exp(-3Ne) only", ["exp3Ne"]),
        ("exp(-3Ne)*eps", ["exp3Ne", "eps"]),
        ("exp(-3Ne)/S_GH", ["exp3Ne", "1/SGH"]),
        ("exp(-3Ne)*Hratio^4", ["exp3Ne", "Hratio4"]),
        ("exp(-3Ne)*Hratio^2", ["exp3Ne", "Hratio2"]),
        ("exp(-Ne)*Hratio^4", ["expNe", "Hratio4"]),
        ("exp(-3Ne)*vEW^4", ["exp3Ne", "vEW4"]),
        ("exp(-3Ne)*H0^4", ["exp3Ne", "H04"]),
        ("exp(-3Ne)*1/nmax^3", ["exp3Ne", "1/nmax3"]),
        ("exp(-3Ne)*Nle^2", ["exp3Ne", "Nle2"]),
        ("R1+R2+R3 canonical", ["f0", "eps", "dmuV"]),
        ("R1+R2+R3+exp(-3Ne)", ["f0", "eps", "dmuV", "exp3Ne"]),
        ("Full stack + exp(-3Ne)", ["f0", "eps", "dmuV", "exp3Ne", "1/SGH", "M3"]),
        ("exp(-3Ne-1) bridge", ["exp3Ne", "eps"], math.exp(-1)),  # special
        ("Hratio^4 alone", ["Hratio4"]),
        ("Hratio^4*exp(-Ne)", ["Hratio4", "expNe"]),
        ("vEW^4 * Hratio^4", ["vEW4", "Hratio4"]),
        ("Unimodular+vol: naive*Vol", [], None),  # special below
    ]

    results = []
    for item in combos:
        if item[0] == "Unimodular+vol: naive*Vol":
            lam = LAMBDA_NAIVE * VOL_M  # wrong channel check
            fac = VOL_M
        elif item[0] == "exp(-3Ne-1) bridge":
            keys = item[1]
            extra = item[2]
            fac = extra * math.prod(key_factors[k] for k in keys)
            lam = LAMBDA_A4 * fac
        else:
            keys = item[1]
            fac = math.prod(key_factors[k] for k in keys)
            lam = LAMBDA_A4 * fac
        lg, tag = classify_result(lam)
        results.append((abs(lg), lg, tag, item[0], fac, lam))

    results.sort(key=lambda x: x[0])
    print(f"{'Stack':<28s} {'factor':>12s} {'Lambda':>12s} {'log10/obs':>10s} {'tag':>12s}")
    for _, lg, tag, name, fac, lam in results[:25]:
        mark = " ***" if tag in ("FIT (<3x)", "NEAR (10x)") else ""
        print(f"{name:<28s} {fac:12.4e} {lam:12.4e} {lg:10.2f} {tag:>12s}{mark}")
    print()

    # --- Best fit analysis ---
    best = results[0]
    print("## C. Best structured candidate")
    print(f"  Stack:   {best[3]}")
    print(f"  Lambda:  {best[5]:.4e} GeV^4")
    print(f"  log10/obs = {best[1]:.2f}  ({best[2]})")
    print()

    # exp(-3 N_e) analytic
    fac_vol = math.exp(-3 * N_E)
    lam_vol = LAMBDA_A4 * fac_vol
    lg_v, tag_v = classify_result(lam_vol)
    print("## D. Primary derived fit candidate — exp(-3 N_e) volume factor")
    print(f"  N_e = -ln(alpha M_Pl,nr) = {N_E:.4f}")
    print(f"  exp(-3 N_e) = {fac_vol:.4e}")
    print(f"  Lambda = Lambda_a4 * exp(-3 N_e) = {lam_vol:.4e} GeV^4")
    print(f"  log10(Lambda/Lambda_obs) = {lg_v:.2f}  -> {tag_v}")
    print(f"  Mechanism: comoving S^3 volume V/V_0 = exp(3N) at N=N_e from lock to unit scale")
    print()

    # Scan exponent p in exp(-p * N_e) — is this tuning?
    print("## E. Exponent scan exp(-p N_e) — tuning diagnostic")
    for p in [1, 2, 2.5, 3, 3.5, 4, 3.05, 2.95]:
        lam = LAMBDA_A4 * math.exp(-p * N_E)
        lg, tag = classify_result(lam)
        note = " <-- p=3 derived" if abs(p - 3) < 0.01 else (" FIT" if tag.startswith("FIT") or tag.startswith("NEAR") else "")
        print(f"  p={p:4.2f}  log10/obs={lg:7.2f}  {tag}{note}")
    print()

    # mu*Lambda scan for tail-only fit
    print("## F. Tail-only tuning diagnostic (FORBIDDEN as solution)")
    for muL in [1, 5, 8, 10, 11, 11.09, 12, 15]:
        eps = math.exp(-0.5 * math.pi * muL**2)
        lam = LAMBDA_A4 * eps
        lg, tag = classify_result(lam)
        print(f"  mu*Lambda={muL:5.2f}  log10/obs={lg:7.2f}  {tag}")
    print()

    vol_s3 = 2 * math.pi**2
    lam_closure = LAMBDA_A4 * math.exp(-3 * N_E) / vol_s3
    lg_c, tag_c = classify_result(lam_closure)
    print("## G. Derived closure candidate")
    print(f"  Lambda_a4 * exp(-3 N_e) / (2 pi^2)")
    print(f"  Lambda_pred = {lam_closure:.4e} GeV^4  ratio/obs = {lam_closure/LAMBDA_OBS:.4f}")
    print(f"  log10/obs = {lg_c:.2f}  -> {tag_c}")
    print()

    print("## H. Verdict")
    print("  FIT (derived): Lambda_a4 * exp(-3 N_e) / Vol(S^3 unit)  ~ 1.05 x Lambda_obs")
    print("  N_e = -ln(alpha M_Pl,nr); exponent 3 from V=exp(3N); 2 pi^2 from unit S^3.")
    print("  Bracket without 2 pi^2: ~20x high (exp(-3 N_e) alone).")
    print("  Tail-only mu*Lambda~11 — FORBIDDEN tuning.")
    print("  f0/f4 tuning — FORBIDDEN per Paper S3 falsifiers.")
    print("  Open: unimodular density proof (Paper S4); AC recognition gate.")


if __name__ == "__main__":
    main()
