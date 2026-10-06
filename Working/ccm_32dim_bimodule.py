#!/usr/bin/env python3
"""CCM two-sided relation on 32 real dims — Cursor Main, 2026-10-03.

Pre-register: Working/CCM_32dim_Bimodule_FORKS_PRE_REGISTER_Cursor_Main_Discipline12c_20261003.md
Upstream: Jammer CCM_Octonion_VERDICT 20261003.

Correct Fano left-multiplication (e_i e_{i+1}=e_{i+3} mod 7, indices 1..7).
Builds C- ~= M4(C) and C+ ~= M2(H), tests commuting placements.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).with_name("ccm_32dim_bimodule_REPORT_20261003.json")
TOL = 1e-8


def _build_fano_table() -> dict[tuple[int, int], tuple[int, int]]:
    """Fano table from Jammer convention e_i e_{i+1}=e_{i+3} (1..7 cyclic), closed."""
    mul: dict[tuple[int, int], tuple[int, int]] = {(0, 0): (1, 0)}
    for i in range(1, 8):
        mul[(0, i)] = (1, i)
        mul[(i, 0)] = (1, i)
        mul[(i, i)] = (-1, 0)

    def idx(k: int) -> int:
        return ((k - 1) % 7) + 1

    for i in range(1, 8):
        a, b, c = i, idx(i + 1), idx(i + 3)
        mul[(a, b)] = (1, c)
        mul[(b, a)] = (-1, c)

    changed = True
    while changed:
        changed = False
        for (a, b), (s, c) in list(mul.items()):
            if a == 0 or b == 0 or c == 0:
                continue
            for pair, val in (
                ((b, c), (s, a)),
                ((c, a), (s, b)),
                ((b, a), (-s, c)),
                ((c, b), (-s, a)),
                ((a, c), (-s, b)),
            ):
                if pair not in mul:
                    mul[pair] = val
                    changed = True
                elif mul[pair] != val:
                    raise RuntimeError(f"Fano conflict at {pair}")
    return mul


_FANO = _build_fano_table()


def fano_mul(i: int, j: int) -> tuple[int, int]:
    return _FANO[(i, j)]


def left_mult(i: int) -> np.ndarray:
    M = np.zeros((8, 8))
    for j in range(8):
        s, k = fano_mul(i, j)
        M[k, j] = s
    return M


def right_mult(i: int) -> np.ndarray:
    M = np.zeros((8, 8))
    for j in range(8):
        s, k = fano_mul(j, i)
        M[k, j] = s
    return M


def gen_algebra(gens: list[np.ndarray], max_dim: int = 80) -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    flat: list[np.ndarray] = []

    def add(M: np.ndarray) -> bool:
        v = M.reshape(-1)
        if flat:
            A = np.column_stack(flat)
            coef, *_ = np.linalg.lstsq(A, v, rcond=None)
            if np.linalg.norm(v - A @ coef) < TOL:
                return False
        basis.append(M.copy())
        flat.append(v)
        return True

    add(np.eye(gens[0].shape[0]))
    for g in gens:
        add(g)
    changed = True
    while changed and len(basis) < max_dim:
        changed = False
        current = list(basis)
        for a, b in itertools.product(current, repeat=2):
            if add(a @ b):
                changed = True
                if len(basis) >= max_dim:
                    break
    return basis


def algebra_dim(gens: list[np.ndarray]) -> int:
    return len(gen_algebra(gens))


def all_commute(As: list[np.ndarray], Bs: list[np.ndarray]) -> bool:
    for a in As:
        for b in Bs:
            if np.linalg.norm(a @ b - b @ a) > TOL:
                return False
    return True


def commutant_dim(As: list[np.ndarray]) -> int:
    n = As[0].shape[0]
    rows = []
    for A in As:
        K = np.kron(np.eye(n), A) - np.kron(A.T, np.eye(n))
        rows.append(K)
    M = np.vstack(rows)
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-6))


def block_diag(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    n, m = A.shape[0], B.shape[0]
    out = np.zeros((n + m, n + m))
    out[:n, :n] = A
    out[n:, n:] = B
    return out


def complexify_real_op(A: np.ndarray) -> np.ndarray:
    """A on R^n → A⊕A on C⊗R^n ≅ R^{2n}."""
    return block_diag(A, A)


def joint_faithful(As: list[np.ndarray], Bs: list[np.ndarray]) -> bool:
    mats = As + Bs
    big = np.vstack(mats)
    s = np.linalg.svd(big, compute_uv=False)
    return bool(np.min(s) > 1e-6)


def to_complex4(A: np.ndarray, wmat: np.ndarray) -> np.ndarray:
    assert np.allclose(A @ wmat, wmat @ A, atol=TOL), "not complex-linear"
    cols = []
    used: list[np.ndarray] = []
    for k in range(8):
        ek = np.eye(8)[:, k]
        if used:
            span = np.column_stack(used)
            if np.linalg.norm(ek - span @ np.linalg.lstsq(span, ek, rcond=None)[0]) < TOL:
                continue
        used.extend([ek, wmat @ ek])
        cols.append(ek)
        if len(cols) == 4:
            break
    U = np.column_stack([x for c in cols for x in (c, wmat @ c)])
    A_u = np.linalg.inv(U) @ A @ U
    C = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for j in range(4):
            a = A_u[2 * i, 2 * j]
            b = A_u[2 * i + 1, 2 * j]
            C[i, j] = a + 1j * b
    return C


def from_complex16(C: np.ndarray) -> np.ndarray:
    n = C.shape[0]
    R = np.zeros((2 * n, 2 * n))
    for i in range(n):
        for j in range(n):
            a, b = C[i, j].real, C[i, j].imag
            R[2 * i, 2 * j] = a
            R[2 * i, 2 * j + 1] = -b
            R[2 * i + 1, 2 * j] = b
            R[2 * i + 1, 2 * j + 1] = a
    return R


def main() -> None:
    Ls = {i: left_mult(i) for i in range(8)}
    for i in range(1, 8):
        assert np.allclose(Ls[i] @ Ls[i], -np.eye(8)), f"L{i}^2"
        for j in range(i + 1, 8):
            assert np.allclose(Ls[i] @ Ls[j] + Ls[j] @ Ls[i], 0), (i, j)

    five = (1, 2, 3, 4, 5)
    comp = tuple(sorted(set(range(1, 8)) - set(five)))
    gens_m4 = [Ls[a] for a in five]
    w = np.eye(8)
    for a in five:
        w = w @ Ls[a]
    assert np.allclose(w @ w, -np.eye(8))
    gens_m2 = [w @ Ls[a] for a in five]

    dim_m4 = algebra_dim(gens_m4)
    dim_m2 = algebra_dim(gens_m2)
    same_space_commute = all_commute(gens_m2, gens_m4)
    central_ok = all(np.allclose(w @ Ls[a], Ls[a] @ w) for a in five)
    w_comp = Ls[comp[0]] @ Ls[comp[1]]
    w_eq_comp = np.allclose(w, w_comp) or np.allclose(w, -w_comp)

    # all 21 five-subsets: dim check (sample all)
    dims21 = []
    for subset in itertools.combinations(range(1, 8), 5):
        d = algebra_dim([Ls[a] for a in subset])
        dims21.append(d)
    report = {
        "five": five,
        "complementary_plane": comp,
        "dim_alg_m4_on_O": dim_m4,
        "dim_alg_m2_on_O": dim_m2,
        "all_21_five_subset_dims": dims21,
        "all_21_are_32": all(d == 32 for d in dims21),
        "same_8space_m2_m4_commute": bool(same_space_commute),
        "omega_central_in_five": bool(central_ok),
        "omega_eq_pm_Lcomp": bool(w_eq_comp),
        "commutant_dim_m4_gens": commutant_dim(gens_m4),
        "commutant_dim_m2_gens": commutant_dim(gens_m2),
    }

    basis_m4 = gen_algebra(gens_m4)
    basis_m2 = gen_algebra(gens_m2)
    cl_basis_m4 = [b for b in basis_m4 if np.allclose(b @ w, w @ b)]
    cl_basis_m2 = [b for b in basis_m2 if np.allclose(b @ w, w @ b)]
    report["n_complex_linear_m4_basis"] = len(cl_basis_m4)
    report["n_complex_linear_m2_basis"] = len(cl_basis_m2)

    # Tensor construction V_ω ⊗_C V_ω
    if len(cl_basis_m4) >= 4 and len(cl_basis_m2) >= 4:
        C_m4 = [to_complex4(b, w) for b in cl_basis_m4]
        C_m2 = [to_complex4(b, w) for b in cl_basis_m2]
        I4 = np.eye(4, dtype=complex)
        pi_m4 = [from_complex16(np.kron(c, I4)) for c in C_m4]
        pi_m2 = [from_complex16(np.kron(I4, c)) for c in C_m2]
        report["tensor_Vω_Vω_commute"] = bool(all_commute(pi_m2, pi_m4))
        report["tensor_real_dim"] = int(pi_m4[0].shape[0])
        report["tensor_joint_faithful"] = bool(joint_faithful(pi_m4, pi_m2))
        report["tensor_m4_complex_alg_dim"] = len(C_m4)
        report["tensor_m2_complex_alg_dim"] = len(C_m2)
    else:
        report["tensor_Vω_Vω_commute"] = False
        report["tensor_joint_faithful"] = False
        report["tensor_note"] = f"cl bases too small: m4={len(cl_basis_m4)} m2={len(cl_basis_m2)}"

    # Also try Kronecker using generator images only (if full basis filter fails)
    if not report.get("tensor_Vω_Vω_commute"):
        # Force complex-linear combinations: (A - w A w)/2 style? For Cl, use
        # average projector P(A) = (A - w A w)/2 if w^2=-I... actually
        # complex-linear iff A w = w A.
        # Build M4(C) as End_C(V): all 8x8 real matrices commuting with w.
        # Dimension should be 32 (real). Then intersect with alg(gens).
        pass

    # Summand-graded C⊗(O⊕O)
    def embed_summand(A8: np.ndarray, which: int) -> np.ndarray:
        Z = np.zeros((8, 8))
        return block_diag(A8, Z) if which == 0 else block_diag(Z, A8)

    m4_s0_c = [complexify_real_op(embed_summand(g, 0)) for g in gens_m4]
    m2_s1_c = [complexify_real_op(embed_summand(g, 1)) for g in gens_m2]
    report["summand_split_commute"] = bool(all_commute(m2_s1_c, m4_s0_c))
    report["summand_split_joint_faithful"] = bool(joint_faithful(m4_s0_c, m2_s1_c))
    report["summand_split_m4_alg_dim"] = algebra_dim(m4_s0_c)
    report["summand_split_m2_alg_dim"] = algebra_dim(m2_s1_c)

    m4_diag_c = [complexify_real_op(block_diag(g, g)) for g in gens_m4]
    m2_diag_c = [complexify_real_op(block_diag(g, g)) for g in gens_m2]
    report["diagonal_commute"] = bool(all_commute(m2_diag_c, m4_diag_c))

    J16 = np.block([[np.zeros((8, 8)), np.eye(8)], [np.eye(8), np.zeros((8, 8))]])
    J32 = complexify_real_op(J16)
    m2_s0_c = [complexify_real_op(embed_summand(g, 0)) for g in gens_m2]
    m2_J = [J32 @ m @ J32 for m in m2_s0_c]
    report["m4_s0_vs_Jm2J_commute"] = bool(all_commute(m2_J, m4_s0_c))
    report["m4_s0_vs_Jm2J_faithful"] = bool(joint_faithful(m4_s0_c, m2_J))

    lr_fail = sum(
        1
        for a, b in itertools.product(range(1, 8), repeat=2)
        if not np.allclose(Ls[a] @ right_mult(b), right_mult(b) @ Ls[a])
    )
    report["left_right_noncommuting_pairs"] = lr_fail

    # Abstract sanity: M4(C) and M2(H) as End factors on C^4 ⊗ C^4
    # Use full End_C(V_ω) ≅ M4(C) by taking all matrices commuting with w
    # Build orthonormal real basis of commutant of {w}
    n = 8
    Kw = np.kron(np.eye(n), w) - np.kron(w.T, np.eye(n))
    _, _, vh = np.linalg.svd(Kw)
    null = vh[np.sum(np.linalg.svd(Kw, compute_uv=False) >= 1e-6) :].T  # wrong
    # simpler nullity extraction:
    u, s, vh = np.linalg.svd(Kw)
    null_vecs = vh[s < 1e-6].T
    report["end_c_dim_real"] = int(null_vecs.shape[1])  # should be 32

    # Landing
    tensor_ok = bool(report.get("tensor_Vω_Vω_commute")) and bool(
        report.get("tensor_joint_faithful")
    )
    # Native W would need faithful commuting pair on summand-graded space
    native_ok = bool(report["summand_split_commute"]) and bool(
        report["summand_split_joint_faithful"]
    )
    j_ok = bool(report["m4_s0_vs_Jm2J_commute"]) and bool(report["m4_s0_vs_Jm2J_faithful"])

    if native_ok or j_ok:
        landing = "W"
        report["w_route"] = "summand_split" if native_ok else "J_swap"
    elif tensor_ok:
        landing = "Wc"
        report["wc_additions"] = [
            "Identify 32-dim Hilbert space with V_ω ⊗_C V_ω (tensor of one complexified O), not summand-graded C⊗(O⊕O).",
            "Place C- on first tensor factor and C+ on second (Kronecker).",
            "Requires 2-plane complex structure ω (SU(3)→U(2) cost from Jammer §2).",
            "Deposited finite algebra O⊕O as two summands is not the bimodule carrier; the carrier is a tensor square of one O.",
        ]
    elif report.get("tensor_note") and dim_m4 == 32 and dim_m2 == 16:
        landing = "U"
    else:
        # If tensor failed only due to complex-linear filter but abstract End dims work,
        # try generator Kronecker after projecting
        landing = "F"

    # Retry tensor via projected generators if needed
    if landing in ("F", "U") and not tensor_ok:
        def proj_cl(A: np.ndarray) -> np.ndarray:
            # Not a projection to commutant; use: if close, keep
            return A

        # Build C+ / C- as complex algebras using omega as i on V
        # Generators L_a for a in five: generally anticommute with? check L_a w + w L_a
        anticomm_w = {
            a: float(np.linalg.norm(Ls[a] @ w + w @ Ls[a])) for a in five
        }
        report["norm_La_anticomm_w"] = anticomm_w
        # For Clifford algebra Cl(0,5), the volume element w is central.
        # If central_ok, L_a commute with w — then all gens are complex-linear.
        if central_ok:
            C_m4 = [to_complex4(g, w) for g in gens_m4]
            C_m2 = [to_complex4(g, w) for g in gens_m2]
            # also full algebra bases
            C_m4b = [to_complex4(b, w) for b in basis_m4 if np.allclose(b @ w, w @ b)]
            C_m2b = [to_complex4(b, w) for b in basis_m2 if np.allclose(b @ w, w @ b)]
            I4 = np.eye(4, dtype=complex)
            pi_m4 = [from_complex16(np.kron(c, I4)) for c in (C_m4b or C_m4)]
            pi_m2 = [from_complex16(np.kron(I4, c)) for c in (C_m2b or C_m2)]
            report["tensor_retry_commute"] = bool(all_commute(pi_m2, pi_m4))
            report["tensor_retry_faithful"] = bool(joint_faithful(pi_m4, pi_m2))
            if report["tensor_retry_commute"] and report["tensor_retry_faithful"]:
                landing = "Wc"
                report["wc_additions"] = [
                    "Identify 32-dim space with V_ω ⊗_C V_ω.",
                    "C- on first factor, C+ on second.",
                    "2-plane ω required; SU(3)→U(2) cost.",
                    "Not the summand-graded deposited O⊕O carrier.",
                ]

    report["landing_fork"] = landing
    report["tol"] = TOL
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"\nLANDING: {landing}")


if __name__ == "__main__":
    main()
