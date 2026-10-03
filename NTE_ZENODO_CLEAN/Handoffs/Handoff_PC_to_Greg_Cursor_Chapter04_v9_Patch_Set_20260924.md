# Handoff — PC → Greg (ratify) → Cursor (apply): Chapter 4 v9 patch set

**From:** PC
**To:** Greg (ratification), then Cursor (byte-exact apply + rename)
**Date:** 2026-09-24
**Base file:** `Book\Chapter_04_Time_as_Expansion_v8.md` (canonical, 30,251 B)
**Target:** `Book\Chapter_04_Time_and_Expansion_v9.md` — v8 left in place
**Status:** PROPOSED — not ratified

---

## 0. What this pass found

Chapter 4 carries three campaigns at once — A9, the emergence register, the retitle — and two of them land on the same sentence, so the pass is structural rather than cosmetic.

Two findings before the patches, because they change what the chapter says rather than how it says it.

**The chapter's central pedagogical move is the A9 error, stated as the chapter's thesis.** Ch 4 runs its whole ledger off Higgs coupling: *"A particle's Higgs coupling sets how deeply it is embedded in the expanding boundary"*, *"the Higgs decides who rides"*, *"The photon has exactly one relevant zero: its Higgs coupling"*, *"the Standard Model's mass dial and the framework's time dial are the same dial"*. A9 fixes embedding depth to **rest energy**, not Higgs coupling. The difference is not pedantic. A proton's rest energy is overwhelmingly strong-interaction binding energy, not the Higgs couplings of its quarks — so on the Higgs reading, almost all of a reader's own participation in time goes unaccounted for. Corrected, the move survives and gets *better*: the bridge between the two ledgers is E = mc², which is a stronger sentence than the one it replaces.

**The chapter says "proper time" throughout where the relation gives cosmic time.** dt/dN = 1/(β_NTE|Φ_NTE|²) is the cosmic lapse. Ch 4 calls its output proper time in eleven places, including in the gravitational-dilation section, where the distinction is the entire subject. The Prelude took this correction at v7; Ch 4 has not had it. Corrected, the dilation section gains the thing it was missing — dilation is the ratio of a local clock to cosmic time, which is what makes it a *ratio* at all.

**On the emergence register.** Greg's ruling — neither emergent from the other, intrinsically bound, possibly the same phenomenon — does not collide with the corpus's N-primary / t-derived ontology, and the patches keep them apart deliberately. *N* and *t* remain two coordinates with *N* primary, because *N* is the one that can be written without circularity; that claim is untouched. What changes is the claim about *time and expansion*, which are not two things one of which produces the other. The chapter already had the right instinct — *"two readings of one expansion"* — and the patches make that the stated position instead of a decoration on an emergence claim.

---

## 1. Patches

### C1 — the retitle

**OLD**

```
# Chapter 4 — Time as Expansion
```

**NEW**

```
# Chapter 4 — Time and Expansion
```

**Cursor also renames the file** to `Chapter_04_Time_and_Expansion_v9.md`. The title appears in the Book deposit register and in Ch 3's forward pointer; both need the same change, and PC has not audited Ch 3 for it — see G3.

---

### C2 — opening: the second commitment restated

**OLD**

```
The previous chapter established that we live on a closed three-dimensional space — an S³, expanding, with no interior to access and no exterior to escape into. The space itself is what is expanding, and the parameter that counts the expansion is *N*, the number of e-folds. That picture is now in place. What remains is the second of Chapter 3's two framework commitments. Surface-only — no ambient embedding — was the first, and did its work in the previous chapter. Time emerging from expansion is the second, and this chapter develops it directly: showing how time arises from the expansion, and what that emergence implies about the nature of past, present, and future.
```

**NEW**

```
The previous chapter established that we live on a closed three-dimensional space — an S³, expanding, with no interior to access and no exterior to escape into. The space itself is what is expanding, and the parameter that counts the expansion is *N*, the number of e-folds. That picture is now in place. What remains is the second of Chapter 3's two framework commitments. Surface-only — no ambient embedding — was the first, and did its work in the previous chapter. The binding of time to expansion is the second, and this chapter develops it directly.

A word on that binding, because the chapter's title turns on it. It would be easy to say that time emerges from expansion, and the framework said so for years. It is not quite right, and the imprecision costs something. Emergence is a one-way word: it puts expansion underneath and time on top, as though one were the cause and the other the product. The framework's actual position is flatter and stranger. Time and expansion are not two phenomena, one of which generates the other. They are one structure, and duration and growth are what it looks like read from two directions. Nothing here derives time from expansion; what the chapter derives is the *rate* — how much duration one e-fold of growth is worth, and for what.
```

---

### C3 — "What Time Is Not": the photon paragraph (A9)

Two violations in three sentences: the photon has no frame to speak from (the four-velocity is 0/0 — undefined, not degenerate), and "proper time identically zero" is the degenerate reading A9 retired.

**OLD**

```
But the picture has one specific failure mode, which Chapter 1 already identified. The photon does not fit it. From a photon's own frame, time does not pass between emission and absorption. The photon's proper time is identically zero. If time is a background dimension we move through, the photon should be moving through it like everything else — and it isn't. The textbook picture handles this by saying that the photon's worldline is a *null geodesic*, on which the spacetime interval vanishes, and treating this as a curiosity rather than a clue.
```

**NEW**

```
But the picture has one specific failure mode, which Chapter 1 already identified. The photon does not fit it. Not because the photon experiences an eternity compressed to nothing, and not because its clock reads zero — the photon has no frame to stand in and no clock to read, and Chapter 1 spent some care establishing that the question is undefined rather than merely extreme. The line has no ruler along it. What can be said without a frame is this: between emission and absorption there is no interval to divide, nothing along the connection that counts. If time were a background dimension we move through, the photon should be moving through it like everything else — and there is no sense in which it is. The textbook picture handles this by calling the photon's worldline a *null geodesic*, on which the spacetime interval vanishes, and treating the vanishing as a curiosity rather than a clue.
```

---

### C4 — "What Time Is": the two opening paragraphs

The rest-energy correction. This is the chapter's spine.

**OLD**

```
In the framework, time is what emerges from the universe's expansion when the expansion is registered by matter — and the registration has two parts, played by two different fields.

The cleanest way to introduce the picture is by the parallel the reader will carry for the rest of the book. The Standard Model Higgs is the field that gives particles their mass: an electron has mass because it couples to the Higgs field; a photon has no mass because it does not. In the framework, that same Higgs coupling does double duty in a second ledger: it is what determines whether a particle *participates in time at all*. A particle's Higgs coupling sets how deeply it is embedded in the expanding boundary, and embedded matter accumulates proper time as the boundary expands. A particle with zero Higgs coupling — no mass — is also a particle with zero embedding depth, and it accumulates no proper time. One coupling, two consequences: mass in the Standard Model's books, participation in time in the framework's.
```

**NEW**

```
In the framework, time is what the universe's expansion amounts to where matter registers it — and the registration has two parts, played by two different fields.

The cleanest way to introduce the picture is by the parallel the reader will carry for the rest of the book. It needs stating carefully, though, because the obvious version of it is wrong, and the framework used to state the obvious version. The Standard Model Higgs is the field that gives fundamental particles their mass: an electron has mass because it couples to the Higgs field; a photon has no mass because it does not. The tempting move is to run the framework's second ledger straight off that coupling — to say that a particle's Higgs coupling is what embeds it in the expanding boundary. It is not. What sets embedding depth is **rest energy**.

For an electron the difference does not show, because an electron's rest energy is essentially the Higgs coupling's doing and the shortcut costs nothing. For a proton it shows immediately: the overwhelming majority of a proton's rest energy is the binding energy of the strong interaction, not the Higgs couplings of the three quarks inside it. The reader is made of protons and neutrons. If Higgs coupling were the dial, almost all of your own participation in time would be unaccounted for.

So the ledger reads: rest energy is what embeds, and embedded matter accumulates duration as the boundary expands. A thing with zero rest energy has zero embedding depth and accumulates nothing — and the photon is the only clean case of it in nature. One quantity, two books: mass in the Standard Model's, embedding depth in the framework's. The bridge between the two books is the oldest equation in modern physics, which is a better foundation than a coupling constant.
```

---

### C5 — the |Φ_NTE| division-of-labour paragraph

**OLD**

```
The second field is the framework's own addition, the *boundary expansion field* |Φ_NTE| — and its job is different in kind. |Φ_NTE| does not couple to particles at all; giving fermions their masses is the Higgs's role, and the framework leaves it there. What |Φ_NTE| does is set the *rate*: its strength governs how fast the boundary is expanding, and therefore how much proper time each e-fold of expansion is worth for the matter embedded in it. The division of labour, in one line: the Higgs decides *who rides*; |Φ_NTE| decides *how fast the ride runs*. In the parallel the book will keep using — the Higgs is the field that gives mass; |Φ_NTE| is the field that gives time — the "gives" works at the level of the whole ride: the field whose strength makes expansion into duration.
```

**NEW**

```
The second field is the framework's own addition, the *boundary expansion field* |Φ_NTE| — and its job is different in kind. |Φ_NTE| does not couple to particles at all; giving fundamental fermions their masses is the Higgs's role, and the framework leaves it there. What |Φ_NTE| does is set the *rate*: its strength governs how fast the boundary is expanding, and therefore how much duration each e-fold of expansion is worth for the matter embedded in it. The division of labour, in one line: rest energy decides *who rides*; |Φ_NTE| decides *how fast the ride runs*. In the parallel the book will keep using — the Higgs is the field that gives mass; |Φ_NTE| is the field that gives time — the "gives" works at the level of the whole ride: the field whose strength makes expansion into duration. The Higgs keeps its place in the parallel because it is where a large part of rest energy comes from, not because it is the dial itself.
```

---

### C6 — the inversion paragraph: cosmic time, not proper time

**OLD**

```
This says: for each e-fold of expansion, an interval of proper time accumulates. The interval depends on the strength of the boundary expansion field. The stronger the field, the smaller the time interval per e-fold. The weaker the field, the larger the interval. Time is not a thing that ticks along independently of expansion. Time is what accumulates with expansion at the rate that |Φ_NTE| sets — for the matter whose Higgs coupling has embedded it in the boundary.
```

**NEW**

```
This says: for each e-fold of expansion, an interval of time accumulates. The interval depends on the strength of the boundary expansion field. The stronger the field, the smaller the interval per e-fold. The weaker the field, the larger it is.

One thing to fix now, because the rest of the chapter depends on it. The time this equation delivers is **cosmic** time — the universe's own clock, the time kept by an observer at rest in the mean expansion. It is not the proper time of any particular observer, who may be moving, or sitting in a gravity well, or both. That is a second step, and the section after next takes it. Cosmic time first, because it is the one the geometry hands over directly; proper time is what a local clock makes of it.
```

---

### C7 — the integral paragraph

**OLD**

```
This is the formal statement of how *t* emerges from *N*. Time, in the framework, is the integrated inverse of the Hubble rate along the e-fold history. The "rate at which time passes" is just another way of describing how rapidly the universe is currently expanding.
```

**NEW**

```
This is the formal statement of how *t* is recovered from *N*. Cosmic time, in the framework, is the integrated inverse of the Hubble rate along the e-fold history. The "rate at which time passes" is another way of describing how rapidly the universe is currently expanding — and the word *another* is doing real work there, because the two descriptions are not related as effect to cause. They are the same fact, taken down in two units.
```

---

### C8 — the clarifying note: keep, sharpen the register

**OLD**

```
A clarifying note before going further. This chapter and others will sometimes use production-flavoured language — "the field that gives time," "what causes time to pass," "the rate at which time accumulates." That language is a working picture for the reader. The framework's fundamental statement is more careful: H = β_NTE|Φ_NTE|² is a *geometric constraint* relating two quantities in the manifold's structure (the local expansion rate and the local field strength), and the proper-time coordinate t is then defined by integrating the inverse of this constraint along the e-fold history — t is a proportionality definition, not a separate dynamical law. The production-flavoured language is an effective description; the underlying claim is that time and the boundary expansion field are two readings of the same geometric structure, related by the constraint. Two readings, one structure — the framework's signature move applied here to time itself.
```

**NEW**

```
A clarifying note before going further. This chapter and others will sometimes use production-flavoured language — "the field that gives time," "what causes time to pass," "the rate at which time accumulates." That language is a working picture for the reader, and it is the language the framework's own name inherited. The fundamental statement is more careful: H = β_NTE|Φ_NTE|² is a *geometric constraint* relating two quantities in the manifold's structure — the local expansion rate and the local field strength — and the cosmic-time coordinate t is then defined by integrating the inverse of that constraint along the e-fold history. t is a proportionality definition, not a separate dynamical law. Nothing is being produced. The underlying claim is that time and the boundary expansion field are two readings of the same geometric structure, related by the constraint, and that neither is underneath the other. Two readings, one structure — the framework's signature move applied here to time itself, and the reason this chapter is called *Time and Expansion* rather than *Time as Expansion*.
```

---

### C9 — "Two Coordinates, One Process": the structural claim, and the framework's name

The framework-name sentence Greg asked for goes here, where the chapter has just finished explaining why *N* is primary — which is exactly the claim the name overstates.

**OLD**

```
So the framework's commitment is not arbitrary. *N* is the coordinate in which the framework's claims can be stated cleanly without circularity. *t* is the coordinate in which most of physics has been done. The relationship between them — *t* emerging from *N* via the boundary expansion field |Φ_NTE| — is the framework's specific structural claim about how time arises.

Two coordinates, one process — the framework's signature move applied to time itself. *N* and *t* are not two parameters but two readings of one expansion, registered from outside as e-folds counted and from inside as duration accumulated. Chapter 1 made the move for the photon; Chapter 3 made it for the universe's surface; here it lands on time itself.
```

**NEW**

```
So the framework's commitment is not arbitrary. *N* is the coordinate in which the framework's claims can be stated cleanly without circularity. *t* is the coordinate in which most of physics has been done. The relationship between them — *t* recovered from *N* through the boundary expansion field |Φ_NTE| — is the framework's specific structural claim, and it is a claim about coordinates, not about which phenomenon is more real.

Two coordinates, one process — the framework's signature move applied to time itself. *N* and *t* are not two parameters but two readings of one expansion, counted from outside as e-folds and accumulated from inside as duration. Chapter 1 made the move for the photon; Chapter 3 made it for the universe's surface; here it lands on time itself.

Which is the moment to be straight about the framework's own name. *Non-Temporal Emergence* is a legacy label from the theory's first years, when the picture really was that time emerged from something prior, and the name has outlived the claim it was built on — the framework no longer holds that expansion produces time, only that the two are one structure with a rate between them. What survives, and what keeps the name honest, is narrower and sharper: at the heart of the framework sits something genuinely non-temporal, and it is the photon. The null connection takes no part in duration at all, and everything in this chapter is an account of what it means for the rest of matter to take part.
```

---

### C10 — the gravitational-dilation section: cosmic vs proper, and the two dilations

**OLD**

```
In the framework, gravitational time dilation has a specific structural reading: the boundary expansion field |Φ_NTE| is *weaker* in regions of higher gravitational potential. The relationship dt/dN = 1/(β_NTE|Φ_NTE|²) means that where |Φ_NTE| is reduced, the rate of proper time accumulation per e-fold increases. Or, putting it the other way around: where mass-energy concentrates curvature locally — which, under the framework's structural reading, is the same fact as the local weakening of the boundary expansion field — the local rate of proper time accumulation per e-fold changes, and clocks register the change as time dilation.
```

**NEW**

```
In the framework, gravitational time dilation has a specific structural reading, and the previous section's distinction is what makes it work. Cosmic time is the universe's clock; a clock in a gravity well is not at rest in the mean expansion, and what it reads is its own proper time. Dilation is the ratio between the two, and the framework says where the ratio comes from: the boundary expansion field |Φ_NTE| is *weaker* in regions of higher gravitational potential. Since the local lapse goes as 1/(β_NTE|Φ_NTE|²), a region where |Φ_NTE| is reduced is a region where the conversion from e-folds to duration runs differently from the cosmic mean. Or, putting it the other way around: where mass-energy concentrates curvature locally — which, under the framework's structural reading, is the same fact as the local weakening of the boundary expansion field — the local conversion rate departs from the cosmic one, and a clock sitting there registers the departure as time dilation.

A boundary worth marking while we are here. This is the *gravitational* dilation, and it is the one the framework offers a structural reading of. The other dilation — the one that comes from relative motion — the framework does not derive and does not claim; it inherits it from special relativity intact, as every theory built on a Lorentzian metric must. Two dilations, one owned and one inherited, and the book will keep them apart.
```

---

### C11 — "Where This Leaves the Photon (Again)": A9 and rest energy together

**OLD**

```
The photon, Chapter 1 established, is not a thing in flight. It's the geometric connection between emission and absorption — one object with two readings: from outside, length in space and time; along the connection itself, both extents vanish together. The two-field picture gives this its mechanism, and gives it with striking economy. The photon has exactly one relevant zero: its Higgs coupling. In the Standard Model's ledger, that zero is why the photon is massless. In the framework's ledger, the *same* zero is why the photon accumulates no time: zero Higgs coupling means zero embedding depth in the expanding boundary, and a structure with no embedding does not enter the dt map at all. It sits on the boundary itself, riding the expansion at the wavefront rather than within the thickness, and the null-time the photon-line registers is exactly that non-participation.
```

**NEW**

```
The photon, Chapter 1 established, is not a thing in flight. It's the geometric connection between emission and absorption — one object measured from outside as a length in space and a length in time, with no ruler along the line itself to measure either with. The two-field picture gives this its mechanism, and gives it with striking economy. The photon has exactly one relevant zero: its rest energy. In the Standard Model's ledger, that zero is why the photon is massless. In the framework's ledger, the *same* zero is why the photon takes no part in time: zero rest energy means zero embedding depth in the expanding boundary, and a structure with no embedding does not enter the dt map at all. It sits on the boundary itself, riding the expansion at the wavefront rather than within the thickness, and the null-time the photon-line carries is exactly that non-participation.
```

---

### C12 — the correlation paragraph

**OLD**

```
So the famous correlation the book opened with — everything massless is timeless, everything massive is temporal, no exceptions — is not two facts that happen to travel together. It is one coupling read in two ledgers. The framework did not have to arrange the correlation; it had to *notice* that the Standard Model's mass dial and the framework's time dial are the same dial. Other species acquired non-zero settings of that one dial at the gauge birth — the cascade event a later chapter develops — and with them acquired both their masses and their participation in time, in one assignment. The heaviest species are the most deeply embedded; the neutrino, at a coupling of roughly one part in a trillion, barely participates at all, a marginality whose consequences become one of the framework's central threads.
```

**NEW**

```
So the famous correlation the book opened with — everything massless is timeless, everything massive is temporal, no exceptions — is not two facts that happen to travel together. It is one quantity read in two ledgers, and the correlation is exact because the quantity is the same quantity. Mass *is* rest energy. The framework did not have to arrange the correspondence; it had to *notice* that the Standard Model's mass dial and the framework's time dial are not two dials. The heaviest species are the most deeply embedded; the neutrino, with a rest energy of order one part in a trillion of the electroweak scale, barely takes part at all, a marginality whose consequences become one of the framework's central threads.

When the dial gets set is a separate question, and the honest answer has two parts. For the fundamental fermions it is set at the gauge birth — the cascade event a later chapter develops — where masses and participation in time are assigned together. For composite matter it is not: most of a proton's rest energy arrives far later, when the strong interaction confines, and on the framework's reading that is when the bulk of ordinary matter takes up its embedding. The reader's own depth in the boundary was not fixed in the first instant.
```

---

### C13 — the closing "for us" paragraph

**OLD**

```
For us, made of atoms whose constituents carry their full couplings, time passes at the rate it does because our matter is embedded in the boundary, and the boundary's expansion — at the rate the local strength of |Φ_NTE| sets — converts e-folds into duration for everything embedded in it. The years we count, the seconds our clocks tick, the moments we experience — all of these are local realisations of dt/dN = 1/(β_NTE|Φ_NTE|²), integrated across the matter we are made of and the e-folds we have lived through.
```

**NEW**

```
For us, made of atoms that carry their full rest energy, time passes at the rate it does because our matter is embedded in the boundary, and the boundary's expansion — at the rate the local strength of |Φ_NTE| sets — converts e-folds into duration for everything embedded in it. The years we count, the seconds our clocks tick, the moments we experience — all of these are local realisations of dt/dN = 1/(β_NTE|Φ_NTE|²), integrated across the matter we are made of and the e-folds we have lived through, and shifted a little from the cosmic rate by the gravity well we happen to sit in.
```

---

### C14 — "What Comes Next": the third pillar

**OLD**

```
We have now seen three pillars of the framework. The first, from Chapter 1, was that the photon's null-time is not a curiosity but the seed observation from which the whole framework grows. The second, from Chapter 3, was that the universe is a closed three-dimensional space without interior or exterior, expanding through e-folds *N*. The third, from this chapter, is that time emerges from this expansion via the boundary expansion field, with H = β_NTE|Φ_NTE|² as the central equation and dt = dN/(β_NTE|Φ_NTE|²) as its inversion.
```

**NEW**

```
We have now seen three pillars of the framework. The first, from Chapter 1, was that the photon's null-time is not a curiosity but the seed observation from which the whole framework grows. The second, from Chapter 3, was that the universe is a closed three-dimensional space without interior or exterior, expanding through e-folds *N*. The third, from this chapter, is that time and that expansion are one structure rather than two, bound by the boundary expansion field, with H = β_NTE|Φ_NTE|² as the central equation and dt = dN/(β_NTE|Φ_NTE|²) as its inversion — and with rest energy deciding which matter the binding reaches.
```

---

### C15 — the last line

**OLD**

```
The shape of time, in the framework, is the shape of expansion. The universe has been expanding, unfolding, and accumulating proper time at every e-fold since whatever counts as the beginning. The geometry of expansion is the record of what has occurred.
```

**NEW**

```
The shape of time, in the framework, is the shape of expansion — not because one was pressed into the other, but because there was only ever one shape. The universe has been expanding, unfolding, and accumulating duration at every e-fold since whatever counts as the beginning. The geometry of expansion is the record of what has occurred.
```

---

## 2. Flags

**G1 — the retitle has dependencies PC has not audited.** Ch 3 forward-points to this chapter, the Book deposit register lists it by title, and Chapter 15 and Appendix C may cite it. Cursor renames the file; someone has to sweep the pointers. PC will do the sweep on request, but it needs the register read first and that is AC's file.

**G2 — the framework-name sentence is firewalled from C21.** You asked for the name sentence with two parts: the surviving non-temporal aspect (the photon), and the universe emerging from a single isolated photon — half a photon really — out of a previous universe. C9 carries the first and **not** the second. C21 is ratified [SPECULATIVE and NON-LOADBEARING] and the discipline is that nothing leans on it; a framework-name sentence in Chapter 4 is about as load-bearing as Book prose gets, and the parent-universe clause would put a speculative claim in the position of explaining what the framework is called. If you want the second half in the Book, the place for it is a late chapter or an appendix note that declares the register first, and PC will draft it there. Say the word and it is a separate patch.

**G3 — the rest-energy correction does not stop at Chapter 4.** The Higgs-coupling-as-embedding-depth line is Chapter 4's thesis, which means it is almost certainly load-bearing in Chapter 5 — the chapter explicitly about why |Φ_NTE| and the SM Higgs cannot be the same field — and probably in Chapter 2. Ch 5 is the most exposed: its whole argument is a comparison between the two fields, and if it draws the comparison through "the Higgs embeds, |Φ_NTE| sets the rate" the correction changes what the comparison is. PC goes to Ch 2 next and Ch 5 after it, unless you want Ch 5 first on exposure grounds. **Recommendation: Ch 5 first.**

**G4 — "proper time" wherever dt/dN is quoted.** Same correction, same reason, across the Book. The Prelude took it at v7; Ch 4 takes it here; Ch 1, Ch 2, Ch 3, Ch 5 and the popular editions have not been checked. This is a mechanical sweep and a good Cursor job once the wording is settled: the rule is that dt/dN delivers cosmic time, and proper time is what a local clock makes of it.

**G5 — N_lock ≈ 0.1, unverified.** Chapter 4 places the gauge birth at *N* less than about 0.1. PC found no N_lock value in the Manifest §3 snapshot and has not read Part 1. Not patched, not confirmed. AC to verify against Part 1 before the Book ships.

**G6 — the confinement point in C12 is PC's reasoning, not a corpus ruling.** That most of a hadron's rest energy — and therefore, under A9, most of its embedding depth — arrives at the QCD confinement transition rather than at gauge birth follows from the corrected rule, but PC has not found the corpus taking a position on it. It is written as a consequence, at that register. If the corpus holds otherwise, C12's second paragraph comes out and the first paragraph stands alone.

---

## 3. Two items from the Appendix C pass, now closed

**A5 is withdrawn — it would have been redundant.** On re-reading `Appendix_C_The_Open_Ledger_v1_3_DRAFT_PC_20260804.md` in full, the appendix **already carries** n_s = 0.9692 and r = 0.0053, already frames the open item as *why* the coupling takes the conformal value rather than as K(Φ) being underived, already records the T_GB promotion-then-demotion, already states the δ_J sign freedom, and already gives DESI at 3.1σ with the void mechanism killed by forward-modelling. Appendix C v1.3 was more current than PC credited it in yesterday's cover note, and **F1 should never have been raised** — the hold was PC's caution carried forward from AC's instruction, not a defect in the file. No A5. The four patches A1–A4 stand as filed.

This also means Chapter 15 was the outlier, not the appendix: the ledger was current and the scorecard had drifted away from it. Every Ch 15 patch you ratified this morning moves the chapter *toward* Appendix C, which is the right direction of travel and worth noting for the record.

**F2 verified.** The CLFV entry in C.4 reads |A(μ→eγ)|²/|A(τ→eγ)|² = tan²θ₂₃. On the framework's own zero-parameter prediction θ₂₃ = π/4, tan²θ₂₃ is exactly 1 — so the appendix states, in trigonometric dress, that the two amplitudes are equal. That is a *stronger* and more falsifiable claim written in a weaker-looking form, and it should be said plainly: the framework predicts the two channels at equal amplitude. Recommend a one-line patch to C.4 in the v1.4 apply. PC will draft it as **A5 (replacement)** on your word.

---

## 4. Registration (discipline 10)

To be added to `NTE_Workflow_Manifest_v10_18.md` §10 under *In progress*:

```
- **Book/ Chapter 4 v9 patch set** (`Handoff_PC_to_Greg_Cursor_Chapter04_v9_Patch_Set_20260924.md`, PC, 2026-09-24) — C1–C15 on `Chapter_04_Time_as_Expansion_v8.md`, retitled and renamed to `Chapter_04_Time_and_Expansion_v9.md`. Three campaigns: A9 (photon frame retired; embedding depth corrected from Higgs coupling to rest energy; cosmic time not proper time; velocity dilation marked inherited), emergence register (time and expansion one structure, neither emergent from the other; N-primary untouched), retitle + framework-name sentence (photon only; parent-universe seed firewalled per C21 register). Flags G1 (retitle pointer sweep), G2 (name sentence scope), G3 (rest-energy correction propagates — Ch 5 most exposed), G4 (cosmic-time sweep Book-wide), G5 (N_lock unverified), G6 (confinement point is PC reasoning). **Status: PROPOSED, awaiting Greg.**
- **Appendix C v1.4 — A5 withdrawn.** Proposed 2026-09-24, withdrawn same day: v1.3 already carries the (n_s, r) values and the ξ framing. F1 retired as raised in error. Replacement A5 offered on the CLFV tan²θ₂₃ = 1 point (F2, verified).
```

---

## 5. On ratification

Cursor applies C1–C15 byte-exact, saves as `Chapter_04_Time_and_Expansion_v9.md`, leaves v8 in place, match-or-report, never force; then re-renders and returns the completion handoff.

PC then goes to **Chapter 5** rather than Chapter 2, on G3's exposure argument — Ch 5 is the two-fields chapter and the rest-energy correction lands hardest there. Ch 2 after it, then Ch 1 v11 and Prelude v8 for the emergence register and the retitle's forward pointers.
