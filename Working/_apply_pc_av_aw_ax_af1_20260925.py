# Apply PC AV/AW/AX/AN4-revised + AF1 (2026-09-25)
from pathlib import Path
import re

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
log = []

def replace_once(text, old, new, label):
    if old not in text:
        raise RuntimeError(f"{label}: OLD not found")
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: OLD count={n}")
    return text.replace(old, new)

# ---------- AF1 Appendix C ----------
appc_src = book / "Appendix_C_The_Open_Ledger_v1_5_DRAFT_PC_20260925.md"
appc = appc_src.read_text(encoding="utf-8")
af1_old = (
    "An almost-certainly-untestable prediction, stated plainly rather than in disguise, "
    "because stating it costs nothing and a surprise observation would score it."
)
af1_new = (
    "Two facts keep that from being more than it is. The heavy scale makes observation almost "
    "certainly unreachable, so this is a prediction written for the record rather than one anyone "
    "expects to collect. And equality is less rare than it sounds: drawing the relevant mixing "
    "structures at random produces a ratio this close to one about one time in ten. That is "
    "substantial, and it is not overwhelming, and the framework says so rather than leaving the "
    "reader to supply their own odds. What the claim is finally worth is that the framework "
    "committed to a definite value of a ratio it was under no obligation to speak to at all — "
    "stated plainly rather than in disguise, because stating it costs nothing and a surprise "
    "observation would score it."
)
if "one time in ten" in appc or "once in ten" in appc:
    log.append("SKIP AF1: already present")
    appc_out = appc
else:
    if af1_old not in appc:
        # show hook for debug
        m = re.search(r"\*\*Charged-lepton flavour violation\.\*\*.{0,1200}", appc, re.S)
        raise RuntimeError("AF1 OLD missing; tail=" + repr((m.group(0)[-250:] if m else "NO BLOCK")))
    appc_out = replace_once(appc, af1_old, af1_new, "AF1")
    log.append("OK AF1")
(appc_src.with_name("Appendix_C_The_Open_Ledger_v1_6_DRAFT_PC_20260925.md")).write_text(appc_out, encoding="utf-8")
log.append("WROTE AppC v1.6")

# ---------- AN4 revised Chapter 3 ----------
ch3 = book / "Chapter_03_A_Closed_Universe_v8.md"
t3 = ch3.read_text(encoding="utf-8")
an4_old = (
    "after sixty e-folds, it is e^60 ≈ 10^26 times larger."
)
# tolerate unicode superscripts / approx variants
candidates = [
    an4_old,
    "after sixty e-folds, it's e⁶⁰ ≈ 10²⁶ times larger.",
    "after sixty e-folds, it's e^60 ≈ 10^26 times larger.",
    "after sixty e-folds, it is e⁶⁰ ≈ 10²⁶ times larger.",
]
an4_new = "after fifty e-folds, it's e⁵⁰ ≈ 5 × 10²¹ times larger."
an4_new_ascii = "after fifty e-folds, it is e^50 ≈ 5 × 10^21 times larger."
applied = False
for c in candidates:
    if c in t3:
        # choose NEW matching style
        new = an4_new if "⁶⁰" in c or "it's" in c else an4_new_ascii
        if "it's" in c and "⁶⁰" in c:
            new = an4_new
        elif "it's" in c:
            new = "after fifty e-folds, it's e^50 ≈ 5 × 10^21 times larger."
        t3 = replace_once(t3, c, new, "AN4")
        applied = True
        break
if not applied:
    # fuzzy
    m = re.search(r"after sixty e-folds,.{}{0,80}larger\.", t3)
    if not m:
        m = re.search(r"after sixty e-folds,.+?larger\.", t3)
    if not m:
        raise RuntimeError("AN4: sixty locus not found")
    t3 = t3[: m.start()] + an4_new + t3[m.end() :]
    log.append("OK AN4 fuzzy")
else:
    log.append("OK AN4")
(book / "Chapter_03_A_Closed_Universe_v9.md").write_text(t3, encoding="utf-8")
log.append("WROTE Ch3 v9")

# ---------- AV Chapter 6 ----------
ch6 = book / "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6_1.md"
t6 = ch6.read_text(encoding="utf-8")

# AV3-ish: Gleason paragraph — remove imported geometry
av3_old = (
    "But the geometry it is selected on is *imported*, not derived here. The chapter's claim, then, "
    "is the one its opening has already named: not that the Born rule appears from nothing, but that "
    "— given what quantum mechanics already assumes about the geometry of states — the form of the "
    "probability rule is no longer a free choice."
)
av3_new = (
    "And the geometry it is selected on is not an abstract postulate the framework borrows from "
    "quantum mechanics. It is the physical three-sphere — the quaternionic piece of the larger "
    "algebra, the same object that supplies the SU(2) factor of the weak force and the boundary "
    "geometry this book has described since Chapter 3. The chapter's claim, then, is the one its "
    "opening has already named: not that the Born rule appears from nothing, but that — given the "
    "geometry the framework attributes to the world — the form of the probability rule is no longer "
    "a free choice."
)
if av3_old in t6:
    t6 = replace_once(t6, av3_old, av3_new, "AV3")
    log.append("OK AV3")
else:
    # alternate from file read
    av3_old2 = (
        "But the geometry it is selected from is *imported*, not derived here. The chapter's claim, then, "
        "is the one its opening has already named: not that the Born rule appears from nothing, but that "
        "— given what quantum mechanics already assumes about the geometry of states — the form of the "
        "probability rule is no longer a free choice."
    )
    if av3_old2 in t6:
        t6 = replace_once(t6, av3_old2, av3_new, "AV3")
        log.append("OK AV3 alt")
    else:
        raise RuntimeError("AV3 OLD not found")

# AV1+AV2+AV6: replace retreat block
av_block_old = (
    "We should be careful about how strong a claim this is. The framework's earlier drafts of this "
    "chapter said that the S³ in quantum mechanics *is* the same S³ as the universe — one three-sphere, "
    "one phase identification, one Hopf projection. That is more than what the structural argument "
    "supports. What the structural argument supports is the weaker but still substantive claim that "
    "the geometric apparatus of quantum mechanics — the three-sphere state space, the U(1) phase to be "
    "quotiented, the Hopf fibration to the Bloch sphere — *shares the Hopf fibration structure* of the "
    "universe's geometry as the framework reads it. The same kind of object, with the same kind of phase, "
    "projected the same way, in both contexts. Whether quantum-mechanical S³ and universe-S³ are "
    "*literally identified* — one geometric object playing both roles — is a stronger claim than the "
    "framework currently supports, and the chapter retreats from it.\n\n"
    "The weaker claim is still doing structural work. If quantum mechanics's S³ and the universe's S³ "
    "shared none of this structure — if they merely happened to be three-spheres for unrelated reasons — "
    "the Born rule's specific form would be a coincidence, separate from the framework's geometric "
    "programme. What the shared Hopf-fibration structure says is that the Born rule's specific form "
    "follows from the same kind of geometric setup the framework attributes to the universe at large: "
    "a three-sphere with a phase to be quotiented, projected through the Hopf fibration. The framework's "
    "claim is that this is not a coincidence. Both contexts inherit the same geometric apparatus because "
    "both involve the kind of three-sphere-with-U(1)-phase structure the framework places at the heart "
    "of physics.\n\n"
    "This is the unification claim the chapter is making, in its honest form. The reason quantum "
    "mechanics has the specific probability rule it has is that the state space of quantum particles "
    "is a three-sphere with a U(1) phase, and the framework's reading of the universe places the same "
    "kind of structure at the heart of physics. The Born rule is what falls out when you do the "
    "geometry on a spin-1/2 system. The unification is structural at the level of *shared "
    "Hopf-fibration apparatus*, not literal identification of one S³ with another. The number 2 "
    "emerges as a topological feature of the geometry that quantum mechanics has — and that the "
    "framework's reading of the universe shares.\n\n"
    "Which is to say: the framework does not derive the qubit's geometry. It takes it from quantum "
    "mechanics, as everyone does, and shows that the same kind of geometry it attributes to the "
    "universe is what the rule falls out of. That is a claim about kinship, not about provenance."
)

av_block_new = (
    "We should be careful about how strong a claim this is, because it is stronger than it looks. "
    "The framework's reading is not that the quantum-mechanical three-sphere resembles the universe's, "
    "or shares its shape, or does the same kind of work. It is that they are one object. The "
    "three-sphere carrying a spin-½ state is the quaternionic part of the larger algebra the "
    "pre-temporal regime lives in — and that same part is the SU(2) factor of the weak force, and the "
    "boundary geometry this book has been describing since Chapter 3. The Hopf circle a quantum state "
    "quotients out is not merely analogous to a gauge fibre. It is the hypercharge fibre. The "
    "framework's papers state this in terms, and add that it is not a metaphor: the inner product is "
    "computed on the physical three-sphere, and the angle in cos²(θ/2) is an angle on the sphere we "
    "inhabit.\n\n"
    "That is the strong reading, and it is doing the structural work. The Born rule's form follows "
    "from the geometry the framework attributes to the universe **because it is that geometry**, not "
    "because both happen to be three-spheres. The number 2 emerges as a topological feature of the "
    "physical boundary.\n\n"
    "And the same two-sphere does double duty, in a way worth holding onto, because two later chapters "
    "turn on it. For a resolved particle, the Hopf fibre is the phase that has to be quotiented away, "
    "and the Bloch sphere is where the probability rule lives. For the neutrino — Chapter 8's "
    "unresolved species — that same fibre is the phase it never engages, and that same sphere is the "
    "base it never reaches. Both arrive at the same two-sphere, because a three-sphere has only one "
    "such bundle structure to offer. Same geometry, opposite relationship to it. The number that sets "
    "the dark-matter coupling in Chapter 9 lives on the sphere the Born rule projects onto.\n\n"
    "One further honesty, because the papers that own this claim do not hide it. What is closed is "
    "the *activation* of the rule: the Hopf fibration does not pre-exist the gauge birth; it is "
    "created by it. What remains open is whether the specific quadratic form can be derived from still "
    "less — pushed back to why a complex Hilbert space, and why bilinearity in amplitude. The chapter "
    "reports a reformulation on the world's geometry, not a derivation of that geometry from nothing."
)

if av_block_old not in t6:
    raise RuntimeError("AV block OLD not found")
t6 = replace_once(t6, av_block_old, av_block_new, "AV1-2-6-7")
log.append("OK AV1/2/6/7 block")

(book / "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v7.md").write_text(t6, encoding="utf-8")
log.append("WROTE Ch6 v7")

# ---------- AW Chapter 8 ----------
ch8 = book / "Chapter_08_The_Unresolved_Particle_v5.md"
t8 = ch8.read_text(encoding="utf-8")
aw1_old = (
    "**Charged leptons must never oscillate.** Resolved species are pinned; pinned species cannot "
    "slide between generations. A muon must never be caught turning into an electron the way "
    "neutrinos turn into each other. The searches exist and are formidably sensitive — the decay "
    "μ → eγ is excluded down to branching ratios below four parts in ten trillion — and the "
    "framework requires the emptiness to persist. A confirmed generation-oscillation of any "
    "resolved fermion breaks the geometric-sliding picture at its root."
)
aw1_new = (
    "**Charged leptons must never oscillate between generations.** Resolved species are pinned; "
    "pinned species cannot slide. A muon must never be caught turning into an electron the way "
    "neutrinos turn into each other, and searches for flavour violation of that oscillatory kind "
    "have come up empty. What the framework requires is that they stay empty. The narrowness of "
    "that requirement matters: the framework does **permit** rare loop-mediated decays such as "
    "μ → eγ, at rates the seesaw's heavy scales push far below anything a current experiment could "
    "reach — Appendix C carries the relation those decays would satisfy. A confirmed **generation "
    "oscillation** of a resolved fermion is what would break the geometric-sliding picture at its "
    "root. An eventual rare decay would not."
)
if aw1_old not in t8:
    raise RuntimeError("AW1 OLD not found; snippet=" + repr(t8[t8.find("Charged leptons") : t8.find("Charged leptons") + 280]))
t8 = replace_once(t8, aw1_old, aw1_new, "AW1")
log.append("OK AW1")

# AW2 derives -> places
for old, new, lab in [
    (
        "and **derives** the heavy scales at structural slots instead of dialling them",
        "and **places** the heavy scales at structural slots instead of dialling them",
        "AW2a",
    ),
    (
        "and derives the heavy scales at structural slots instead of dialling them",
        "and places the heavy scales at structural slots instead of dialling them",
        "AW2b",
    ),
]:
    if old in t8:
        t8 = replace_once(t8, old, new, lab)
        log.append(f"OK {lab}")
        break
else:
    # softer search
    if re.search(r"derives the heavy scales", t8):
        t8 = re.sub(r"derives the heavy scales", "places the heavy scales", t8, count=1)
        log.append("OK AW2 regex")
    else:
        log.append("WARN AW2: derives-heavy not found")

(book / "Chapter_08_The_Unresolved_Particle_v6.md").write_text(t8, encoding="utf-8")
log.append("WROTE Ch8 v6")

# ---------- AX Chapter 7 ----------
ch7 = book / "Chapter_07_The_Gauge_Birth_v4.md"
t7 = ch7.read_text(encoding="utf-8")

ax1 = (
    "\n\nA word about **embedding depth**, because the term has two jobs and the difference matters "
    "later. At the gauge birth it names a property of a fundamental mode — how strongly that mode "
    "engages |Φ_NTE|, which is what fixes its place in the locking order and becomes its Yukawa "
    "coupling. That is the sense this chapter and the next one use. But what embeds a **thing** in "
    "the expansion, now, is its rest energy, and for anything composite the rest energy is mostly "
    "not Yukawa at all: a proton's mass is about ninety-nine per cent the binding energy of massless "
    "gluons. Chapter 1 made that point and it stands — rest energy is what embeds, wherever the rest "
    "energy came from. The two readings coincide for a fundamental fermion and part company for "
    "everything built out of them."
)

ax2 = (
    "\n\nOne caution about the counting, because this book uses **N** for more than one thing and a "
    "reader will try to put them on a single axis. **N_lock ≈ 0.1** measures the **span** of the "
    "locking transition — how much expansion the cascade takes to complete, with the heaviest modes "
    "locking around a thousandth of an e-fold and the leptons around a hundredth. It is not a depth "
    "on the inflationary counter, which measures how far back the structures we read in the microwave "
    "background left the horizon. And neither is the total run, which the framework puts in the "
    "region of a hundred and forty e-folds (Part 1). Three counters, three jobs, one letter."
)

# Insert AX1 after first Mass/embedding depth bullet paragraph
needle = "The **ordering** of masses follows from *δ*; the **specific δ values** are structural inputs the framework has not yet derived from deeper principles — honest scope, and Appendix C carries the gap by name."
if needle not in t7:
    # alt from earlier read
    needle = "The **ordering** of masses follows from *δ*; the **specific δ values** are structural inputs the framework has not yet derived from deeper principles — honest scope, and Appendix C carries the gap by name."
if needle not in t7:
    m = re.search(r"\*\*3\. Mass\.\*\*.+?\n\n", t7, re.S)
    if not m:
        raise RuntimeError("AX1 insert point not found")
    t7 = t7[: m.end()] + ax1.lstrip("\n") + "\n" + t7[m.end() :]
    log.append("OK AX1 after Mass section")
else:
    t7 = replace_once(t7, needle, needle + ax1, "AX1")
    log.append("OK AX1")

# Insert AX2 after N_lock mention
nlock = re.search(r"N_lock[^\n]{0,120}", t7)
if not nlock:
    raise RuntimeError("AX2: N_lock not found")
# find end of paragraph containing first N_lock
pos = nlock.start()
para_end = t7.find("\n\n", pos)
if para_end < 0:
    raise RuntimeError("AX2: para end not found")
if "Three counters, three jobs" not in t7:
    t7 = t7[:para_end] + ax2 + t7[para_end:]
    log.append("OK AX2")
else:
    log.append("SKIP AX2: already present")

(book / "Chapter_07_The_Gauge_Birth_v5.md").write_text(t7, encoding="utf-8")
log.append("WROTE Ch7 v5")

print("\n".join(log))
print("ALL_DONE")
