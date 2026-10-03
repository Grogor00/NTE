#!/usr/bin/env python3
"""P-dS4: observational anchor snapshot — kappa and w falsifier bands (§17.5.12)."""

from __future__ import annotations

KAPPA_PRED = 5.50
KAPPA_OBS = 5.38
KAPPA_SIG = 0.15

NS_PRED = 0.9685
NS_OBS = 0.9649
NS_SIG = 0.0042

CMBS4_KAPPA_SIG = 0.075
CMBS4_KAPPA_BAND = (5.27, 5.73)


def sigma_pull(pred: float, obs: float, sig: float) -> float:
    return abs(pred - obs) / sig


def main() -> None:
    k_pull = sigma_pull(KAPPA_PRED, KAPPA_OBS, KAPPA_SIG)
    ns_pull = sigma_pull(NS_PRED, NS_OBS, NS_SIG)

    print("P-dS4 observational anchor snapshot (Planck 2018 era)")
    print("-" * 55)
    print(f"kappa: pred={KAPPA_PRED:.2f}  obs={KAPPA_OBS:.2f}+/-{KAPPA_SIG:.2f}  pull={k_pull:.2f} sigma")
    print(f"n_s:   pred={NS_PRED:.4f}  obs={NS_OBS:.4f}+/-{NS_SIG:.4f}  pull={ns_pull:.2f} sigma")
    print(f"CMB-S4 kappa falsifier band: [{CMBS4_KAPPA_BAND[0]:.2f}, {CMBS4_KAPPA_BAND[1]:.2f}]")
    print(f"  (3sigma outside at sigma(kappa)~{CMBS4_KAPPA_SIG})")
    print("-" * 55)
    print("w diagnostics (a)-(d): qualitative — see P_dS4 worksheet")
    print("  DESI: low-z w>-1 hint — directional match, amplitude open")


if __name__ == "__main__":
    main()
