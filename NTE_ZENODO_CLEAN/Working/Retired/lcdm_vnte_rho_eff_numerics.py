#!/usr/bin/env python3
"""V_NTE D1: rho_eff from candidate V_NTE vs 3H^2/(8piG) at cosmological epochs.

Genuine test of P1 tautological relabelling (Jammer P1 review SS1.3).
Uses canonical trajectory |Phi|^2 = v_EW^2 (H/H0), not working-profile e^{-N}.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

# --- Corpus constants (GeV units, hbar=c=1) ---
ALPHA = 2.38e-47  # GeV^-1, SS2.4.2
V_EW = 246.0  # GeV
M_PL = 2.435e18  # GeV, reduced Planck mass
OM_R, OM_M, OM_L = 9.0e-5, 0.315, 0.685
N_LOCK = 0.105  # SS17.5.4 candidate
N_E = 63.4  # Hartle-Hawking e-folds


def h_ratio(N: float) -> float:
    return math.sqrt(OM_R * math.exp(-4 * N) + OM_M * math.exp(-3 * N) + OM_L)


def dh_dN(N: float) -> float:
    f = OM_R * math.exp(-4 * N) + OM_M * math.exp(-3 * N) + OM_L
    df = -4 * OM_R * math.exp(-4 * N) - 3 * OM_M * math.exp(-3 * N)
    return df / (2 * math.sqrt(f))


def phi_and_phidot(N: float, H0: float) -> tuple[float, float, float]:
    """Return (Phi [GeV], Phi_dot [GeV^2], H [GeV])."""
    hr = h_ratio(N)
    H = H0 * hr
    phi2 = V_EW**2 * hr
    phi = math.sqrt(phi2)
    dhr = dh_dN(N)
    dphi_dN = V_EW**2 * dhr / (2 * phi)
    phidot = H * dphi_dN
    return phi, phidot, H


def rho_friedmann(H: float) -> float:
    """rho_eff target = 3 H^2 / (8 pi G) = 3 H^2 M_Pl^2 (8piG=1/M_Pl^2)."""
    return 3.0 * H**2 * M_PL**2


def w_cosmo(N: float) -> float:
    """Effective w from Friedmann component weights at N."""
    hr = h_ratio(N)
    num = OM_R * math.exp(-4 * N) + OM_M * math.exp(-3 * N)  # radiation + matter (no Lambda pressure)
    den = hr**2
    # rho_Lambda contributes to H but w_L = -1; total w = sum w_i Omega_i
    wr = 1.0 / 3.0
    wm = 0.0
    wl = -1.0
    fr = OM_R * math.exp(-4 * N) / den
    fm = OM_M * math.exp(-3 * N) / den
    fl = OM_L / den
    return wr * fr + wm * fm + wl * fl


def w_scalar(kin: float, pot: float) -> float:
    """Scalar-field w = p/rho, p = kin - pot (K=1)."""
    rho = kin + pot
    if abs(rho) < 1e-300:
        return float("nan")
    return (kin - pot) / rho


def rho_components(N: float, H0: float) -> dict:
    hr = h_ratio(N)
    rho0 = 3.0 * H0**2 * M_PL**2
    rho_tot = rho0 * hr**2
    rho_r = rho0 * OM_R * math.exp(-4 * N)
    rho_m = rho0 * OM_M * math.exp(-3 * N)
    rho_l = rho0 * OM_L
    return {"tot": rho_tot, "r": rho_r, "m": rho_m, "l": rho_l}


def v_leading(phi: float) -> float:
    """E1: V = 3 alpha^2 M_Pl^2 Phi^4 (Companion 9 extension E1)."""
    return 3.0 * ALPHA**2 * M_PL**2 * phi**4


def v_post_ontraj(phi: float) -> float:
    """E2 / F3 post-locking on-trajectory extended (Companion 8 eq 10a)."""
    return 3.0 * ALPHA**2 * M_PL**2 * phi**4 - (ALPHA**2 / 8.0) * phi**6


def v_pre_ontraj(phi: float, A: float) -> float:
    """E3 / F3 pre-temporal on-trajectory (Companion 8 eq 10b)."""
    return 3.0 * ALPHA**2 * M_PL**2 * phi**4 - (ALPHA**2 * A**2 / 8.0) * phi**2


def v_hilltop_smooth(phi: float) -> float:
    """Session 4 smooth connection: leading + Phi^6 subleading (post form global)."""
    return v_post_ontraj(phi)


def v_inverted(phi: float, phidot: float, K: float = 1.0) -> float:
    """Friedmann inversion: V = 3 alpha^2 M_Pl^2 Phi^4 - (1/2) K Phi_dot^2 (always consistent)."""
    return 3.0 * ALPHA**2 * M_PL**2 * phi**4 - 0.5 * K * phidot**2


def v_marcolli_leading(phi: float, lam0: float | None = None) -> float:
    """Marcolli sigma-field leading quartic (structural confluence, SS7.11)."""
    if lam0 is None:
        lam0 = 3.0 * ALPHA**2 * M_PL**2
    return lam0 * phi**4


def v_anchor_v1min(phi: float) -> float:
    """F3 (V1'-min) anchoring term at v_EW — illustrative, lambda tuned to min at v_EW."""
    v0 = v_post_ontraj(phi)
    # Quadratic anchor (Companion 8 SS5.6): add lambda*(Phi^2 - v_EW^2)^2
    # Choose lambda so dV/dPhi = 0 at phi = v_EW (local minimum feature)
    # d/dphi [3a^2 M^2 phi^4 - a^2/8 phi^6 + lam (phi^2-v^2)^2] = 0 at phi=v
    # 12 a^2 M^2 v^3 - 3 a^2/8 v^5 + 4 lam v (v^2-v^2) ... at phi=v the anchor deriv is 0 always
    # Need second derivative > 0; use small lambda for illustration only
    lam = ALPHA**2 * M_PL**2 / (8.0 * V_EW**4)  # order-of-magnitude anchor
    return v0 + lam * (phi**2 - V_EW**2) ** 2


@dataclass
class Epoch:
    name: str
    N: float
    z_label: str


EPOCHS = [
    Epoch("Today (Lambda-dom)", 0.0, "z=0"),
    Epoch("Matter-Lambda equality", math.log(OM_M / OM_L) / 3.0, "z~0.39"),
    Epoch("DESI BAO era", -0.406, "z~0.5"),
    Epoch("Matter-dom anchor", -3.0, "z~19"),
    Epoch("BBN (radiation dom)", -20.72, "z~1e9"),
]


@dataclass
class Candidate:
    label: str
    motivated: str
    v_fn: Callable[..., float]
    uses_phidot: bool = False
    extra_kw: dict | None = None


def pre_A(H0: float) -> float:
    """Slope A in |Phi|^2 = A y pre-temporal linear profile (Companion 8 SS5.3)."""
    N_at_lock = -N_LOCK  # N from today at locking (small negative)
    hr_lock = h_ratio(N_at_lock)
    phi2_lock = V_EW**2 * hr_lock
    return phi2_lock / N_LOCK


def eval_candidate(
    cand: Candidate,
    N: float,
    H0: float,
    K: float = 1.0,
    A: float = 0.0,
) -> dict:
    phi, phidot, H = phi_and_phidot(N, H0)
    rho_t = rho_friedmann(H)
    kin = 0.5 * K * phidot**2

    if cand.uses_phidot:
        V = cand.v_fn(phi, phidot, K=K)
    elif cand.label.startswith("E3") or cand.label.startswith("pre"):
        V = cand.v_fn(phi, A)
    else:
        V = cand.v_fn(phi)

    rho_v = kin + V
    frac_kin = kin / rho_t if rho_t else float("nan")
    return {
        "phi_gev": phi,
        "phi_over_vEW": phi / V_EW,
        "phidot_gev2": phidot,
        "H_over_H0": H / H0,
        "rho_target": rho_t,
        "rho_kin": kin,
        "rho_pot": V,
        "rho_total": rho_v,
        "ratio": rho_v / rho_t,
        "delta_pct": 100.0 * (rho_v / rho_t - 1.0),
        "frac_kin": frac_kin,
    }


def main() -> None:
    H0 = ALPHA * V_EW**2
    A = pre_A(H0)

    candidates = [
        Candidate(
            "C0_inverted",
            "Friedmann inversion (control — must match)",
            v_inverted,
            uses_phidot=True,
        ),
        Candidate(
            "E1_quartic_only",
            "Companion 9 E1: global 3 alpha^2 M_Pl^2 Phi^4",
            v_leading,
        ),
        Candidate(
            "E2_post_Phi6",
            "Companion 8 F3 post / E2: + Phi^6 subleading",
            v_post_ontraj,
        ),
        Candidate(
            "E3_pre_Phi2",
            "Companion 8 F3 pre / E3: + Phi^2 subleading (A from N_lock)",
            v_pre_ontraj,
        ),
        Candidate(
            "hilltop_smooth",
            "Session 4 smooth Phi^4-Phi^6 (= E2 globally)",
            v_hilltop_smooth,
        ),
        Candidate(
            "anchor_V1min",
            "F3 (V1'-min) anchor at v_EW (illustrative)",
            v_anchor_v1min,
        ),
    ]

    print("# V_NTE rho_eff vs Friedmann target (P1 genuine test)")
    print(f"# H0 = alpha v_EW^2 = {H0:.4e} GeV")
    print(f"# M_Pl,red = {M_PL:.4e} GeV; pre-temporal A = {A:.4e} GeV^2")
    print(f"# Trajectory: |Phi|^2 = v_EW^2 (H/H0); K(Phi)=1")
    print()

    for ep in EPOCHS:
        hr = h_ratio(ep.N)
        om_r_frac = OM_R * math.exp(-4 * ep.N) / hr**2
        om_m_frac = OM_M * math.exp(-3 * ep.N) / hr**2
        om_l_frac = OM_L / hr**2
        print(f"## {ep.name} ({ep.z_label}, N={ep.N:.3f})")
        print(f"   Omega_r/m/L fractions: {om_r_frac:.4g} / {om_m_frac:.4g} / {om_l_frac:.4g}")
        print(
            "| Candidate | rho_VNTE/rho_FRI | delta % | kin/rho_FRI | Phi/v_EW |"
        )
        print("|-----------|------------------|---------|-------------|----------|")
        for cand in candidates:
            r = eval_candidate(cand, ep.N, H0, A=A)
            print(
                f"| {cand.label} | {r['ratio']:.6g} | {r['delta_pct']:+.2e} | "
                f"{r['frac_kin']:.4g} | {r['phi_over_vEW']:.4g} |"
            )
        print()

    # Component scaling diagnostic: does E1 potential alone scale like rho_total?
    print("## Scaling diagnostic (E1 potential / rho_FRI vs epoch)")
    print("| Epoch | rho_pot/rho_FRI | kin/rho_FRI needed for match |")
    print("|-------|-----------------|------------------------------|")
    for ep in EPOCHS:
        r_e1 = eval_candidate(candidates[1], ep.N, H0, A=A)
        r_c0 = eval_candidate(candidates[0], ep.N, H0, A=A)
        print(
            f"| {ep.name} | {r_e1['rho_pot']/r_e1['rho_target']:.6g} | "
            f"{r_c0['frac_kin']:.6g} |"
        )
    print()

    print("## Equation-of-state diagnostic (genuine scaling test)")
    print("Scalar w from (1/2 Phi_dot^2 - V)/(rho); LCDM w_eff from Omega weights.")
    print("| Epoch | w_LCDM | w_scalar E1 | w_scalar E2 | kin/V_E1 | Phi/M_Pl |")
    print("|-------|--------|-------------|-------------|----------|----------|")
    for ep in EPOCHS:
        r1 = eval_candidate(candidates[1], ep.N, H0, A=A)
        r2 = eval_candidate(candidates[2], ep.N, H0, A=A)
        wc = w_cosmo(ep.N)
        ws1 = w_scalar(r1["rho_kin"], r1["rho_pot"])
        ws2 = w_scalar(r2["rho_kin"], r2["rho_pot"])
        kin_v = r1["rho_kin"] / r1["rho_pot"] if r1["rho_pot"] else float("nan")
        phi, _, _ = phi_and_phidot(ep.N, H0)
        print(
            f"| {ep.name} | {wc:.4f} | {ws1:.4f} | {ws2:.4f} | "
            f"{kin_v:.4e} | {phi/M_PL:.4e} |"
        )
    print()

    print("## Component fraction vs single-field V interpretation")
    print("If rho_VNTE = rho_tot, does scalar w match thermal w of dominant component?")
    print("| Epoch | dom | rho_r/tot | rho_m/tot | w_dom | w_scalar E1 | mismatch |")
    print("|-------|-----|-----------|-----------|-------|-------------|----------|")
    for ep in EPOCHS:
        comp = rho_components(ep.N, H0)
        fr = comp["r"] / comp["tot"]
        fm = comp["m"] / comp["tot"]
        fl = comp["l"] / comp["tot"]
        if fr > 0.9:
            dom, w_dom = "radiation", 1.0 / 3.0
        elif fm > 0.9:
            dom, w_dom = "matter", 0.0
        elif fl > 0.9:
            dom, w_dom = "Lambda", -1.0
        else:
            dom, w_dom = "mixed", w_cosmo(ep.N)
        r1 = eval_candidate(candidates[1], ep.N, H0, A=A)
        ws1 = w_scalar(r1["rho_kin"], r1["rho_pot"])
        print(
            f"| {ep.name} | {dom} | {fr:.4g} | {fm:.4g} | {w_dom:.3f} | "
            f"{ws1:.4f} | {ws1 - w_dom:+.4f} |"
        )
    print()

    print("## Subleading correction magnitude (E2/E3 vs E1 leading)")
    print("| Epoch | dV_E2/rho | dV_E3/rho | inverted kin/rho |")
    print("|-------|-----------|-----------|------------------|")
    for ep in EPOCHS:
        phi, phidot, H = phi_and_phidot(ep.N, H0)
        rho_t = rho_friedmann(H)
        v1 = v_leading(phi)
        d2 = (v_post_ontraj(phi) - v1) / rho_t
        d3 = (v_pre_ontraj(phi, A) - v1) / rho_t
        kin_frac = 0.5 * phidot**2 / rho_t
        print(f"| {ep.name} | {d2:.4e} | {d3:.4e} | {kin_frac:.4e} |")
    print()

    print("# Verdict summary:")
    print("# 1. MAGNITUDE: E1 quartic V = 3 alpha^2 M_Pl^2 Phi^4 matches rho_FRI at every epoch")
    print("#    ON the H=alpha Phi^2 + |Phi|^2=v_EW^2(H/H0) trajectory (tautology class).")
    print("# 2. SCALING: rho magnitude tracks LCDM eras because Phi is slaved to H.")
    print("# 3. GENUINE FAIL: scalar w from V_E1 ~ -1 always (V dominates); NOT w=1/3 at BBN,")
    print("#    w=0 in matter era. Thermal split is in SM+Lambda bookkeeping, not V_NTE quartic.")
    print("# 4. SUBLEADING: E2 Phi^6 / E3 Phi^2 corrections negligible (Phi << M_Pl on post-lock traj).")
    print("# 5. CLOSURE PATH: inverted V(Phi,Phi_dot) or Lagrange-multiplier (Appendix B) - not unique V(Phi).")


if __name__ == "__main__":
    main()
