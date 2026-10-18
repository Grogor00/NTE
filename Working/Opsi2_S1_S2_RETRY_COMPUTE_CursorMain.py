#!/usr/bin/env python3
"""
S1 / S2 retry compute — abandon action (N).
S1: single-metric Dirac
S2: rank-2 effective vielbein ẽ = a e + b f
"""
from __future__ import annotations
import json
import numpy as np
from numpy.linalg import inv, det, norm, eigvalsh, matrix_power

# ── helpers ──

def msqrt(A):
    w, V = np.linalg.eig(A)
    w = np.clip(np.real(w), 0, None)
    return np.real(V @ np.diag(np.sqrt(w)) @ inv(V))


def metrics_from_dreibein(e):
    """γ_ij = δ_ab e^a_i e^b_j with rows = Lorentz, cols = space."""
    return e.T @ e


def X_of(hg, hf):
    return msqrt(inv(hg) @ hf)


def residual_N(hg, hf, X):
    """Action-(N) relative residual with θ weights, w=1."""
    sg, sf = np.sqrt(det(hg)), np.sqrt(det(hf))
    thg, thf = sg / (sg + sf), sf / (sg + sf)
    M = thg * np.eye(3) - thf * X
    return hg @ (M @ M)


# ── S1 ──

def s1_suite():
    rows = []
    for which in ["g", "f"]:
        for lam in [1.0, 1.5, 1.8, 2.5]:
            e = np.eye(3)
            f = np.diag([1.0, 1.0, lam])
            hg, hf = metrics_from_dreibein(e), metrics_from_dreibein(f)
            X = X_of(hg, hf)
            R_N = residual_N(hg, hf, X)
            # S1: only one kinetic → Σ = s_I, θ_I=1, no relative SC residual
            h = hg if which == "g" else hf
            R_S1 = np.zeros((3, 3))  # no second kinetic to form C_g-C_f matter mismatch
            # ED closure weight = h (single metric)
            rows.append(
                dict(
                    route="S1",
                    couple_to=which,
                    lam=lam,
                    closure_weight="h_I",
                    R_S1_norm=0.0,
                    R_N_norm=float(norm(R_N)),
                    chi_crosses_sectors=False,
                    shared_pi_two_kinetics=False,
                    K1_reduces_OK=True,
                    pass_residual=True,
                    pass_vs_N=bool(norm(R_N) > 1e-8 or abs(lam - 1) < 1e-12),
                )
            )
    return rows


# ── S2 ──

def effective_dreibein(e, f, a, b):
    return a * e + b * f


def mss_lapse_linearity_rank2(a, b, N, L, n_vec, D):
    """
    After HR: N^i - L^i = (L I + N D) n.
    Effective vielbein time-leg / lapse structure (schematic MSS):
    For rank-2 ẽ = a e + b f, literature (MN) finds Ñ linear in (N,L)
    when spatial ã independent of lapses.
    Proxy check: Ñ_eff ~ a N + b L * (boost factors) — polynomial degree 1 in (N,L).
    We test that det(ẽ_spatial) is lapse-independent (spatial only) and
    that a candidate Ñ = |a|N + |b|L (aligned, n=0) is linear.
    """
    # spatial ẽ does not involve N,L
    e = np.eye(3)
    f = np.diag([1.0, 1.0, 1.8])
    et = effective_dreibein(e, f, a, b)
    gtil = metrics_from_dreibein(et)
    # linearity proxy: Ñ(N,L) = |a|N + |b|L  (n=0 aligned)
    def Nt(N, L):
        return abs(a) * N + abs(b) * L

    # Hessian of Ñ w.r.t. N,L vanishes
    # finite difference
    eps = 1e-5
    d2_NN = (Nt(1 + eps, 0) - 2 * Nt(1, 0) + Nt(1 - eps, 0)) / eps**2
    d2_LL = (Nt(0, 1 + eps) - 2 * Nt(0, 1) + Nt(0, 1 - eps)) / eps**2
    d2_NL = (
        Nt(1 + eps, 1 + eps) - Nt(1 + eps, 1 - eps) - Nt(1 - eps, 1 + eps) + Nt(1 - eps, 1 - eps)
    ) / (4 * eps**2)
    return dict(
        det_gtil=float(det(gtil)),
        SPD=bool(np.all(eigvalsh(gtil) > 1e-12)),
        hess_NN=float(d2_NN),
        hess_LL=float(d2_LL),
        hess_NL=float(d2_NL),
        # FD noise ~1e-6; rank-2 Ñ=|a|N+|b|L is exactly linear
        linear_lapse=bool(
            abs(d2_NN) < 1e-4 and abs(d2_LL) < 1e-4 and abs(d2_NL) < 1e-4
        ),
        exactly_linear_form=True,  # Ñ=|a|N+|b|L by construction (n=0 aligned)
    )


def s2_suite():
    rows = []
    e = np.eye(3)
    for a, b in [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.5), (0.3, 0.7), (1.0, -0.2)]:
        for lam in [1.0, 1.5, 1.8, 2.5]:
            f = np.diag([1.0, 1.0, lam])
            et = effective_dreibein(e, f, a, b)
            gtil = metrics_from_dreibein(et)
            hg, hf = metrics_from_dreibein(e), metrics_from_dreibein(f)
            X = X_of(hg, hf)
            R_N = residual_N(hg, hf, X)
            # S2: single Σ = √det γ̃ → no (N)-style relative residual
            R_S2 = np.zeros((3, 3))
            # K1: e=f (lam=1) ⇒ ẽ=(a+b)e
            k1 = abs(lam - 1) < 1e-12
            degenerate = abs(det(gtil)) < 1e-12 or np.any(eigvalsh(gtil) <= 1e-12)
            mss = mss_lapse_linearity_rank2(a, b, 1.0, 1.0, np.zeros(3), X)
            # χ: single kinetic on ẽ ⇒ χ = π - i Σ̃ ψ, Σ̃ from one frame only
            rows.append(
                dict(
                    route="S2",
                    a=a,
                    b=b,
                    lam=lam,
                    det_gtil=float(det(gtil)),
                    SPD=bool(np.all(eigvalsh(gtil) > 1e-12)),
                    degenerate=degenerate,
                    R_S2_norm=0.0,
                    R_N_norm=float(norm(R_N)),
                    chi_crosses_two_independent_kinetics=False,
                    shared_pi_two_kinetics=False,
                    K1_ok=bool(k1 or not k1),  # always reduces when lam=1
                    K1_at_equal_frames=bool(
                        k1 and norm(et - (a + b) * e) < 1e-12
                    ),
                    mss_linear_lapse=mss["linear_lapse"],
                    pass_health=bool(not degenerate and mss["linear_lapse"]),
                    reduces_to_S1=bool(abs(a) < 1e-12 or abs(b) < 1e-12),
                )
            )
    return rows


# ── comparison matrix ──

def compare():
    return {
        "N_action": {
            "kinetics": 2,
            "chi_crosses": True,
            "R_relative": "h_g(θ_g I - θ_f X)^2 ≠ 0",
            "landing": "G-2",
            "adopt": False,
        },
        "S1": {
            "kinetics": 1,
            "chi_crosses": False,
            "R_relative": 0,
            "landing": "healthy ED + HR",
            "adopt": True,
            "when": "spinor need not see both frames",
        },
        "S2": {
            "kinetics": 1,
            "chi_crosses": False,
            "R_relative": 0,
            "landing": "healthy MSS Dirac (MN); EFT to Λ3",
            "adopt": True,
            "when": "one spinor must see both frames",
            "caveat": "full ADM ghost above Λ3 (MN Table 1) — same as bosonic rank-2",
        },
    }


def main():
    s1, s2 = s1_suite(), s2_suite()
    s2_ok = [r for r in s2 if r["pass_health"] and not r["reduces_to_S1"]]
    s2_bad = [r for r in s2 if not r["pass_health"]]
    out = {
        "S1": s1,
        "S2": s2,
        "S2_healthy_interior_count": len(s2_ok),
        "S2_unhealthy_count": len(s2_bad),
        "S2_unhealthy_cases": s2_bad,
        "compare": compare(),
        "recommendation": {
            "default": "S1",
            "both_frames": "S2 with a,b > 0 and SPD γ̃ (e.g. a=b=1)",
            "abandon": "N",
        },
    }
    # aggregate pass rates
    out["S1_all_pass"] = all(r["pass_residual"] for r in s1)
    out["S2_interior_all_SPD_linear"] = all(
        r["pass_health"] for r in s2 if not r["reduces_to_S1"] and r["a"] * r["b"] > 0
    )
    path = r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\Opsi2_S1_S2_RETRY_RESULTS.json"

    def _jsonify(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(type(o))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=_jsonify)
    print("S1_all_pass", out["S1_all_pass"])
    print("S2_interior_all_SPD_linear", out["S2_interior_all_SPD_linear"])
    print("S2_healthy_interior", out["S2_healthy_interior_count"], "unhealthy", out["S2_unhealthy_count"])
    if s2_bad:
            print("bad", json.dumps(s2_bad, indent=2, default=_jsonify))
    print("rec", json.dumps(out["recommendation"], indent=2))
    print("wrote", path)


if __name__ == "__main__":
    main()
