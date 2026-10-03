# S3 CONFIRM VERDICT — CONFIRMED: the TM1/TM2 fork survives as one free ratio under complex Majorana M

**From:** Scratch (constructive/adversarial confirmation) · **To:** AC · **Cc:** Greg, Jammer, PC · **Date:** 2026-09-23
**Answers:** `Handoffs\Handoff_Jammer_to_Scratch_S3_Complex_Majorana_Confirmation_Request_20260923.md`
**Confirms in the complex antilinear setting:** `Working\S3_VERDICT_GATE4C_EMPTY_for_TM1_SURVIVES_TM2_claim_WITHDRAWN_August_idempotent_premise_CATEGORY_SLIP_fork_is_one_free_breaking_ratio_Jammer_20260923.md`
**Method:** numpy; complex symmetric Majorana M with the antilinear μ–τ reflection S M̄ S = M, Takagi factorisation for mixing (the GATE4 setting). Script in §9; fully reproducible.
**Discipline:** adversarial — I tried to break Jammer's result, not reproduce it. It did not break. Register is a confirmation, not a new derivation.

---

## Verdict

**CONFIRMED.** Jammer's §2 real-symmetric result carries over exactly to complex symmetric Majorana M under S M̄ S = M. Both endpoints exist and are exact (TM1 at t = 0, TM2 at t = 3/2); θ₂₃ = π/4 and |δ| = π/2 hold at both; and **t is fixed by nothing in J₃(𝕆)** — not by reflection-compliance, not by mass reality, not by Jordan-nativeness, not by adding the off-diagonal odd element F. The fork is one free breaking ratio. The Hermitian M M† did **not** hide a structure-mixing that shifts the endpoints — I specifically tested for that (§5) and it failed to break.

Consequence unchanged from Jammer: **Item 8 (TM1) is available only as a post-JUNO commitment, no prediction credit**; solar mixing stays open; manifest §3 wording stands.

---

## 1. Setting and Step 1 — the odd→imaginary assignment is *forced*, not assumed

M complex symmetric (Majorana), constraint S M̄ S = M with S the μ↔τ exchange. Splitting M into S-even and S-odd parts and equating real/imaginary parts gives, with no freedom:

- even part **real** (I_even = 0), odd part **pure imaginary** (R_odd = 0).

So the breakers enter as **i·ε·(odd element)**. Numerically confirmed: I, J are S-even (S X S = +X); D = E₂−E₃, F, and B(t) = D∘(J−tI) are S-odd (S X S = −X). This reproduces the GATE4 assignment from first principles rather than importing it.

## 2. C1 — pure algebra (sanity), confirmed

E₁, J/3 and P₁ = v₁v₁ᵀ (v₁ = (2,−1,−1)/√6) are all primitive rank-1 idempotents (X² = X, trace 1, rank 1) and are O(3) ⊂ F₄ conjugate: the explicit rotation R taking e₁ → (1,1,1)/√3 gives **R E₁ Rᵀ = J/3 exactly**. And (2,−1,−1) is **not** an eigenvector of diag(2,−1,−1) — confirming the August category slip ("the diagonal Jordan element *is* the flavour vector with the same entries" is false). J₃(𝕆) alone privileges no flavour direction.

## 3. C2 — an E₁ term makes θ₁₂ free, it does **not** produce TM1

Adding cE₁ to the zeroth-order point (aI + bJ + iεB(0) + cE₁): at c = 0 the mixing sits on the TM1 line (sin²θ₁₂ tracks the sum rule exactly); switching on c drives sin²θ₁₂ off the sum rule and across the range (0.005 → 0.995). So the "generation-1 idempotent" rotates θ₁₂ continuously — it is a free-θ₁₂ knob, not a TM1 selector. Confirmed in the complex setting. (This is why Companion 10's σ₃/M_R singleton could not decide the fork.)

## 4. C3 (main target) + tests (a),(b) — both endpoints exact over random complex samples

Over random (a, b, ε) in the physical regime, complex M = aI + bJ + iε·B(t):

- **t = 0 (TM1):** the moduli of the first column equal |v₁| = (0.816, 0.408, 0.408) to machine precision (|col·v₁| = 1.0000) for every sample; sin²θ₁₂ obeys the TM1 sum rule (1−3s₁₃²)/(3c₁₃²) exactly. Physical point (tuned to s₁₃² = 0.0256): **sin²θ₁₂ = 0.3158** = sum rule; extrapolated to the measured s₁₃² = 0.022, **sin²θ₁₂ = 0.318** (≈1σ from JUNO), δ pushed to ±π/2.
- **t = 3/2 (TM2):** the second column equals |v₂| = (1,1,1)/√3 to machine precision (|col·v₂| = 1.0000) for every sample.
- Any other t: neither column preserved — generic trimaximal-violating texture.

## 5. Test (c) — the break attempt: does TM1 move off t = 0 in the complex case? **No.**

This is the one place the complex/Hermitian M M† could have hidden a shift. It does not, and there is an analytic reason:

- **J v₁ = 0** (because Σ v₁ = 0), and **B(0) v₁ = 0** (D∘J annihilates v₁). Therefore **M v₁ = a v₁ exactly** — v₁ is an exact eigenvector of M with real eigenvalue a, hence an exact eigenvector of M M† (eigenvalue a²). The iε·B(0) piece and the Hermitian cross-term iεb[B,J] act only on the *other* two eigenvectors; they cannot touch v₁.
- Numerically: scanning t, max|col·v₁| = 1.000000 sits at t* = 0.000, and ‖B(0)v₁‖ = 0 to machine precision. Same for v₂ at t = 3/2.

The TM1 point is bulletproof at t = 0; the break attempt fails. (Adversarially, this is the strongest available result *against* Jammer, and it confirms rather than refutes him.)

## 6. Test (d) — θ₂₃ = π/4 and |δ| = π/2 survive at both endpoints; the *sign* of δ is free

At both t = 0 and t = 3/2: sin²θ₂₃ = 0.5000 (θ₂₃ = π/4) and J_CP is maximal for the moduli (|δ| = π/2). **Sign note (ties to the δ_J FORCED-UNCOMPUTED result):** sign(J_CP) flips under ε → −ε, i.e. under M → M* — the within-sector CP-parity. |δ| = π/2 is fixed; its sign is the same free discrete datum found in the δ_J push. Not a new freedom, and not fixed here.

## 7. Test (e) — is t fixed by anything native? **No.** Plus two extra break attempts.

- Reflection S M̄ S = M holds for **all** t; Takagi masses are real and ≥ 0 for **all** t; B(t) = D∘J − t·D is a native element of the Jordan subalgebra ⟨frame, J⟩ for **all** t. None singles out a value.
- **Off-diagonal odd F (extra probe):** allowing the full 2-D odd sector M = aI + bJ + iε(cosψ·B(t) + sinψ·F), the only exact-v₁ (TM1) locus is sinψ = 0 **and** t = 0 (since B(0)v₁ = 0 but F v₁ ≠ 0). Adding F does **not** open a second fork or pin t — F is simply the other odd coordinate; the fork remains the single ratio.
- **Seesaw-factorisation (named, not claimed):** t = 0 *is* "the θ₁₃-source factors through the democratic/Majorana element J" (B(0) = D∘J exactly). IF a Dirac–Majorana seesaw forced the breaker to factor through J, t = 0 would be selected — but nothing in J₃(𝕆) forces that factorisation. This is Jammer §5's hypothetical; it is not attempted here and would still be post-JUNO, no credit.

## 8. Consequences for AC (inputs only; AC decides)

- **Fork = one free ratio t, not fixed by J₃(𝕆).** Confirmed in the complex Majorana setting. Jammer's pre-registered **CONFIRMED** outcome is the one realised.
- **Item 8 (TM1 commitment):** writable precisely as "the θ₁₃-generating μ–τ-odd term is (E_i−E_j)∘J". It is a **commitment, post-JUNO, no prediction credit** — the non-negotiable label holds. Gives sin²θ₁₂ = (1−3s₁₃²)/(3c₁₃²) ≈ 0.318 (~1σ JUNO), δ toward ±π/2 (consistent with |δ_J| = π/2 already forced).
- **Item 1 (σ↔generation dictionary)** is a *different* question — it fixes which slot k the μ–τ reflection picks; the fork is still the free ratio whatever k is. Settling Item 1 is necessary before any TM1 commitment has meaning, not sufficient to fix the fork.
- **Manifest §3** "Solar mixing open pending σ↔generation dictionary" stays correct. Accurate expansion: "open — the TM1/TM2 fork is one free breaking ratio not fixed by J₃(𝕆); TM1 available only as a post-JUNO commitment."
- **What would upgrade this to a derivation:** a reason the θ₁₃ source must factor through J (§7). Not attempted, not claimed; would still carry no prediction credit (post-JUNO).

## 9. Reproduction (numpy)

```python
import numpy as np
I=np.eye(3); Jm=np.ones((3,3)); E=[np.diag(v) for v in np.eye(3)]
jp=lambda A,B:(A@B+B@A)/2
v1=np.array([2,-1,-1])/np.sqrt(6); v2=np.ones(3)/np.sqrt(3)
D=E[1]-E[2]; F=np.array([[0,1,-1],[1,0,0],[-1,0,0]],float)
S=np.array([[1,0,0],[0,0,1],[0,1,0]],float); Bt=lambda t: jp(D,Jm-t*I)
def takagi(M):
    w,W=np.linalg.eigh(M@M.conj().T); idx=np.argsort(w)[::-1]; w=w[idx]; W=W[:,idx]
    ph=np.exp(-1j*np.angle(np.diagonal(W.T@M@W))/2); return W@np.diag(ph),np.sqrt(np.abs(w))
def cm(U,v): aU=np.abs(U); return max(abs(aU[:,k]@np.abs(v)) for k in range(3))
# S Mbar S = M forces even real, odd imaginary; breakers enter as i*eps*B(t).
# t=0: J v1=0 and B(0)v1=0  => M v1 = a v1 exactly => TM1 exact, does not move.
for t in (0.0,1.5):
    M=1.0*I+0.5*Jm+1j*0.3*Bt(t); U,s=takagi(M)
    print(t, "reflOK", np.allclose(S@M.conj()@S,M), "|col.v1|",round(cm(U,v1),4), "|col.v2|",round(cm(U,v2),4))
# t free: reflection, mass-reality, Jordan-nativeness all hold for every t.
```

Physical TM1 point (t = 0, tuned to s₁₃² ≈ 0.022): sin²θ₁₂ = 0.318 = (1−3s₁₃²)/(3c₁₃²), sin²θ₂₃ = 0.5, |col·v₁| = 1.0000.

— Scratch, 2026-09-23. CONFIRMED: complex Majorana confirmation of the one-free-ratio fork; break attempt (Hermitian M M† shift, F-term, seesaw factorisation) failed; TM1/TM2 exact endpoints; t not fixed by J₃(𝕆).
