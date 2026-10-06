#!/usr/bin/env python3
"""Apply AC GO: C16×3 + C14×1 + C12×3 (C12 item1 = 2 loci). Match-or-report."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Core_Papers")
REPORT = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_apply_C16_C14_C12_seven_REPORT_20261003.txt"
)

PATCHES: list[tuple[str, str, str, str]] = [
    (
        "C16-1",
        "Companion_16_Octonion_Gauge_Species_v10_19_0.md",
        "The gauge-birth temperature $T_{\\mathrm{GB}}=M_{\\mathrm{Pl}}/\\sqrt{2\\pi}$ is fixed elsewhere (Companion 9 / Companion 12 fibre modulus).",
        "The gauge-birth temperature $T_{\\mathrm{GB}}=M_{\\mathrm{Pl}}/\\sqrt{2\\pi}$ is **conditional**: its Companion 9 saddle-width derivation is withdrawn under Door B, and the Companion 12 fibre-modulus relation $\\beta_{\\mathrm{GB}}M_{\\mathrm{Pl}}=\\sqrt{2\\pi}$ is the candidate independent grounding and remains open. It characterises the saddle scale and is not a post-inflationary reheating temperature (Part 2 §8.3).",
    ),
    (
        "C16-2",
        "Companion_16_Octonion_Gauge_Species_v10_19_0.md",
        "- *Cosmological observables* ($n_s$, $r$) — do not follow from $G_2$ representation content; they are conditional on open $K(\\Phi)$ (Companion 15 §6.1: metric-only channel proven empty).",
        "- *Cosmological observables* ($n_s$, $r$) — do not follow from $G_2$ representation content. Native values from $\\Phi_{\\mathrm{NTE}}$ are **withdrawn** (2026-09-26), frame-level $K(\\Phi)$ with them (Companion 17, audit trail only), and the cosmological origin sector is deposited **open** (Part 3; option D, 2026-09-27). Companion 15 §6.1's metric-only-channel theorem stands.",
    ),
    (
        "C16-3",
        "Companion_16_Octonion_Gauge_Species_v10_19_0.md",
        "| Overclaim that $n_s$ is closed from G₂ content | $n_s$/$r$ conditional on $K(\\Phi)$ (Part 3; Companion 15) |",
        "| Overclaim that $n_s$ is closed from G₂ content | Native $n_s$/$r$ **withdrawn** (2026-09-26); $K(\\Phi)$ withdrawn with them; origin sector open (Part 3, option D) |",
    ),
    (
        "C14-1",
        "Companion_14_RW_Spectral_Action_v10_19_0.md",
        "| $n_s$, $r$, $K(\\Phi)$ | Remain open / conditional (Part 3); the RW expansion does not close $K(\\Phi)$. |",
        "| $n_s$, $r$, $K(\\Phi)$ | Native $n_s$/$r$ **withdrawn** (2026-09-26); frame-level $K(\\Phi)$ withdrawn with them (Companion 17, audit trail only); cosmological origin sector open (Part 3, option D). The RW expansion bears on none of them. |",
    ),
    (
        "C12-1a",
        "Companion_12_Chord_v10_19_0.md",
        "is a distinct counter from the inflationary e-fold depth N_e ≈ 63 — the two must not be conflated",
        "is a distinct counter from the Hartle–Hawking energy-scale ratio N_HH ≈ 63 (Companion 8 §2) — and from the inflationary pivot depth N_*; the three must not be conflated",
    ),
    (
        "C12-1b",
        "Companion_12_Chord_v10_19_0.md",
        "the n_s = 1 − 2/N_e form shares the e-fold depth N_e with the rest of the framework",
        "the n_s = 1 − 2/N_* form requires an inflationary pivot depth N_*, which is **not** the Hartle–Hawking ratio N_HH ≈ 63; identifying the two is the category error that produced the withdrawn native (n_s, r)",
    ),
    (
        "C12-2",
        "Companion_12_Chord_v10_19_0.md",
        "(the inflation sector's current status is carried in the master trilogy and Companion 9, presented there as conditional)",
        "(native $(n_s, r)$ from $\\Phi_{\\mathrm{NTE}}$ are **withdrawn** — 2026-09-26 — and the cosmological origin sector is deposited **open**: Part 3, option D, 2026-09-27)",
    ),
    (
        "C12-3a",
        "Companion_12_Chord_v10_19_0.md",
        "the unimodular projection on this geometry removes the extensive vacuum term, so empty space does not gravitate catastrophically, and this stands independently of a₄ (Companion 11)",
        "the unimodular / trace-free formulation removes the extensive vacuum term, so empty space does not gravitate catastrophically, and this stands independently of a₄. **Adopted and credited** (Buchmüller–Dragon 1988; Henneaux–Teitelboim 1989; Companion 11). **Whether NTE's 𝕆 ⊕ 𝕆 triple yields the projection intrinsically is open** — the Chamseddine–Connes–Mukhanov route requires M₂(ℍ) ⊕ M₄(ℂ)",
    ),
    (
        "C12-3b",
        "Companion_12_Chord_v10_19_0.md",
        "the cosmological-constant suppression — the mechanism stands (Companion 11), the number is not claimed",
        "the cosmological-constant suppression — the mechanism is **adopted and credited**, not derived here (Companion 11); the number is not claimed",
    ),
]


def adjacent(text: str, needle: str, radius: int = 160) -> tuple[str, str]:
    i = text.find(needle)
    if i < 0:
        return ("", "")
    pre = text[max(0, i - radius) : i].replace("\n", "↵")
    post = text[i + len(needle) : i + len(needle) + radius].replace("\n", "↵")
    return pre, post


def main() -> None:
    cache: dict[str, str] = {}
    for _, fn, _, _ in PATCHES:
        if fn not in cache:
            raw = (ROOT / fn).read_bytes()
            # preserve CRLF if present
            cache[fn] = raw.decode("utf-8")

    results: list[str] = []
    for pid, fn, old, new in PATCHES:
        text = cache[fn]
        count = text.count(old)
        if count != 1:
            results.append(f"FAIL {pid}: match count={count} (need 1) in {fn}")
            results.append(f"  old={old!r}")
            continue
        pre, post = adjacent(text, old)
        cache[fn] = text.replace(old, new, 1)
        results.append(f"OK {pid}: replaced once in {fn}")
        results.append(f"  MATCH_BEFORE… {pre[-140:]}")
        results.append(f"  MATCH_AFTER…  {post[:140]}")

    fails = [r for r in results if r.startswith("FAIL")]
    if fails:
        REPORT.write_text("\n".join(results) + "\nNO FILES WRITTEN.\n", encoding="utf-8")
        print("\n".join(results))
        raise SystemExit(1)

    for fn, text in cache.items():
        path = ROOT / fn
        # preserve original newline style
        raw0 = path.read_bytes()
        nl = b"\r\n" if b"\r\n" in raw0 else b"\n"
        data = text.replace("\r\n", "\n").replace("\n", nl.decode("ascii")).encode("utf-8")
        path.write_bytes(data)

    lines = list(results)
    lines.append("")
    lines.append("=== VERIFY-THEN-REPORT (re-read from disk) ===")
    all_ok = True
    for pid, fn, old, new in PATCHES:
        disk = (ROOT / fn).read_text(encoding="utf-8")
        ok_new = new in disk
        ok_old = old not in disk
        status = "APPLIED" if ok_new and ok_old else "VERIFY_FAIL"
        if status != "APPLIED":
            all_ok = False
        lines.append(f"{status} {pid}: new_present={ok_new} old_absent={ok_old}")
        if ok_new:
            pre, post = adjacent(disk, new)
            lines.append(f"  ADJ_BEFORE… {pre[-140:]}")
            lines.append(f"  ADJ_AFTER…  {post[:140]}")

    lines.append("")
    lines.append("SUMMARY: " + ("ALL 9 LOCI APPLIED (7 logical patches; C12-1 has 2 loci)" if all_ok else "VERIFY FAILURES"))
    lines.append("C11 mimetic line: NOT STRUCK (per GO §4).")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    if not all_ok:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
