# Handoff — AC → Cursor: Triage `Working candidates\` and `Working\`

**From:** AC (Claude) · **To:** Cursor Main · **Cc:** Greg · **Date:** 2026-09-22
**Status:** Greg-directed. Two-phase: Cursor inventories and classifies **every** file, applies only the unambiguous moves (rules R1–R5), and **holds** everything else for AC verification.
**Addressing:** name/path only (manifest §6 discipline 9). No Drive IDs anywhere in the report.

---

## Scope

| Folder | Action |
|---|---|
| `G:\My Drive\NTE_ZENODO_CLEAN\Working candidates\` | Every file triaged → `Working\` (keep) or `Working\Retired\` (superseded / spent). Goal: folder empty. |
| `G:\My Drive\NTE_ZENODO_CLEAN\Working\` | Every top-level file triaged → stays, or → `Working\Retired\` if superseded. |
| `Working\Farnsworth_Archive_Pull_20260802\` | **Do not move.** Inventory only (it is live source for the open route-B E(Φ_NTE) build). |
| `Working\__pycache__\` | Report only. Python cache, not corpus — recommend deletion to Greg. |

**Out of bounds — do not touch:** `Core_Papers\`, `Book\`, `Popular_Editions\`, `Pedagogical_Notes\`, `Handoffs\`, `paper-build\`, `References\`, `Outreach\`, `potential\`, `New folder\`. These are the **reference sets** you check supersession against.

---

## Hard guards

1. **Move, never copy.** A second copy is how Appendix C v1.3 went missing. No twins.
2. **Nothing is deleted.** `Working\Retired\` is quarantine.
3. **Name collision at destination:** SHA-256 both. Identical → the candidate goes to `Working\Retired\` (duplicate). Different → **FLAG**, move nothing.
4. **Never rename** without AC confirmation — including the 8.3 short-name files. Propose the real name in the report instead.
5. **Nothing goes into `paper-build\`.** Tooling that belongs there is either already there (then the candidate is superseded) or flagged.
6. Preserve file bytes exactly.

---

## Known item — act on this one specifically

`Working candidates\strip_corpus_metadata.py` (10,029 B, modified 2026-06-27) is the **pre-fix** copy containing the ORPHAN_SEE regex that deleted every standalone "see" from rendered PDFs (fix filed 2026-08-04). → `Working\Retired\`.
**Also confirm** that the live copy in `paper-build\` contains the corrected pattern `(?:;\s*)?\b[Ss]ee\b(?=\s*[);])`. Report the line verbatim. If `paper-build\` still has the old pattern, that is a render-blocking finding — report it at the top.

---

## Rules Cursor may apply without AC (R1–R5)

| Rule | Condition | Destination |
|---|---|---|
| **R1 duplicate** | Byte-identical (SHA-256) to a file in `Working\` or any reference set | `Working\Retired\` |
| **R2 run artifact** | `.json` run reports, `_*grep_report.txt`, logs, `__pycache__` contents | `Working\Retired\` |
| **R3 spent one-off script** | Name matches `apply_*`, `fix_*`, `seed_*`, `update_ledger_*`, `housekeeping_*`, `rename_*`, `reopen_*`, `batch_verify_*`, `_discover_*`, `_find_*`, `_test_*`, `_run_*`, `*mojibake*`, `codepoint_probe.py`, `build_depreciated_*` — **and** the patch/task it performed is evidenced as done (a completion handoff in `Handoffs\`, or its target file already carries the change). If you cannot evidence completion → FLAG. | `Working\Retired\` |
| **R4 tooling superseded** | A same-named script exists in `paper-build\` and differs (the live one wins) | `Working\Retired\` |
| **R5 versioned supersession** | Same document stem exists at a **higher version or later date** in a reference set or `Working\` — e.g. any `*_v10_17_*` / `*_v10_18_0_*` document whose `v10_19_0` successor exists; `*DECONTAMINATED_PILOT*` drafts of companions now canonical in `Core_Papers\` | `Working\Retired\` |

Everything not matched by R1–R5 → **FLAG**. When in doubt, flag.

---

## FLAG categories AC expects (do not move these)

- **8.3 short-name files** (`CO381~1.MD`, `CO4419~1.MD`, `CO6356~1.MD`, `CO516C~1.MD`, `CO36DE~1.MD`, `COD347~1.MD`, `COEFB4~1.MD`, `CO00A2~1.MD`, `CO21D3~1.MD`, `CO6C86~1.MD`, and any others). Read each header; report the document title, version stamp, date, and the probable original long filename. AC expects most are companion decontamination pilots (cf. the 170-character `Companion_11_..._DECONTAMINATED_PILOT_..._20260626.md` beside them — Windows path-length truncation), but they must be identified, not assumed.
- **Physics numerics scripts** — `farnsworth_stage*`, `paper_s22_*`, `kappa_closure_*`, `clfv_cartan_ratio_numerical.py`, `p5_flux_dial_worksheet.py`, `alpha_to_beta_nte_audit.py`, `alpha_beta_nte_corpus_fix_pass.py`, `pc03_tier2_beta_audit.py`, `healpix_ring.py`. For each: which canonical file cites it or the result it computes (grep `Core_Papers\` and `Working\` for the filename and for its key output numbers). AC decides keep vs retire.
- **Prose working documents** — `Wagenveld_Sprint_*`, `Programme_S_Paper_S6_*`, `Paper_PhiNTE_Necessity_*`, `Paper_A1_*`, `Paper_A2_*`, `Standalone_Papers_Accessibility_Tiering_*`, `Publication_Title_Block_Standard_*`, `P5_v0_3_Zenodo_Changelog_*`, `PC_Book_Pedagogical_Pivot_Pass_*`, `PC_Audit_Repairs_*`, `Paper_Scope_Alignment_Sweep_Results.md`, `P1_Kappa_FM5_Audit_*`, and every other prose file not caught by R5.
- **Anything in `Working\` itself** that R1–R5 do not catch.

For every flagged prose file, include in the report:
- first heading and any status/version/date line,
- the **first 12 non-empty lines** verbatim,
- grep hits for the following **withdrawn-claim markers** (count + one sample line each): `sin^2\theta_{12} = 1/3` / `sin²θ₁₂ = 1/3`, `six-note`, `two pathways`, `S^7/\mathbb{Z}_2` / `S⁷/Z₂`, `Planck-radius`, `void` + `DESI` in the same paragraph, `β_NTE` + `√6/π` / `sqrt(6)/pi`, `Cabibbo`, `θ₁₃ =`, `T_GB` without `conditional` nearby,
- whether a successor exists (nearest-name match in reference sets), with its filename and modified date.

That packet is what lets AC verify without re-reading 100+ files through Drive.

---

## Deliverables

1. **`Working\Working_Candidates_Triage_Report_20260922.md`** — one table covering **every** file in both folders: filename · size · modified · SHA-256 (first 12) · rule or FLAG · destination · action (MOVED / HELD). Then the FLAG packets. Then the `paper-build\strip_corpus_metadata.py` line check.
2. Totals line: files seen / moved to Working / moved to Retired / held.
3. **Completion handoff** to `Handoffs\` addressed to AC.
4. **Registration (discipline 10):** add one line to manifest §10 under an "In progress" item: *Working-candidates triage 2026-09-22 — N held for AC verification; report at `Working\Working_Candidates_Triage_Report_20260922.md`.*

Do not empty or remove the `Working candidates\` folder itself — Greg removes it once AC clears the held items.

---

— AC, 2026-09-22.
