# Handoff — Cursor → AC: G6 / G7 / G8 reports (Ch 13/9/10 findings routing)

**From:** Cursor Main · **To:** AC · **Cc:** Greg, PC · **Date:** 2026-09-25
**In response to:** `Handoffs\Handoff_AC_to_PC_Cursor_Rulings_Ch13_Ch9_Ch10_Findings_20260925.md` §§1–2, §8.

Raw dump: `Working\_g6_g7_grep_20260925_OUT.txt`

---

## G6 — ~40 Mpc / coherence / free-streaming

**Searched `Core_Papers\` for:** `40 Mpc`, `forty megaparsec`, `coherence length`, `coherence mass`, `free-stream`, `free streaming`, `Mpc` (relevant hits only below), `M_c`.

| Hit | File · section | Sentence (verbatim core) | Register language |
|---|---|---|---|
| **Primary** | `NTE_v10_19_0_Part2_Structure.md` · **§IX** | “A mass-dependent DM:baryon variance $\sigma(M) \propto M^{-1/2}$ above the **neutrino free-streaming coherence mass** $M_c \sim 4\times10^{14} M_\odot$, with large scatter below it… The $M^{-1/2}$ scaling is a generic CLT consequence; the **NTE-specific content is its combination with the mean $\kappa \approx 5.50$ and the coherence scale $M_c$**. … (The amplitude within one coherence volume is open.)” | Framed under **Falsifiable prediction.** Explicitly: scale itself is free-streaming (standard), NTE-specific = combination with κ + $M_c$. Amplitude open. |
| Echo | `NTE_v10_19_0_Part3_Accounting.md` · Predictions triage | Same: “combination with $\kappa\approx5.50$ and the coherence mass $M_c$.” | Prediction / falsifiability list (item 2). |
| Echo | Part 3 · Falsifiability register | “Absence of the $\sigma(M)\propto M^{-1/2}$ scaling above $M_c$ … falsifies the two-sector mechanism.” | Falsifier on the **scaling**, not on a length. |

**Not found in `Core_Papers\`:** `40 Mpc`, `forty megaparsec`, `coherence length` (as a length). Companion 15 / Part 1 hits for “coherence” are unrelated (ratio coherence, decoherence, chord coherence claim).

**Cursor read for AC:** corpus deposits a **coherence mass** $M_c\sim4\times10^{14}M_\odot$ labelled neutrino free-streaming, not a 40 Mpc length. Register language already separates CLT / free-streaming from NTE-specific content (κ + scale combination). Matches AC’s expectation that the free-streaming scale is **adopted / cross-check**, not derived from NTE’s mass scale. **No deposited “~40 Mpc” figure** for PC to inherit as derived.

---

## G7 — `mediat*` stem

| File · section | Sentence core | Neutrino / DM subject? |
|---|---|---|
| `Part1` · §III | “This bilateral support — **not a mediating role** — is the geometric structure on which the dark-matter cross-thickness coupling acts” | **Yes — explicit denial** of mediation for the bridge. |
| `Companion_05` · Abstract | “a geometric coupling, **not a particle mediator**” | **Yes — denial.** |
| `Part2` · §IX | “EM-**mediated** baryon physics confined to one orientation” | No — EM/baryons, ordinary language. |
| `Part2` · §XI | “neutrino-**mediated** boundary stiffening” (Li-7 / $^7$Be) | Neutrino subject, but **BBN lithium** channel, not the DM cross-thickness picture. |
| `Part2` · §XIV–XV | “entanglement-**mediating** density” (null-time gluons in QGP) | No — gluons / entanglement. |

**Cursor read:** deposited corpus **rejects** mediation for the DM bridge (Part 1 + C5). No load-bearing “neutrino mediates the coupling” claim found in `Core_Papers\` for the cross-thickness DM mechanism. Book Ch 10’s “mediated through” defect does **not** appear to be inherited from a current corpus sentence of that form; Part 2’s “through this neutrino backbone” is geometric coupling language without the mediation word.

---

## G8 — Book render lane

**Report:** the standing `paper-build` render path has **no `Book\` configuration**.

- Defaults: `paper-build\pdf-defaults.yaml`, `pdf-defaults-master.yaml` — used only with `Core_Papers\` + `prepare_master_pdf.py` / `prepare_paper_pdf.py` → `paper-build\pdf-out\`.
- Existing scripts (`_render_p1_p3.ps1`, `_render_c17_c20_stale.ps1`, etc.) hard-code `Core_Papers\`.
- Grep of `paper-build\` for `Book\` / `Chapter_` → **no matches**.

**What it would take:** a Book pandoc defaults file (or reuse companion defaults), a `Book\` → `pdf-out` (or `Book\pdf-out`) copy/prepare script, and a currency check (PDF newer than `.md`). Until that exists, opening-arc and later chapter `.md` files have **no PDF currency path** — confirming AC’s “standing configuration gap.”

---

## Also this tick

Re-rendered stale Companion PDFs (md 2026-09-18 > pdf 2026-09-05): **C17, C18, C19, C20** — all CURRENCY_OK as of 2026-09-25 18:36–18:37 NZST. Other Core_Papers PDFs were already current.

— Cursor Main, 2026-09-25.
