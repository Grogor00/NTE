from pathlib import Path
book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")

def show(path, needles):
    t = path.read_text(encoding="utf-8")
    print("===", path.name, "len", len(t))
    for n in needles:
        i = t.find(n)
        print(f"  find {n!r}: {i}")
        if i >= 0:
            print("   CTX:", repr(t[i:i+200]))

show(book/"Appendix_C_The_Open_Ledger_v1_5_DRAFT_PC_20260925.md", [
    "almost-certainly-untestable",
    "Charged-lepton flavour violation",
    "Charged lepton flavour violation",
    "surprise observation",
])
show(book/"Chapter_03_A_Closed_Universe_v8.md", ["sixty e-folds", "after sixty"])
show(book/"Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6_1.md", [
    "imported",
    "retreats from it",
    "We should be careful about how strong",
    "does not derive the qubit",
])
show(book/"Chapter_08_The_Unresolved_Particle_v5.md", [
    "Charged leptons must never oscillate",
    "derives the heavy",
    "places the heavy",
])
show(book/"Chapter_07_The_Gauge_Birth_v4.md", [
    "embedding depth",
    "N_lock",
    "**3. Mass.**",
])
