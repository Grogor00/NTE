from pathlib import Path
import re

book = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book")
log = []

def once(text, old, new, label):
    if old not in text:
        raise RuntimeError(label + ": OLD missing")
    if text.count(old) != 1:
        raise RuntimeError(label + f": count={text.count(old)}")
    return text.replace(old, new)

# ===== AF1 =====
appc_path = book / "Appendix_C_The_Open_Ledger_v1_5_DRAFT_PC_20260925.md"
appc = appc_path.read_text(encoding="utf-8")
af1_old = (
    "An almost-certainly-untestable prediction, stated plainly rather than in disguise, "
    "because stating it costs nothing and a surprise observation would score it."
)
# file may omit leading An
if af1_old not in appc:
    af1_old = (
        "almost-certainly-untestable prediction, stated plainly rather than in disguise, "
        "because stating it costs nothing and a surprise observation would score it."
    )
    af1_new = (
        "two facts keep that from being more than it is. The heavy scale makes observation almost "
        "certainly unreachable, so this is a prediction written for the record rather than one anyone "
        "expects to collect. And equality is less rare than it sounds: drawing the relevant mixing "
        "structures at random produces a ratio this close to one about one time in ten. That is "
        "substantial, and it is not overwhelming, and the framework says so rather than leaving the "
        "reader to supply their own odds. What the claim is finally worth is that the framework "
        "committed to a definite value of a ratio it was under no obligation to speak to at all — "
        "stated plainly rather than in disguise, because stating it costs nothing and a surprise "
        "observation would score it."
    )
    # capitalise if preceded by sentence end
    idx = appc.find(af1_old)
    if idx < 0:
        raise RuntimeError("AF1: still missing")
    # if previous nonspace is letter, keep lowercase start; if . or start, capitalize Two
    prev = appc[:idx].rstrip()
    if not prev.endswith(".") and not prev.endswith("!"):
        # mid-sentence continuation after comma?
        pass
    af1_new = "Two" + af1_new[3:]  # Two facts...
else:
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

if "one time in ten" in appc:
    log.append("SKIP AF1")
    appc2 = appc
else:
    appc2 = once(appc, af1_old, af1_new, "AF1")
    log.append("OK AF1")
out_c = book / "Appendix_C_The_Open_Ledger_v1_6_DRAFT_PC_20260925.md"
out_c.write_text(appc2, encoding="utf-8")
log.append("WROTE " + out_c.name)

# ===== AN4 Ch3 =====
ch3 = (book / "Chapter_03_A_Closed_Universe_v8.md").read_text(encoding="utf-8")
m = re.search(r"after sixty e-folds,.+?larger\.", ch3)
if not m:
    raise RuntimeError("AN4 locus missing")
# Prefer unicode form matching chapter
new_an4 = "after fifty e-folds, it's e\u2075\u2070 \u2248 5 \u00d7 10\u00b2\u00b9 times larger."
# if original uses ascii, use ascii
if "e^" in m.group(0) or "10^" in m.group(0):
    new_an4 = "after fifty e-folds, it is e^50 \u2248 5 \u00d7 10^21 times larger."
elif "it's" in m.group(0):
    new_an4 = "after fifty e-folds, it's e\u2075\u2070 \u2248 5 \u00d7 10\u00b2\u00b9 times larger."
else:
    new_an4 = "after fifty e-folds, it is e\u2075\u2070 \u2248 5 \u00d7 10\u00b2\u00b9 times larger."
ch3n = ch3[: m.start()] + new_an4 + ch3[m.end() :]
(book / "Chapter_03_A_Closed_Universe_v9.md").write_text(ch3n, encoding="utf-8")
log.append("OK AN4 -> Ch3 v9; OLD=" + m.group(0)[:80])

# ===== AV Ch6 =====
ch6p = book / "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v6_1.md"
t6 = ch6p.read_text(encoding="utf-8")

# Fix imported sentence in Gleason para
# extract exact
m = re.search(r"But the geometry it is selected.{0,40}imported.{0,400}?free choice\.", t6)
if not m:
    raise RuntimeError("AV3 imported locus missing")
av3_new = (
    "And the geometry it is selected on is not an abstract postulate the framework borrows from "
    "quantum mechanics. It is the physical three-sphere — the quaternionic piece of the larger "
    "algebra, the same object that supplies the SU(2) factor of the weak force and the boundary "
    "geometry this book has described since Chapter 3. The chapter's claim, then, is the one its "
    "opening has already named: not that the Born rule appears from nothing, but that — given the "
    "geometry the framework attributes to the world — the form of the probability rule is no longer "
    "a free choice."
)
t6 = t6[: m.start()] + av3_new + t6[m.end() :]
log.append("OK AV3")

# Replace retreat section: from "We should be careful about how strong a claim this is."
# through kinship/provenance paragraph
start = t6.find("We should be careful about how strong a claim this is.")
if start < 0:
    raise RuntimeError("AV retreat start missing")
# end after provenance paragraph — look for next ## 
end_markers = [
    "\n## The Tsirelson Bound, Revisited\n",
    "\n## Tsirelson",
]
end = -1
for em in end_markers:
    end = t6.find(em, start)
    if end > 0:
        break
if end < 0:
    raise RuntimeError("AV retreat end missing")

av_block_new = (
    "We should be careful about how strong a claim this is, because it is stronger than it looks. "
    "The framework's reading is not that the quantum-mechanical three-sphere resembles the universe's, "
    "or shares its shape, or does the same kind of work. It is that they are one object. The "
    "three-sphere carrying a spin-\u00bd state is the quaternionic part of the larger algebra the "
    "pre-temporal regime lives in — and that same part is the SU(2) factor of the weak force, and the "
    "boundary geometry this book has been describing since Chapter 3. The Hopf circle a quantum state "
    "quotients out is not merely analogous to a gauge fibre. It is the hypercharge fibre. The "
    "framework's papers state this in terms, and add that it is not a metaphor: the inner product is "
    "computed on the physical three-sphere, and the angle in cos\u00b2(\u03b8/2) is an angle on the sphere we "
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
    "reports a reformulation on the world's geometry, not a derivation of that geometry from nothing.\n"
)
t6 = t6[:start] + av_block_new + t6[end:]
log.append("OK AV1/2/5/6/7 block")
(book / "Chapter_06_Why_Quantum_Mechanics_is_Geometry_v7.md").write_text(t6, encoding="utf-8")
log.append("WROTE Ch6 v7")

# ===== AW Ch8 =====
t8 = (book / "Chapter_08_The_Unresolved_Particle_v5.md").read_text(encoding="utf-8")
m = re.search(r"\*\*Charged leptons must never oscillate\.\*\*.+?root\.", t8, re.S)
if not m:
    raise RuntimeError("AW1 locus missing")
aw1_new = (
    "**Charged leptons must never oscillate between generations.** Resolved species are pinned; "
    "pinned species cannot slide. A muon must never be caught turning into an electron the way "
    "neutrinos turn into each other, and searches for flavour violation of that oscillatory kind "
    "have come up empty. What the framework requires is that they stay empty. The narrowness of "
    "that requirement matters: the framework does **permit** rare loop-mediated decays such as "
    "\u03bc \u2192 e\u03b3, at rates the seesaw's heavy scales push far below anything a current experiment could "
    "reach — Appendix C carries the relation those decays would satisfy. A confirmed **generation "
    "oscillation** of a resolved fermion is what would break the geometric-sliding picture at its "
    "root. An eventual rare decay would not."
)
t8 = t8[: m.start()] + aw1_new + t8[m.end() :]
log.append("OK AW1")
if "derives the heavy scales" in t8:
    t8 = t8.replace("derives the heavy scales", "places the heavy scales", 1)
    log.append("OK AW2")
else:
    log.append("WARN AW2 missing")
(book / "Chapter_08_The_Unresolved_Particle_v6.md").write_text(t8, encoding="utf-8")
log.append("WROTE Ch8 v6")

# ===== AX Ch7 =====
t7 = (book / "Chapter_07_The_Gauge_Birth_v4.md").read_text(encoding="utf-8")
ax1 = (
    "\n\nA word about **embedding depth**, because the term has two jobs and the difference matters "
    "later. At the gauge birth it names a property of a fundamental mode — how strongly that mode "
    "engages |\u03a6_NTE|, which is what fixes its place in the locking order and becomes its Yukawa "
    "coupling. That is the sense this chapter and the next one use. But what embeds a **thing** in "
    "the expansion, now, is its rest energy, and for anything composite the rest energy is mostly "
    "not Yukawa at all: a proton's mass is about ninety-nine per cent the binding energy of massless "
    "gluons. Chapter 1 made that point and it stands — rest energy is what embeds, wherever the rest "
    "energy came from. The two readings coincide for a fundamental fermion and part company for "
    "everything built out of them."
)
ax2 = (
    "\n\nOne caution about the counting, because this book uses **N** for more than one thing and a "
    "reader will try to put them on a single axis. **N_lock \u2248 0.1** measures the **span** of the "
    "locking transition — how much expansion the cascade takes to complete, with the heaviest modes "
    "locking around a thousandth of an e-fold and the leptons around a hundredth. It is not a depth "
    "on the inflationary counter, which measures how far back the structures we read in the microwave "
    "background left the horizon. And neither is the total run, which the framework puts near "
    "\u223c140 e-folds (Part 1). Three counters, three jobs, one letter."
)

if "two jobs and the difference matters" not in t7:
    m = re.search(r"\*\*3\. Mass\.\*\*.+?(?=\n\*\*4\.|\n## )", t7, re.S)
    if not m:
        raise RuntimeError("AX1 Mass section missing")
    t7 = t7[: m.end()] + ax1 + t7[m.end() :]
    log.append("OK AX1")
else:
    log.append("SKIP AX1")

if "Three counters, three jobs" not in t7:
    m = re.search(r"N_lock.{0,200}", t7)
    if not m:
        raise RuntimeError("AX2 N_lock missing")
    para_end = t7.find("\n\n", m.start())
    t7 = t7[:para_end] + ax2 + t7[para_end:]
    log.append("OK AX2")
else:
    log.append("SKIP AX2")

(book / "Chapter_07_The_Gauge_Birth_v5.md").write_text(t7, encoding="utf-8")
log.append("WROTE Ch7 v5")

Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Working\_apply_pc_av_aw_ax_af1_log.txt").write_text(
    "\n".join(log), encoding="utf-8"
)
print("\n".join(log))
