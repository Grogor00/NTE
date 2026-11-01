#!/usr/bin/env python3
"""One O(psi^4) run with the f-metric Hessian. Prereg filed before this file."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "old", HERE / "Opsi2_Opsi4_Substitution_PARALLEL_CursorMain.py"
)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
k0 = old.k0
RNG = np.random.default_rng(20261101)


def draw_background():
    for _ in range(40):
        gamma = k0.random_spd(RNG)
        f3 = k0.random_spd(RNG)
        n = RNG.normal(size=3)
        n = 0.25 * n / max(1.0, float(norm(n)))
        try:
            D = k0.D_of_n(gamma, f3, n)
        except (ValueError, np.linalg.LinAlgError):
            continue
        if abs(np.linalg.det(D)) < 1e-8 or abs(np.linalg.det(f3)) < 1e-10:
            continue
        return gamma, f3, n, D
    return None


def hessian(N, L, f3, D):
    A = L * f3 + N * (f3 @ D)
    if abs(np.linalg.det(A)) < 1e-10:
        return None
    return A


def quartic(G, A):
    try:
        x = np.linalg.solve(A, G)
    except np.linalg.LinAlgError:
        return None
    return -0.5 * float(G @ x)


def defect_from(values):
    if any(v is None for v in values.values()):
        return None
    dN = abs(values[(2.0, 1.0)] - 2 * values[(1.0, 1.0)] + values[(0.0, 1.0)])
    dL = abs(values[(1.0, 2.0)] - 2 * values[(1.0, 1.0)] + values[(1.0, 0.0)])
    return max(dN, dL)


def frozen_g_only(f3, n, D, psi, sg):
    j = old.alpha_current(psi)
    pts = [(1.0, 1.0), (2.0, 1.0), (0.0, 1.0), (1.0, 2.0), (1.0, 0.0)]
    vals = {}
    for N, L in pts:
        A = hessian(N, L, f3, D)
        if A is None:
            return None
        G = sg * (L * np.eye(3) + N * D.T) @ j
        vals[(N, L)] = quartic(G, A)
    return defect_from(vals)


def full_frozen(gamma, f3, n, D, psi, q, sg, sf):
    pts = [(1.0, 1.0), (2.0, 1.0), (0.0, 1.0), (1.0, 2.0), (1.0, 0.0)]
    vals = {}
    for N, L in pts:
        A = hessian(N, L, f3, D)
        if A is None:
            return None

        def fg(p, N=N, L=L):
            hg, hf, _ = old.shift_values(p, N, L, psi, sg, sf, gamma, f3, False, D)
            return hg + hf

        try:
            G = old.grad_of(fg, n) + old.kin_grad(n, N, L, psi, q, sg, sf, False)
        except (ValueError, np.linalg.LinAlgError):
            return None
        vals[(N, L)] = quartic(G, A)
    return defect_from(vals)


def live_g_only(gamma, f3, n, D, psi, sg):
    pts = [(1.0, 1.0), (2.0, 1.0), (0.0, 1.0), (1.0, 2.0), (1.0, 0.0)]
    vals = {}
    for N, L in pts:
        A = hessian(N, L, f3, D)
        if A is None:
            return None

        def fg(p, N=N, L=L):
            hg, _, _ = old.shift_values(p, N, L, psi, sg, 0.0, gamma, f3, False, None)
            return hg

        try:
            G = old.grad_of(fg, n)
        except (ValueError, np.linalg.LinAlgError):
            return None
        vals[(N, L)] = quartic(G, A)
    return defect_from(vals)


def identity(gamma, f3, n, D, psi, q, sg, sf):
    def hf(p):
        return sf * float((1.0 * p) @ old.M_current(p, psi)[0])

    try:
        u_f = old.grad_of(hf, n)
        k_f = old.kin_grad(n, 0.0, 1.0, psi, q, sg, sf, False)
        k_g = old.kin_grad(n, 1.0, 0.0, psi, q, sg, sf, False)
    except (ValueError, np.linalg.LinAlgError):
        return None
    DinvT = f3 @ inv(D) @ inv(f3)
    left = u_f + k_f
    right = DinvT @ k_g
    scale = max(float(norm(left)), float(norm(right)), 1e-15)
    return float(norm(left - right) / scale)


def eq10(f3, D):
    M = f3 @ D
    return float(norm(M - M.T) / max(float(norm(M)), 1e-15))


def median(xs):
    a = [x for x in xs if x is not None]
    if len(a) < 20:
        return None, len(a)
    return float(np.median(a)), len(a)


def main():
    ctrl, full, ident, live, asym = [], [], [], [], []
    for _ in range(40):
        bg = draw_background()
        if bg is None:
            continue
        gamma, f3, n, D = bg
        sg = float(RNG.uniform(0.4, 2.0))
        sf = float(RNG.uniform(0.4, 2.0))
        psi = RNG.normal(size=4) + 1j * RNG.normal(size=4)
        psi = psi / norm(psi)
        q = RNG.normal(size=3)
        q = q / max(float(norm(q)), 1e-8)
        ctrl.append(frozen_g_only(f3, n, D, psi, sg))
        full.append(full_frozen(gamma, f3, n, D, psi, q, sg, sf))
        ident.append(identity(gamma, f3, n, D, psi, q, sg, sf))
        live.append(live_g_only(gamma, f3, n, D, psi, sg))
        asym.append(eq10(f3, D))
    mc, nc = median(ctrl)
    mf, nf = median(full)
    mi, ni = median(ident)
    ml, nl = median(live)
    ma, na = median(asym)
    control = bool(mc is not None and mc < 1e-8)
    if not control or mf is None or mi is None:
        outcome = "no decision"
    elif mf < 1e-8 and mi < 1e-8:
        outcome = "removed"
    elif mf > 1e-3 and mi > 1e-3:
        outcome = "survives"
    elif (mf < 1e-8 and mi > 1e-3) or (mf > 1e-3 and mi < 1e-8):
        outcome = "void"
    else:
        outcome = "no decision"
    out = {
        "n_control": nc,
        "frozen_g_only_median_defect": mc,
        "n_full": nf,
        "full_median_defect": mf,
        "n_identity": ni,
        "identity_median_rel_residual": mi,
        "n_live": nl,
        "live_g_only_median_defect": ml,
        "n_eq10": na,
        "fD_asymmetry_median_rel": ma,
        "controls_pass": control,
        "outcome": outcome,
    }
    (HERE / "Opsi2_Opsi4_fHessian_RESULTS.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8"
    )
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
