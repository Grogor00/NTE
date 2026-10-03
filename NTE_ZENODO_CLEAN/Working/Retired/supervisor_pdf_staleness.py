#!/usr/bin/env python3
"""Report stale PDFs (md newer than pdf or pdf missing)."""
from pathlib import Path

ROOT = Path(r"C:\Users\gregw\OneDrive\Desktop\NTE v10_6")
BOOK = Path(r"C:\Users\gregw\OneDrive\Desktop\Book")
PAPER_BUILD = ROOT / "paper-build"
PDF_OUT = PAPER_BUILD / "pdf-out"
BOOK_PDF = BOOK / "paper-build" / "pdf-out"

# Mirror build-pdfs.ps1 paper list (canonical Papers/)
PAPERS = [
    "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_v0_2_20260526.md",
    "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_v0_2_20260526.md",
    "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md",
    "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md",
    "Paper_Hopf_Bundle_Bare_Coupling_v0_1_20260526.md",
    "Paper_F1_Trace_Anomaly_S3xS1_Uniqueness_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_P4_Theta23_Z2_Chirality_Superposed_Majorana_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_Kappa_AB_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_S1_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_S2_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_OctonionExtension_Pedagogical_Pivot_v1_0_20260530.md",
    "Paper_External_Empirical_Surface_Clean_Gates_Pedagogical_Pivot_v1_0_20260530.md",
    "Companion_1_Entanglement_v10_6.md",
    "Companion_2_BornRule_Hopf_v10_6_v2.md",
    "Companion_3_Quantisation_Compactness_v10_6.md",
    "Companion_4_Hierarchy_Resonance_v10_6.md",
    "Companion_5_StateSpace_Surface_v10_8.md",
    "Companion_6_Gap5_BornRule_GaugeBirth_v10_6_v2.md",
    "Companion_7_Neutrino_v10_17_2.md",
    "Companion_8_VNTE_Trajectory_v10_8.md",
    "Companion_9_VNTE_Stage3_v10_8.md",
    "Companion_10_Gap1_M1_Pathways_v10_17_2.md",
    "Companion_11_Lambda_Unimodular_Closure_v10_17_2.md",
    "Companion_12_Spectral_Chord_Closure_v10_17_2.md",
    "Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md",
    "NTE_v10_17_Part1_Foundations.md",
    "NTE_v10_17_Part2_Structure.md",
    "NTE_v10_17_Part3_Accounting.md",
    "Paper_S6_M_R_Heat_Kernel_v1_0.md",
    "Paper_Popular_v10_8_Full_Edition.md",
    "Paper_External_Empirical_Surface_Clean_Gates_v0_1_20260530.md",
    "Paper_Kappa_AB_v10_17_2.md",
    "Paper_S2_v1_0_Consolidation_20260525.md",
    "Paper_S1_v0_4.md",
    "Paper_OctonionExtension_v10_9.md",
    "Paper_Popular_v10_8_Reader_Edition.md",
    "NTE_Corpus_Papers_Index.md",
]
WORKING = [("NTE_Reader_Glossary_Companion_v1_0.md", ROOT / "Working")]


def stale(md: Path, pdf: Path) -> bool:
    if not md.exists():
        return False
    if not pdf.exists():
        return True
    return md.stat().st_mtime > pdf.stat().st_mtime + 1


def main() -> None:
    stale_papers = []
    for name in PAPERS:
        md = ROOT / "Papers" / name
        pdf = PDF_OUT / (Path(name).stem + ".pdf")
        if stale(md, pdf):
            stale_papers.append(name)
    for name, src in WORKING:
        md = src / name
        pdf = PDF_OUT / (Path(name).stem + ".pdf")
        if stale(md, pdf):
            stale_papers.append(name)

    stale_books = []
    book_md = BOOK / "Chapter_*.md"
    for md in BOOK.glob("Chapter_*.md"):
        if "depreciated" in str(md) or "Book_with_TP" in str(md):
            continue
        pdf = BOOK_PDF / (md.stem + ".pdf")
        if stale(md, pdf):
            stale_books.append(md.name)

    for extra in [BOOK / "Appendix_A_NTE_Popular_Paper_Reader_Edition.md", BOOK / "Appendix_B_NTE_Corpus_Links.md"]:
        if extra.exists():
            pdf = BOOK_PDF / (extra.stem + ".pdf")
            if stale(extra, pdf):
                stale_books.append(extra.name)

    print(f"STALE_PAPERS:{';'.join(stale_papers)}")
    print(f"STALE_BOOKS:{';'.join(stale_books)}")
    print(f"count_papers={len(stale_papers)} count_books={len(stale_books)}")


if __name__ == "__main__":
    main()
