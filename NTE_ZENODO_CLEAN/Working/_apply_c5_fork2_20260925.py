# -*- coding: utf-8 -*-
"""Apply Greg-ratified Companion 5 Fork 2 flatness patches."""
from pathlib import Path

c5 = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Core_Papers\Companion_05_StateSpace_v10_19_0.md")
text = c5.read_text(encoding="utf-8")
report = []

patches = [
    (
        "C5-1",
        "Flatness (Ω_k = 0) is required by the Euler closure condition on S³.",
        "Spatial curvature is negative and small: the closed S³ requires Ω_k < 0 strictly, with |Ω_k| driven toward zero by the e-fold run.",
    ),
    (
        "C5-3",
        "flatness (Euler closure), CPN symmetry",
        "near-flatness (closed S³ with |Ω_k| diluted by the e-fold run), CPN symmetry",
    ),
    (
        "C5-4",
        "Spatial flatness Ω_k = 0 (non-zero curvature would falsify the boundary identification).",
        "Spatial curvature sign: the boundary ontology requires a closed S³, hence Ω_k < 0 strictly; a confirmed Ω_k > 0 at significance falsifies the framework at the ontological level (Part 3, falsifiability item 11). Note this is one-sided — confirming Ω_k < 0 would not confirm NTE, since every closed cosmology predicts that sign.",
    ),
]

for pid, old, new in patches:
    n = text.count(old)
    if n == 1:
        text = text.replace(old, new, 1)
        report.append(f"{pid}: APPLIED")
    else:
        report.append(f"{pid}: FAIL count={n}")

# C5-2 whole paragraph — locate by heading
old_p = """**Flatness.** The Euler identity e^{iπ} + 1 = 0 encodes the zero-sum energy constraint at the Janus boundary: the total energy of the manifold must vanish, and zero total energy requires zero spatial curvature, Ω_k = 0. The universe is flat because the boundary condition demands it. NTE derives flatness both dynamically (from H(N) = β_NTE|Φ_NTE(N)|²) and topologically (from Euler closure): the Euler identity explains why the initial conditions had to be flat, the Hubble relation explains how flatness is maintained."""

new_p = """**Near-flatness.** The boundary ontology requires a closed S³, so spatial curvature is negative: Ω_k < 0 strictly, and exact flatness is excluded by the geometry. What the framework accounts for is the *observed* near-flatness — the e-fold run drives |Ω_k| toward zero from below, so the observable patch is flat to any achievable precision (Planck 2018: Ω_k = 0.0007 ± 0.0019). Observed flatness is thus a consequence of the expansion history rather than a separate boundary condition. The framework fixes the *sign* and not the magnitude. Earlier versions of this paper derived exact Ω_k = 0 from the Janus zero-energy condition; that derivation is **withdrawn** (2026-09-24). It conflated the bilateral sum over the CPN pair with the single-sector Friedmann energy, and the bilateral sum vanishes with each sector closed. Read as a statement about the manifold's total energy it points the other way: a spatially compact universe has identically zero total energy, so the premise supports closure, not flatness."""

n = text.count(old_p)
if n == 1:
    text = text.replace(old_p, new_p, 1)
    report.append("C5-2: APPLIED")
else:
    report.append(f"C5-2: FAIL count={n}")
    # try softer locate
    if "**Flatness.**" in text and "Euler identity e^{iπ} + 1 = 0 encodes the zero-sum" in text:
        report.append("C5-2: markers present but paragraph text differs — need manual")

# Manifest-style registration append if a Register section exists — skip if not

c5.write_text(text, encoding="utf-8")
out = Path(r"C:\Users\gregw\Desktop\NTE v10_6\Workflow\_c5_apply_report.txt")
out.write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
