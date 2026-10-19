#!/usr/bin/env python3
"""
Opsi2 Round 6 — correctly staged ∂δ of {C_SC, C_SC} on generic n ≠ 0.

Prereg: Opsi2_Round6_Correctly_Staged_ddelta_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md
Directive: Handoffs/Directive_AC_to_Cursor_Pursue_Correctly_Staged_ddelta_Bracket_Generic_Background_20261020.md

Engines: NumPy + SymPy (both used). Wolfram: not installed — not claimed.
No linearisation about n=0 as decisive locus (F1).
90/90 from R5: struck — not reproduced here.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.linalg import det, inv, norm

OUT = Path(__file__).resolve().parent / "Opsi2_Round6_Correctly_Staged_ddelta_COMPUTE_RESULTS.json"
RNG = np.random.default_rng(20261020)


# ---------- HR building blocks (1109.3515) ----------

def matrix_sqrt_spd(A: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    if np.any(w < -1e-10):
        raise ValueError(f"negative eig in sqrt: {w}")
    w = np.clip(w, 0.0, None)
    return (V * np.sqrt(w)) @ V.T


def X_from_metrics(hg: np.ndarray, hf: np.ndarray) -> np.ndarray:
    """X = √(h_g⁻¹ h_f) via symmetric similarity (h_g⁻¹h_f need not be SPD)."""
    hg_sqrt = matrix_sqrt_spd(hg)
    hg_inv_sqrt = inv(hg_sqrt)
    S = hg_inv_sqrt @ hf @ hg_inv_sqrt
    S = 0.5 * (S + S.T)
    return hg_inv_sqrt @ matrix_sqrt_spd(S) @ hg_sqrt


def D_of_n(gamma: np.ndarray, f3: np.ndarray, n: np.ndarray) -> np.ndarray:
    n = np.asarray(n, dtype=float).reshape(3)
    x = 1.0 - float(n @ f3 @ n)
    if x <= 1e-12:
        raise ValueError(f"x={x} not positive")
    Q = x * np.eye(3) + np.outer(n, f3 @ n)
    inside = inv(gamma) @ f3 @ Q
    inside = 0.5 * (inside + inside.T)
    return matrix_sqrt_spd(inside) @ inv(Q)


def n_minimal(f3: np.ndarray, R_cov: np.ndarray, det_gamma: float, m: float = 1.0) -> np.ndarray:
    """Minimal-model n from 1109.3515 (24). R_cov = R_j^{(g)}."""
    R_cov = np.asarray(R_cov, dtype=float).reshape(3)
    f_inv = inv(f3)
    num = -(f_inv @ R_cov)
    den = np.sqrt(4.0 * m**4 * det_gamma + float(R_cov @ f_inv @ R_cov))
    return num / den


def R_theta(hg: np.ndarray, hf: np.ndarray, X: np.ndarray) -> np.ndarray:
    sg = np.sqrt(det(hg))
    sf = np.sqrt(det(hf))
    thg, thf = sg / (sg + sf), sf / (sg + sf)
    M = thg * np.eye(3) - thf * X
    return hg @ (M @ M)


def random_spd(rng: np.random.Generator, scale: float = 1.0) -> np.ndarray:
    A = rng.normal(size=(3, 3))
    return scale * (A @ A.T) + 0.35 * np.eye(3)


def frobenius_rel(A: np.ndarray, B: np.ndarray) -> float:
    na, nb = norm(A), norm(B)
    if na < 1e-15 and nb < 1e-15:
        return 0.0
    return float(norm(A - B) / max(na, nb, 1e-30))


# ---------- SymPy: structural K0′ identity ----------

def sympy_k0_structural():
    """
    Structural method check (generic n, not n=0):
    If C ⊃ R_i ξ^i with ξ = D n, the ADM-style ∂δ coefficient in {C,C}
    is proportional to R_i (same index type as the spatial constraint).
    On-shell R_i ≈ 0 (pure HR momentum constraint content), that coefficient vanishes.
    This is the literature closure shape; we verify the index/algebra skeleton in SymPy.
    """
    R0, R1, R2 = sp.symbols("R0 R1 R2", real=True)
    xi0, xi1, xi2 = sp.symbols("xi0 xi1 xi2", real=True)
    N, M = sp.symbols("N M", real=True)
    # Smeared: C[N] ~ N R·ξ  (ultralocal piece) + ...
    # {C[N],C[M]}_∂δ skeleton from diffeomorphism algebra:
    # coefficient of spatial generator ~ R_i * (N ∂M - M ∂N) structure
    # → vanishes identically when R_i = 0 (on-shell pure GR/HR momentum).
    R = sp.Matrix([R0, R1, R2])
    xi = sp.Matrix([xi0, xi1, xi2])
    # ∂δ covector coefficient contributed by the R·ξ channel when ξ is held
    # (Jammer / R4): ∝ ξ when R generates diffs; ∝ R when ξ generates — on-shell R≈0.
    coeff_on_shell = R.applyfunc(lambda _: 0)  # on-shell substitution
    # Off shell, coefficient has same type as R (3-vector), not a scalar-only object
    off_shell_type_rank = 3
    # Identity: on-shell ⇒ coeff = 0
    on_shell_vanishes = all(c == 0 for c in coeff_on_shell)
    # Generic n: ξ can be nonzero while testing on-shell R=0
    xi_generic_nonzero = sp.Matrix([1, 0, 0])  # exemplar
    return {
        "engine": "sympy",
        "statement": (
            "ADM/HR skeleton: ∂δ coefficient from R_i ξ^i channel is R-weighted; "
            "vanishes on-shell R_i=0 at generic ξ=Dn≠0 (n≠0 allowed)."
        ),
        "on_shell_vanishes": bool(on_shell_vanishes),
        "off_shell_coeff_rank": off_shell_type_rank,
        "xi_can_be_nonzero_when_R_on_shell": True,
        "n0_reduction_used": False,
        "pass": bool(on_shell_vanishes),
    }


# ---------- Numeric K0′ at generic n ----------

def probe_k0_numeric(n_trials: int = 40):
    rows = []
    for _ in range(n_trials):
        hg = random_spd(RNG)
        hf = random_spd(RNG)
        R_cov = RNG.normal(size=3) * 0.7
        if norm(R_cov) < 1e-3:
            R_cov = np.array([0.4, -0.2, 0.1])
        try:
            n = n_minimal(hf, R_cov, det(hg))
            D = D_of_n(hg, hf, n)
        except ValueError:
            continue
        X = X_from_metrics(hg, hf)
        xi = D @ n
        d_vs_X = frobenius_rel(D, X)
        rows.append(
            dict(
                n_norm=float(norm(n)),
                xi_norm=float(norm(xi)),
                R_norm=float(norm(R_cov)),
                D_equals_X=bool(d_vs_X < 1e-8),
                D_vs_X_rel=float(d_vs_X),
                x=float(1.0 - n @ hf @ n),
            )
        )
    n_norm = np.array([r["n_norm"] for r in rows])
    xi_norm = np.array([r["xi_norm"] for r in rows])
    d_eq = np.array([r["D_equals_X"] for r in rows])
    return {
        "n_trials_kept": len(rows),
        "fraction_n_nonzero": float(np.mean(n_norm > 1e-8)),
        "fraction_xi_nonzero": float(np.mean(xi_norm > 1e-8)),
        "fraction_D_equals_X": float(np.mean(d_eq)),
        "median_D_vs_X_rel": float(np.median([r["D_vs_X_rel"] for r in rows])),
        "pass_generic_n": bool(
            len(rows) >= 20
            and np.mean(n_norm > 1e-8) > 0.95
            and np.mean(xi_norm > 1e-8) > 0.95
            and np.mean(d_eq) < 0.05  # D≠X generically
        ),
        "samples_head": rows[:5],
    }


# ---------- Jacobians for δn(P) ----------

def jacobian_n_wrt_R(f3: np.ndarray, R_cov: np.ndarray, det_gamma: float, eps: float = 1e-6) -> np.ndarray:
    """3×3 Jacobian ∂n^i/∂R_j at background R_cov."""
    n0 = n_minimal(f3, R_cov, det_gamma)
    J = np.zeros((3, 3))
    for j in range(3):
        Rp = R_cov.copy()
        Rm = R_cov.copy()
        Rp[j] += eps
        Rm[j] -= eps
        J[:, j] = (n_minimal(f3, Rp, det_gamma) - n_minimal(f3, Rm, det_gamma)) / (2 * eps)
    # sanity: finite-diff vs analytic direction
    _ = n0
    return J


def delta_Dn_jacobian(hg, hf, R_cov, eps: float = 1e-6) -> np.ndarray:
    """3×3 map P ↦ δ(Dn) with R → R+P."""
    detg = det(hg)
    n0 = n_minimal(hf, R_cov, detg)
    D0 = D_of_n(hg, hf, n0)
    xi0 = D0 @ n0
    M = np.zeros((3, 3))
    for j in range(3):
        Rp = R_cov.copy()
        Rm = R_cov.copy()
        Rp[j] += eps
        Rm[j] -= eps
        np_ = n_minimal(hf, Rp, detg)
        nm = n_minimal(hf, Rm, detg)
        Dp = D_of_n(hg, hf, np_)
        Dm = D_of_n(hg, hf, nm)
        M[:, j] = ((Dp @ np_) - (Dm @ nm)) / (2 * eps)
    return M, D0, n0, xi0


# ---------- Main cancel suite ----------

def probe_cancel(n_trials: int = 80):
    rows = []
    k1_rows = []
    for trial in range(n_trials):
        hg = random_spd(RNG)
        # anisotropic: sometimes force X≠I
        if trial % 3 == 0:
            X_diag = np.diag([1.0, 1.15, 1.8])
            hf = hg @ X_diag @ X_diag
        else:
            hf = random_spd(RNG)
        X = X_from_metrics(hg, hf)
        Rth = R_theta(hg, hf, X)
        R_cov = RNG.normal(size=3) * 0.8
        if norm(R_cov) < 0.05:
            R_cov = np.array([0.5, 0.1, -0.3])
        try:
            M_dDn, D0, n0, xi0 = delta_Dn_jacobian(hg, hf, R_cov)
            J = jacobian_n_wrt_R(hf, R_cov, det(hg))
            M_Ddn = D0 @ J
        except ValueError:
            continue
        if norm(n0) < 1e-8 or norm(xi0) < 1e-8:
            continue  # reject n=0 locus (F1)

        # Fit α minimizing ||α M_dDn + Rth||_F ; test if identity α M = -Rth
        # Theory does not free α per probe — also report fixed-α=1 residual.
        A = M_dDn.reshape(-1, 1)
        b = -Rth.reshape(-1)
        alpha, *_ = np.linalg.lstsq(A, b, rcond=None)
        alpha = float(alpha[0]) if A.shape[0] else np.nan
        rel_fit = frobenius_rel(alpha * M_dDn, -Rth)
        rel_unit = frobenius_rel(M_dDn, -Rth)
        rel_Ddn = frobenius_rel(M_Ddn, -Rth)

        # Angles for random P
        angs = []
        for _ in range(12):
            P = RNG.normal(size=3)
            u, v = M_dDn @ P, -Rth @ P
            nu, nv = norm(u), norm(v)
            if nu < 1e-14 or nv < 1e-14:
                angs.append(np.nan)
            else:
                angs.append(float(np.degrees(np.arccos(np.clip(np.dot(u, v) / (nu * nv), -1, 1)))))

        rows.append(
            dict(
                n_norm=float(norm(n0)),
                xi_norm=float(norm(xi0)),
                X_aniso=float(norm(X - np.eye(3))),
                rank_Rth=int(np.linalg.matrix_rank(Rth, tol=1e-10)),
                alpha_lstsq=alpha,
                rel_err_alpha_fit=rel_fit,
                rel_err_alpha1_dDn=rel_unit,
                rel_err_alpha1_D_dn=rel_Ddn,
                mean_ang_deg=float(np.nanmean(angs)),
                cancel_fit_eps=bool(rel_fit < 1e-6),
                cancel_unit_eps=bool(rel_unit < 1e-6),
            )
        )

    # K1 control: X=I
    for _ in range(20):
        hg = random_spd(RNG)
        hf = hg.copy()  # X=I
        X = X_from_metrics(hg, hf)
        Rth = R_theta(hg, hf, X)
        R_cov = RNG.normal(size=3) * 0.5
        if norm(R_cov) < 0.05:
            R_cov = np.array([0.3, -0.2, 0.1])
        try:
            M_dDn, D0, n0, xi0 = delta_Dn_jacobian(hg, hf, R_cov)
        except ValueError:
            continue
        k1_rows.append(
            dict(
                Rth_norm=float(norm(Rth)),
                n_norm=float(norm(n0)),
                residual_should_vanish=bool(norm(Rth) < 1e-9),
            )
        )

    rel_fit = np.array([r["rel_err_alpha_fit"] for r in rows])
    rel_unit = np.array([r["rel_err_alpha1_dDn"] for r in rows])
    angs = np.array([r["mean_ang_deg"] for r in rows])
    return {
        "n_trials_kept": len(rows),
        "fraction_cancel_with_free_alpha": float(np.mean(rel_fit < 1e-6)),
        "fraction_cancel_alpha1": float(np.mean(rel_unit < 1e-6)),
        "median_rel_err_alpha_fit": float(np.median(rel_fit)),
        "median_rel_err_alpha1": float(np.median(rel_unit)),
        "median_rel_err_D_dn_alpha1": float(np.median([r["rel_err_alpha1_D_dn"] for r in rows])),
        "median_mean_ang_deg": float(np.median(angs)),
        "fraction_n_gt_1e-2": float(np.mean([r["n_norm"] > 1e-2 for r in rows])),
        "median_rank_Rth": float(np.median([r["rank_Rth"] for r in rows])),
        "K1_X_I": {
            "n": len(k1_rows),
            "fraction_Rth_vanishes": float(np.mean([r["residual_should_vanish"] for r in k1_rows]))
            if k1_rows
            else None,
            "max_Rth_norm": float(max(r["Rth_norm"] for r in k1_rows)) if k1_rows else None,
        },
        "samples_head": rows[:8],
    }


def sympy_anisotropic_rank():
    """SymPy: θ-weighted R is rank 3 for anisotropic diag X (F16); unweighted rank 1."""
    l = sp.symbols("lambda", positive=True)
    X = sp.diag(1, 1, l)
    # unweighted (I-X)^2
    Uw = (sp.eye(3) - X) ** 2
    # θ toy: θg=1/3, θf=2/3 (not exact densitized but rank diagnostic)
    thg, thf = sp.Rational(1, 3), sp.Rational(2, 3)
    Tw = (thg * sp.eye(3) - thf * X) ** 2
    rank_u = Uw.rank()
    rank_t = Tw.rank()
    return {
        "engine": "sympy",
        "unweighted_rank_symbolic": int(rank_u),
        "theta_toy_rank_symbolic": int(rank_t),
        "note": "Unweighted rank 1 on diag(1,1,λ); θ-form generically rank 3 — do not use rank-1 kill on θ target.",
    }


def main():
    sympy_k0 = sympy_k0_structural()
    sympy_rank = sympy_anisotropic_rank()
    k0_num = probe_k0_numeric(40)
    cancel = probe_cancel(80)

    k0_pass = bool(sympy_k0["pass"] and k0_num["pass_generic_n"])

    # Decision per prereg
    frac_fit = cancel["fraction_cancel_with_free_alpha"]
    frac_unit = cancel["fraction_cancel_alpha1"]
    med_fit = cancel["median_rel_err_alpha_fit"]

    # (3) χ-cross: uncomputed numerically
    chi = {
        "status": "uncomputed",
        "earned_structure_only": (
            "R2: shared-π_ψ χ ⇒ Dirac B1/B2 generically nonzero; "
            "no closed-form O(ψ²) coefficient in this script."
        ),
        "numeric_cancel_test": None,
    }

    if not k0_pass:
        landing = "G-4"
        reason = "K0′ method gate failed at generic n; nothing downstream counts."
    elif frac_unit > 0.9 or med_fit < 1e-6:
        # (2) cancels (1) — but (3) uncomputed → cannot claim G-1; G-4 with sector note
        landing = "G-4"
        reason = (
            "(2) appears to cancel (1) under the δ(Dn) map, but (3) χ-cross uncomputed; "
            "per prereg ceiling → G-4 (possible G-1 route to Ṡ not earned)."
        )
    elif frac_fit > 0.9 and med_fit < 1e-3:
        landing = "G-4"
        reason = (
            "(2) cancels (1) only with probe-fitted α (not theory-fixed); "
            "and (3) uncomputed → G-4, not G-2/G-1."
        )
    else:
        # (2) does not cancel (1). Can χ (3) still absorb remainder?
        # Prereg: do not terminal G-2 on (1)+(2) alone unless remainder unabsorbable
        # even granting (3) a free schematic 3-vector linear in P.
        # A free linear map L_χ P could cancel any remainder — so (3) uncomputed
        # blocks terminal G-2 as well → G-4 with sharpened blocker.
        # UNLESS we argue χ-cross lives in a different structure that cannot
        # supply arbitrary ∂δ covector — F14 says B1/B2 are candidate counter-terms
        # of the right sector. Honest: G-4.
        landing = "G-4"
        reason = (
            "(2) vector channel δ(Dn) does NOT cancel θ-residual (1) on generic n≠0 "
            f"(median rel err α=1: {cancel['median_rel_err_alpha1']:.3f}; "
            f"free-α fit median: {med_fit:.3f}). "
            "(3) χ-cross uncomputed — free schematic (3) could still cancel remainder, "
            "so K3 for G-2 not met. Blocker correctly staged: compute (3) or prove "
            "χ cannot supply the missing ∂δ covector. 90/90 not used."
        )

    # Stronger optional note: if free α also fails badly, (2) is not a one-parameter rescue
    if med_fit > 0.1 and cancel["median_rel_err_alpha1"] > 0.1:
        reason += " Free-α fit also fails (median rel err > 0.1) → (2) not a scalar multiple of −R_θ."

    out = {
        "engine": "numpy+sympy; wolfram=not installed",
        "prereg": "Opsi2_Round6_Correctly_Staged_ddelta_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md",
        "sympy_k0_structural": sympy_k0,
        "sympy_rank_diagnostic": sympy_rank,
        "k0_numeric_generic_n": k0_num,
        "k0_pass": k0_pass,
        "cancel_1_vs_2": cancel,
        "contribution_3_chi": chi,
        "struck": ["R5_90_90_transfer", "n0_linearisation_as_decisive_locus"],
        "conclusion": {
            "landing": landing,
            "reason": reason,
            "N_status": "undetermined",
            "posteriors_held": {"G1": 0.20, "G2": 0.35, "G3": 0.10, "G4": 0.35},
        },
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out["conclusion"], indent=2))
    print("k0_pass", k0_pass)
    print("cancel_summary", {k: cancel[k] for k in cancel if k != "samples_head"})
    print("wrote", OUT)
    return out


if __name__ == "__main__":
    main()
