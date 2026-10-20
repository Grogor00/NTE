#!/usr/bin/env python3
"""Chi-corrected diagonal {E_g,E_g}_D: field content + F23 projection. NumPy || Wolfram."""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_CN_Dirac_Chi_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_CN_Dirac_Chi_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261021)


def rel_residual(R, p, a, b):
    v = R + a * p
    u = R + b * p
    nu = float(u @ u)
    nv = float(norm(v))
    if nu < 1e-18 or nv < 1e-18:
        return None
    proj = (float(v @ u) / nu) * u
    return float(norm(v - proj) / nv)


def run_numpy(n=200):
    rels, swaps, k1s, ratios = [], [], [], []
    for _ in range(n):
        sg = float(RNG.uniform(0.2, 2.0))
        sf = float(RNG.uniform(0.2, 2.0))
        S = sg + sf
        a = sg**2 / S
        b = S
        R = RNG.normal(size=3)
        p = RNG.normal(size=3)
        r = rel_residual(R, p, a, b)
        rs = rel_residual(R, p, sf**2 / S, S)
        rk = rel_residual(R, p, sg, sg)
        if None in (r, rs, rk):
            continue
        rels.append(r)
        swaps.append(rs)
        k1s.append(rk)
        ratios.append(a / b)
    rels = np.array(rels)
    return {
        "engine": "numpy",
        "n": int(len(rels)),
        "median_rel_residual": float(np.median(rels)),
        "fraction_rel_gt_1e-3": float(np.mean(rels > 1e-3)),
        "median_rel_swap": float(np.median(swaps)),
        "max_rel_K1_sf0": float(np.max(k1s)),
        "median_a_over_b": float(np.median(ratios)),
        "monomial": "p_j",
        "formula": "a=Sigma_g^2/Sigma, b=Sigma",
        "pass_Mb": bool(np.median(rels) > 0.05 and np.max(k1s) < 1e-8),
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_CN_Dirac_Chi_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": proc.stderr[-300:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(2) as ex:
        fn = ex.submit(run_numpy)
        fw = ex.submit(run_wolfram)
        ny = fn.result()
        wl = fw.result()
    wls = wl.get("summary") or {}
    out = {
        "numpy": ny,
        "wolfram": wl,
        "both_Mb": bool(ny.get("pass_Mb") and wls.get("pass_Mb")),
        "field_content": {
            "diagonal_chi_correction": "(Sigma_g^2/Sigma) * p_j",
            "not": "(psi.alpha.psi)*(pi)",
            "R3_distinctness_for_diagonal": False,
            "reason": "both legs are E_g; no pi_f in {chi, E_g}",
        },
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"numpy": ny, "wolfram_pass": wls.get("pass_Mb"), "wolfram_median": wls.get("median_rel_residual"), "both": out["both_Mb"]}, indent=2))


if __name__ == "__main__":
    main()
