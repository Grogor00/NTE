# -*- coding: utf-8 -*-
"""Apply Greg-ratified 2026-09-25 Book patches (Cursor Main)."""
from pathlib import Path
import shutil

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
report = []


def apply_once(path: Path, old: str, new: str, pid: str) -> bool:
    t = path.read_text(encoding="utf-8")
    n = t.count(old)
    if n == 1:
        path.write_text(t.replace(old, new, 1), encoding="utf-8")
        report.append(f"{pid}: APPLIED ({path.name})")
        return True
    report.append(f"{pid}: FAIL count={n} ({path.name})")
    # write a short old preview for debug
    if n == 0 and len(old) > 40:
        report.append(f"  preview: {old[:80]!r}")
    return False


def bump(src_name: str, dst_name: str) -> Path:
    src = book / src_name
    dst = book / dst_name
    shutil.copy2(src, dst)
    return dst


def replace_span(path: Path, start_marker: str, end_marker: str, new: str, pid: str, include_end=True) -> bool:
    t = path.read_text(encoding="utf-8")
    i = t.find(start_marker)
    if i < 0:
        report.append(f"{pid}: FAIL start marker")
        return False
    j = t.find(end_marker, i)
    if j < 0:
        report.append(f"{pid}: FAIL end marker")
        return False
    if include_end:
        j += len(end_marker)
    old = t[i:j]
    return apply_once(path, old, new, pid)


# ---- Ch10 v8 -> v9 ----
ch10 = bump("Chapter_10_The_Silvered_Boundary_v8.md", "Chapter_10_The_Silvered_Boundary_v9.md")
t = ch10.read_text(encoding="utf-8")

i = t.find("above roughly 4")
if i >= 0:
    j = t.find(".", i) + 1
    old = t[i:j]
    new = (
        "above it, a system is large enough to average over many independent patches of the coupling; below it, it is not. "
        "The mass itself is around four hundred trillion suns — but that figure is not a constant of the theory, and the next paragraph says why."
    )
    apply_once(ch10, old, new, "AC4")
else:
    report.append("AC4: FAIL locate")

t = ch10.read_text(encoding="utf-8")
# AC5: from "One caveat travels" through end of that paragraph block
start = t.find("One caveat travels with this")
if start < 0:
    report.append("AC5: FAIL locate start")
else:
    end = t.find("not how large it is at the bottom.", start)
    if end < 0:
        report.append("AC5: FAIL locate end")
    else:
        end = end + len("not how large it is at the bottom.")
        old = t[start:end]
        new = (
            "Three caveats travel with that figure, and the framework states them rather than leaving them implicit. "
            "The free-streaming scale is standard neutrino physics, not an NTE derivation; what is the framework's own is the *combination* — "
            "this scaling law, around this particular mean of 5.50, with the transition at this scale. "
            "The *size* of the scatter within a single coherence patch is not predicted at all, and the corpus carries that amplitude as open: "
            "the framework predicts that the scatter is there and how it falls away with mass, not how large it is at the bottom. "
            "And the threshold is not a fixed number. Free-streaming scales inversely with the neutrino's mass, so the coherence mass moves as the neutrino mass moves, "
            "and the neutrino mass is not something the framework has pinned. Four hundred trillion suns is the value at a standard reference mass, not a constant the geometry hands down. "
            "A reader should hold it as an order of magnitude with a dial attached, and the surveys that test the transition will have to be read against whatever the neutrino mass turns out to be."
        )
        apply_once(ch10, old, new, "AC5")

t = ch10.read_text(encoding="utf-8")
i = t.find("above the coherence mass, around 4")
if i >= 0:
    j = t.find(".", i) + 1
    old = t[i:j]
    new = "above the coherence mass — cluster-scale, and moving with the neutrino mass as §5 described."
    apply_once(ch10, old, new, "AC6")
else:
    report.append("AC6: FAIL locate")

t = ch10.read_text(encoding="utf-8")
i = t.find("They are not two parallel realities")
if i >= 0:
    end = t.find("separate fiction.", i)
    if end >= 0:
        old = t[i : end + len("separate fiction.")]
    else:
        old = t[i : t.find(".", i) + 1]
    new = (
        "They are not two parallel realities in the science-fiction sense — no alternate version of the reader who took a different career lives in the other orientation. "
        "But they are two, and both are real: the framework's own structure requires it, because a mirror that were merely our own sector counted twice would supply no extra matter for the dark-matter ratio to measure."
    )
    apply_once(ch10, old, new, "AL1")
else:
    report.append("AL1: FAIL locate")

# ---- Ch15 ----
ch15 = bump("Chapter_15_The_Score_v5.md", "Chapter_15_The_Score_v6.md")
t = ch15.read_text(encoding="utf-8")
i = t.find("Chapter 10's companion claim:")
if i < 0:
    i = t.find("Chapter 10")
# find coherence mass claim
k = t.find("coherence mass of around 4")
if k >= 0:
    start = t.rfind(".", 0, k) + 1
    while start < len(t) and t[start] in " \n":
        start += 1
    end = t.find(".", k) + 1
    old = t[start:end]
    new = (
        "Chapter 10's companion claim: the transition to tight convergence above the neutrino free-streaming coherence mass, which is cluster-scale — of order 10¹⁴ solar masses — and which the framework adopts rather than derives. "
        "It is also not a fixed threshold: free-streaming scales inversely with the neutrino mass, so the transition moves with a quantity the framework has not pinned. "
        "What the framework claims is the combination of that scale with the scaling law and the mean, not the scale itself."
    )
    apply_once(ch15, old, new, "AK1")
else:
    report.append("AK1: FAIL locate")

# ---- Appendix C ----
appc_src = "Appendix_C_The_Open_Ledger_v1_4_DRAFT_PC_20260924.md"
appc = bump(appc_src, "Appendix_C_The_Open_Ledger_v1_5_DRAFT_PC_20260925.md")  # noqa: filename confirmed
t = appc.read_text(encoding="utf-8")
i = t.find("**Rubin Observatory and Euclid**")
if i >= 0:
    # to next blank line or next ** heading
    j = t.find("\n\n", i)
    old = t[i:j]
    new = (
        "**Rubin Observatory and Euclid** — the transition in the dark-matter-fraction scatter at the neutrino free-streaming coherence mass, mapped across hundreds of millions of systems; "
        "and the void anatomy of the Hubble tension (framework: directional scatter of 2–4 km/s/Mpc correlated with line-of-sight density). "
        "Two honest qualifications on the transition. The free-streaming scale is standard neutrino physics rather than an NTE derivation — what the framework claims is its combination with the M^(−1/2) scaling and the mean of 5.50, "
        "and the scatter's amplitude within a single coherence patch is carried as open. And the threshold is not fixed: free-streaming scales inversely with the neutrino mass, "
        "so the transition sits at a cluster-scale mass of order 10¹⁴ suns for a standard reference neutrino mass and moves as that mass moves. "
        "A survey result on the transition has to be read against whichever neutrino mass turns out to be right."
    )
    apply_once(appc, old, new, "AF2'")
else:
    report.append("AF2': FAIL locate")

# ---- Ch12 ----
ch12 = bump("Chapter_12_The_Chord_v4_1.md", "Chapter_12_The_Chord_v4_2a.md")
t = ch12.read_text(encoding="utf-8")
i = t.find("A word on the register")
if i >= 0:
    end = t.find("\n\n", i)
    old = t[i:end]
    new = (
        "A word on the register, because the book grades every note — and this note's grade has moved twice, which makes it the chapter's best worked example of grading. "
        "The bare coupling sits in the framework's derived tier. The gauge-birth temperature does not. "
        "For a period of the framework's development it did: its derivation was taken to have closed through the width of the saddle at which the Lorentzian universe is born, and it was promoted. "
        "Then the argument underneath was examined directly and the saddle it assumed turned out not to be there — an artefact of where the expansion had been cut off — and the note was demoted again, to a cross-check held at conditional register. "
        "A candidate route to grounding it independently remains open, through a modulus of the framework's fibre geometry, and until that closes the temperature is conditional.\n\n"
        "So the first and second notes do not match at register, and the chapter should not pretend otherwise. "
        "Of the results the chord sounds cleanly, two stand at the derived tier: the bare coupling and the volume signature a later section develops. "
        "That is a thinner spine than the framework carried a year ago, and the thinning was the framework's own doing."
    )
    apply_once(ch12, old, new, "AJ1")
else:
    report.append("AJ1: FAIL locate")

t = ch12.read_text(encoding="utf-8")
core = "the size of the temporal circle itself is fixed"
i = t.find(core)
if i >= 0:
    # sentence containing this — start after previous period
    start = t.rfind(".", 0, i) + 1
    while start < len(t) and t[start] in " \n":
        start += 1
    # end before "When the mode" if present else period
    end2 = t.find("When the mode", i)
    if end2 < 0:
        end2 = t.find(".", i) + 1
    old = t[start:end2].rstrip()
    new = (
        'In the framework\'s committed geometry the relation is meant to be tighter than an analogy: the size of the temporal circle and the temperature of the gauge birth would be one statement rather than two, joined by this single √(2π) relation. '
        "That identification is the framework's proposal and it is not yet established — it is the candidate grounding named above, and it is the open item on which the note's register turns. "
        "If it closes, the two statements become one and the note is derived. Until then the chapter states it as what it is: an identification the framework has made and not yet earned. "
    )
    apply_once(ch12, old, new, "AJ2")
else:
    report.append("AJ2: FAIL locate")

t = ch12.read_text(encoding="utf-8")
i = t.find("If the saddle-width derivation behind the gauge-birth temperature fails")
if i >= 0:
    end = t.find("\n\n", i)
    old = t[i:end]
    new = (
        "The gauge-birth temperature has already had one audit go against it — the saddle the width argument assumed was found not to exist, which is why the note sits at conditional rather than derived. "
        "What remains at risk is the surviving route: if the fibre-modulus identification fails to close, or closes on something other than the Planck mass over the square root of 2π, the second note does not recover, "
        "and the single relation that would have fixed the temporal circle goes with it."
    )
    apply_once(ch12, old, new, "AJ3")
else:
    report.append("AJ3: FAIL locate")

t = ch12.read_text(encoding="utf-8")
i = t.find("And the count was never the point.")
if i >= 0:
    end = t.find("\n\n", i)
    old = t[i:end]
    new = (
        "And the count was never the point. The framework commits to the chord — the joint sound the instrument makes — not to a tally of notes, "
        "and the tally has changed as the mathematics matured: one note removed by the framework's own accounting, another promoted to the derived tier and then demoted again when the argument under it was found to rest on a truncation artefact, "
        "perhaps others still to be identified as the work continues. A tally that only ever grows is a sales figure."
    )
    apply_once(ch12, old, new, "AJ4")
else:
    report.append("AJ4: FAIL locate")

# ---- Ch3 ----
ch3 = bump("Chapter_03_A_Closed_Universe_v7.md", "Chapter_03_A_Closed_Universe_v8.md")
t = ch3.read_text(encoding="utf-8")
old = "has long since passed beyond our Hubble horizon"
new = "lies far beyond the **cosmological event horizon** — the bound introduced above, and the one that actually applies"
if old in t:
    apply_once(ch3, old, new, "AN1")
else:
    report.append("AN1: FAIL locate")

t = ch3.read_text(encoding="utf-8")
old = "as the one species whose unfinished identity spans the thickness"
new = (
    "— not carrying the coupling, not mediating it, but being the structure that makes it show up in the equations describing what we measure —"
)
if old in t:
    apply_once(ch3, old, new, "AN2")
else:
    report.append("AN2: FAIL locate")

t = ch3.read_text(encoding="utf-8")
marker = "is a story for the chapters that develop it carefully."
if marker in t and "not a bookkeeping device" not in t:
    insert = (
        marker
        + " The other side is not a bookkeeping device, and not our own matter counted twice. "
        "It is real, with its own matter, gravitating in its own right — which is exactly why there is something for the ratio κ to measure."
    )
    apply_once(ch3, marker, insert, "AN3")
else:
    report.append("AN3: SKIP/FAIL")

# Ch3 greps
t = ch3.read_text(encoding="utf-8").lower()
for term in ["redundan", "bookkeeping", "counted twice", "same universe", "gauge choice", "not real", "one sector"]:
    report.append(f"Ch3-grep {term}={t.count(term)}")

# ---- Ch6 AO7 ----
ch6 = bump(
    "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6.md",
    "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6_1.md",
)
t = ch6.read_text(encoding="utf-8")
old = "gives well-defined proper time"
new = "gives well-defined cosmic time"
if old in t:
    apply_once(ch6, old, new, "AO7")
else:
    # try broader
    i = t.find("proper time")
    report.append(f"AO7: FAIL exact; proper time at {i}")
    if i >= 0:
        report.append(repr(t[max(0, i - 60) : i + 40]))

out = Path(r"C:\Users\gregw\Desktop\NTE v10_6\Workflow\_cursor_apply_report_20260925.txt")
out.write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
