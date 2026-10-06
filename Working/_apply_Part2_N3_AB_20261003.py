#!/usr/bin/env python3
"""Part 2 N-3 A + redrafted B. Match-or-report; verify-then-report."""
from __future__ import annotations

from pathlib import Path

PART2 = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Core_Papers\NTE_v10_19_0_Part2_Structure.md"
)
REPORT = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_apply_Part2_N3_AB_REPORT_20261003.txt"
)

# Item A (unchanged from 2026-09-28 register)
A_OLD = (
    r"One mechanism, $H(x,N)=\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$ with spatially varying "
    r"$|\Phi|$, still yields the Hubble-tension signature (§XIII) and the DM variance (§IX); "
    r"it does **not** reproduce DESI DR2's $(w_0>-1,\,w_a<0)$ pattern."
)
A_NEW = (
    r"One mechanism, $H(x,N)=\beta_{\mathrm{NTE}}|\Phi(x,N)|^2$ with spatially varying "
    r"$|\Phi|$, still yields the Hubble-tension signature (§XIII); it does **not** reproduce "
    r"DESI DR2's $(w_0>-1,\,w_a<0)$ pattern. (The DM:baryon variance of §IX has a different "
    r"origin — the central limit theorem, not spatial $|\Phi|$ variation — and is not a "
    r"consequence of this mechanism.)"
)

# B-1
B1_OLD = (
    r"(Structurally similar to Wiltshire/Célérier, but with a specific mechanism: spatial "
    r"$|\Phi_{\mathrm{NTE}}|^2$ variation under the pointwise constraint.)"
)
B1_NEW = (
    r"(Structurally similar to Wiltshire/Célérier in the **void sampling bias**. The earlier "
    r"claim of a distinct mechanism — spatial $|\Phi_{\mathrm{NTE}}|^2$ variation under the "
    r"pointwise constraint — is **withdrawn**: under Door B, $|\Phi|^2$ relabels the expansion "
    r"history, so varying it is varying $H$, which those treatments already have. The "
    r"distinction is elsewhere; see below.)"
)

B2_APPEND = (
    " What distinguishes NTE here is **not** the void treatment but the status of the "
    "acceleration. In timescape-type models the acceleration is **apparent** — an artefact of "
    "averaging over inhomogeneity or of observer location — and dissolves once that is "
    "properly accounted. In NTE the acceleration is **real and global**, with $w = -1$ exactly, "
    "and the void effect is a **sampling bias on distance indicators layered on top of it**. "
    "The two make opposite commitments about what survives better averaging. A second, sharper "
    "commitment follows (§XII): the same void bias that eases the Hubble tension pushes a CPL "
    "fit toward $w_0 < -1$, so **it cannot also explain DESI's $w_0 > -1$** — NTE forecloses "
    "that escape rather than taking it. The $w = -1$ asymptote rests on the **adopted** "
    "unimodular / trace-free formulation in which $\\Lambda$ enters as an integration constant "
    "rather than vacuum energy (Companion 11 — adopted and credited; the "
    "Chamseddine–Connes–Mukhanov grounding is a candidate, not shown for NTE's algebra). The "
    "commitment is real and falsifiable; its support is adopted, not derived."
)

# B-3: append after unloading clause. Anchor on the exact phrase ending the unloading idea.
B3_ANCHOR = (
    r"As matter radiates into photons and $|\Phi_{\mathrm{NTE}}|$ thins, the boundary's "
    r"geometric impedance to expansion decreases — acceleration as *mechanical unloading*, "
    r"not a dark-energy fluid."
)
B3_NEW = (
    r"As matter radiates into photons and $|\Phi_{\mathrm{NTE}}|$ thins, the boundary's "
    r"geometric impedance to expansion decreases — acceleration as *mechanical unloading*, "
    r"not a dark-energy fluid. (**Description, not mechanism**: under Door B, $|\Phi|$ thinning "
    r"is $H$ falling restated. The phrase is retained as physical picture; it carries no "
    r"explanatory content the expansion history does not already carry.)"
)


def adj(text: str, needle: str, radius: int = 140) -> tuple[str, str]:
    i = text.find(needle)
    if i < 0:
        return "", ""
    return (
        text[max(0, i - radius) : i].replace("\n", "↵"),
        text[i + len(needle) : i + len(needle) + radius].replace("\n", "↵"),
    )


def main() -> None:
    raw = PART2.read_bytes()
    nl = b"\r\n" if b"\r\n" in raw else b"\n"
    text = raw.decode("utf-8")
    lines: list[str] = []

    steps: list[tuple[str, str, str]] = [
        ("A", A_OLD, A_NEW),
        ("B1", B1_OLD, B1_NEW),
        ("B3", B3_ANCHOR, B3_NEW),
    ]

    for pid, old, new in steps:
        c = text.count(old)
        if c != 1:
            lines.append(f"FAIL {pid}: count={c}")
            lines.append(f"  old={old!r}")
            # fuzzy help
            if pid == "A" and "DM variance" in text:
                j = text.find("DM variance")
                lines.append(f"  near={text[j-80:j+120]!r}")
            if pid == "B1" and "Wiltshire" in text:
                j = text.find("Wiltshire")
                lines.append(f"  near={text[j-40:j+160]!r}")
            if pid == "B3" and "mechanical unloading" in text:
                j = text.find("mechanical unloading")
                lines.append(f"  near={text[j-100:j+80]!r}")
            REPORT.write_text("\n".join(lines) + "\nNO WRITE\n", encoding="utf-8")
            print("FAIL — see report")
            raise SystemExit(1)
        pre, post = adj(text, old)
        text = text.replace(old, new, 1)
        lines.append(f"OK {pid}")
        lines.append(f"  BEFORE… {pre[-120:]}")
        lines.append(f"  AFTER…  {post[:120]}")

    # B2+B4: append after B1_NEW (now in text once)
    if text.count(B1_NEW) != 1:
        lines.append(f"FAIL B2: B1_NEW count={text.count(B1_NEW)}")
        REPORT.write_text("\n".join(lines) + "\nNO WRITE\n", encoding="utf-8")
        raise SystemExit(1)
    if B2_APPEND.strip() in text:
        lines.append("SKIP B2: already present")
    else:
        text = text.replace(B1_NEW, B1_NEW + B2_APPEND, 1)
        lines.append("OK B2+B4: appended distinction + C11 dependency after B1")

    out = text.replace("\r\n", "\n").replace("\n", nl.decode("ascii")).encode("utf-8")
    PART2.write_bytes(out)

    disk = PART2.read_text(encoding="utf-8")
    lines.append("")
    lines.append("=== VERIFY-THEN-REPORT ===")
    checks = [
        ("A_new", A_NEW in disk),
        ("A_old_gone", A_OLD not in disk),
        ("B1_new", B1_NEW in disk),
        ("B1_old_gone", B1_OLD not in disk),
        ("B2_present", "What distinguishes NTE here" in disk),
        ("B4_present", "support is adopted, not derived" in disk),
        ("B3_present", "Description, not mechanism" in disk),
        ("B3_anchor_gone", B3_ANCHOR not in disk),
    ]
    for name, ok in checks:
        lines.append(f"{'PASS' if ok else 'FAIL'} {name}")
    # adjacent for key news
    for label, needle in [
        ("A", A_NEW),
        ("B1", B1_NEW),
        ("B3", "Description, not mechanism"),
    ]:
        if needle in disk:
            pre, post = adj(disk, needle if label != "B3" else "(**Description, not mechanism**")
            lines.append(f"ADJ {label}_BEFORE… {pre[-100:]}")
            lines.append(f"ADJ {label}_AFTER…  {post[:100]}")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    # avoid console encode crash
    REPORT_PART = REPORT.read_text(encoding="utf-8")
    print(REPORT_PART.encode("ascii", "replace").decode("ascii"))


if __name__ == "__main__":
    main()
