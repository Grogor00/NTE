#!/usr/bin/env python3
"""Discharge (A) spin connection and (B) densitized phi. NumPy || Wolfram."""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.linalg import lstsq, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_CN_AB_Discharge_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_CN_AB_Discharge_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261021)


def sympy_ratios():
    sg, sf = sp.symbols("sg sf", positive=True)
    S = sg + sf
    ratio_psi = sp.simplify((sg**2 / S) / S)
    # phi = S**(1/2) psi => p_psi = p_phi / S on both the bracket and C_i
    ratio_phi = sp.simplify((sg**2 / S / S) / (S / S))
    return {
        "engine": "sympy",
        "ratio_psi": str(ratio_psi),
        "ratio_phi": str(ratio_phi),
        "both_(sg/S)**2": bool(sp.simplify(ratio_psi - (sg / S) ** 2) == 0 and sp.simplify(ratio_phi - ratio_psi) == 0),
        "A_p_channel": "Sigma_g**2/Sigma unchanged; omega adds an independent bilinear with the same prefactor",
    }


def project(v, cols):
    cols = np.column_stack(cols)
    coef, *_ = lstsq(cols, v, rcond=None)
    return float(norm(v - cols @ coef) / max(norm(v), 1e-30))


def run_numpy(n=200):
    single, enlarged, k1, swap = [], [], [], []
    for _ in range(n):
        sg = float(RNG.uniform(0.3, 2.0))
        sf = float(RNG.uniform(0.3, 2.0))
        S = sg + sf
        a = sg**2 / S
        b = S
        R = RNG.normal(size=3)
        Rf = RNG.normal(size=3)
        p = RNG.normal(size=3)
        bil = RNG.normal(size=3)
        u1 = R + b * p
        single.append(project(R + a * p, [u1]))
        enlarged.append(project(R + a * p + a * bil, [u1, Rf]))
        k1.append(project(R + sg * p, [R + sg * p]))
        swap.append(project(R + (sf**2 / S) * p + (sf**2 / S) * bil, [R + S * p, R]))
    single, enlarged, k1, swap = map(np.array, (single, enlarged, k1, swap))
    return {
        "engine": "numpy",
        "n": n,
        "median_single": float(np.median(single)),
        "median_enlarged_with_omega": float(np.median(enlarged)),
        "fraction_enlarged_gt_1e-3": float(np.mean(enlarged > 1e-3)),
        "max_K1": float(np.max(k1)),
        "median_K5_swap": float(np.median(swap)),
        "pass_G2": bool(np.median(enlarged) > 1e-3 and np.max(k1) < 1e-8),
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(HERE),
    )
    sym = HERE / "Opsi2_CN_AB_WOLFRAM_SYMBOLIC.json"
    num = HERE / "Opsi2_CN_AB_WOLFRAM_NUMERIC.json"
    return {
        "returncode": proc.returncode,
        "stderr_tail": proc.stderr[-200:],
        "symbolic": json.loads(sym.read_text(encoding="utf-8")) if sym.is_file() else {},
        "numeric": json.loads(num.read_text(encoding="utf-8")) if num.is_file() else {},
    }


def main():
    with concurrent.futures.ThreadPoolExecutor(2) as ex:
        fs = ex.submit(sympy_ratios)
        fn = ex.submit(run_numpy)
        fw = ex.submit(run_wolfram)
        sy, ny, wl = fs.result(), fn.result(), fw.result()
    wnum = wl.get("numeric") or {}
    out = {
        "sympy": sy,
        "numpy": ny,
        "wolfram": wl,
        "both_G2": bool(ny.get("pass_G2") and wnum.get("pass_G2") and sy.get("both_(sg/S)**2")),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "ratio_stable": sy.get("both_(sg/S)**2"),
        "numpy_pass": ny.get("pass_G2"),
        "numpy_median_enlarged": ny.get("median_enlarged_with_omega"),
        "wolfram_pass": wnum.get("pass_G2"),
        "wolfram_median_enlarged": wnum.get("median_enlarged_with_omega"),
        "both": out["both_G2"],
    }, indent=2))


if __name__ == "__main__":
    main()
