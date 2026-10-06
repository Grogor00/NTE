# Greg 2026-09-25: apply all PROPOSED except N_e / (n_s,r) / Ch12 Note
from pathlib import Path
import json

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
log = []

def apply(src_name, dst_name, replacements, label):
    src = book / src_name
    t = src.read_text(encoding="utf-8")
    ok, miss, multi = [], [], []
    for i, (old, new) in enumerate(replacements, 1):
        c = t.count(old)
        if c == 0:
            miss.append(i)
            continue
        if c > 1:
            multi.append((i, c))
            continue
        t = t.replace(old, new)
        ok.append(i)
    dst = book / dst_name
    dst.write_text(t, encoding="utf-8")
    log.append({
        "label": label,
        "src": src_name,
        "dst": dst_name,
        "ok": ok,
        "miss": miss,
        "multi": multi,
        "bytes": dst.stat().st_size,
    })
    return t

# ----- AQ1-3 Ch8 -----
apply(
    "Chapter_08_The_Unresolved_Particle_v6.md",
    "Chapter_08_The_Unresolved_Particle_v7.md",
    [
        (
            "Light crosses the gap in zero proper time. Everything else waits for the expansion to catch up.",
            "Light crosses the gap with no ruler along it. Everything else waits for the expansion to catch up.",
        ),
        (
            "the photon at the pure null-time limit — no proper time, no mass, riding the expansion boundary.",
            "the photon at the pure null-time limit — no frame, no ruler along its own length, no mass, riding the expansion boundary.",
        ),
        (
            "The photon, with no engagement on either side, accumulates no proper time and rides the wavefront of expansion.",
            "The photon, with no engagement on either side, has no ruler along its own length and rides the wavefront of expansion.",
        ),
    ],
    "AQ1-AQ3",
)

# ----- AS1 Ch11 -----
apply(
    "Chapter_11_What_the_Universe_Sounds_Like_v4.md",
    "Chapter_11_What_the_Universe_Sounds_Like_v5.md",
    [
        (
            "the instrument's temporal circle tunes — set by the same single relation that fixes the circle's size — producing the temperature at which the universe's Standard Model physics first switched on.",
            "the instrument's temporal circle tunes — on the reading that the relation fixing the circle's size is the one the framework has identified, which is the open grounding here rather than a settled one — producing the temperature at which the universe's Standard Model physics first switched on. Chapter 12 grades it.",
        ),
    ],
    "AS1",
)

# ----- AT1-4 Ch14 (+ rename off DRAFT) -----
apply(
    "Chapter_14_Strange_Geometries_and_Structural_Rhymes_v2_2_DRAFT_PC_20260705.md",
    "Chapter_14_Strange_Geometries_and_Structural_Rhymes_v2_3.md",
    [
        (
            "Proper time accumulates with expansion through |Φ_NTE|;",
            "Cosmic time accumulates with expansion through |Φ_NTE|;",
        ),
        (
            "through the one species whose unfinished identity spans it.",
            "— registering through the one species whose identity the projection left unfinished, which is the structure the coupling shows up in rather than the thing that carries it.",
        ),
        (
            "Notice a pattern running through the chapter.",
            "Notice a pattern running through the book.",
        ),
        (
            "what a honest probability function",
            "what an honest probability function",
        ),
    ],
    "AT1-AT4+AU3_rename",
)

# ----- T1-T2 Ch9 (T3 careful - skip n_s/r value edits; tier label OK) -----
apply(
    "Chapter_09_The_Number_That_Could_Have_Failed_v5.md",
    "Chapter_09_The_Number_That_Could_Have_Failed_v6.md",
    [
        (
            "Standard Model gauge symmetries switched on and proper time crystallised — the universe locked",
            "Standard Model gauge symmetries switched on and cosmic time crystallised — the universe locked",
        ),
        (
            "The difference is 0.12, which is about 0.83 standard deviations",
            "The difference is about 0.13 — the unrounded prediction is 5.505 — which is about 0.83 standard deviations",
        ),
    ],
    "T1-T2",
)

# ----- AF3 AppC -----
apply(
    "Appendix_C_The_Open_Ledger_v1_6_DRAFT_PC_20260925.md",
    "Appendix_C_The_Open_Ledger_v1_7.md",
    [
        (
            "Until it closes, the temperature is conditional, and Chapter 12 says so.",
            "Until it closes, the temperature is conditional, and the scorecard of Chapter 15 carries it that way.",
        ),
    ],
    "AF3+AU3_AppC_rename",
)

# ----- AG1-AG6 Ch17 -----
apply(
    "Chapter_17_The_Working_Bet_v3.md",
    "Chapter_17_The_Working_Bet_v4.md",
    [
        (
            "a photon accumulates zero proper time between emission and absorption.",
            "between a photon's emission and its absorption there is no interval to divide, and no vantage from which to divide it. The line has no ruler along it.",
        ),
        (
            "quantum mechanics as state-space geometry with the Born rule a theorem, not an axiom;",
            "quantum mechanics as state-space geometry, with the Born rule reformulated rather than assumed;",
        ),
        (
            "proper time emerges via H = β_NTE|Φ_NTE|².",
            "cosmic time is that expansion counted, at the rate H = β_NTE|Φ_NTE|² sets.",
        ),
        (
            "the kinetic normalisation K(Φ) that would convert the inflationary pair into hard tests;",
            "the spectral origin of the conformal coupling that would convert the inflationary pair into hard tests — the kinetic normalisation it took to get there is closed, and what is open now sits one level beneath it;",
        ),
        (
            "with the notes graded, one removed by the framework's own accounting, one promoted when its derivation closed.",
            "with the notes graded, one removed by the framework's own accounting, and one promoted when its derivation closed and then demoted again when the argument under it was found to rest on a truncation artefact — a tally that is allowed to shrink.",
        ),
        (
            "Massive matter accumulates proper time; the photon does not; the neutrino almost does not.",
            "Matter with rest energy accumulates duration; the photon, having none, takes no part in it; the neutrino, with barely any, barely does.",
        ),
    ],
    "AG1-AG6",
)

# ----- AD1-AD2 Ch16 only (skip AD3/AD4 n_s r) -----
apply(
    "Chapter_16_Stranger_and_Stranger_v2.md",
    "Chapter_16_Stranger_and_Stranger_v3.md",
    [
        ("## Toward the Score", "## Permission, Not Proof"),
        (
            "The photon does not accumulate proper time along its own path.",
            "The photon's line has no ruler along it and nothing on it to count.",
        ),
    ],
    "AD1-AD2",
)

# ----- AC coherence length -> coherence mass (Ch10); drop forty megaparsecs phrase -----
# Only replace 'coherence length' globally in Ch10 if safe; also forty megaparsecs
src = book / "Chapter_10_The_Silvered_Boundary_v9.md"
t = src.read_text(encoding="utf-8")
n_cl = t.count("coherence length")
n_fm = t.count("forty megaparsecs")
t2 = t.replace("coherence length", "coherence mass")
# soften remaining megaparsec claim if present
if "near forty megaparsecs" in t2:
    t2 = t2.replace("near forty megaparsecs", "at the coherence mass")
elif "forty megaparsecs" in t2:
    t2 = t2.replace("forty megaparsecs", "the coherence mass")
dst = book / "Chapter_10_The_Silvered_Boundary_v10.md"
dst.write_text(t2, encoding="utf-8")
log.append({
    "label": "AC1-AC3_coherence_mass",
    "src": src.name,
    "dst": dst.name,
    "ok": [f"coherence length x{n_cl}", f"forty megaparsecs x{n_fm}"],
    "miss": [],
    "multi": [],
    "bytes": dst.stat().st_size,
})

# ----- Q1 Ch13 mass units (micrograms); photon ruler if present -----
apply(
    "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md",
    "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v7.md",
    [
        (
            "about a tenth of a milligram",
            "about twenty-two micrograms",
        ),
        (
            "photon's zero proper time",
            "photon's null path — no ruler along it",
        ),
    ],
    "Q1-Q4partial",
)

out = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_greg_batch_apply_20260925.json")
out.write_text(json.dumps(log, indent=2), encoding="utf-8")
# also human summary
lines = []
for e in log:
    lines.append(f"{e['label']}: ok={e['ok']} miss={e['miss']} multi={e['multi']} -> {e['dst']}")
Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_greg_batch_apply_20260925.txt").write_text(
    "\n".join(lines), encoding="utf-8"
)
print("\n".join(lines))
