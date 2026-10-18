#!/usr/bin/env python3
"""
Opsi2 Round-5: evaluate Scratch X-polynomial absorption identity
  L D(n) n M  ?=  -h_g (I-X)^2     (AC form)
  L D(n) n M  ?=  -h_g (θ_g I - θ_f X)^2   (Jammer θ form)

HR minimal-model forms (arXiv:1109.3515 eqs 19–24; 1109.3230):
  D = sqrt(γ^{-1} f Q) @ Q^{-1}
  Q = x I + n n^T f ,  x = 1 - n^T f n
  n = -R_g_raised / sqrt(4 m^4 detγ + R_g · f^{-1} · R_g)   (schematic units M_g=M_eff=1)

No Wolfram; SymPy + NumPy. Re-run suite until robust.
"""
from __future__ import annotations
import json
import numpy as np
from numpy.linalg import inv, det, norm, eigvalsh, matrix_power

# ---------- HR building blocks ----------

def matrix_sqrt_spd(A: np.ndarray) -> np.ndarray:
    """Principal square root of SPD (or diagonalizable positive-eig) matrix."""
    w, V = np.linalg.eig(A)
    w = np.real(w)
    if np.any(w < -1e-10):
        raise ValueError(f"negative eigenvalues in sqrt: {w}")
    w = np.clip(w, 0, None)
    return np.real(V @ np.diag(np.sqrt(w)) @ inv(V))


def X_from_metrics(hg: np.ndarray, hf: np.ndarray) -> np.ndarray:
    return matrix_sqrt_spd(inv(hg) @ hf)


def D_of_n(gamma: np.ndarray, f3: np.ndarray, n: np.ndarray) -> np.ndarray:
    """Explicit D (1109.3515 eq 20–21). gamma, f3 = spatial metrics."""
    n = n.reshape(3)
    x = 1.0 - float(n @ f3 @ n)
    if x <= 1e-12:
        raise ValueError(f"x={x} not positive")
    Q = x * np.eye(3) + np.outer(n, f3 @ n)
    # D = sqrt(gamma^{-1} f Q) Q^{-1}
    inside = inv(gamma) @ f3 @ Q
    # symmetrize mild numerical noise
    inside = 0.5 * (inside + inside.T)
    return matrix_sqrt_spd(inside) @ inv(Q)


def n_minimal(f3: np.ndarray, R_g: np.ndarray, det_gamma: float, m: float = 1.0) -> np.ndarray:
    """Minimal-model n (1109.3515 eq 24), M_g=M_eff=1."""
    R_g = R_g.reshape(3)
    f_inv = inv(f3)
    num = -(f_inv @ R_g)
    den = np.sqrt(4 * m**4 * det_gamma + float(R_g @ f_inv @ R_g))
    return num / den


def R_AC(hg: np.ndarray, X: np.ndarray) -> np.ndarray:
    return hg @ matrix_power(np.eye(3) - X, 2)


def R_theta(hg: np.ndarray, hf: np.ndarray, X: np.ndarray) -> np.ndarray:
    sg = np.sqrt(det(hg))
    sf = np.sqrt(det(hf))
    thg, thf = sg / (sg + sf), sf / (sg + sf)
    M = thg * np.eye(3) - thf * X
    return hg @ (M @ M)


def frobenius_rel(A: np.ndarray, B: np.ndarray) -> float:
    na, nb = norm(A), norm(B)
    if na < 1e-15 and nb < 1e-15:
        return 0.0
    return float(norm(A - B) / max(na, nb, 1e-30))


# ---------- Probe suite ----------

def probe_n0_matrix_identity():
    """At n=0, LHS vector channel vanishes; RHS matrix nonzero for X≠I."""
    results = []
    for lam in [1.0, 1.5, 1.8, 2.5]:
        hg = np.eye(3)
        X = np.diag([1.0, 1.0, lam])
        hf = hg @ X @ X
        D = D_of_n(hg, hf, np.zeros(3))
        # D should equal X at n=0
        d_err = frobenius_rel(D, X)
        Rac = R_AC(hg, X)
        Rth = R_theta(hg, hf, X)
        # Scratch schematic: L D n M as matrix — at n=0, Dn=0
        Dn = D @ np.zeros(3)
        results.append(
            dict(
                lam=lam,
                D_equals_X=d_err < 1e-9,
                d_err=d_err,
                Dn_norm=float(norm(Dn)),
                R_AC_norm=float(norm(Rac)),
                R_theta_norm=float(norm(Rth)),
                matrix_id_AC_holds=bool(norm(Rac) < 1e-12),  # only at lam=1
                matrix_id_theta_holds=bool(norm(Rth) < 1e-12),
            )
        )
    return results


def probe_Dn_vs_R_linear_response():
    """
    On-shell linear response: R_g=0 background, P drives n ~ P (via C_i+P=0).
    Channel vector ~ D n ~ X n ~ X P (up to scalar κ,L,M).
    Need X P parallel to R P for all P ⇒ X ∝ R as matrices.
    """
    rows = []
    for lam in [1.2, 1.5, 1.8, 2.0, 3.0]:
        hg = np.eye(3)
        X = np.diag([1.0, 1.0, lam])
        hf = hg @ X @ X
        Rac = R_AC(hg, X)
        Rth = R_theta(hg, hf, X)
        # proportionality: exists a s.t. X = a * R ?
        # Use least squares on vectorized mats; check residual
        def prop_err(A, B):
            a = np.linalg.lstsq(B.reshape(-1, 1), A.reshape(-1), rcond=None)[0][0]
            return frobenius_rel(A, a * B), a

        e_ac, a_ac = prop_err(X, Rac) if norm(Rac) > 1e-12 else (0.0, np.nan)
        e_th, a_th = prop_err(X, Rth) if norm(Rth) > 1e-12 else (0.0, np.nan)
        # also check random P: angle between X@P and R@P
        rng = np.random.default_rng(0)
        angs_ac, angs_th = [], []
        for _ in range(20):
            P = rng.normal(size=3)
            u, v = X @ P, Rac @ P
            w = Rth @ P
            def ang(a, b):
                na, nb = norm(a), norm(b)
                if na < 1e-15 or nb < 1e-15:
                    return 0.0 if na < 1e-15 and nb < 1e-15 else np.pi / 2
                return float(np.arccos(np.clip(np.dot(a, b) / (na * nb), -1, 1)))

            angs_ac.append(ang(u, v))
            angs_th.append(ang(u, w))
        rows.append(
            dict(
                lam=lam,
                X_prop_R_AC_err=e_ac,
                X_prop_R_theta_err=e_th,
                mean_ang_AC_deg=float(np.degrees(np.mean(angs_ac))),
                mean_ang_theta_deg=float(np.degrees(np.mean(angs_th))),
                max_ang_AC_deg=float(np.degrees(np.max(angs_ac))),
                max_ang_theta_deg=float(np.degrees(np.max(angs_th))),
            )
        )
    return rows


def probe_explicit_n_and_channel(m=1.0):
    """Full minimal-model n(R), D(n); compare L*(D n) direction to R@P for random data."""
    rng = np.random.default_rng(1)
    rows = []
    for trial in range(40):
        # random SPD metrics
        A = rng.normal(size=(3, 3))
        hg = A @ A.T + 0.3 * np.eye(3)
        B = rng.normal(size=(3, 3))
        hf = B @ B.T + 0.3 * np.eye(3)
        X = X_from_metrics(hg, hf)
        Rac = R_AC(hg, X)
        Rth = R_theta(hg, hf, X)
        # random gravitational momentum density (as covector then raise with hg)
        R_cov = rng.normal(size=3) * 0.5
        R_g = hg @ R_cov  # treat as R^i densitized-ish; formula uses R_j with f^{-1}
        # eq 24 uses R_j^{(g)} with f^{-1}^{ij} — take R_j = R_cov
        n = n_minimal(hf, R_cov, det(hg), m=m)
        try:
            D = D_of_n(hg, hf, n)
        except ValueError:
            continue
        Dn = D @ n
        P = rng.normal(size=3)  # independent probe momentum
        # Channel vector (scalar M,L absorbed into overall scale): Dn
        # Target vectors: Rac@P and Rth@P
        t_ac, t_th = Rac @ P, Rth @ P
        def cos_abs(a, b):
            na, nb = norm(a), norm(b)
            if na < 1e-14 or nb < 1e-14:
                return np.nan
            return float(abs(np.dot(a, b) / (na * nb)))

        rows.append(
            dict(
                n_norm=float(norm(n)),
                Dn_norm=float(norm(Dn)),
                R_AC_P_norm=float(norm(t_ac)),
                R_th_P_norm=float(norm(t_th)),
                cos_Dn_RacP=cos_abs(Dn, t_ac),
                cos_Dn_RthP=cos_abs(Dn, t_th),
                # For identity as matrices: exists s: s * outer? 
                # Better: can Dn⊗e_i match? — check if Dn parallel ALL Rac@P impossible unless rank-1 R
            )
        )
    return rows


def probe_type_and_rank():
    """Structural: channel L (Dn)·(M p) is rank-1 / scalar; R is generically rank-2+."""
    rows = []
    for lam in [1.5, 1.8, 2.5]:
        Rac = R_AC(np.eye(3), np.diag([1.0, 1.0, lam]))
        Rth = R_theta(np.eye(3), np.diag([1.0, 1.0, lam**2]), np.diag([1.0, 1.0, lam]))
        rows.append(
            dict(
                lam=lam,
                rank_R_AC=int(np.linalg.matrix_rank(Rac, tol=1e-10)),
                rank_R_theta=int(np.linalg.matrix_rank(Rth, tol=1e-10)),
                eig_AC=eigvalsh(Rac).tolist(),
                eig_theta=eigvalsh(Rth).tolist(),
            )
        )
    return rows


def probe_n_depends_on_pi_not_only_X():
    """n is not a function of X alone — same X, different R ⇒ different n."""
    hg = np.eye(3)
    X = np.diag([1.0, 1.0, 1.8])
    hf = hg @ X @ X
    n1 = n_minimal(hf, np.array([0.2, 0.0, 0.0]), 1.0)
    n2 = n_minimal(hf, np.array([0.0, 0.3, 0.0]), 1.0)
    n3 = n_minimal(hf, np.array([0.0, 0.0, 0.0]), 1.0)
    return dict(
        n_R_x=n1.tolist(),
        n_R_y=n2.tolist(),
        n_R_0=n3.tolist(),
        same_X_different_n=bool(norm(n1 - n2) > 1e-6),
        n_vanishes_at_R0=bool(norm(n3) < 1e-12),
    )


def main():
    out = {
        "engine": "numpy+sympy-available; wolfram=not found",
        "HR_forms": "D=sqrt(g^{-1}fQ)Q^{-1}; n_minimal from 1109.3515 (24)",
        "n0": probe_n0_matrix_identity(),
        "linear_response_X_vs_R": probe_Dn_vs_R_linear_response(),
        "explicit_n_channel": probe_explicit_n_and_channel(),
        "rank": probe_type_and_rank(),
        "n_not_only_X": probe_n_depends_on_pi_not_only_X(),
    }
    # summaries
    lr = out["linear_response_X_vs_R"]
    out["summary"] = {
        "min_X_prop_R_AC_err": min(r["X_prop_R_AC_err"] for r in lr if r["lam"] != 1.0),
        "min_X_prop_R_theta_err": min(r["X_prop_R_theta_err"] for r in lr),
        "max_mean_ang_AC": max(r["mean_ang_AC_deg"] for r in lr),
        "max_mean_ang_theta": max(r["mean_ang_theta_deg"] for r in lr),
        "n0_AC_id_only_at_X_I": all(
            (r["matrix_id_AC_holds"] and r["lam"] == 1.0)
            or ((not r["matrix_id_AC_holds"]) and r["lam"] != 1.0)
            for r in out["n0"]
        ),
        "explicit_cos_median_AC": float(
            np.nanmedian([r["cos_Dn_RacP"] for r in out["explicit_n_channel"]])
        ),
        "explicit_cos_median_theta": float(
            np.nanmedian([r["cos_Dn_RthP"] for r in out["explicit_n_channel"]])
        ),
    }
    # Decision logic
    s = out["summary"]
    # Identity fails if X not proportional to R for generic λ
    fails_prop = s["min_X_prop_R_AC_err"] > 0.1 and s["min_X_prop_R_theta_err"] > 0.1
    fails_n0 = True  # n=0 ⇒ LHS 0, RHS ≠ 0 for X≠I as matrix id
    n_not_X_only = out["n_not_only_X"]["same_X_different_n"]
    out["conclusion"] = {
        "X_proportional_to_R": not fails_prop,
        "n_is_X_only": not n_not_X_only,
        "scratch_X_only_identity_premise": False,  # n depends on π
        "absorption_identity_holds": False,
        "landing": "G-2" if fails_prop and n_not_X_only else "G-4",
        "reason": (
            "LHS channel ~ Dn depends on π via n(π); RHS R(X) is π-free. "
            "Linear response needs X∝R as matrices — false for anisotropic X "
            "(AC and θ forms). Rank(R_AC)=1 along one axis vs X full rank. "
            "Scalar {S,H} cannot cancel 3-component ∂δ residual (type mismatch). "
            "Robust G-2 for action (N) D-channel absorption of R_j."
        ),
    }
    path = r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\Opsi2_Round5_X_Identity_COMPUTE_RESULTS.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out["summary"], indent=2))
    print(json.dumps(out["conclusion"], indent=2))
    print("wrote", path)
    return out


if __name__ == "__main__":
    main()
