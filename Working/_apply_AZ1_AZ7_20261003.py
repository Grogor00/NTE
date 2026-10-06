#!/usr/bin/env python3
"""Apply PC AZ1–AZ7 Book patches. Match-or-report; verify-then-report."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
REPORT = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_apply_AZ1_AZ7_REPORT_20261003.txt"
)

PATCHES: list[tuple[str, str, str, str]] = [
    (
        "AZ1",
        "Chapter_15_The_Score_v6.md",
        "**The dark-energy equation of state w = −1, exactly — naked, and currently losing.** A clean cosmological constant: structural quietness, not a dynamical field, and no dial anywhere in the framework to turn. DESI DR2 — baryon acoustic oscillations with the CMB, supernova-independent — prefers evolving dark energy over w = −1 at about 3.1σ. The framework has no answer to that.",
        "**The dark-energy equation of state w = −1, exactly — naked, and under pressure.** A clean cosmological constant: structural quietness, not a dynamical field, and no dial anywhere in the framework to turn. The pressure is real, and it is worth stating at its actual strength, because earlier editions of this scorecard overstated it against the framework's own interest. DESI's second data release taken on its own is well described by a flat universe with a constant equation of state, and does not exclude w = −1. The 3.1σ figure that circulates is narrower than it sounds: it is a preference for a two-parameter evolving equation of state over the constant one, when DESI's baryon acoustic oscillations are combined with the microwave background — a comparison between models, not a measurement of w. On that same combination the Bayesian evidence modestly favours the constant. And the supernova-driven part of the case softened in 2026, when a recalibration of the DES sample brought it from about 4.2σ to 3.2σ. **What is left is a real and unresolved tension rather than a refutation**: the data prefer a shape the framework cannot produce, and the framework has no internal adjustment available.",
    ),
    (
        "AZ2",
        "Chapter_15_The_Score_v6.md",
        "**Currently losing:** w = −1 against DESI DR2 at about 3.1σ, with nothing internal to absorb it",
        "**Currently losing:** w = −1 against the DESI-plus-microwave-background combination, which prefers an evolving equation of state over a constant one, with nothing internal to absorb it — §4 states the figure at its proper strength",
    ),
    (
        "AZ3",
        "Appendix_C_The_Open_Ledger_v1_7.md",
        "DESI's second data release, combined with the microwave background, currently prefers an evolving equation of state at roughly 3.1 standard deviations from −1 in the supernova-independent combination. (The significance quoted from supernova-based combinations was higher still until a 2026 recalibration of the DES sample brought it down from about 4.2σ to 3.2σ — a reminder that the measurement side is itself moving.)",
        "DESI's second data release, combined with the microwave background, prefers an evolving equation of state over a constant one at roughly 3.1 standard deviations. That figure is worth unpacking, because this ledger has quoted it more strongly than it deserves. **It is a comparison between two models on a joint likelihood, not a direct measurement of w, and not an exclusion of −1 by DESI alone** — DESI's baryon acoustic oscillations on their own are well described by a flat universe with a constant equation of state, and on the same joint data the Bayesian evidence modestly favours the constant. The supernova-based route softened too: a 2026 recalibration of the DES sample brought it from about 4.2σ to 3.2σ. The measurement side is itself moving, and so is our reading of it. **The tension is real and the framework has no answer to it; it is simply not as sharp as this ledger previously implied.**",
    ),
    (
        "AZ4",
        "Appendix_C_The_Open_Ledger_v1_7.md",
        "Framework: w = −1 exactly, currently in ~3.1σ tension (C.1).",
        "Framework: w = −1 exactly, currently in tension with the DESI-plus-CMB combination — stated at its proper strength in C.1.",
    ),
    (
        "AZ5",
        "Chapter_07_The_Gauge_Birth_v5.md",
        "**4. The bang.** Pre-temporal matter sat at enormous density **without** gauge forces to thermalise it. When strong, weak, and electromagnetic interactions switch on, that matter is violently out of equilibrium. The energy released fills the hot radiation bath we later see as the **cosmic microwave background**.\n\nSo: the Big Bang, on this reading, was **not** the beginning of time. It was the **thermal scream** when time and the Standard Model arrived. No inflaton required — the energy was already there, locked in pre-temporal matter, released when the rules changed.",
        "**4. The bang.** Pre-temporal matter sat at enormous density **without** gauge forces to thermalise it. When strong, weak, and electromagnetic interactions switch on, that matter is violently out of equilibrium, and the reorganisation releases an enormous amount of energy.\n\nSo: the Big Bang, on this reading, was **not** the beginning of time. It was the **thermal scream** when time and the Standard Model arrived — the energy already there, locked in pre-temporal matter, released when the rules changed.\n\nHow that scream connects to the hot radiation bath we later see as the cosmic microwave background is a question the framework leaves open, and it is worth saying why rather than passing over it. The gauge birth happens at a temperature the geometry sets near the Planck scale. The radiation era that nucleosynthesis and the microwave background sit on top of begins far cooler. **If** the framework's early history contains an epoch of accelerated expansion between the two, energy conservation alone caps the temperature at the end of it some two thousand times below the gauge birth's, and the two cannot be the same event. **If** it contains no such epoch, they may connect directly. **The framework does not currently select between those histories.** What drove early acceleration, or whether anything did, is open work — Chapter 15 and the Open Ledger carry it as open, and this book will not pick a side it has not earned. So the thermal scream is the framework's account of **where the energy came from**. It is not yet its account of **how that energy became the particular bath we observe**.",
    ),
    (
        "AZ6",
        "Chapter_07_The_Gauge_Birth_v5.md",
        '- **"What banged?"** → Thermalisation when gauge forces switched on, not inflaton decay.',
        '- **"What banged?"** → Thermalisation when gauge forces switched on. Whether that thermalisation is also the beginning of the radiation era we observe is open, for the reason given above — so this question changes category rather than closing.',
    ),
    (
        "AZ7",
        "Chapter_07_The_Gauge_Birth_v5.md",
        "And what there was, the moment the rules changed, thermalised into everything we observe.",
        "And what there was, the moment the rules changed, thermalised — into the universe whose later history the rest of this book describes.",
    ),
]


def adj(text: str, needle: str, radius: int = 120) -> tuple[str, str]:
    i = text.find(needle)
    if i < 0:
        return "", ""
    return (
        text[max(0, i - radius) : i].replace("\n", "↵"),
        text[i + len(needle) : i + len(needle) + radius].replace("\n", "↵"),
    )


def main() -> None:
    cache: dict[str, tuple[bytes, str]] = {}
    lines: list[str] = []

    for pid, fn, old, new in PATCHES:
        if fn not in cache:
            raw = (ROOT / fn).read_bytes()
            # Normalize newlines for matching; restore on write.
            text = raw.decode("utf-8").replace("\r\n", "\n")
            cache[fn] = (raw, text)
        raw, text = cache[fn]
        c = text.count(old)
        if c != 1:
            lines.append(f"FAIL {pid}: count={c} in {fn}")
            # show nearby key
            key = old[:40]
            j = text.find(key[:20]) if len(key) > 20 else -1
            if j >= 0:
                lines.append(f"  near={text[j:j+100]!r}")
            REPORT.write_text("\n".join(lines) + "\nNO WRITE\n", encoding="utf-8")
            raise SystemExit(1)
        pre, post = adj(text, old)
        text = text.replace(old, new, 1)
        cache[fn] = (raw, text)
        lines.append(f"OK {pid}")
        lines.append(f"  BEFORE… {pre[-100:]}")
        lines.append(f"  AFTER…  {post[:100]}")

    for fn, (raw0, text) in cache.items():
        nl = b"\r\n" if b"\r\n" in raw0 else b"\n"
        data = text.replace("\r\n", "\n").replace("\n", nl.decode("ascii")).encode("utf-8")
        (ROOT / fn).write_bytes(data)

    lines.append("")
    lines.append("=== VERIFY-THEN-REPORT ===")
    all_ok = True
    for pid, fn, old, new in PATCHES:
        disk = (ROOT / fn).read_text(encoding="utf-8")
        ok = (new in disk) and (old not in disk)
        all_ok = all_ok and ok
        lines.append(f"{'APPLIED' if ok else 'VERIFY_FAIL'} {pid}")
        if new in disk:
            pre, post = adj(disk, new[:80] if len(new) > 80 else new)
            # use full new for adj when short
            needle = new if len(new) < 200 else new[:120]
            if needle in disk:
                pre, post = adj(disk, needle)
            lines.append(f"  ADJ_BEFORE… {pre[-90:]}")
            lines.append(f"  ADJ_AFTER…  {post[:90]}")

    lines.append("")
    lines.append(
        "SUMMARY: ALL AZ1–AZ7 APPLIED"
        if all_ok
        else "SUMMARY: VERIFY FAILURES — inspect"
    )
    lines.append("C21 v0.7: noted as PC-cut; not in this apply set.")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT.read_text(encoding="utf-8").encode("ascii", "replace").decode("ascii"))
    if not all_ok:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
