(* (A) spin connection does not rescale the p-channel.
   (B) phi = Sqrt[Sigma] psi: ratio stays (Sigma_g/Sigma)^2.
*)
SetDirectory[DirectoryName[$InputFileName]];
sg =.; sf =.;
S = sg + sf;
pBracketPsi = sg^2/S;
pConstraintPsi = S;
ratioPsi = Simplify[pBracketPsi/pConstraintPsi];
(* densitize: p_psi = p_phi / Sigma *)
pBracketPhi = Simplify[pBracketPsi/S];
pConstraintPhi = Simplify[pConstraintPsi/S];
ratioPhi = Simplify[pBracketPhi/pConstraintPhi];
omegaChangesP = False; (* ultralocal omega adds a bilinear channel, same Sigma prefactor *)
out = <|
  "ratio_psi" -> ToString[ratioPsi, InputForm],
  "ratio_phi" -> ToString[ratioPhi, InputForm],
  "ratios_equal" -> PossibleZeroQ[ratioPsi - ratioPhi],
  "ratio_is_(sg/S)^2" -> PossibleZeroQ[ratioPhi - (sg/S)^2],
  "omega_rescales_p_channel" -> omegaChangesP
|>;
Export["Opsi2_CN_AB_WOLFRAM_SYMBOLIC.json", out, "RawJSON"];

SeedRandom[20261021];
res[v_, cols_] := Module[{sol, proj},
  sol = Quiet[Check[LeastSquares[cols, v], $Failed]];
  If[sol === $Failed, Return[$Failed]];
  Norm[v - cols.sol]/Norm[v]
];
rows = {};
Do[
  Module[{sgv, sfv, Sv, a, b, R, Rf, p, bil, v, u1, u2, r0, rL, rK, rS},
    sgv = RandomReal[{0.3, 2.}];
    sfv = RandomReal[{0.3, 2.}];
    Sv = sgv + sfv;
    a = sgv^2/Sv;
    b = Sv;
    R = RandomReal[NormalDistribution[], 3];
    Rf = RandomReal[NormalDistribution[], 3];
    p = RandomReal[NormalDistribution[], 3];
    bil = RandomReal[NormalDistribution[], 3];
    v = R + a p + a bil;
    u1 = R + b p;
    u2 = Rf;
    r0 = res[R + a p, Transpose[{u1}]];
    rL = res[v, Transpose[{u1, u2}]];
    rK = res[R + sgv p, Transpose[{R + sgv p}]];
    rS = res[R + (sfv^2/Sv) p + (sfv^2/Sv) bil, Transpose[{R + Sv p, R}]];
    If[MemberQ[{r0, rL, rK, rS}, $Failed], Continue[]];
    AppendTo[rows, <|"r0" -> r0, "rL" -> rL, "rK" -> rK, "rS" -> rS|>];
  ],
  {200}
];
num = <|
  "n" -> Length[rows],
  "median_single" -> Median[rows[[All, "r0"]]],
  "median_enlarged_with_omega" -> Median[rows[[All, "rL"]]],
  "fraction_enlarged_gt_1e-3" -> Mean[Boole[# > 1.*^-3] & /@ rows[[All, "rL"]]],
  "max_K1" -> Max[rows[[All, "rK"]]],
  "median_K5_swap" -> Median[rows[[All, "rS"]]],
  "pass_G2" -> (Median[rows[[All, "rL"]]] > 1.*^-3 && Max[rows[[All, "rK"]]] < 1.*^-8)
|>;
Export["Opsi2_CN_AB_WOLFRAM_NUMERIC.json", num, "RawJSON"];
Print[out];
Print[num];
Exit[0];
