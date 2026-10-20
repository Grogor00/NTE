(* K0' + matter. Solve the n-equation. Test P - C_N (Dn).
   Same decision rule as the prereg. ASCII twin: Opsi2_K0prime_Matter_nEOM_Wolfram.txt
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

tryBackground[] := Module[{gamma, f3, n, x, Dmat, Dn, sqrtg, beta1, m2, U, VbarM, Vbar, potVec, V, pot},
  gamma = randomSPD[];
  f3 = randomSPD[];
  n = RandomReal[NormalDistribution[], 3];
  n = 0.25 n/Max[1., Norm[n]];
  x = 1. - n.f3.n;
  If[x <= 0.2, Return[$Failed]];
  Dmat = Quiet[Check[DOfN[gamma, f3, n], $Failed]];
  If[Dmat === $Failed, Return[$Failed]];
  If[Quiet[Det[Dmat]] === 0. || Abs[Det[Dmat]] < 1.*^-8, Return[$Failed]];
  Dn = Dmat.n;
  If[Norm[n] < 1.*^-3 || Norm[Dn] < 1.*^-3, Return[$Failed]];
  sqrtg = Sqrt[Det[gamma]];
  beta1 = 1.; m2 = 1.;
  U = 2. m2 sqrtg beta1 (f3.n)/Sqrt[x];
  VbarM = Quiet[Check[(beta1/Sqrt[x]) f3.Inverse[Dmat], $Failed]];
  If[VbarM === $Failed, Return[$Failed]];
  Vbar = Inverse[gamma].VbarM.Inverse[gamma];
  potVec = 2. m2 sqrtg Vbar.gamma.Dn;
  If[Norm[Inverse[gamma].U - potVec] > 1.*^-6, Return[$Failed]];
  V = beta1 Sqrt[x] Tr[Dmat];
  pot = 2. m2 sqrtg V;
  <|"gamma" -> gamma, "Dn" -> Dn, "U" -> U, "pot" -> pot|>
];

pureHR[nTry_] := Module[{rows, k, bg, gamma, Dn, U, pot, R, R0, C, P, Coff, Poff},
  rows = {};
  Do[
    bg = tryBackground[];
    If[bg === $Failed, Continue[]];
    gamma = bg["gamma"]; Dn = bg["Dn"]; U = bg["U"]; pot = bg["pot"];
    R = U;
    R0 = -R.Dn - pot;
    C = R0 + R.Dn + pot;
    P = C Dn + Inverse[gamma].(R - U);
    Coff = (R0 + 1.7) + R.Dn + pot;
    Poff = Coff Dn + Inverse[gamma].(R - U);
    AppendTo[rows, <|
      "resid" -> Norm[P - C Dn],
      "Pon" -> Norm[P],
      "Poff" -> Norm[Poff]
    |>];
  , {k, nTry}];
  <|
    "n_kept" -> Length[rows],
    "max_resid" -> Max[rows[[All, "resid"]]],
    "max_P_on_C0" -> Max[rows[[All, "Pon"]]],
    "min_P_when_C_nonzero" -> Min[rows[[All, "Poff"]]],
    "pass" -> (
      Length[rows] >= 20 &&
      Max[rows[[All, "resid"]]] < 1.*^-8 &&
      Max[rows[[All, "Pon"]]] < 1.*^-8 &&
      Min[rows[[All, "Poff"]]] > 1.*^-3
    )
  |>
];

oneMatter[bg_, sg_, sf_, swap_] := Module[
  {gamma, Dn, U, pot, s1, s2, S, wg, wbr, wtot, J, b, Eg, cur, R, R0, Cgrav, CN,
   ginv, Pgrav, P, resid, analytic, R0off, CgravOff, Coff, Poff, residOff,
   curJ, RJ, R0J, CgravJ, CJ, PJ, Rf, total, theta},
  gamma = bg["gamma"]; Dn = bg["Dn"]; U = bg["U"]; pot = bg["pot"];
  s1 = sg; s2 = sf;
  If[swap, s1 = sf; s2 = sg];
  S = s1 + s2;
  wg = s1;
  wbr = If[S > 0, s1^2/S, s1];
  wtot = S;
  J = RandomReal[NormalDistribution[], 3];
  b = RandomReal[NormalDistribution[], 3];
  Eg = RandomReal[{-1., 1.}];
  cur = J + b;
  R = U - wg cur;
  R0 = -R.Dn - pot - Eg - wg Dn.cur;
  Cgrav = R0 + R.Dn + pot;
  CN = Cgrav + Eg + wg Dn.cur;
  ginv = Inverse[gamma].cur;
  Pgrav = Cgrav Dn + Inverse[gamma].(R - U);
  P = Pgrav + (Eg + wg Dn.cur) Dn + wbr ginv;
  resid = P - CN Dn;
  analytic = (wbr - wg) ginv;
  R0off = R0 + 1.7;
  CgravOff = R0off + R.Dn + pot;
  Coff = CgravOff + Eg + wg Dn.cur;
  Poff = CgravOff Dn + Inverse[gamma].(R - U) + (Eg + wg Dn.cur) Dn + wbr ginv;
  residOff = Poff - Coff Dn;
  curJ = J;
  RJ = U - wg curJ;
  R0J = -RJ.Dn - pot - Eg - wg Dn.curJ;
  CgravJ = R0J + RJ.Dn + pot;
  CJ = CgravJ + Eg + wg Dn.curJ;
  PJ = CgravJ Dn + Inverse[gamma].(RJ - U) + (Eg + wg Dn.curJ) Dn + wbr Inverse[gamma].curJ;
  Rf = -R - wtot cur;
  total = R + Rf + wtot cur;
  theta = If[S > 0, s1/S, 1.];
  <|
    "resid" -> Norm[resid],
    "analytic_err" -> Norm[resid - analytic],
    "off_minus_on" -> Norm[residOff - resid],
    "total_mom" -> Norm[total],
    "resid_J" -> Norm[PJ - CJ Dn],
    "Pon" -> Norm[P],
    "theta" -> theta,
    "factor" -> Abs[wbr - wg]
  |>
];

collectMode[nKeep_, mode_] := Module[{rows, tries, bg, sg, sf, s, row},
  rows = {};
  tries = 0;
  While[Length[rows] < nKeep && tries < nKeep*25,
    tries++;
    bg = tryBackground[];
    If[bg === $Failed, Continue[]];
    Which[
      mode === "matter",
        sg = RandomReal[{0.3, 2.}]; sf = RandomReal[{0.3, 2.}];
        row = oneMatter[bg, sg, sf, False],
      mode === "sf0",
        sg = RandomReal[{0.3, 2.}];
        row = oneMatter[bg, sg, 0., False],
      mode === "k5",
        sg = RandomReal[{0.3, 2.}]; sf = RandomReal[{0.3, 2.}];
        row = oneMatter[bg, sg, sf, True],
      mode === "ef",
        s = RandomReal[{0.3, 2.}];
        row = oneMatter[bg, s, s, False]
    ];
    AppendTo[rows, row];
  ];
  rows
];

summarise[rows_, label_] := <|
  "label" -> label,
  "n" -> Length[rows],
  "median_abs_resid" -> Median[rows[[All, "resid"]]],
  "max_abs_resid" -> Max[rows[[All, "resid"]]],
  "fraction_gt_1e-3" -> Mean[Boole[# > 1.*^-3] & /@ rows[[All, "resid"]]],
  "max_analytic_err" -> Max[rows[[All, "analytic_err"]]],
  "max_off_minus_on" -> Max[rows[[All, "off_minus_on"]]],
  "max_total_mom" -> Max[rows[[All, "total_mom"]]],
  "median_resid_J_only" -> Median[rows[[All, "resid_J"]]],
  "median_theta_g" -> Median[rows[[All, "theta"]]],
  "median_abs_factor" -> Median[rows[[All, "factor"]]],
  "min_P_on_surface" -> Min[rows[[All, "Pon"]]]
|>;

pure = pureHR[200];
matter = summarise[collectMode[200, "matter"], "matter"];
sf0 = summarise[collectMode[80, "sf0"], "sf0"];
k5 = summarise[collectMode[200, "k5"], "k5"];
ef = summarise[collectMode[80, "ef"], "ef"];

analyticOK = (
  matter["max_analytic_err"] < 1.*^-6 &&
  sf0["max_analytic_err"] < 1.*^-6 &&
  k5["max_analytic_err"] < 1.*^-6 &&
  matter["max_off_minus_on"] < 1.*^-6 &&
  matter["max_total_mom"] < 1.*^-6
);
passG2 = (
  pure["pass"] && analyticOK &&
  sf0["max_abs_resid"] < 1.*^-8 &&
  matter["median_abs_resid"] > 1.*^-3 &&
  matter["fraction_gt_1e-3"] >= 0.95 &&
  k5["median_abs_resid"] > 1.*^-3 &&
  k5["fraction_gt_1e-3"] >= 0.95
);
passMa = pure["pass"] && matter["median_abs_resid"] < 1.*^-8;
lane = Which[passG2, "G-2", passMa, "M-a", True, "G-4"];

summary = <|
  "engine" -> "WolframEngine15",
  "lane" -> lane,
  "pass_G2" -> passG2,
  "pass_Ma" -> passMa,
  "pure_n_kept" -> pure["n_kept"],
  "pure_max_resid" -> pure["max_resid"],
  "pure_min_P_off" -> pure["min_P_when_C_nonzero"],
  "pure_pass" -> pure["pass"],
  "median_abs_resid" -> matter["median_abs_resid"],
  "matter_fraction" -> matter["fraction_gt_1e-3"],
  "matter_max_analytic_err" -> matter["max_analytic_err"],
  "matter_median_J_only" -> matter["median_resid_J_only"],
  "matter_median_theta" -> matter["median_theta_g"],
  "sf0_max" -> sf0["max_abs_resid"],
  "k5_median" -> k5["median_abs_resid"],
  "k5_fraction" -> k5["fraction_gt_1e-3"],
  "ef_median" -> ef["median_abs_resid"],
  "ef_median_theta" -> ef["median_theta_g"],
  "max_total_mom" -> matter["max_total_mom"],
  "max_off_minus_on" -> matter["max_off_minus_on"]
|>;

Export["Opsi2_K0prime_Matter_nEOM_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
