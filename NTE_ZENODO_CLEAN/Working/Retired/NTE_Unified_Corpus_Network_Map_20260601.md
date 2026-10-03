# NTE unified corpus network (static map)

**Companion to Canvas:** `nte-unified-corpus-network.canvas.tsx` (Cursor canvases folder on Desktop workspace).

If the Canvas panel shows the title but no diagram, refresh the canvas or use this Mermaid block in any Markdown preview.

```mermaid
flowchart TB
  subgraph EXT["External research"]
    CC[Chamseddine-Connes]
    HK[Gilkey / Vassilevich]
    DS[Friedrich / Bar S3]
    PR[Penrose CCC]
    OC[Farnsworth / Marcolli]
    HF[Hopf / monopole]
    SM[SM + NuFIT]
    ST[Starobinsky]
  end

  subgraph AX["NTE axioms (minimal)"]
    A1[Null-time ds2=0]
    A2[H = a|Phi|^2]
    A3[S3 x S1 substrate]
    A4[E-folds N]
    A5[Surface ontology]
    A6[Unimodular Lambda quiet]
  end

  subgraph GR["Greg bindings"]
    G1[Janus / CPN]
    G2[Gauge birth]
    G3[F1 d=3]
    G4[kappa0]
    G5[theta23 pathway]
    G6[Yukawa m_nu2]
    G7[Fractal CCC]
  end

  subgraph CP["Unified corpus"]
    M[Master trilogy]
    S2[S2 + C12 chord]
    C11[C11 Lambda]
    C13[C13 neutrino]
    T1[Tier-1 P1 P4 P5]
    BK[Popular + Book]
    CR[CR2 honest register]
  end

  CC --> A3
  CC --> A6
  HK --> A3
  DS --> A3
  PR --> A4
  OC --> A3
  HF --> G4
  SM --> G5
  SM --> G6

  G1 --> A5
  G2 --> A3
  G4 --> S2
  G6 --> C13

  A3 --> S2
  A3 --> T1
  A6 --> C11
  A2 --> M
  S2 --> C11
  CR --> M
```

---

## Reading guide

| Layer | Role |
|-------|------|
| **External** | Established mathematics and phenomenology NTE adopts |
| **Axioms** | Six load-bearing constraints (small count, large reach) |
| **Greg bindings** | Minimum novel concepts that stitch streams together |
| **Corpus** | Master, chord, companions, standalones, pedagogy, CR2 honesty |

Edge types in the interactive Canvas: **adopts** (external to axiom), **extends** (Greg to axiom), **derives** (axiom to corpus), **binds** (Greg to corpus).
