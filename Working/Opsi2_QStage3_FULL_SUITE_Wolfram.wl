(* Q-Stage3 full suite in Wolfram — mirrors NumPy compute
   Seed 20261020; 60 random trials + K1 on W (not on excess)
*)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261020];

randomSPD[] := Module[{A},
  A = RandomReal[NormalDistribution[0, 1], {3, 3}];
  A.Transpose[A] + 0.4 IdentityMatrix[3]
];

matrixSqrtSPD[A_] := Module[{S, e, v},
  S = (A + Transpose[A])/2;
  {e, v} = Eigensystem[S];
  e = Clip[Re[e], {0, Infinity}];
  Transpose[v].DiagonalMatrix[Sqrt[e]].v
];

XFrom[hg_, hf_] := Module[{hs, his, S},
  hs = matrixSqrtSPD[hg];
  his = Inverse[hs];
  S = (his.hf.his + Transpose[his.hf.his])/2;
  his.matrixSqrtSPD[S].hs
];

nTrials = 60;
rows = {};
Do[
  Module[{hg, hf, X, G, W, Walt, pig, p, pif, rem, rem0, excess, pred, pred2},
    hg = randomSPD[];
    If[EvenQ[trial],
      X = DiagonalMatrix[{1., 1.2, 1.7}];
      hf = hg.X.X;
      ,
      hf = randomSPD[];
      X = XFrom[hg, hf];
    ];
    G = hg.X;
    W = hg.(IdentityMatrix[3] - X).(IdentityMatrix[3] - X);
    Walt = hg + hf - 2 G;
    pig = RandomReal[NormalDistribution[0, 1], 3];
    p = RandomReal[NormalDistribution[0, 1], 3];
    pif = -pig - p;
    rem = hg.pig + hf.pif + W.p;
    rem0 = hg.pig + hf.(-pig);
    excess = rem - rem0;
    pred = (W - hf).p;
    pred2 = hg.(IdentityMatrix[3] - 2 X).p;
    AppendTo[rows, <|
      "W_match_alt" -> Norm[W - Walt],
      "excess_vs_pred" -> Norm[excess - pred],
      "excess_vs_pred2" -> Norm[excess - pred2],
      "excess_norm" -> Norm[excess],
      "rem_norm" -> Norm[rem],
      "rem0_norm" -> Norm[rem0],
      "W_norm" -> Norm[W],
      "Wp_norm" -> Norm[W.p]
    |>];
  ],
  {trial, 0, nTrials - 1}
];

(* K1: matter coefficient W vanishes at X=I — NOT excess *)
k1W = Table[
  Module[{hg, hf, X, W},
    hg = randomSPD[];
    hf = hg;
    X = XFrom[hg, hf];
    W = hg.(IdentityMatrix[3] - X).(IdentityMatrix[3] - X);
    Norm[W]
  ],
  {20}
];

(* Algebraic identities (symbolic diagonal) *)
hg = DiagonalMatrix[Array[hgS, 3]];
X = DiagonalMatrix[Array[xS, 3]];
hf = hg.X.X;
W = hg.(IdentityMatrix[3] - X).(IdentityMatrix[3] - X);
Wdiff = Simplify[W - (hg + hf - 2 hg.X)];
pig = Array[pgS, 3];
p = Array[pS, 3];
excess = Simplify[(hg.pig + hf.(-pig - p) + W.p) - (hg.pig + hf.(-pig))];
e1 = Simplify[excess - (W - hf).p];
e2 = Simplify[excess - hg.(IdentityMatrix[3] - 2 X).p];
WAtI = Simplify[W /. {xS[1] -> 1, xS[2] -> 1, xS[3] -> 1}];
exAtI = Simplify[excess /. {xS[1] -> 1, xS[2] -> 1, xS[3] -> 1}];

a =.; b =.; c =.;
det = Simplify[a c + b^2];

summary = <|
  "engine" -> "WolframEngine15",
  "n_trials" -> Length[rows],
  "max_W_match_alt" -> Max[rows[[All, "W_match_alt"]]],
  "max_excess_vs_pred" -> Max[rows[[All, "excess_vs_pred"]]],
  "max_excess_vs_pred2" -> Max[rows[[All, "excess_vs_pred2"]]],
  "median_excess_norm" -> Median[rows[[All, "excess_norm"]]],
  "median_rem0_norm" -> Median[rows[[All, "rem0_norm"]]],
  "fraction_excess_gt_1e-8" -> Mean[Boole[# > 1.*^-8] & /@ rows[[All, "excess_norm"]]],
  "identities_hold_numerically" -> (
    Max[rows[[All, "excess_vs_pred"]]] < 1.*^-8 &&
    Max[rows[[All, "excess_vs_pred2"]]] < 1.*^-8 &&
    Max[rows[[All, "W_match_alt"]]] < 1.*^-8
  ),
  "K1_W_max_norm_at_X_I" -> Max[k1W],
  "K1_W_vanishes_at_X_I" -> (Max[k1W] < 1.*^-8),
  "symbolic" -> <|
    "W_equals_hg_hf_minus_2G" -> PossibleZeroQ[Together[Tr[Wdiff.Wdiff]]],
    "excess_equals_(W-hf).p" -> PossibleZeroQ[Together[e1.e1]],
    "excess_equals_hg.(I-2X).p" -> PossibleZeroQ[Together[e2.e2]],
    "W_vanishes_at_X_I" -> PossibleZeroQ[Together[Tr[WAtI.WAtI]]],
    "excess_at_X_I_equals_minus_hg_p" -> PossibleZeroQ[Together[(exAtI + hg.p).(exAtI + hg.p)]],
    "dirac_det" -> ToString[det, InputForm],
    "dirac_det_if_c_0" -> ToString[Simplify[det /. c -> 0], InputForm],
    "excess_formula" -> ToString[excess, InputForm]
  |>,
  "diagnosis" -> <|
    "note" -> "K1 applies to matter weight W=hg(I-X)^2, which vanishes at X=I. On-shell excess hg(I-2X)p equals -hg p at X=I and is a different object (not the K1 residual).",
    "F12" -> "nonvanishing of {C_SC,C_SC} or excess alone is not G-2",
    "dirac_det_independent_of_a_if_c_0" -> True
  |>
|>;

Export["Opsi2_QStage3_WOLFRAM_FULL_RESULTS.json", summary, "RawJSON"];
Print[summary];
Exit[0];
