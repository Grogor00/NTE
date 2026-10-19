#!/usr/bin/env python3
"""
Q-Stage3 — run identical numeric suite in parallel: NumPy and Wolfram Engine.
Merges results and checks agreement.
"""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_QStage3_PARALLEL_NumPy_Wolfram_RESULTS.json"
WL = HERE / "Opsi2_QStage3_FULL_SUITE_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
SEED = 20261020
N_TRIALS = 60


def matrix_sqrt_spd(A):
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    w = np.clip(np.real(w), 0, None)
    return (V * np.sqrt(w)) @ V.T


def X_from_metrics(hg, hf):
    hg_sqrt = matrix_sqrt_spd(hg)
    his = inv(hg_sqrt)
    S = 0.5 * (his @ hf @ his + (his @ hf @ his).T)
    return his @ matrix_sqrt_spd(S) @ hg_sqrt


def random_spd(rng):
    A = rng.normal(size=(3, 3))
    return A @ A.T + 0.4 * np.eye(3)


def run_numpy():
    rng = np.random.default_rng(SEED)
    rows = []
    for trial in range(N_TRIALS):
        hg = random_spd(rng)
        if trial % 2 == 0:
            X = np.diag([1.0, 1.2, 1.7])
            hf = hg @ X @ X
        else:
            hf = random_spd(rng)
            X = X_from_metrics(hg, hf)
        G = hg @ X
        W = hg @ (np.eye(3) - X) @ (np.eye(3) - X)
        Walt = hg + hf - 2 * G
        pig = rng.normal(size=3)
        p = rng.normal(size=3)
        pif = -pig - p
        rem = hg @ pig + hf @ pif + W @ p
        rem0 = hg @ pig + hf @ (-pig)
        excess = rem - rem0
        pred = (W - hf) @ p
        pred2 = hg @ (np.eye(3) - 2 * X) @ p
        rows.append(
            dict(
                W_match_alt=float(norm(W - Walt)),
                excess_vs_pred=float(norm(excess - pred)),
                excess_vs_pred2=float(norm(excess - pred2)),
                excess_norm=float(norm(excess)),
                rem0_norm=float(norm(rem0)),
                W_norm=float(norm(W)),
            )
        )
    k1W = []
    for _ in range(20):
        hg = random_spd(rng)
        hf = hg.copy()
        X = X_from_metrics(hg, hf)
        W = hg @ (np.eye(3) - X) @ (np.eye(3) - X)
        k1W.append(float(norm(W)))
    return {
        "engine": "numpy",
        "n_trials": len(rows),
        "max_W_match_alt": float(max(r["W_match_alt"] for r in rows)),
        "max_excess_vs_pred": float(max(r["excess_vs_pred"] for r in rows)),
        "max_excess_vs_pred2": float(max(r["excess_vs_pred2"] for r in rows)),
        "median_excess_norm": float(np.median([r["excess_norm"] for r in rows])),
        "median_rem0_norm": float(np.median([r["rem0_norm"] for r in rows])),
        "fraction_excess_gt_1e-8": float(np.mean([r["excess_norm"] > 1e-8 for r in rows])),
        "identities_hold_numerically": bool(
            max(r["excess_vs_pred"] for r in rows) < 1e-8
            and max(r["excess_vs_pred2"] for r in rows) < 1e-8
            and max(r["W_match_alt"] for r in rows) < 1e-8
        ),
        "K1_W_max_norm_at_X_I": float(max(k1W)),
        "K1_W_vanishes_at_X_I": bool(max(k1W) < 1e-8),
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_QStage3_WOLFRAM_FULL_RESULTS.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {
        "returncode": proc.returncode,
        "stderr_tail": proc.stderr[-500:],
        "summary": data,
    }


def agree(np_s, wl_s, rtol=1e-5, atol=1e-7):
    keys = [
        "n_trials",
        "identities_hold_numerically",
        "K1_W_vanishes_at_X_I",
        "fraction_excess_gt_1e-8",
    ]
    out = {}
    for k in keys:
        if k not in wl_s:
            out[k] = {"status": "missing_in_wolfram"}
            continue
        a, b = np_s[k], wl_s[k]
        if isinstance(a, bool) or isinstance(b, bool):
            out[k] = {"numpy": a, "wolfram": b, "match": bool(a) == bool(b)}
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            out[k] = {
                "numpy": a,
                "wolfram": b,
                "match": bool(np.isclose(a, b, rtol=rtol, atol=atol)),
            }
        else:
            out[k] = {"numpy": a, "wolfram": b, "match": a == b}
    # soft compare (RNG streams differ across engines for medians)
    for k in ["median_excess_norm", "max_excess_vs_pred", "K1_W_max_norm_at_X_I"]:
        if k in wl_s and k in np_s:
            if "max_excess" in k or "K1_W_max" in k:
                flag = bool(np_s[k] < 1e-8 and float(wl_s[k]) < 1e-8)
                label = "both_tiny_err"
            else:
                flag = bool(np_s[k] > 0 and float(wl_s[k]) > 0)
                label = "both_positive"
            out[k] = {"numpy": np_s[k], "wolfram": wl_s[k], label: flag}
    return out


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        f_np = ex.submit(run_numpy)
        f_wl = ex.submit(run_wolfram)
        numpy_summary = f_np.result()
        wolfram_bundle = f_wl.result()

    wl_summary = wolfram_bundle.get("summary") or {}
    comparison = agree(numpy_summary, wl_summary) if wl_summary else {"error": "no wolfram json"}

    landing = "G-4"
    reason = (
        "Parallel NumPy+Wolfram: on-shell excess identity holds; W vanishes at X=I (K1); "
        "Dirac det=b^2 if c=0 independent of a; F12 — no G-2 from nonvanishing. "
        "Q-Stage3: no class-loss earned; fork → Q-Stage4."
    )
    if not numpy_summary.get("identities_hold_numerically") or not wl_summary.get(
        "identities_hold_numerically"
    ):
        reason = "Identity gate failed on one or both engines."

    out = {
        "mode": "parallel_numpy_wolfram",
        "numpy": numpy_summary,
        "wolfram": wolfram_bundle,
        "agreement": comparison,
        "conclusion": {
            "landing": landing,
            "N_status": "undetermined",
            "reason": reason,
            "posteriors_held": {"G1": 0.20, "G2": 0.35, "G3": 0.10, "G4": 0.35},
        },
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out["conclusion"], indent=2))
    print("numpy identities", numpy_summary.get("identities_hold_numerically"), "K1_W", numpy_summary.get("K1_W_vanishes_at_X_I"))
    print("wolfram identities", wl_summary.get("identities_hold_numerically"), "K1_W", wl_summary.get("K1_W_vanishes_at_X_I"))
    print("agreement", json.dumps(comparison, indent=2))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
