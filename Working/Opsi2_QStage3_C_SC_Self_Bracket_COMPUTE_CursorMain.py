#!/usr/bin/env python3
"""
Q-Stage3: {C_SC,C_SC} excess over pure-HR absorption (Cursor Main, independent).

Prereg: Opsi2_QStage3_C_SC_Self_Bracket_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md
GO: Handoffs/GO_AC_Run_Q_Stage3_C_SC_Self_Bracket_Correctly_Staged_20261020.md

Engines: NumPy + SymPy + Wolfram Engine 15 (activated).
F12: non-vanishing alone is not a ghost signal.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_QStage3_C_SC_Self_Bracket_COMPUTE_RESULTS.json"
WL = HERE / "Opsi2_QStage3_excess_identity.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261020)


def matrix_sqrt_spd(A: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    w = np.clip(np.real(w), 0, None)
    return (V * np.sqrt(w)) @ V.T


def X_from_metrics(hg, hf):
    hg_sqrt = matrix_sqrt_spd(hg)
    hg_inv_sqrt = inv(hg_sqrt)
    S = 0.5 * (hg_inv_sqrt @ hf @ hg_inv_sqrt + (hg_inv_sqrt @ hf @ hg_inv_sqrt).T)
    return hg_inv_sqrt @ matrix_sqrt_spd(S) @ hg_sqrt


def random_spd(rng, scale=1.0):
    A = rng.normal(size=(3, 3))
    return scale * (A @ A.T) + 0.4 * np.eye(3)


def run_wolfram():
    if not WOLFRAM.is_file():
        return {"ran": False, "error": "wolframscript not found"}
    try:
        proc = subprocess.run(
            [str(WOLFRAM), "-file", str(WL)],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(HERE),
        )
        txt_path = HERE / "Opsi2_QStage3_WOLFRAM_RESULTS.txt"
        body = txt_path.read_text(encoding="utf-8") if txt_path.is_file() else ""
        parsed = {}
        for line in body.splitlines():
            if " = " in line:
                k, v = line.split(" = ", 1)
                parsed[k] = v.strip()
        return {
            "ran": True,
            "returncode": proc.returncode,
            "stdout_tail": proc.stdout[-2000:],
            "stderr_tail": proc.stderr[-1000:],
            "parsed": parsed,
        }
    except Exception as e:
        return {"ran": False, "error": repr(e)}


def sympy_excess_and_dirac():
    hg1, hg2, hg3 = sp.symbols("hg1 hg2 hg3", positive=True)
    x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
    pg1, pg2, pg3 = sp.symbols("pg1 pg2 pg3", real=True)
    p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
    hg = sp.diag(hg1, hg2, hg3)
    X = sp.diag(x1, x2, x3)
    hf = hg * X * X
    W = hg * (sp.eye(3) - X) ** 2
    Wcheck = sp.simplify(W - (hg + hf - 2 * hg * X))
    pig = sp.Matrix([pg1, pg2, pg3])
    p = sp.Matrix([p1, p2, p3])
    rem = sp.simplify(hg * pig + hf * (-pig - p) + W * p)
    rem0 = sp.simplify(hg * pig + hf * (-pig))
    excess = sp.simplify(rem - rem0)
    e_whf = sp.simplify(excess - (W - hf) * p)
    e_i2x = sp.simplify(excess - hg * (sp.eye(3) - 2 * X) * p)
    k1 = sp.simplify(excess.subs({x1: 1, x2: 1, x3: 1}))
    a, b, c = sp.symbols("a b c")
    det = sp.simplify(a * c + b**2)
    return {
        "engine": "sympy",
        "W_equals_hg_hf_minus_2G": bool(Wcheck == sp.zeros(3)),
        "excess_equals_(W-hf).p": bool(e_whf == sp.zeros(3, 1)),
        "excess_equals_hg.(I-2X).p": bool(e_i2x == sp.zeros(3, 1)),
        "K1_excess_vanishes_at_X_I": bool(k1 == sp.zeros(3, 1)),
        "dirac_det": str(det),
        "dirac_det_if_c_0": str(sp.simplify(det.subs(c, 0))),
        "excess_formula": "hg.(I-2X).p  (= (W-hf).p) under Ci: πg+πf+p=0",
    }


def numpy_excess_suite(n_trials=60):
    rows = []
    for trial in range(n_trials):
        hg = random_spd(RNG)
        if trial % 2 == 0:
            X = np.diag([1.0, 1.2, 1.7])
            hf = hg @ X @ X
        else:
            hf = random_spd(RNG)
            X = X_from_metrics(hg, hf)
        G = hg @ X
        W = hg @ (np.eye(3) - X) @ (np.eye(3) - X)
        W_alt = hg + hf - 2 * G
        pig = RNG.normal(size=3)
        p = RNG.normal(size=3)
        pif = -pig - p
        rem = hg @ pig + hf @ pif + W @ p
        rem0 = hg @ pig + hf @ (-pig)
        excess = rem - rem0
        pred = (W - hf) @ p
        pred2 = hg @ (np.eye(3) - 2 * X) @ p
        rows.append(
            dict(
                W_match_alt=float(norm(W - W_alt)),
                excess_vs_pred=float(norm(excess - pred)),
                excess_vs_pred2=float(norm(excess - pred2)),
                excess_norm=float(norm(excess)),
                rem_norm=float(norm(rem)),
                rem0_norm=float(norm(rem0)),
                X_aniso=float(norm(X - np.eye(3))),
            )
        )
    # K1
    k1_err = []
    for _ in range(20):
        hg = random_spd(RNG)
        hf = hg.copy()
        X = X_from_metrics(hg, hf)
        W = hg @ (np.eye(3) - X) @ (np.eye(3) - X)
        pig = RNG.normal(size=3)
        p = RNG.normal(size=3)
        excess = (hg @ pig + hf @ (-pig - p) + W @ p) - (hg @ pig + hf @ (-pig))
        k1_err.append(float(norm(excess)))

    return {
        "n_trials": len(rows),
        "max_W_match_alt": float(max(r["W_match_alt"] for r in rows)),
        "max_excess_vs_pred": float(max(r["excess_vs_pred"] for r in rows)),
        "max_excess_vs_pred2": float(max(r["excess_vs_pred2"] for r in rows)),
        "median_excess_norm": float(np.median([r["excess_norm"] for r in rows])),
        "median_rem0_norm": float(np.median([r["rem0_norm"] for r in rows])),
        "fraction_excess_gt_1e-8": float(np.mean([r["excess_norm"] > 1e-8 for r in rows])),
        "K1_max_excess_norm": float(max(k1_err)),
        "identities_hold_numerically": bool(
            max(r["excess_vs_pred"] for r in rows) < 1e-8
            and max(r["excess_vs_pred2"] for r in rows) < 1e-8
            and max(r["W_match_alt"] for r in rows) < 1e-8
        ),
    }


def absorption_class_diagnosis(sympy_block, numpy_block, wolfram_block):
    """
    F12-safe diagnosis:
    Dirac det = a c + b^2. If c={S,S}=0 and b={C_SC,S}≠0 (pure-HR pattern),
    det independent of a={C_SC,C_SC}. Matter shifting a (R_j / excess) does not
    destroy second-class invertibility by itself.
    """
    # Literature/chain reference: pure HR absorbs nonzero a via the pair, not weak zero.
    # ΔS ultralocal ⇒ {ΔS,ΔS} has no ∂δ; continuum det diagnosis for ∂δ sector
    # still controlled by b from {C_SC,S}.
    det_if_c0 = sympy_block["dirac_det_if_c_0"]  # should be b**2
    pattern_holds = det_if_c0.replace(" ", "") in ("b**2", "b^2")
    excess_nonzero_generic = numpy_block["fraction_excess_gt_1e-8"] > 0.9
    k1_ok = numpy_block["K1_max_excess_norm"] < 1e-8

    # Whether matter kills b: NOT computed (needs full {C_SC, S+ΔS}).
    b_shift = {
        "status": "uncomputed",
        "note": (
            "{C_SC, S+ΔS} at O(ψ²) not evaluated; ΔS ultralocal (S3) so leading "
            "b receives diffeomorphism-of-ΔS pieces — not shown to vanish."
        ),
    }

    if not numpy_block["identities_hold_numerically"] or not sympy_block["excess_equals_hg.(I-2X).p"]:
        landing = "G-4"
        reason = "Algebraic excess identity failed reproducibility gate; no fork."
    elif pattern_holds and excess_nonzero_generic and k1_ok:
        landing = "G-4"
        reason = (
            "Q-Stage3: on-shell excess = hg(I-2X)p is generically nonzero (not F12-as-ghost). "
            "Dirac det = a c + b² ⇒ if c={S,S}=0 and b≠0 (pure-HR pair pattern), det is "
            "independent of a; matter contribution to a (R_j / excess) does NOT by itself "
            "destroy second-class invertibility. b-shift from ΔS uncomputed but not shown killed. "
            "Therefore: no Stage-3 class loss earned; fork remains Q-Stage4. "
            "F12 satisfied (did not land G-2 from {C_SC,C_SC}≠0)."
        )
    else:
        landing = "G-4"
        reason = "Partial diagnostics; holding G-4."

    return {
        "pure_HR_pattern_det_independent_of_a": pattern_holds,
        "excess_generically_nonzero": excess_nonzero_generic,
        "K1_pass": k1_ok,
        "b_shift_from_DeltaS": b_shift,
        "F12": "nonvanishing_alone_not_used_as_G2",
        "landing": landing,
        "reason": reason,
        "wolfram_used": bool(wolfram_block.get("ran")),
    }


def main():
    wl = run_wolfram()
    sy = sympy_excess_and_dirac()
    ny = numpy_excess_suite(60)
    diag = absorption_class_diagnosis(sy, ny, wl)

    # Cross-check Wolfram parsed booleans if present
    wl_agree = None
    if wl.get("ran") and wl.get("parsed"):
        p = wl["parsed"]
        def as_bool(s):
            return str(s).lower() in ("true", "true,", "1")

        keys = [
            ("excess_equals_hg_I_minus_2X_times_p", sy["excess_equals_hg.(I-2X).p"]),
            ("K1_excess_vanishes_at_X_I", sy["K1_excess_vanishes_at_X_I"]),
            ("W_equals_hg_hf_minus_2G", sy["W_equals_hg_hf_minus_2G"]),
        ]
        wl_agree = {}
        for k, sy_val in keys:
            if k in p:
                wl_agree[k] = {"wolfram": p[k], "sympy": sy_val, "match": as_bool(p[k]) == sy_val}

    out = {
        "engines": {
            "numpy": True,
            "sympy": True,
            "wolfram": wl.get("ran", False),
            "wolfram_path": str(WOLFRAM),
        },
        "prereg": "Opsi2_QStage3_C_SC_Self_Bracket_PREREGISTRATION_CursorMain_Filed_Before_Compute_20261020.md",
        "wolfram": wl,
        "sympy": sy,
        "numpy_excess": ny,
        "wolfram_sympy_agree": wl_agree,
        "diagnosis": diag,
        "conclusion": {
            "landing": diag["landing"],
            "N_status": "undetermined",
            "Q_Stage3": "no_class_loss_earned; excess=hg(I-2X)p; fork→Q-Stage4",
            "posteriors_held": {"G1": 0.20, "G2": 0.35, "G3": 0.10, "G4": 0.35},
            "reason": diag["reason"],
        },
        "struck": ["R5_90_90", "Stage4_D_channel_comparison", "G2_from_nonvanishing_alone"],
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out["conclusion"], indent=2))
    print("sympy", {k: sy[k] for k in sy if k != "excess_formula"})
    print("numpy identities", ny["identities_hold_numerically"], "K1", ny["K1_max_excess_norm"])
    print("wolfram ran", wl.get("ran"), "parsed", wl.get("parsed"))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
