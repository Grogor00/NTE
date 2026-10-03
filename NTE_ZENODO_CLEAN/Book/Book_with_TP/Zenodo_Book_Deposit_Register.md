# Zenodo book deposit — maintenance register

**Deposit:** [The Shape of Time](https://zenodo.org/records/19535903)  
**DOI (cite):** [10.5281/zenodo.19535902](https://doi.org/10.5281/zenodo.19535902)  
**License:** CC BY-NC-ND 4.0  
**Greg-owned:** upload, version bump, record description edits

**Corpus deposit (separate):** [10.5281/zenodo.19440067](https://doi.org/10.5281/zenodo.19440067) · [record 19440068](https://zenodo.org/records/19440068) · maintenance: `NTE v10_6/Zenodo_Corpus_Deposit_Register.md`

**Last register sync:** 2026-06-01 — **v3 published (Greg)**; local bundle matches live record

---

## When to publish a new Zenodo version

Publish **v2+** on the book record when any of these change:

- Any chapter or appendix **PDF** rebuilt after source ratification
- **Appendix B** link table changes (new filenames on the record)
- Book structure changes (e.g. Ch 16 / Ch 17 split — **required for current manuscript**)
- Prelude or Popular Reader Edition PDF refreshed

Do **not** bump Zenodo for markdown-only edits that have not been rebuilt and ratified for export.

---

## Maintenance workflow (Greg + Cursor)

1. **Ratify** chapter/appendix markdown (AC ledger / handoff).
2. **Rebuild PDFs:**  
   `powershell -File "Book\paper-build\build-pdfs.ps1"`
3. **Stage upload bundle:**  
   `powershell -File "Book\paper-build\export-zenodo-bundle.ps1"`  
   → outputs `Book\paper-build\zenodo-upload\` + `MANIFEST.md`
4. **Review** `MANIFEST.md` (file list, sizes) against live record.
5. **Upload** new version on [zenodo.org/records/19535903](https://zenodo.org/records/19535903) (Zenodo UI: New version → add/replace files → publish).
6. **Update** `Book/Appendix_B_NTE_Corpus_Links.md` if any **public filename** on the record changed; rebuild Appendix B PDF; re-export bundle.
7. **Update** `NTE v10_6/Outreach/Distribution_Campaign_v1_20260530.md` §2 book table if URLs/filenames changed.
8. **Log** version + date below.

---

## Live record (v3, published 2026-06-01)

**20 PDFs** (Prelude + Ch 1–17 + Appendix A + B). Cite DOI [10.5281/zenodo.19535902](https://doi.org/10.5281/zenodo.19535902); files at [record 19535903](https://zenodo.org/records/19535903).

| v3 content delta | Notes |
|------------------|-------|
| Ch 3, 6, 7, 9, 13, 15, 17 | Rebuilt after epigraph/voice pass + Ch 13 CR2 Λ sync |
| Ch 5, 10 | Canonical filenames **v6_2**, **v6** (drop **v6_1** / **v5** from record if still listed) |
| Other chapters | Unchanged filenames; bytes from 2026-05-31 pipeline where not in rebuild set |

## v1 → v2 (2026-05-31)

| Change | v1 | v2 |
|--------|-----|-----|
| Ch 16 / 17 | `Chapter_16_The_Working_Bet_v1.pdf` only | `Chapter_16_Stranger_and_Stranger_v1_1.pdf` + `Chapter_17_The_Working_Bet_v2.pdf` |
| Appendix A | `Appendix_A_NTE_Popular_Paper_v10_8_v7.pdf` | `Appendix_A_NTE_Popular_Paper_Reader_Edition.pdf` |
| Appendix B | Drive-path index | Zenodo URL index |
| All chapters | Pre–pipeline-clean builds | Rebuilt after metadata strip / title fixes |

---

## Canonical file list (must match export bundle)

Source of truth: `Book/paper-build/export-zenodo-bundle.ps1` (same order as `build-pdfs.ps1`).

| # | PDF filename | Source markdown |
|---|--------------|-----------------|
| 1 | Prelude_The_Forty_Million_Year_Instant_v5.pdf | Prelude_The_Forty_Million_Year_Instant_v5.md |
| 2–17 | Chapter_1 … Chapter_17 | (see build-pdfs.ps1) |
| 18 | Appendix_A_NTE_Popular_Paper_Reader_Edition.pdf | Appendix_A_NTE_Popular_Paper_Reader_Edition.md |
| 19 | Appendix_B_NTE_Corpus_Links.pdf | Appendix_B_NTE_Corpus_Links.md |

Download URL pattern:  
`https://zenodo.org/records/19535903/files/{filename}?download=1`

---

## Version log

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-05-30 | Initial book deposit; 18 files; Ch 16 = Working Bet only; Appendix A = v10_8_v7 filename |
| v2 | 2026-05-31 | 20 PDFs; Ch 16/17 split; Prelude v5; Appendix A/B refresh; pipeline-clean builds |
| **v3** | **2026-06-01** | **Published (Greg).** Current live — 7 chapter PDF refresh; Ch 5 v6_2 + Ch 10 v6 canonical; matches `paper-build/zenodo-upload/` |

---

## Cursor automation (optional)

- After book PDF rebuild batch: run `export-zenodo-bundle.ps1` and attach `MANIFEST.md` to handoff.
- Do **not** upload to Zenodo without Greg (credentials + publish click).
