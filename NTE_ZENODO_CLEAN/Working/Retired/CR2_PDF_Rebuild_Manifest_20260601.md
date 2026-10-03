# CR2 PDF Rebuild Manifest — patched standalones

**Author:** Cursor PC  
**Date:** 2026-06-01  
**Queue item:** PS-08 (pc_scratch)  
**Build tooling:** `NTE v10_6/paper-build/build-pdfs.ps1` (Pandoc + MiKTeX)

---

## Summary

Five corpus sources were patched during CR2 wave 2 (2026-06-01). Existing PDFs in `paper-build/pdf-out/` predate the patches (2026-05-31). This manifest lists rebuild targets, patch provenance, and build status.

| # | Alias | Source `.md` | CR2 patch lane | Prior PDF (stale) | Build script entry |
|---|-------|--------------|----------------|-------------------|-------------------|
| 1 | **S2** | `Papers/Paper_S2_v1_0_Consolidation_20260525.md` | MAIN-05 (CR-H1 a₄=0) | `Paper_S2_v1_0_Consolidation_20260525.pdf` (2026-05-31) | ✅ `$papers` |
| 2 | **Hopf pivot** | `Papers/Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md` | PS-05 (B3 κ₀ rep-theory language) | `Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.pdf` (2026-05-31) | ✅ `$pedagogical` |
| 3 | **P5 v0.3** | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` | PS-07 (Zenodo snapshot; CR2 B1 honest-scope) | *none* (new file) | ⚠️ **not in `build-pdfs.ps1`** — one-off build attempted |
| 3b | P5 v0.2 (legacy) | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md` | Wave 1 B1 body patch (PS-06 PASS) | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.pdf` (2026-05-31) | ✅ `$technical` |
| 4 | **S6 pivot** | `Papers/Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md` | PS-03 (CR2 B1 neutrino honesty) | `Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.pdf` (2026-05-31) | ✅ `$pedagogical` |
| 5 | **Popular** | `Papers/Paper_Popular_v10_8_Full_Edition.md` | PS-04 (CR2 B1 grep-scrub) | `Paper_Popular_v10_8_Full_Edition.pdf` (2026-05-31) | ✅ `$papers` |
| 6 | **P5 pivot** | `Papers/Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.md` | PS-09 (CR2 B1 neutrino honesty) | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.pdf` (2026-05-31) | ✅ `$pedagogical` |

**Source mtime (post-patch):** all listed `.md` files ≥ 2026-06-01 16:40 local; PDFs still 2026-05-31 → rebuild required (P5 pivot PDF refreshed PS-11).

---

## Patch detail (one line each)

1. **S2** — §5.4–§5.5: a₄=0 (F₁=0); boxed 270β_GB struck; abstract item 4 + §7 Λ reroute; chord 6→5 framing (`Handoff_Cursor_Main_to_AC_S2_CR-H1_Patch_For_Ratification_20260601.md`).
2. **Hopf pivot** — B3: 3 = SU(2) gauge-field components (not Killing-spinor polarisations); 2-dim fundamental Killing-spinor space; κ₀ = 3/√(4π) unchanged (`Working/CR2_B3_kappa0_RepTheory_Verdict_Claude_Jammer_20260601.md`).
3. **P5 v0.3** — √Δm²₃₁ ≈ 0.0495 eV comparand; solar 0.993× Tier A; atmospheric ≈1.49×; (8π)^(2/3) ratio; falsifier/tier register (`Working/P5_v0_3_Zenodo_Changelog_20260601.md`).
4. **S6 pivot** — Retracted 0.997× atmospheric; solar sub-1%; atmospheric ≈1.49×; honest single-M_R scope (Jammer B1 verdict §3.2).
5. **Popular** — No 0.997×; solar-only Tier A; atmospheric open; 1.49× alignment (`NTE_Stream_Notes_PC.md` PS-04).
6. **P5 pivot** — Retracted 0.997× atmospheric; solar 0.993× Tier A; atmospheric ≈1.49×; (8π)^(2/3) ratio; single-*M_R* honest scope (PS-09; mirrors S6 pivot).

---

## Rebuild command (in-script targets)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "NTE v10_6\paper-build\build-pdfs.ps1" -Only @(
  "Paper_S2_v1_0_Consolidation_20260525.md",
  "Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.md",
  "Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.md",
  "Paper_Popular_v10_8_Full_Edition.md"
)
```

## P5 v0.3 one-off (Greg / build-script follow-up)

Add `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` to `$technical` in `build-pdfs.ps1` when Zenodo PDF is canonical. Until then, one-off Pandoc pass (same pipeline as script) — see rebuild log below.

---

## Rebuild log (PS-08 execution)

**2026-06-01 ~17:20 local — Cursor PC**

| Target | Output PDF | Status | Notes |
|--------|-----------|--------|-------|
| S2 | `Paper_S2_v1_0_Consolidation_20260525.pdf` | ✅ **REBUILT** | 123.7 KB; Pandoc ⚠ emoji warnings (Libertinus) — cosmetic only |
| Hopf pivot | `Paper_Hopf_Bundle_Bare_Coupling_Pedagogical_Pivot_v1_0_20260530.pdf` | ✅ **REBUILT** | 42.9 KB |
| P5 v0.2 | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_2_arxiv_20260526.pdf` | ✅ **REBUILT** | 79.2 KB; legacy arxiv filename retained in build script |
| P5 v0.3 | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.pdf` | ✅ **REBUILT** | 79.4 KB; one-off Pandoc pass (not yet in `$technical`) |
| S6 pivot | `Paper_S6_M_R_Heat_Kernel_Pedagogical_Pivot_v1_0_20260530.pdf` | ✅ **REBUILT** | 42.7 KB |
| Popular | `Paper_Popular_v10_8_Full_Edition.pdf` | ✅ **REBUILT** | 116.2 KB |

**2026-06-01 ~17:28 local — Cursor PC (PS-11)**

| Target | Output PDF | Status | Notes |
|--------|-----------|--------|-------|
| P5 pivot | `Paper_Solar_Neutrino_Mass_Yukawa_Duality_Pedagogical_Pivot_v1_0_20260530.pdf` | ✅ **REBUILT** | 42.5 KB; post PS-09 B1 patch; `$pedagogical` in `build-pdfs.ps1` |

**Tooling:** `paper-build/build-pdfs.ps1 -Only` (5 in-script targets) + manual pipeline for P5 v0.3. MiKTeX + Pandoc available.

**Follow-up for Greg:** add P5 v0.3 to `$technical` in `build-pdfs.ps1`; run `export-zenodo-bundle.ps1` when bundle refresh authorised.

---

## Greg actions (residual)

1. Add `Paper_Solar_Neutrino_Mass_Yukawa_Duality_v0_3_zenodo_20260601.md` to `$technical` in `build-pdfs.ps1` for future bundle exports.
2. Refresh Zenodo bundle via `paper-build/export-zenodo-bundle.ps1` when CR2 ratification gate clears.
3. Optional: strip ⚠ emoji from S2 source if PDF font warnings are undesirable.

---

## Full rebuild log (2026-06-13 — post CR2 MB stamp + CLFV Category H)

**Cursor Main** — full `build-pdfs.ps1` (27 PDFs) + `Book/paper-build/build-pdfs.ps1` (20 PDFs); Zenodo bundles refreshed (`-SkipBuild`).

| Bundle | Count | Output |
|--------|-------|--------|
| NTE corpus | **27** | `NTE v10_6/paper-build/pdf-out/` |
| NTE Zenodo Live | **9** | `NTE v10_6/paper-build/zenodo-upload/` |
| Book | **20** | `Book/paper-build/pdf-out/` |
| Book Zenodo | **20** | `Book/paper-build/zenodo-upload/` |

**Load-bearing refresh:** `NTE_v10_17_Part3_Accounting.pdf` (§17.5.12 Category H CLFV + CR-V1 canon).

**Cosmetic warnings only:** Libertinus missing Λ/μ/ν in some mono blocks; S2 ⚠ emoji; glossary hyperref undefined — PDFs complete.

---

## Companion PDF addendum (2026-06-13)

**Cursor Main** — added `$companions` (C1–C13) to `paper-build/build-pdfs.ps1`; built **13** PDFs → `paper-build/pdf-out/Companion_*.pdf`.

| # | Source | PDF |
|---|--------|-----|
| 1 | `Companion_1_Entanglement_v10_6.md` | ✓ |
| 2 | `Companion_2_BornRule_Hopf_v10_6_v2.md` | ✓ |
| 3 | `Companion_3_Quantisation_Compactness_v10_6.md` | ✓ |
| 4 | `Companion_4_Hierarchy_Resonance_v10_6.md` | ✓ |
| 5 | `Companion_5_StateSpace_Surface_v10_8.md` | ✓ |
| 6 | `Companion_6_Gap5_BornRule_GaugeBirth_v10_6_v2.md` | ✓ |
| 7 | `Companion_7_Neutrino_v10_17_2.md` | ✓ |
| 8 | `Companion_8_VNTE_Trajectory_v10_8.md` | ✓ |
| 9 | `Companion_9_VNTE_Stage3_v10_8.md` | ✓ |
| 10 | `Companion_10_Gap1_M1_Pathways_v10_17_2.md` | ✓ |
| 11 | `Companion_11_Lambda_Unimodular_Closure_v10_17_2.md` | ✓ |
| 12 | `Companion_12_Spectral_Chord_Closure_v10_17_2.md` | ✓ |
| 13 | `Companion_13_Yukawa_Nu2_D5_Inverse_v10_17_2.md` | ✓ |

**Index sync:** `Papers/COMPANION_CANONICAL_INDEX.md` — v10.17.2 filenames for C7/C10–C13.

**Not in Zenodo Live tier** (9-file Greg upload set unchanged). Add to `export-zenodo-bundle.ps1` Full tier if archive export needed.

---

— Cursor PC, 2026-06-01. — Cursor Main full-rebuild addendum, 2026-06-13. — Cursor Main companion-pipeline addendum, 2026-06-13.
