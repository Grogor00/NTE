from pathlib import Path
book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
log = []

def bump(path_name, pairs, label):
    p = book / path_name
    t = p.read_text(encoding="utf-8")
    ok, miss = [], []
    for i, (o, n) in enumerate(pairs, 1):
        c = t.count(o)
        if c != 1:
            miss.append((i, c))
            continue
        t = t.replace(o, n)
        ok.append(i)
    p.write_text(t, encoding="utf-8")
    log.append(f"{label}: ok={ok} miss={miss}")

bump(
    "Chapter_09_The_Number_That_Could_Have_Failed_v6.md",
    [
        (
            "the dark-matter-to-baryon ratio joins the maximal CP phase and the maximal atmospheric angle in the strictest zero-parameter tier, with the spectral index and tensor ratio carried as conditional, the mass scales as cross-checks, and the framework's live",
            "the dark-matter-to-baryon ratio joins — as the framework's own claim, not a borrowed one — the maximal atmospheric angle, with the maximal CP phase carried as sign-free, in the strictest zero-parameter tier, with the spectral index and tensor ratio carried as conditional, the mass scales as cross-checks, and the framework's live",
        )
    ],
    "T3",
)

bump(
    "Chapter_17_The_Working_Bet_v4.md",
    [
        (
            "- **Time from expansion** — *N* is primary; cosmic time is that expansion counted, at the rate H = β_NTE|Φ_NTE|² sets.",
            "- **Time and expansion as one structure** — *N* is primary as a coordinate, because it is the one that can be written without circularity; cosmic time is that expansion counted, at the rate H = β_NTE|Φ_NTE|² sets.",
        )
    ],
    "AG3_bullet",
)

bump(
    "Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v7.md",
    [
        (
            "sets how expansion becomes experienced time through the central equation",
            "sets the rate at which expansion is counted as time through the central equation",
        )
    ],
    "Q5",
)

Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_greg_batch_apply_pass2.txt").write_text(
    "\n".join(log), encoding="utf-8"
)
print("\n".join(log))
