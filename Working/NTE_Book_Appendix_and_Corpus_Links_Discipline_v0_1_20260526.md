# NTE Book — Appendix & Corpus Links Discipline v0.1

**Status:** Greg-ratified 2026-05-26 (edition filenames updated 2026-05-30)  
**Book folder:** `C:\Users\gregw\OneDrive\Desktop\Book\`

---

## §1. Publication structure

| Component | Location | Notes |
|-----------|----------|--------|
| **Main text** | `Chapter_*` + `Prelude_*` | Lay register; points to appendix/corpus, does not embed papers |
| **Appendix A** | `Appendix_A_NTE_Popular_Paper_Reader_Edition.md` | **Popular Paper Reader Edition** only — **not** Full Edition |
| **Popular Paper Full Edition** | `Papers/Paper_Popular_v10_8_Full_Edition.md` | Separate corpus paper (~13k words); **never** auto-synced into Appendix A |
| **Appendix B** | `Appendix_B_NTE_Corpus_Links.md` | Link index to Master, Companions, standalones |

**Rule:** Chapters say *Appendix A (Reader Edition)* / *Appendix B* / *technical corpus* — not "the popular paper" without edition.

**Rule:** **Full Edition ≠ Reader Edition.** Different filenames, different word counts, different jobs. Cross-refs at top of each `Paper_Popular_*.md`.

---

## §2. Appendix A build

```bash
python "NTE v10_6/Working/build_book_appendix_a.py"
```

- Strips workshop editorial tail from Popular Paper before merge.
- Source of truth for book: `Papers/Paper_Popular_v10_8_Reader_Edition.md`. Full corpus edition: `Paper_Popular_v10_8_Full_Edition.md`.
- After Popular Paper revision: re-run `build_book_appendix_a.py` (Reader Edition only).

---

## §3. Appendix B / external links

- **Now:** relative paths into `NTE v10_6/Papers/`.
- **At publication:** Greg supplies stable URLs (arXiv, project site); PC or AC patches Appendix B table — no need to duplicate paper bodies in the book folder.

---

## §4. Chapter forward-reference discipline

When prose needs proofs:

- Prefer *Appendix A* for lay compressed account.
- Prefer *Appendix B* + named Companion for technical derivation.
- Avoid Drive IDs in reader-facing book files.

---

## §5. Reader edition (workshop DNA)

- **Strip:** all `## Editorial notes` blocks and author-only tails — run `Working/strip_book_workshop_dna.py` on `Book/*.md` before export.
- **Avoid in body:** `Path A/B`, `PATCH-`, Drive IDs, `PC stands down`, version manifests in prose.
- **Ch 16:** trade epilogue is the tightened §1–§5 close (no full-chapter recap).
- **Appendix A:** rebuild via `build_book_appendix_a.py` after Popular Paper edits.
- **Corpus sync (2026-05-26):** book + Popular Reader Edition aligned to master v10.17.6, companions v10.17.2, Paper S2 v1.0, P0 sunshine closure; Ch 12/13/15/16 tier register updated.

---

## §6. Reception / trade edition note

Appendix placement answers reviewer question *"where are the proofs?"* without bloating chapters. Popular Paper as appendix keeps the main arc readable while giving skeptics a single downloadable NTE statement.

— Cursor 2026-05-26; edition filenames 2026-05-30
