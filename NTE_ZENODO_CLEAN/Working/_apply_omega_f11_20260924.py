#!/usr/bin/env python3
"""Apply AC Omega_k + T_GB + F11 ratified patches 20260924."""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
P1 = ROOT / "Core_Papers" / "NTE_v10_19_0_Part1_Foundations.md"
P3 = ROOT / "Core_Papers" / "NTE_v10_19_0_Part3_Accounting.md"
MAN = ROOT / "NTE_Workflow_Manifest_v10_18.md"
report = []

def once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        report.append(f"{label} FAIL: expected 1, got {n}")
        return text, False
    report.append(f"{label} OK")
    return text.replace(old, new, 1), True

# --- P3-Ω ---
p3 = P3.read_text(encoding="utf-8")
old = r"- Spatial flatness $\Omega_k = 0$ (boundary-only ontology); $w = -1$ (geometric-unloading de Sitter asymptote)."
new = (
    r"- Spatial flatness $\Omega_k \to 0$ — the $S^3$ is closed, and its radius after the e-fold run "
    r"is vast compared with the observable patch, so curvature is undetectable at every scale we can "
    r"probe (Planck 2018: $\Omega_k = 0.0007 \pm 0.0019$). Observed flatness is thus a consequence of "
    r"the expansion history, not an assumption. Exact $\Omega_k = 0$ is **not** claimed: a closed $S^3$ "
    r"of finite radius has $\Omega_k < 0$, and exact flatness would contradict the closure the boundary "
    r"ontology rests on. $w = -1$ (geometric-unloading de Sitter asymptote)."
)
p3, ok = once(p3, old, new, "P3-Ω")

# --- P1-Ω ---
p1 = P1.read_text(encoding="utf-8")
old = r"consistent with Part 3 carrying $H_0$, $w$, and $\Omega_k$ as construction/inherited rather than as new FRW dynamics"
new = r"consistent with Part 3 carrying $H_0$ as a consequence of construction, and $w$ and $\Omega_k \to 0$ as structural consequences of the boundary ontology, rather than as new FRW dynamics"
p1, ok = once(p1, old, new, "P1-Ω")

# --- Manifest ---
man = MAN.read_text(encoding="utf-8")

# Report §3 T_GB / Omega lines before
m_der = re.search(r"^\*\*Derived / structural\.\*\*[^\n]+", man, re.M)
m_cond = re.search(r"^\*\*Conditional — NOT fixed[^\n]+", man, re.M)
m_open = re.search(r"^\*\*Open\.\*\*[^\n]+", man, re.M)
report.append("--- MF §3 BEFORE ---")
for label, m in [("Derived", m_der), ("Conditional", m_cond), ("Open", m_open)]:
    report.append(f"{label} VERBATIM: {m.group(0) if m else 'NOT FOUND'}")

# MF-Ω: replace Ω_k = 0 in Derived line
if m_der and "Ω_k = 0" in m_der.group(0):
    old_bit = "Ω_k = 0"
    new_bit = (
        "Ω_k → 0 (closed S³; radius vast after the e-fold run — observed flatness predicted, "
        "not assumed; exact Ω_k = 0 not claimed, and would contradict closure)"
    )
    # only in Derived line
    start, end = m_der.start(), m_der.end()
    line = man[start:end]
    if line.count(old_bit) != 1:
        report.append(f"MF-Ω FAIL: Ω_k=0 count in Derived = {line.count(old_bit)}")
    else:
        man = man[:start] + line.replace(old_bit, new_bit, 1) + man[end:]
        report.append("MF-Ω OK")
else:
    report.append("MF-Ω FAIL: Derived line missing or no Ω_k = 0")

# MF-T: replace T_GB derived wording in Derived line
man_der2 = re.search(r"^\*\*Derived / structural\.\*\*[^\n]+", man, re.M)
old_t = (
    "**T_GB = M_Pl/√(2π)** — closed at the Hartle–Hawking Gaussian saddle-width (Companion 9), "
    "fibre-modulus identification β_GB·M_Pl = √(2π) from the spectral side (Companion 12); "
    "√(2π) is the Gaussian normalisation, not fitted."
)
new_t = (
    "T_GB = M_Pl/√(2π) — CONDITIONAL (2026-08). The Gaussian-width argument assumes a nucleation "
    "saddle of the constrained system; the raw-trace saddle is ruled out (Companion 9 addendum / "
    "Companion 15 §6.3). The Companion 12 fibre-modulus identification β_GB·M_Pl = √(2π) is the "
    "candidate independent grounding and is OPEN. Not graded unconditionally derived."
)
if man_der2 and old_t in man_der2.group(0):
    start, end = man_der2.start(), man_der2.end()
    line = man[start:end]
    man = man[:start] + line.replace(old_t, new_t, 1) + man[end:]
    report.append("MF-T OK")
elif "CONDITIONAL (2026-08). The Gaussian-width argument" in man:
    report.append("MF-T SKIP: already patched")
else:
    report.append("MF-T FAIL: OLD T_GB clause not found in Derived")
    # show snippet
    if man_der2:
        i = man_der2.group(0).find("T_GB")
        report.append(f"  T_GB context: {man_der2.group(0)[i:i+200]!r}")

# MF-R registrations
regs = """- **CLOSED 2026-09-24 — Ω_k register.** Part 3's derived entry claimed exact spatial flatness, which a closed S³ of finite radius cannot have. Corrected to Ω_k → 0 with the e-fold-run reasoning; Part 1 §2.3's account of Part 3's grading corrected with it (it mis-stated w and Ω_k as construction/inherited). Greg-ratified. No numbers change. Found by PC during the 2026-09-24 Book campaign (flag N1); Chapter 3 needed no change.
- **CLOSED 2026-09-24 — T_GB snapshot contradiction.** §3 graded T_GB derived and conditional simultaneously, citing Companion 12 both ways. Part 3 wins: conditional, fibre-modulus grounding open. Chapter 15 patches B1/B10 confirmed correct and released. Found by PC (flag F5).
"""
if "CLOSED 2026-09-24 — Ω_k register" in man:
    report.append("MF-R SKIP: already present")
else:
    man = man.replace("**In progress:**", "**In progress:**\n" + regs, 1)
    report.append("MF-R OK")

# --- P3-F11 ---
old11 = (
    r"10. **Mathematical.** $a_4 \neq 0$ for the untwisted Dirac operator on $S^3\times S^1$ "
    r"(would contradict CC 2008), or $C^2/E_4 \neq 0$ pointwise there, falsifies the spectral substrate claims."
)
new11 = old11 + (
    "\n11. **Spatial curvature sign.** The boundary ontology requires a closed $S^3$, so in the convention "
    r"$\Omega_k \equiv -kc^2/(a^2H^2)$ with $k=+1$, NTE requires $\Omega_k < 0$ **strictly**: exact flatness "
    "is excluded by the geometry, and an open universe is excluded outright. **A confirmed $\\Omega_k > 0$ "
    "at significance falsifies the framework**, and does so at the level of the ontology rather than of any "
    "single derivation — there is no closed-$S^3$ reading of an open universe. Current data are consistent "
    "and impose no tension: Planck 2018 gives $\\Omega_k = 0.0007 \\pm 0.0019$, with a marginally positive "
    "central value well within uncertainty of zero. Three honest qualifications. (i) The falsifier is "
    "**one-sided**: confirming $\\Omega_k < 0$ would not confirm NTE, since every closed-universe cosmology "
    "predicts the same sign. (ii) It is **not NTE-distinguishing** and does not join the three empirical "
    "handles above. (iii) NTE predicts the sign, **not the magnitude** — the e-fold run drives $|\\Omega_k|$ "
    "toward values plausibly far below any achievable sensitivity, and curvature constraints are in any case "
    "degenerate with the dark-energy sector, so this is a falsifier that may never fire in either direction. "
    "It is recorded because a framework should state what would refute it, including where refutation is "
    "unlikely to be reachable."
)
if "Spatial curvature sign" in p3:
    report.append("P3-F11 SKIP: already present")
else:
    p3, ok = once(p3, old11, new11, "P3-F11")

reg11 = (
    "- **CLOSED 2026-09-24 — falsifiability item 11 added (curvature sign).** NTE requires Ω_k < 0 "
    "strictly (closed S³); a confirmed Ω_k > 0 falsifies the ontology. Greg-ratified. Recorded with three "
    "qualifications: one-sided, not NTE-distinguishing, sign-only with magnitude plausibly unreachable. "
    "Arises from the Ω_k → 0 register correction of the same date.\n"
)
if "falsifiability item 11 added" in man:
    report.append("MF-11 SKIP")
else:
    man = man.replace("**In progress:**", "**In progress:**\n" + reg11, 1)
    report.append("MF-11 OK")

# After snapshot of three §3 lines
m_der = re.search(r"^\*\*Derived / structural\.\*\*[^\n]+", man, re.M)
m_cond = re.search(r"^\*\*Conditional — NOT fixed[^\n]+", man, re.M)
m_open = re.search(r"^\*\*Open\.\*\*[^\n]+", man, re.M)
report.append("--- MF §3 AFTER ---")
for label, m in [("Derived", m_der), ("Conditional", m_cond), ("Open", m_open)]:
    report.append(f"{label} VERBATIM: {m.group(0) if m else 'NOT FOUND'}")

man = re.sub(
    r"(\*\*Last updated\.\*\*\s*)([^\n]+)",
    lambda m: m.group(1)
    + "2026-09-24 — Ω_k→0 register; T_GB conditional in Derived; falsifiability item 11. Prior: "
    + m.group(2),
    man,
    count=1,
)

P1.write_text(p1, encoding="utf-8")
P3.write_text(p3, encoding="utf-8")
MAN.write_text(man, encoding="utf-8")
report.append("written P1 P3 MAN")
for line in report:
    print(line)
