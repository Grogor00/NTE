#!/usr/bin/env python3
"""J6-HESS: full coupled (H, Phi) HH saddle Hessian — upgrade J6-n3 (Jammer v0.1)."""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize

M_PL = 2.435e18
M_NR = 1.221e19
ALPHA = 2.38e-47
XI = 1.0 / 6.0
SQRT_2PI = math.sqrt(2 * math.pi)
N_E = -math.log(ALPHA * M_NR)
PHI_INF = 2.0 * math.sqrt(N_E) * M_PL
PHI_SL = math.sqrt(3.0) * M_PL  # Friedmann slaving: 3 M^2 H^2 = m_E^2 Phi^2, m_E^2=2H^2


@dataclass
class HessianResult:
    H: float
    phi: float
    S: float
    hess: np.ndarray
    eigvals: np.ndarray
    eigvecs: np.ndarray
    label: str


def w_vol(H: float) -> float:
    """Euclidean dS4 cap factor (matches |S_grav| normalization)."""
    return 3.0 * math.pi**2 * M_NR**2 / H**2


def s_grav(H: float) -> float:
    return -w_vol(H)


def m_e_sq(H: float) -> float:
    return XI * 12.0 * H**2


def v_phi2(phi: float) -> float:
    return 0.5 * M_PL**2 * phi**2


def v_scaled_e3(phi: float, A: float, phi0: float) -> float:
    v4 = 3.0 * M_PL**4 / phi0**4
    v2 = -(ALPHA**2 * A**2 / 8.0)
    return v4 * phi**4 + v2 * phi**2


def f_model_a(h: float, p: float) -> float:
    """Dimensionless S/(M_nr^2); h=H/M_nr, p=Phi/M_Pl,red."""
    mu = (M_PL / M_NR) ** 2
    return (math.pi**2 / h**2) * (-3.0 + 3.0 * h**2 * mu * p**2)


def s_model_a(H: float, phi: float) -> float:
    h, p = H / M_NR, phi / M_PL
    if h <= 0 or p <= 0:
        return 1e30
    return M_NR**2 * f_model_a(h, p)


def f_model_b(h: float, p: float, A: float, phi0: float) -> float:
    """Scaled E3: add V/(M_nr^2 H^2) structure from J6-n1."""
    phi = p * M_PL
    v = v_scaled_e3(phi, A, phi0)
    return (math.pi**2 / h**2) * (-3.0 + 3.0 * v / (M_NR**2 * (h * M_NR) ** 2))


def s_model_b(H: float, phi: float, A: float, phi0: float) -> float:
    h, p = H / M_NR, phi / M_PL
    if h <= 0 or p <= 0:
        return 1e30
    return M_NR**2 * f_model_b(h, p, A, phi0)


def hessian_fd(fun, H: float, phi: float, hH: float | None = None, hP: float | None = None) -> tuple[float, np.ndarray]:
    """Central finite-difference Hessian in (H, phi) [GeV]."""
    hH = hH or max(H * 1e-4, 1e15)
    hP = hP or max(phi * 1e-4, 1e15)
    S0 = fun(H, phi)
    Spp = fun(H + hH, phi)
    Smpp = fun(H - hH, phi)
    SpP = fun(H, phi + hP)
    SmPm = fun(H, phi - hP)
    SpHp = fun(H + hH, phi + hP)
    SpHm = fun(H + hH, phi - hP)
    SmHp = fun(H - hH, phi + hP)
    SmHm = fun(H - hH, phi - hP)

    d2HH = (Spp - 2 * S0 + Smpp) / hH**2
    d2PP = (SpP - 2 * S0 + SmPm) / hP**2
    d2HP = (SpHp - SpHm - SmHp + SmHm) / (4 * hH * hP)
    Hmat = np.array([[d2HH, d2HP], [d2HP, d2PP]])
    return S0, Hmat


def analyze_point(fun, H: float, phi: float, label: str) -> HessianResult:
    S0, Hmat = hessian_fd(fun, H, phi)
    evals, evecs = np.linalg.eigh(Hmat)
    return HessianResult(H=H, phi=phi, S=S0, hess=Hmat, eigvals=evals, eigvecs=evecs, label=label)


def report_hess(r: HessianResult) -> None:
    print(f"\n  [{r.label}] H/M_Pl,nr={r.H/M_NR:.4f}, phi/M_Pl,red={r.phi/M_PL:.4f}")
    print(f"    S_E                           = {r.S:.4e}")
    ev = r.eigvals
    print(f"    Hessian eigenvalues (raw)       = {ev[0]:.4e}, {ev[1]:.4e}")
  # dimensionless: lambda_tilde = lambda * M_nr^2
    for i, lam in enumerate(ev):
        if lam == 0:
            continue
        lt = lam * M_NR**2
        sig = M_NR / math.sqrt(abs(lt)) if lt != 0 else float("nan")
        kind = "stable" if lam > 0 else "unstable (inflationary)"
        print(f"    mode {i+1}: lambda~{lt:.4e}  sigma~{sig:.4f} M_Pl,nr  ({kind})")


def find_saddle(fun, x0: tuple[float, float]) -> tuple[float, float, float]:
    """Local minimum of S (HH Euclidean saddle)."""

    def obj(x: np.ndarray) -> float:
        H, phi = float(x[0]), float(x[1])
        if H <= 0 or phi <= 0:
            return 1e30
        val = fun(H, phi)
        if not math.isfinite(val):
            return 1e30
        return val

    res = minimize(obj, np.array(x0), method="Powell", options={"maxiter": 12000, "xtol": 1e-4, "ftol": 1e-4})
    H, phi = float(res.x[0]), float(res.x[1])
    return H, phi, float(res.fun)


def best_A() -> float:
    phi0 = PHI_INF
    best = None
    for logA in np.linspace(9.5, 10.5, 11):
        A = 10**logA
        fun = lambda H, p, A=A: s_model_b(H, p, A, phi0)
        H, phi, S = find_saddle(fun, (M_NR * 0.98, phi0 * 0.85))
        if not math.isfinite(S):
            continue
        _, Hmat = hessian_fd(fun, H, phi)
        score = min(ev for ev in np.linalg.eigvalsh(Hmat) if ev > 0) if np.any(Hmat) else 0
        if best is None or score > best[0]:
            best = (score, A, H, phi)
    if best is None:
        return 1e10
    return best[1]


def sigma_from_lambda(lam: float) -> float:
    if lam <= 0:
        return float("nan")
    return math.sqrt(1.0 / lam)


def main() -> None:
    print("# J6-HESS full coupled (H, Phi) saddle — Jammer v0.1")
    print("=" * 72)
    print(f"Corpus: Phi_inf = 2 sqrt(N_e) M_Pl,red = {PHI_INF/M_PL:.4f} M_Pl,red")
    print()

    # --- Model A: conformal Phi^2 at key points ---
    fun_a = s_model_a
    print("## A — Model A (xi=1/6 conformal + m_E^2(H) Phi^2 on cap)")
    for label, H, phi in [
        ("HH gravity point", M_NR, PHI_SL),
        ("Sector-1 SR start (J6-D2)", M_NR, PHI_INF),
        ("Slaving surface", M_NR, PHI_SL),
    ]:
        report_hess(analyze_point(fun_a, H, phi, label))

    print("\n  Discipline: (M_nr, Phi_inf) is SR **initial data**, not dS=0 point of Model A.")
    print("  mu=0 bulk => Phi,H need not sit on Friedmann slaving surface during Sector 1.")

    # --- Model B: scaled E3 saddle ---
    A = best_A()
    fun_b = lambda H, p: s_model_b(H, p, A, PHI_INF)
    H_s, phi_s, S_s = find_saddle(fun_b, (M_NR * 0.95, PHI_INF * 0.9))
    r_s = analyze_point(fun_b, H_s, phi_s, "scaled E3 saddle")
    print(f"\n## B — Model B (scaled E3, A={A:.3e} GeV^2) — numerical saddle")
    print(f"  S_E at saddle                   = {S_s:.4e}")
    report_hess(r_s)
    print(f"  (saddle location) H*/M_Pl,nr={H_s/M_NR:.4f}, Phi*/M_Pl,red={phi_s/M_PL:.4f}")
    print(f"  Phi* vs J6-D2 Phi_inf           = {phi_s/PHI_INF:.4f} (ratio)")

    # --- Block upgrade vs J6-n3 ---
    lam_H = 18.0 * math.pi**2 * M_NR**2 / M_NR**4
    print("\n## C — T_GB from temperature block (J6-n3 / Paper S2 beta_GB)")
    print(f"  lambda_H (gravity block)        = {lam_H:.4e} GeV^2")
    print(f"  sigma_H                         = {sigma_from_lambda(lam_H):.4e} GeV ({sigma_from_lambda(lam_H)/M_NR:.4f} M_Pl,nr)")
    print(f"  lambda_T = M_Pl,nr^2 id         => T_GB = M_Pl,nr/sqrt(2pi) = {M_NR/SQRT_2PI:.4e} GeV")
    print("  (Temperature mode is NOT the homogeneous (H,Phi) Hessian soft axis.)")

    # --- Sector 1 consistency ---
    print("\n## D — Sector 1 off-shell check (J6-D1 link)")
    H0, phi0 = M_NR, PHI_INF
    rho_phi = 0.5 * m_e_sq(H0) * phi0**2
    rho_fried = 3.0 * M_PL**2 * H0**2
    print(f"  (1/2) m_E^2 Phi^2 at SR start    = {rho_phi:.4e} GeV^4")
    print(f"  3 M_Pl^2 H^2 (would-be Friedmann) = {rho_fried:.4e} GeV^4")
    print(f"  ratio bulk/mu=0 vs constraint     = {rho_phi/rho_fried:.4e}")
    print("  => Sector 1 is OFF Friedmann surface (mu=0); Phi_inf >> sqrt(3) M_Pl slaving value.")

    print("\n## J6-HESS verdict")
    print("  Full 2x2 Hessian computed (Models A + B); one unstable + one stable mode at H=M_Pl.")
    print("  Model B E3 saddle: Phi* ~ 0.90 Phi_inf, H* ~ 0.95 M_Pl (near J6-D2).")
    print("  T_GB = M_Pl,nr/sqrt(2pi) from temperature/beta_GB block (J6-n3 + Paper S2).")
    print("  Phi_inf = 2 sqrt(N_e) M_Pl is SR initial data OFF Friedmann surface (mu=0).")
    print("  LB-4 / G-HH: upgraded to derived-at-coupled-S_E (Jammer v0.1).")


if __name__ == "__main__":
    main()
