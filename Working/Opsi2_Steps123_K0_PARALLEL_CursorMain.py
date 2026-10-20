#!/usr/bin/env python3
"""Steps 1–3: K0' numeric (NumPy) in parallel with Wolfram. Mapping/matter in the verdict."""
from __future__ import annotations

import json
import subprocess
import concurrent.futures
from pathlib import Path

import numpy as np
from numpy.linalg import det, inv, norm

HERE = Path(__file__).resolve().parent
OUT = HERE / "Opsi2_Steps123_K0_PARALLEL_RESULTS.json"
WL = HERE / "Opsi2_Steps123_K0_Wolfram.wl"
WOLFRAM = Path(r"C:\Program Files\Wolfram Research\Wolfram Engine\15.0\wolframscript.exe")
RNG = np.random.default_rng(20261021)


def matrix_sqrt_spd(A):
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    w = np.clip(np.real(w), 0, None)
    return (V * np.sqrt(w)) @ V.T


def D_of_n(gamma, f3, n):
    x = 1.0 - float(n @ f3 @ n)
    if x <= 1e-12:
        raise ValueError("x")
    Q = x * np.eye(3) + np.outer(n, f3 @ n)
    inside = inv(gamma) @ f3 @ Q
    inside = 0.5 * (inside + inside.T)
    return matrix_sqrt_spd(inside) @ inv(Q)


def random_spd(rng):
    A = rng.normal(size=(3, 3))
    return A @ A.T + 0.4 * np.eye(3)


def run_numpy(n_try=80):
    beta0, beta1, m2 = 0.0, 1.0, 1.0
    rows = []
    for _ in range(n_try):
        gamma = random_spd(RNG)
        f3 = random_spd(RNG)
        n = RNG.normal(size=3)
        n = 0.25 * n / max(1.0, norm(n))
        x = 1.0 - float(n @ f3 @ n)
        if x <= 0.2:
            continue
        try:
            D = D_of_n(gamma, f3, n)
        except ValueError:
            continue
        Dn = D @ n
        if norm(n) < 1e-3 or norm(Dn) < 1e-3:
            continue
        if abs(np.linalg.det(D)) < 1e-8 or np.linalg.cond(D) > 1e6:
            continue
        sg = np.sqrt(det(gamma))
        V = beta0 + beta1 * np.sqrt(x) * np.trace(D)
        R = 2 * m2 * sg * beta1 * (f3 @ n) / np.sqrt(x)  # C_i = 0
        R0 = -float(R @ Dn) - 2 * m2 * sg * V  # C = 0
        C = R0 + float(R @ Dn) + 2 * m2 * sg * V
        Ci = R - 2 * m2 * sg * beta1 * (f3 @ n) / np.sqrt(x)
        try:
            VbarM = (beta1 / np.sqrt(x)) * (f3 @ inv(D))
        except np.linalg.LinAlgError:
            continue
        Vbar = inv(gamma) @ VbarM @ inv(gamma)
        P44 = (R0 + float(R @ Dn) + 2 * m2 * sg * V) * Dn + inv(gamma) @ R - 2 * m2 * sg * (Vbar @ gamma @ Dn)
        P45 = C * Dn
        Cnz = C + 1.7
        Pnz = Cnz * Dn
        rows.append(
            dict(
                n_norm=float(norm(n)),
                C_abs=float(abs(C)),
                Ci_norm=float(norm(Ci)),
                P44=float(norm(P44)),
                P44_vs_45=float(norm(P44 - P45)),
                P_nz=float(norm(Pnz)),
            )
        )
    return {
        "engine": "numpy",
        "model": "minimal beta2=beta3=0 beta1=1",
        "n_kept": len(rows),
        "max_Ci": float(max(r["Ci_norm"] for r in rows)),
        "max_C_when_set_0": float(max(r["C_abs"] for r in rows)),
        "max_P_when_C0": float(max(r["P44"] for r in rows)),
        "max_P44_vs_45": float(max(r["P44_vs_45"] for r in rows)),
        "min_P_when_C_nonzero": float(min(r["P_nz"] for r in rows)),
        "fraction_n_gt_1e-3": float(np.mean([r["n_norm"] > 1e-3 for r in rows])),
        "pass": bool(
            len(rows) >= 20
            and max(r["P44"] for r in rows) < 1e-8
            and max(r["P44_vs_45"] for r in rows) < 1e-8
            and min(r["P_nz"] for r in rows) > 1e-3
        ),
    }


def run_wolfram():
    proc = subprocess.run(
        [str(WOLFRAM), "-file", str(WL)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(HERE),
    )
    path = HERE / "Opsi2_Steps123_K0_WOLFRAM.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    return {"returncode": proc.returncode, "stderr_tail": proc.stderr[-400:], "summary": data}


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        a = ex.submit(run_numpy)
        b = ex.submit(run_wolfram)
        numpy_s = a.result()
        wolfram_b = b.result()
    wl = wolfram_b.get("summary") or {}
    out = {
        "numpy": numpy_s,
        "wolfram": wolfram_b,
        "both_pass": bool(numpy_s.get("pass") and wl.get("pass")),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"numpy_pass": numpy_s.get("pass"), "wolfram_pass": wl.get("pass"), "both": out["both_pass"], "numpy": {k: numpy_s[k] for k in numpy_s if k != "engine"}}, indent=2))
    print("wolfram", {k: wl.get(k) for k in ("n_kept", "max_P_when_C0", "max_P44_vs_45", "min_P_when_C_nonzero", "pass")})


if __name__ == "__main__":
    main()
