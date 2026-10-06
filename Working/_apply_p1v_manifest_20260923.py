#!/usr/bin/env python3
"""Apply Part1 §V + manifest repairs from AC handoff 20260923."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN")
P1 = ROOT / "Core_Papers" / "NTE_v10_19_0_Part1_Foundations.md"
MAN = ROOT / "NTE_Workflow_Manifest_v10_18.md"

report = []

# --- P1V ---
p1 = P1.read_text(encoding="utf-8")
old_raw = "($n_\\gamma V_H = 1$)"
new_raw = (
    "($n_\\gamma V_H = 1$, with $V_H \\equiv R_H^3 = (c/H_{\\mathrm{dS}})^3$ — "
    "one photon per Hubble cube; the $\\mathcal{O}(1)$ geometric factor is a "
    "convention of the order-of-magnitude trigger)"
)
n = p1.count(old_raw)
if n != 1:
    report.append(f"P1V FAIL: expected 1 match, got {n}")
    i = p1.find("n_\\gamma V_H")
    report.append(f"  context: {p1[i-10:i+50]!r}" if i >= 0 else "  not found")
else:
    p1 = p1.replace(old_raw, new_raw, 1)
    P1.write_text(p1, encoding="utf-8")
    report.append("P1V OK")

# verifies / N_gamma exact claim — report only
verifies_hits = []
for m in re.finditer(r".{0,40}(1\.00000000|verifies\s+N[^\n.]{0,40}).{0,40}", p1, re.I):
    verifies_hits.append(m.group(0).strip())
if verifies_hits:
    report.append("VERIFIES LINE(S) PRESENT — not patched:")
    for h in verifies_hits:
        report.append(f"  VERBATIM: {h}")
else:
    report.append("VERIFIES LINE: none in Part 1 (no N_γ=1.00000000 / verifies claim in §V)")

# --- Manifest ---
man = MAN.read_text(encoding="utf-8")

# MF-1
if re.search(r"^10\.\s+\*\*A draft that is not registered", man, re.M):
    report.append("MF-1 SKIP: discipline 10 already present")
elif re.search(r"^10\.\s+\*\*", man, re.M):
    report.append("MF-1 SKIP: some discipline 10 already present — report only")
    m = re.search(r"^10\.\s+\*\*[^\n]+", man, re.M)
    report.append(f"  existing: {m.group(0)[:160]}")
else:
    m = re.search(
        r"^9\.\s+\*\*Address everything by name and path — never by Drive ID\. NON-NEGOTIABLE\.\*\*[^\n]*",
        man,
        re.M,
    )
    if not m:
        report.append("MF-1 FAIL: item 9 not found")
    else:
        insert = (
            "\n10. **A draft that is not registered does not exist.** Any stream delivering a draft — "
            "PC chapters and appendices, Scratch and Jammer verdicts included — registers it in §10 as "
            "part of its own delivery, with filename, date and status. Registration is the deliverer's "
            "job, not something AC is expected to notice. Two 2026 failures trace to this: Chapter 12 "
            "v4.1 (drafted 2026-07-04, unratified until 2026-09-18) and Appendix C v1.3 (drafted "
            "2026-08-04, invisible to the Book bring-up brief written to find it)."
        )
        man = man[: m.end()] + insert + man[m.end() :]
        report.append("MF-1 OK: discipline 10 inserted after item 9")

# MF-2
old_sentence = (
    "Claude cannot edit in place, delete, move, or rename — Greg via the Drive UI."
)
m2 = re.search(r"^- \*\*File ops \(drive\.file scope\):[^\n]*\n", man, re.M)
if m2:
    report.append(f"MF-2 OLD bullet VERBATIM: {man[m2.start():m2.end()].rstrip()}")
else:
    report.append("MF-2: File ops bullet not found; searching sentence")
if old_sentence in man:
    report.append(f"MF-2 OLD sentence VERBATIM: {old_sentence}")
    new_bullet = (
        "- **Claude can edit, delete, rename and move corpus files** — by authoring a Cursor "
        "instruction (OLD/NEW patch blocks or an explicit directive), which Cursor executes on the "
        "local synced tree and which propagates to Drive. Drive-connector create/copy is the "
        "direct-write path; Cursor is the path for in-place edits, deletes, renames and moves. A "
        "failed retrieval is stale search or duplicate-name churn — diagnose and route around it; "
        "never report it as missing capability.\n"
    )
    if m2:
        man = man[: m2.start()] + new_bullet + man[m2.end() :]
        report.append("MF-2 OK: replaced File ops bullet")
    else:
        report.append("MF-2 FAIL: had sentence but no File ops bullet match")
else:
    if "Claude can edit, delete, rename and move corpus files" in man:
        report.append("MF-2 SKIP: already corrected")
    else:
        report.append("MF-2 FAIL: OLD sentence not found")

# MF-3
block = """- **CLOSED 2026-09-23 — S1 (λ/R_H 0.625 vs 3.92).** Not a contradiction: ħ vs h on the same relation, differing by exactly 2π (0.6245 and 3.9240). Neither is a typical photon wavelength (Wien peak 0.79 R_H); the honest statement is λ ∼ R_H, which canonical Part 1 already gives. No archive sweep needed. Verdict: `Working\\S1_VERDICT_lambda_RH_0p625_vs_3p92_SAME_RELATION_hbar_vs_h_BOTH_on_R3_not_4pi3_Jammer_20260923.md`. C21 §5 unblocked.
- **CLOSED 2026-09-23 — Part 1 §V trigger-volume convention.** Greg ratified remedy (a): V_H ≡ R_H³ stated explicitly; all numbers unchanged. The alternative (4π/3, moving T_reset to 1.38 × 10⁻²⁹ K and N_total by 0.48 e-folds) was declined.
- **DELIVERED 2026-09-23 — S3 (GATE4C vs the August idempotent correction).** Jammer verdict + Scratch complex-Majorana confirmation, both filed in `Working\\`. Outcome: both prior positions made the same category error in opposite directions; the fork is one free breaking ratio t in the μ–τ-odd term (t = 0 → TM1, t = 3/2 → TM2, t unfixed by J₃(𝕆)). GATE4C's \"TM1 not delivered\" survives; its \"no generation-1 mechanism\" and \"TM2 = genuine prediction 0.341\" are withdrawn. The August \"traceless(E₁) = TM1 column\" is withdrawn — **it appears in no deposited file, so no corpus patch is required.** AC arbitration: `Handoff_AC_to_PC_Scratch_Jammer_S3_Arbitration_20260923.md`.
"""
if "Part 1 §V trigger-volume convention" in man:
    report.append("MF-3 SKIP: §V registration already present")
else:
    man = man.replace("**In progress:**", "**In progress:**\n" + block, 1)
    report.append("MF-3 OK: S1 / §V / S3 registered")

man = re.sub(
    r"(\*\*Last updated\.\*\*\s*)([^\n]+)",
    lambda m: m.group(1)
    + "2026-09-23 — Part1 §V V_H≡R_H³; discipline 10; Claude file-ops correction; S1/S3/§V closed. Prior: "
    + m.group(2),
    man,
    count=1,
)
MAN.write_text(man, encoding="utf-8")
report.append("manifest written")

for line in report:
    print(line)
