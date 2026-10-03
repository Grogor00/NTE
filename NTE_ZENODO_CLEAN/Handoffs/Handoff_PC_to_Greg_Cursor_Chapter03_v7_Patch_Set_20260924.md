# Handoff — PC → Greg (ratify) → Cursor (apply): Chapter 3 v7 patch set

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply)
**Date:** 2026-09-24
**Base file:** `Book\Chapter_03_A_Closed_Universe_v6_1.md` (canonical, 22,932 B)
**Target:** `Book\Chapter_03_A_Closed_Universe_v7.md` — v6.1 left in place
**Status:** PROPOSED — not ratified

Patch series **M**, flags series **N**, to avoid collision with the A–F and G–K series already in flight today.

---

## 0. What this pass found

Chapter 3 is the last unswept chapter of the opening arc and it carries three things the earlier passes did not turn up.

**It reports Chapter 1 inaccurately.** Ch 3 summarises the photon as *"a single object with two readings"*, and uses the two-readings formula twice more. That is the exact refrain Chapter 1 v10 retired by name, on the ground that there are not two readers — there is one vantage, ours, and one fact about the object it is looking at. Chapter 3's summary of Chapter 1 therefore describes a version of Chapter 1 that no longer exists. Three instances, one of them in a paragraph whose whole job is to recapitulate.

**It carries the Chapter 4 retitle pointer, as a section heading.** `## Towards Time as Expansion`. This is the G1 pointer, and it is the last one PC has found.

**It contains a real physics error that is not a register issue.** Ch 3 identifies the Hubble horizon with the boundary past which things leave our causal future. Those are two different surfaces. Galaxies beyond the Hubble radius do still send us light — we routinely observe galaxies whose recession velocity exceeded *c* at the moment of emission — and the surface that actually bounds our causal future is the cosmological event horizon, which in our universe lies further out. This is a well-known confusion with a well-known literature, and it sits inside the chapter's *conservative anchor* for the flatness argument, which makes it the worst place in the chapter to have it. M6 repairs it, and the argument survives the repair intact.

Plus the emergence register in four places, the cosmic/proper correction, and two small prose defects.

---

## 1. Patches

### M1 — the flatness argument: emergence register

**OLD**

```
It's not, and the framework's structure gives a clean reason why. Chapter 1 established that *t* emerges from the expansion, not the other way around. There is no temporal starting point for *t* in the conventional Big Bang sense — no first moment, no zero on a clock that pre-existed the universe.
```

**NEW**

```
It's not, and the framework's structure gives a clean reason why. Chapter 1 established that *t* is the expansion counted, not a second thing the expansion gives rise to. There is no temporal starting point for *t* in the conventional Big Bang sense — no first moment, no zero on a clock that pre-existed the universe.
```

---

### M2 — the hand-off to Chapter 4: emergence register and cosmic time

Two corrections in one paragraph. Note this paragraph also names the next chapter's subject, so it has to survive the retitle.

**OLD**

```
This matters because of the central claim from Chapter 1: time is not the primary parameter. *N* is. What we experience as time is a consequence of expansion, with the boundary expansion field |Φ_NTE| parameterising the rate at which proper time accumulates per e-fold. Chapter 4 will work this out in detail. For now, hold the picture: *N* is the geometric count of expansion, *t* is what emerges from *N* with |Φ_NTE| setting the rate, and the universe is an expanding closed three-dimensional space whose radius has grown so vast through a huge run of e-folds that it appears, locally, flat.
```

**NEW**

```
This matters because of the central claim from Chapter 1: time is not the primary *parameter*. *N* is — and that is a statement about which coordinate can be written without circularity, not about which phenomenon is more real. What we experience as time and what the geometry does as it expands are one structure, with the boundary expansion field |Φ_NTE| parameterising the rate at which cosmic time accumulates per e-fold. Chapter 4 will work this out in detail. For now, hold the picture: *N* is the geometric count of expansion, *t* is what that count amounts to for anything embedded in it with |Φ_NTE| setting the rate, and the universe is an expanding closed three-dimensional space whose radius has grown so vast through a huge run of e-folds that it appears, locally, flat.
```

---

### M3 — the photon recap: the retired refrain

**OLD**

```
Chapter 1 established that the photon is not a thing in flight — it's the geometric connection between emission and absorption, a single object with two readings. The Ch 3 picture gives this its structural location.
```

**NEW**

```
Chapter 1 established that the photon is not a thing in flight — it's the geometric connection between emission and absorption, a single object with length to anyone measuring it from outside and no ruler along its own. The Ch 3 picture gives this its structural location.
```

---

### M4 — the entangled-pair recap: the refrain again, and the vantage

**OLD**

```
From the structure's vantage, the two endpoints are aspects of one situation. From the laboratory vantage, they look like two particles in different rooms. Both readings real; both are readings of one object.
```

**NEW**

```
There is no vantage belonging to the structure itself from which its two endpoints could be seen as one — that is the point, and it is why the one-object claim is a claim about the object rather than about a privileged observer of it. From the laboratory vantage, which is the only one there is, they appear as two particles in different rooms. Two appearances, one object, and nothing between the endpoints for a signal to travel on.
```

---

### M5 — the closing summary of both phenomena

**OLD**

```
Both phenomena are the same structural move: one object appearing as two, with both readings real. The photon's null-time is the first instance; entanglement is the second. Both are features of the same expanding S³ — the photon's two ends drawn apart in spatial-and-temporal extent, the entangled pair's two ends in spatial extent.
```

**NEW**

```
Both phenomena are the same structural move: one object appearing as two, with the appearance every bit as real as the object. The photon's null-time is the first instance; entanglement is the second. Both are features of the same expanding S³ — the photon's two ends drawn apart in spatial-and-temporal extent, the entangled pair's two ends in spatial extent — and in neither case is there anything along the inside of the link for the reader's intuition to put a traveller on.
```

---

### M6 — the Hubble horizon: a physics correction

The chapter's conservative anchor currently rests on identifying the Hubble radius with the boundary of our causal future. It is not that boundary. The anchor works — it just has to be built on the right surface, and on the right fact, which is that the *observable* patch is bounded and small compared with the S³ radius.

**OLD**

```
Even leaving the framework's argument aside, our access to the universe is bounded by the *Hubble horizon* — the proper distance beyond which space is expanding faster than light can carry information back. Galaxies past this boundary recede at velocities exceeding *c*, not because they move through space at superluminal speeds but because the space between us and them stretches faster than light can cross. Whatever lies past the Hubble horizon is gone from our causal future. We cannot see it, signal it, or be influenced by it.

What this gives us is a hard observational limit. Whatever the global geometry of the universe is, we can only ever measure the patch within our Hubble horizon — and that patch is small enough that, even if the S³'s radius weren't effectively infinite by the framework's argument, the curvature would still be undetectable inside it. The framework's structural argument is the primary claim; the Hubble-horizon argument is the conservative anchor. Both converge.
```

**NEW**

```
Even leaving the framework's argument aside, our access to the universe is bounded. The *Hubble radius* is the proper distance at which space is receding at exactly the speed of light, and it is worth being careful here because it is routinely mistaken for a wall. It is not one: galaxies beyond it recede faster than *c* — not by moving through space at superluminal speeds, but because the space between us and them stretches faster than light can cross it — and we nonetheless see a great many of them, because light emitted out there can be handed inward from one stretch of space to the next until it reaches a region receding more slowly than it travels. The surface that really does bound what we can ever see or signal is the *cosmological event horizon*, further out, and what lies beyond it is genuinely gone from our causal future.

What this gives us is a hard observational limit either way. Whatever the global geometry of the universe is, we can only ever measure inside a bounded patch — and that patch is small enough that, even if the S³'s radius weren't effectively infinite by the framework's argument, the curvature would still be undetectable inside it. The framework's structural argument is the primary claim; the bounded-patch argument is the conservative anchor. Both converge.
```

---

### M7 — the section heading: the Chapter 4 retitle pointer

**OLD**

```
## Towards Time as Expansion
```

**NEW**

```
## Towards Time and Expansion
```

---

### M8 — the paragraph under that heading

Carries both the emergence register and the zero-proper-time residue Ch 2 v8 removed from the corresponding phrase.

**OLD**

```
The picture is now in place. Closed three-dimensional space. No interior, no exterior. Expansion as a change in the metric, parameterised by *N*. Photons riding the wavefront. Entanglement as zero-proper-time features of the same surface. Time, somehow, emerging from expansion through the boundary expansion field — but this last piece is the one we have not yet worked out.

The next chapter takes that piece up directly. What does it mean for time to emerge from expansion? What role does the boundary expansion field play in setting the rate? And what does this tell us about the difference between the world we observe and the world the framework actually describes?
```

**NEW**

```
The picture is now in place. Closed three-dimensional space. No interior, no exterior. Expansion as a change in the metric, parameterised by *N*. Photons riding the wavefront. Entanglement as a feature of the same surface with nothing accumulating along it. Time bound to that expansion through the boundary expansion field — but the nature of the binding, and its rate, is the piece we have not yet worked out.

The next chapter takes that piece up directly. If time and expansion are one structure rather than two, what exactly is the relation between them, and why is *N* the coordinate that can be written down first? What role does the boundary expansion field play in setting the rate? And what does this tell us about the difference between the world we observe and the world the framework actually describes?
```

---

### M9 — a prose defect

**OLD**

```
the universe is one closed three-dimensional space, finite in volume but with no edge or boundary, and every point on it's part of the same manifold.
```

**NEW**

```
the universe is one closed three-dimensional space, finite in volume but with no edge or boundary, and every point on it is part of the same manifold.
```

---

## 2. Flags

**N1 — Ω_k = 0 needs a register check, and it is AC's, not PC's.** Manifest §3 lists **Ω_k = 0** under *Derived / structural*. Chapter 3's position is that the universe is a closed S³ whose radius has grown so vast that curvature is undetectable — which is Ω_k ≈ 0, not Ω_k = 0. Strictly, a closed S³ of finite radius cannot have Ω_k exactly zero; exact flatness and genuine closure are different geometries. Ch 3's reading is the sensible one and I have not patched it, but §3's bare "Ω_k = 0" reads as a claim of exact flatness, which would contradict the closure the whole framework rests on. Either §3 should read "Ω_k → 0 (closed; radius vast)" or Part 3 says something more precise that §3 has compressed. **Part 3 wins; PC has not read it.** Not blocking, but it is the framework's own geometry, so it should not sit ambiguous.

**N2 — M6 is a correction to physics, not to register, and PC would like AC's eye on it.** The Hubble-radius / event-horizon distinction as I have written it is standard cosmology and I am confident in it. What I am less confident about is whether the corpus's own treatment of the Hubble horizon — which appears in Part 1 §V in the conformal-reset material, where R_H does load-bearing work — uses the term in the same sense Ch 3 was using it, or in the correct one. If Part 1 has inherited the same conflation, this is not a Book defect but a corpus one, and it would matter there in a way it does not here, because R_H enters the trigger condition numerically. **Recommend AC check Part 1 §V's use of R_H against M6 before the Book ships.** This is the one finding today that could have consequences outside the Book.

**N3 — the two-readings refrain may survive elsewhere.** Ch 1 v10 retired it; Ch 3 v6.1 still carried three instances, which means the v10 sweep was chapter-local rather than Book-wide. Chapters 6 onward, the popular editions and Appendix A have not been checked for it. It should be added to the mechanical sweep alongside the cosmic-time rule, since both are single-phrase searches with settled replacements.

**N4 — the retitle sweep is now closed, pending the deposit register.** M7 is the last forward pointer PC has found. Chapters 1, 2 and 5 refer to Chapter 4 by number only. The Book deposit register remains unaudited and is AC's file.

---

## 3. Where the Book campaign stands

| File | State |
|---|---|
| Prelude → v8 | proposed (with Ch 1) |
| Ch 1 → v11 | proposed |
| Ch 2 → v8 | proposed |
| Ch 3 → v7 | proposed (this file) |
| Ch 4 → v9 | **ratified**, awaiting Cursor |
| Ch 5 → v8 | proposed |
| Ch 15 → v4 | **ratified**, awaiting Cursor |
| Appendix C → v1.4 | **ratified** (A1–A5), awaiting Cursor |

The opening arc and both ledger documents are now drafted or ratified. What has never had a pass of any kind: **Chapters 6–14**, the **popular editions**, and **Appendix A** (which syncs from the Reader edition). The popular editions are the largest remaining body of uncorrected photon-frame prose in the corpus and should go before Appendix A, since A takes its text from them.

---

## 4. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ Chapter 3 v7 patch set** (`Handoff_PC_to_Greg_Cursor_Chapter03_v7_Patch_Set_20260924.md`, PC, 2026-09-24) — M1–M9 on `Chapter_03_A_Closed_Universe_v6_1.md`. Emergence register (4); retired "two readings" refrain removed (3 instances — Ch 1 v10's sweep was chapter-local, see N3); Chapter 4 retitle pointer in the `Towards Time as Expansion` heading (M7 — last known pointer, N4); cosmic time (M2); zero-proper-time residue (M8); prose defect (M9). **Physics correction M6: the chapter conflated the Hubble radius with the boundary of our causal future; corrected to the cosmological event horizon, with the flatness anchor rebuilt on the bounded observable patch.** Flags N1 (Ω_k = 0 vs closure — AC/Part 3), **N2 (check Part 1 §V's R_H against M6 — possible corpus-side conflation where it enters the trigger condition numerically)**, N3 (two-readings sweep is Book-wide), N4 (retitle sweep closed pending deposit register). **Status: PROPOSED, awaiting Greg.**
```

---

## 5. On ratification

Cursor applies M1–M9 byte-exact, saves as `Chapter_03_A_Closed_Universe_v7.md`, leaves v6.1 in place, match-or-report, never force; re-renders; returns the completion handoff.

PC then takes the **popular editions**, which have had no A9 pass and feed Appendix A. Before drafting those, PC recommends the mechanical sweep be specified as one Cursor job across the whole Book and both editions — the cosmic-time rule, the two-readings refrain, and the photon-frame vocabulary all now have settled replacements, and finding the instances is a search rather than a judgement. PC will write that specification on your word; it will save a good deal of chapter-by-chapter reading on Chapters 6–14.
