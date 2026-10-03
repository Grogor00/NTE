from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
handoff = Path(
    r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Handoffs\Handoff_Cursor_to_PC_Emergence_Register_Grep_20260921.md"
)

current = [
    "Prelude_The_Forty_Million_Year_Instant_v7.md",
    "Chapter_01_The_Photons_Journey_v10.md",
    "Chapter_02_Entanglement_as_Geometry_v7.md",
    "Chapter_03_A_Closed_Universe_v6_1.md",
    "Chapter_04_Time_as_Expansion_v8.md",
    "Chapter_05_The_Eighth_Colour_v7.md",
    "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6.md",
    "Chapter_07_The_Gauge_Birth_v4.md",
    "Chapter_08_The_Unresolved_Particle_v5.md",
    "Chapter_09_The_Number_That_Could_Have_Failed_v4.md",
    "Chapter_10_The_Silvered_Boundary_v7.md",
    "Chapter_11_What_the_Universe_Sounds_Like_v4.md",
    "Chapter_12_The_Chord_v4_1.md",
    "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md",
    "Chapter_14_Strange_Geometries_and_Structural_Rhymes_v2_2_DRAFT_PC_20260705.md",
    "Chapter_15_The_Score_v3.md",
    "Chapter_16_Stranger_and_Stranger_v2.md",
    "Chapter_17_The_Working_Bet_v3.md",
    "Appendix_A_Popular_Reader_Edition_v10_19_0.md",
    "Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md",
]

g1 = re.compile(r"\bemerg(?:e|es|ed|ent|ence)\b", re.I)
g2_phrases = [
    re.compile(r"time comes from", re.I),
    re.compile(r"produces time", re.I),
    re.compile(r"generates time", re.I),
    re.compile(r"generating time", re.I),
    re.compile(r"produce \*t\*", re.I),
    re.compile(r"produces \*t\*", re.I),
]
g3 = re.compile(r"\barises from\b", re.I)
time_near = re.compile(r"\btime\b|\*t\*", re.I)
g4_before = re.compile(r"\bbefore\b", re.I)
g4_cues = re.compile(
    r"time|temporal|epoch|beginning|expansion|universe|big bang|gauge.?birth|inflation|manifold",
    re.I,
)
g5 = re.compile(r"Non-Temporal Emergence", re.I)


def words_within(text: str, pos: int, window: int = 20) -> str:
    words = list(re.finditer(r"\S+", text))
    idx = None
    for i, m in enumerate(words):
        if m.start() <= pos < m.end():
            idx = i
            break
        if m.start() > pos:
            idx = max(0, i - 1)
            break
    if idx is None:
        idx = max(0, len(words) - 1)
    lo = max(0, idx - window)
    hi = min(len(words), idx + window + 1)
    return " ".join(w.group() for w in words[lo:hi])


def classify_context(line: str, prev: str, nxt: str) -> list[str]:
    blob = f"{prev} {line} {nxt}".lower()
    marks: list[str] = []
    if any(
        x in blob
        for x in [
            '"',
            "\u201c",
            "\u201d",
            "quote",
            "said",
            "wrote",
            "first framed",
            "originally",
            "once thought",
            "historical",
            "we used to",
            "earlier draft",
            "withdrawn",
        ]
    ):
        marks.append("possible quote/history")
    if "non-temporal emergence" in blob:
        marks.append("framework name")
    if "time is emergent" in blob or ("#" in line and "emergent" in line.lower()):
        marks.append("title/structural")
    return marks


results = []
totals = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for name in current:
    path = book / name
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    file_hits: dict[int, list] = {1: [], 2: [], 3: [], 4: [], 5: []}

    for i, line in enumerate(lines):
        prev = lines[i - 1] if i > 0 else ""
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        ln = i + 1

        for m in g1.finditer(line):
            file_hits[1].append(
                (ln, m.group(), line, prev, nxt, classify_context(line, prev, nxt))
            )

        for pat in g2_phrases:
            for m in pat.finditer(line):
                file_hits[2].append(
                    (ln, m.group(), line, prev, nxt, classify_context(line, prev, nxt))
                )

        for m in g3.finditer(line):
            joined = prev + " " + line + " " + nxt
            pos = joined.lower().find("arises from")
            local = words_within(joined, pos if pos >= 0 else 0)
            if time_near.search(local):
                file_hits[3].append(
                    (ln, m.group(), line, prev, nxt, classify_context(line, prev, nxt))
                )

        if g4_before.search(line):
            blob = f"{prev} {line} {nxt}"
            if g4_cues.search(blob):
                file_hits[4].append(
                    (ln, "before", line, prev, nxt, classify_context(line, prev, nxt))
                )

        for m in g5.finditer(line):
            file_hits[5].append((ln, m.group(), line, prev, nxt, ["framework name"]))

    counts = {k: len(v) for k, v in file_hits.items()}
    for k, v in counts.items():
        totals[k] += v
    results.append((name, counts, file_hits))

out: list[str] = []
out.append("# Handoff — Cursor → PC: Emergence-register grep (read-only)")
out.append("")
out.append(
    "**From:** Cursor · **To:** Claude_PC · **Cc:** Greg, AC · **Date:** 2026-09-21"
)
out.append(
    "**Re:** `Handoff_PC_to_Cursor_Emergence_Register_Grep_ReadOnly_20260921.md`"
)
out.append("**Status:** Complete — read-only; no edits.")
out.append(
    "**Scope:** Current Book versions only (Prelude v7, Ch1 v10, Ch2–17 latest, App A, App C). "
    "Skipped superseded Ch1 v8/v9, Prelude v6, App B, Zenodo registers, `paper-build/`."
)
out.append("")
out.append("---")
out.append("")
out.append("## Totals (all files)")
out.append("")
out.append("| Group | Hits |")
out.append("|-------|------|")
out.append(f"| 1 emerge* | {totals[1]} |")
out.append(
    f"| 2 time-comes-from / produces-time / generates-time / produce *t* | {totals[2]} |"
)
out.append(f"| 3 arises from near time/*t* | {totals[3]} |")
out.append(f"| 4 before + pre-temporal cues (heuristic) | {totals[4]} |")
out.append(f"| 5 Non-Temporal Emergence (count only) | {totals[5]} |")
out.append("")
out.append("---")
out.append("")

for name, counts, file_hits in results:
    out.append(f"## `{name}`")
    out.append("")
    out.append(
        f"Counts: G1={counts[1]} · G2={counts[2]} · G3={counts[3]} · G4={counts[4]} · G5={counts[5]}"
    )
    out.append("")
    if sum(counts.values()) == 0:
        out.append("*No hits.*")
        out.append("")
        continue
    for g in (1, 2, 3, 4, 5):
        for ln, term, line, prev, nxt, marks in file_hits[g]:
            mark = f" · **[{'; '.join(marks)}]**" if marks else ""
            out.append(f"### G{g} · L{ln} · `{term}`{mark}")
            out.append("```")
            if prev:
                out.append(f"{ln - 1}| {prev}")
            out.append(f"{ln}| {line}")
            if nxt:
                out.append(f"{ln + 1}| {nxt}")
            out.append("```")
            out.append("")
    out.append("")

out.append("---")
out.append("")
out.append("## Notes for PC")
out.append("")
out.append(
    "- G4 is heuristic (`before` + nearby temporal/epoch cues); expect false positives in ordinary narrative sequencing."
)
out.append("- G5 is framework-name only — not a patch target per handoff.")
out.append(
    "- Assertion vs quotation marks are best-effort; verify strong hits in context before drafting."
)
out.append("")
out.append("— Cursor, 2026-09-21.")
out.append("")

handoff.write_text("\n".join(out), encoding="utf-8", newline="\n")
print("wrote", handoff)
print("totals", totals)
for name, counts, _ in results:
    s = sum(counts.values())
    if s:
        print(
            f"{s:3} {name}  G1={counts[1]} G2={counts[2]} G3={counts[3]} G4={counts[4]} G5={counts[5]}"
        )
