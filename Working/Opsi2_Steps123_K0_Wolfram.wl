(* K0' minimal model: P^i = C (Dn)^i on C_i=0, generic n.
   1111.2070 eqs (13)(15)(19)(42)(44)(45), beta2=beta3=0, beta1=1.
*)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261021];

matrixSqrtSPD[A_] := Module[{S, e, v},
  S = (A + Transpose[A])/2;
  {e, v} = Eigensystem[S];
  e = Clip[Re[e], {0, Infinity}];
  Transpose[v].DiagonalMatrix[Sqrt[e]].v
];

DOfN[gamma_, f3_, n_] := Module[{x, Q, inside},
  x = 1. - n.f3.n;
  If[x <= 1.*^-12, Return[$Failed]];
  Q = x IdentityMatrix[3] + KroneckerProduct[n, f3.n];
  inside = Inverse[gamma].f3.Q;
  inside = (inside + Transpose[inside])/2;
  matrixSqrtSPD[inside].Inverse[Q]
];

randomSPD[] := Module[{A},
  A = RandomReal[NormalDistribution[], {3, 3}];
  A.Transpose[A] + 0.4 IdentityMatrix[3]
];

beta0 = 0.; beta1 = 1.; m2 = 1.;
rows = {};
Do[
  Module[{gamma, f3, n, x, Dmat, Dn, sg, V, R, R0, Cval, Ci, VbarM, Vbar,
      Pfrom44, Pfrom45, Cnonzero, Pnz},
    gamma = randomSPD[];
    f3 = randomSPD[];
    n = RandomReal[NormalDistribution[], 3];
    n = 0.25 n/Max[1., Norm[n]];
    x = 1. - n.f3.n;
    If[x <= 0.2, Continue[]];
    Dmat = DOfN[gamma, f3, n];
    If[Dmat === $Failed || Quiet[Det[Dmat]] === 0., Continue[]];
    Dn = Dmat.n;
    If[Norm[n] < 1.*^-3 || Norm[Dn] < 1.*^-3, Continue[]];
    sg = Sqrt[Det[gamma]];
    V = beta0 + beta1 Sqrt[x] Tr[Dmat];
    (* C_i = 0 fixes R_i *)
    R = 2 m2 sg beta1 (f3.n)/Sqrt[x];
    R0 = -R.Dn - 2 m2 sg V; (* C = 0 *)
    Cval = R0 + R.Dn + 2 m2 sg V;
    Ci = R - 2 m2 sg beta1 (f3.n)/Sqrt[x];
    VbarM = Quiet[Check[(beta1/Sqrt[x]) f3.Inverse[Dmat], $Failed]];
    If[VbarM === $Failed, Continue[]];
    Vbar = Inverse[gamma].VbarM.Inverse[gamma];
    Pfrom44 = (R0 + R.Dn + 2 m2 sg V) Dn + Inverse[gamma].R - 2 m2 sg Vbar.gamma.Dn;
    Pfrom45 = Cval Dn;
    (* second probe: C_i=0 but C != 0 *)
    Cnonzero = R0 + 1.7 + R.Dn + 2 m2 sg V;
    Pnz = Cnonzero Dn;
    AppendTo[rows, <|
      "n_norm" -> Norm[n],
      "Dn_norm" -> Norm[Dn],
      "C_abs" -> Abs[Cval],
      "Ci_norm" -> Norm[Ci],
      "P44_norm_when_C0" -> Norm[Pfrom44],
      "P44_vs_P45" -> Norm[Pfrom44 - Pfrom45],
      "P_when_C_nonzero" -> Norm[Pnz],
      "C_nonzero_abs" -> Abs[Cnonzero]
    |>];
  ],
  {80}
];

summary = <|
  "engine" -> "WolframEngine15",
  "model" -> "minimal beta2=beta3=0 beta1=1",
  "n_kept" -> Length[rows],
  "fraction_n_nonzero" -> Mean[Boole[# > 1.*^-3] & /@ rows[[All, "n_norm"]]],
  "max_Ci" -> Max[rows[[All, "Ci_norm"]]],
  "max_C_when_set_0" -> Max[rows[[All, "C_abs"]]],
  "max_P_when_C0" -> Max[rows[[All, "P44_norm_when_C0"]]],
  "max_P44_vs_45" -> Max[rows[[All, "P44_vs_P45"]]],
  "min_P_when_C_nonzero" -> Min[rows[[All, "P_when_C_nonzero"]]],
  "pass" -> (
    Length[rows] >= 20 &&
    Max[rows[[All, "P44_norm_when_C0"]]] < 1.*^-8 &&
    Max[rows[[All, "P44_vs_P45"]]] < 1.*^-8 &&
    Min[rows[[All, "P_when_C_nonzero"]]] > 1.*^-3 &&
    Mean[Boole[# > 1.*^-3] & /@ rows[[All, "n_norm"]]] > 0.95
  )
|>;
Export["Opsi2_Steps123_K0_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
