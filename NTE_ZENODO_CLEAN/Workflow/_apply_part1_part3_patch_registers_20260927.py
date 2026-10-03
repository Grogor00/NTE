# -*- coding: utf-8 -*-
"""Apply AC Part1 + Part3 patch registers (Greg GO 2026-09-27). Match-or-report."""
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Core_Papers")
report = []

def apply(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        report.append(f"MISS {label}: OLD not found in {path.name}")
        # help: show nearby
        needle = old[:60]
        idx = text.find(needle[:30]) if len(needle) > 30 else -1
        report.append(f"  needle30 idx={idx}")
        return
    count = text.count(old)
    if count != 1:
        report.append(f"AMBIG {label}: found {count} times in {path.name}")
        return
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    report.append(f"OK {label}")

def insert_after(path: Path, anchor: str, addition: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        report.append(f"SKIP {label}: already present")
        return
    if anchor not in text:
        report.append(f"MISS {label}: anchor not found")
        return
    # insert after the line containing anchor (full line)
    lines = text.splitlines(keepends=True)
    out = []
    done = False
    for line in lines:
        out.append(line)
        if (not done) and (anchor in line):
            # ensure addition ends with newline
            add = addition if addition.endswith("\n") else addition + "\n"
            out.append(add)
            done = True
    if not done:
        report.append(f"MISS {label}: anchor line not written")
        return
    path.write_text("".join(out), encoding="utf-8")
    report.append(f"OK {label}")

p1 = ROOT / "NTE_v10_19_0_Part1_Foundations.md"
p3 = ROOT / "NTE_v10_19_0_Part3_Accounting.md"

# --- Part 1 Item 1 abstract ---
apply(
    p1,
    r"The spectral index $n_s$ and tensor ratio $r$ are **conditional** on frame-closed $K(\Phi)$ from $\xi=1/6$ (Companion 17; $(n_s,r)=(0.9692,0.0053)$ at $N_e=63.4$) with Euclidean-section / $N_e$ / spectral-$\xi$ caveats — not claimed as fixed zero-parameter predictions.",
    r"Native values of the spectral index $n_s$ and tensor ratio $r$ from $\Phi_{\mathrm{NTE}}$ are **withdrawn** (Door B, 2026-09-26): $\Phi_{\mathrm{NTE}}$ is a relabelling of the expansion history, not an inflaton, and Companion 17 is retained as audit trail only. An accelerated epoch is required for the universe to exist at all, and the mechanism supplying it is **open** (Part 3, cosmological origin sector).",
    "P1-1-abstract",
)

# trailer — AC used escaped underscores in display; live text uses n_s/r
apply(
    p1,
    r"n_s/r conditional on frame-closed K(Φ), Companion 17;",
    r"native n_s/r withdrawn (Door B); Companion 17 audit trail only;",
    "P1-1-trailer",
)

# --- Part 1 Item 2 Schwarzschild ---
# live may use em-dash or ASCII hyphen-minus around "gravitational"
text = p1.read_text(encoding="utf-8")
old_schwarz_candidates = [
    r"Where $|\Phi|^2$ is reduced (a gravitational well), less proper time accrues per e-fold — gravitational time dilation as $|\Phi_{\mathrm{NTE}}|^2$ variation, recovering the Schwarzschild factor $\tau(x)/\tau(\infty) = 1 - GM/rc^2$ to first post-Newtonian order.",
    r"Where $|\Phi|^2$ is reduced (a gravitational well), less proper time accrues per e-fold - gravitational time dilation as $|\Phi_{\mathrm{NTE}}|^2$ variation, recovering the Schwarzschild factor $\tau(x)/\tau(\infty) = 1 - GM/rc^2$ to first post-Newtonian order.",
]
new_schwarz = r"Gravitational time dilation is **inherited (General Relativity)**, not derived here: $\beta_{\mathrm{NTE}}|\Phi(x)|^2$ is a local expansion rate, not the lapse $\sqrt{g_{00}}$ that sources the Schwarzschild factor — a bound well has no local Hubble flow. The framework recovers GR's result; it does not derive it. (Regraded 2026-09-27; see Part 3.)"
matched = False
for old in old_schwarz_candidates:
    if old in text:
        apply(p1, old, new_schwarz, "P1-2-schwarzschild")
        matched = True
        break
if not matched:
    # find by unique start and dump dash codepoint
    idx = text.find("Where $|\\Phi|^2$ is reduced")
    if idx < 0:
        report.append("MISS P1-2-schwarzschild: start not found")
    else:
        frag = text[idx : idx + 280]
        # locate char between e-fold and gravitational
        mid = frag.find("e-fold")
        report.append(f"MISS P1-2-schwarzschild: dash vicinity={frag[mid:mid+40]!r}")

# --- Part 1 Item 3 N-2 ---
apply(
    p1,
    r"(A structural identification, $\ell(N) = 1/(\beta_{\mathrm{NTE}}|\Phi|^2) = 1/H(N)$, makes the boundary's proper-length thickness and the Hubble radius the same object;",
    r"(The instantaneous proper-length thickness is $\ell(N) = 1/(\beta_{\mathrm{NTE}}|\Phi|^2) = 1/H(N)$, the Hubble radius — the **integrand** of the accumulated thickness above, not the integral. The two coincide only for constant $H$ and diverge in the de Sitter future, where $\ell \to$ const while $T \to \infty$; §V's reset trigger uses $\ell$.",
    "P1-3-N2",
)

# --- Part 1 Item 4 Z2 ---
apply(
    p1,
    r"The field carries a $\Phi \to -\Phi$ $Z_2$ symmetry (the constraint uses $|\Phi|^2$ throughout), which also fixes the leading allowed Higgs-portal coupling.",
    r"The constraint uses $|\Phi|^2$ throughout. (Earlier drafts read the resulting $\Phi \to -\Phi$ invariance as a $Z_2$ symmetry fixing a leading Higgs-portal coupling; both are withdrawn under Door B — the sign of a relabelling is not a symmetry, and the portal term was withdrawn from Companion 9 on 2026-09-27.)",
    "P1-4-Z2",
)

# --- Part 3 Item 1 flatness ---
apply(
    p3,
    r"Observed flatness is thus a consequence of the expansion history, not an assumption.",
    r"Why the observable patch is flat to present precision is **open**, pending the expansion history (see Open work — cosmological origin sector). The sign claim below is independent of it.",
    "P3-1-flatness",
)

# --- Part 3 Item 2 time dilation ---
apply(
    p3,
    r"$\sigma(\kappa;M) \propto M^{-1/2}$ (two-sector equations + CLT); gravitational time dilation (from $H(x,N)=\beta_{\mathrm{NTE}}|\Phi|^2$).",
    r"$\sigma(\kappa;M) \propto M^{-1/2}$ (two-sector equations + CLT).",
    "P3-2-dilation-cut",
)

# add to adopted/imported tier — after the Adopted header's first content block.
# AC: "add to the adopted/imported tier" with the bullet starting "- Gravitational time dilation"
adopted_bullet = (
    r"- Gravitational time dilation — **inherited (General Relativity)**. Previously graded derived "
    r'"from $H(x,N)=\beta_{\mathrm{NTE}}|\Phi|^2$"; withdrawn 2026-09-27. Under Door B, '
    r"$\beta_{\mathrm{NTE}}|\Phi(x)|^2$ is a local expansion rate, not the lapse $\sqrt{g_{00}}$ "
    r"that sources the Schwarzschild factor — a bound well has no local Hubble flow. "
    r"The framework recovers GR's result; it does not derive it."
)
# Place after Adopted header line
text3 = p3.read_text(encoding="utf-8")
anchor = "**Adopted from established external programmes (imported, credited — not NTE-derived).**"
if adopted_bullet in text3:
    report.append("SKIP P3-2-dilation-add: already present")
elif anchor not in text3:
    report.append("MISS P3-2-dilation-add: Adopted header not found")
else:
    # insert as first bullet under Adopted section (after blank line following header if any)
    lines = text3.splitlines(keepends=True)
    out = []
    done = False
    for i, line in enumerate(lines):
        out.append(line)
        if (not done) and (anchor in line):
            # if next line is blank, keep it then insert
            if i + 1 < len(lines) and lines[i + 1].strip() == "":
                pass  # blank will be appended on next iteration; insert after blank
            else:
                out.append(adopted_bullet + "\n")
                done = True
                continue
        if (not done) and i > 0 and anchor in lines[i - 1] and line.strip() == "":
            out.append(adopted_bullet + "\n")
            done = True
    if not done:
        # fallback: after header immediately
        out = []
        for line in lines:
            out.append(line)
            if (not done) and (anchor in line):
                out.append(adopted_bullet + "\n")
                done = True
    if done:
        p3.write_text("".join(out), encoding="utf-8")
        report.append("OK P3-2-dilation-add")
    else:
        report.append("MISS P3-2-dilation-add: failed insert")

# --- Part 3 Item 3 falsifier 11 ---
apply(
    p3,
    r"the e-fold run drives $|\Omega_k|$ toward values plausibly far below any achievable sensitivity, and curvature constraints are in any case degenerate with the dark-energy sector",
    r"$|\Omega_k|$ is expected to be far below any achievable sensitivity — though the expansion history that would establish this is itself open (see Open work) — and curvature constraints are in any case degenerate with the dark-energy sector",
    "P3-3-falsifier11",
)

out_path = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_apply_part1_part3_patch_registers_REPORT_20260927.txt")
out_path.write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
