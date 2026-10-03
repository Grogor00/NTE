# P-BH2b — horizon shell / null-time junction model v0.1 (§22.12)

**Stream:** Cursor → Jammer  
**Date:** 2026-05-23  
**Status:** **S0 junction scaffold** — extends P-BH1 + P-BH2  
**Prior:** `P_BH2_Boundary_Info_Carrier_v0_1`, `BH_Nthickness_Shell_v0_1`

---

## §1. Junction picture

At Schwarzschild radius $r_s$, three layers meet on the **S³ boundary** (no bulk):

```
  [interior-side embedded matter]  ←→  [shell: N-thickness + |Φ| thinning]  ←→  [null-time mediators, depth 0]
         e-fold depth > 0                    r ≈ r_s                           photons/gluons, y=0
```

**Category discipline (Part 1 §IV):** correlations live in **null-time exchange geometry**; massive endpoints are e-fold-embedded; manifold separation between endpoints does not degrade directed entanglement until decoherence.

---

## §2. Junction conditions (programme)

| Interface | Condition |
|-----------|-----------|
| **Embedded ↔ shell** | $|Φ_{\rm NTE}|^2$ slaved via §2.3; $\ell(r_s)/\ell_\infty = 2$ (P-BH1a, solar mass) |
| **Shell ↔ null-time** | Mediators at **zero e-fold depth** co-move with boundary wavefront; shell is geometrically the **transition locus** where embedded depth meets zero-depth sector |
| **Information** | No storage in $r<r_s$ bulk; correlation register = null-time network + optional ν bilateral modes (P-BH2) **on shell** |

**Not specified:** dynamic fall-in equations; quantum field theory on shell — Jammer.

---

## §3. Decoherence at horizon (Part 1 §IV.3 extension)

Environmental coupling at shell: thermal/null-time flux across horizon increases **new** exchange connections → standard decoherence pattern applied to **shell-resident** coherent structures. No faster-than-$c$ communication.

---

## §4. Consistency checks

| Check | Status |
|-------|--------|
| §16 no-bulk | ✓ junction is boundary-only |
| §22.13 global 𝕆→ℍ | ✓ $|Φ|\to 0$ does **not** restore local octonions |
| P-BH1b area law | Multiplicative $(A/4G)\,g(\ell)$ programme orthogonal to junction class |
| P-BH4 strong field | **Required** before numeric junction transport claims |

---

## §5. Deliverables

| ID | Task | Status |
|----|------|--------|
| P-BH2b | This junction note | **Done v0.1** |
| P-BH2c | ν mode count at shell | Open (Companion 7) |
| P-BH2d | Junction transport sketch | Jammer |

---

## §6. Cross-references

- Part 1 §IV (Axiom 1.7); §22.12–§22.13  
- `bh_nthickness_shell.py`, `P_BH2_Boundary_Info_Carrier_v0_1`

— Cursor P-BH2b v0.1, 2026-05-23.
