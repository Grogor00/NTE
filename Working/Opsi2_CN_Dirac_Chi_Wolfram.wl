(* Diagonal chi-correction to {E_g, E_g}_D.
   coeff_bracket = Sigma_g^2 / Sigma * p
   coeff_constraint = Sigma * p
   Project v = R + coeff_bracket p onto u = R + coeff_constraint p.
*)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261021];

resNorm[R_, p_, a_, b_] := Module[{v, u, uu},
  v = R + a p;
  u = R + b p;
  uu = u.u;
  If[uu < 1.*^-18 || Norm[v] < 1.*^-18, Return[$Failed]];
  Norm[v - (v.u/uu) u]/Norm[v]
];

rows = {};
Do[
  Module[{sg, sf, S, a, b, R, p, rel, relSwap, relK1},
    sg = RandomReal[{0.2, 2.}];
    sf = RandomReal[{0.2, 2.}];
    S = sg + sf;
    a = sg^2/S; (* Dirac ddelta weight *)
    b = S;      (* C_i matter weight, pi ~ Sigma psi *)
    R = RandomReal[NormalDistribution[], 3];
    p = RandomReal[NormalDistribution[], 3];
    rel = resNorm[R, p, a, b];
    relSwap = resNorm[R, p, sf^2/S, S];
    relK1 = resNorm[R, p, sg, sg]; (* sf = 0 => a = b = sg *)
    If[rel === $Failed || relSwap === $Failed || relK1 === $Failed, Continue[]];
    AppendTo[rows, <|"rel" -> rel, "relSwap" -> relSwap, "relK1" -> relK1, "ratio" -> a/b|>];
  ],
  {200}
];

summary = <|
  "engine" -> "WolframEngine15",
  "n" -> Length[rows],
  "median_rel_residual" -> Median[rows[[All, "rel"]]],
  "fraction_rel_gt_1e-3" -> Mean[Boole[# > 1.*^-3] & /@ rows[[All, "rel"]]],
  "median_rel_swap" -> Median[rows[[All, "relSwap"]]],
  "max_rel_K1_sf0" -> Max[rows[[All, "relK1"]]],
  "median_a_over_b" -> Median[rows[[All, "ratio"]]],
  "monomial" -> "p_j not (psi.alpha.psi)*pi",
  "formula" -> "a=Sigma_g^2/Sigma, b=Sigma",
  "pass_Mb" -> (Median[rows[[All, "rel"]]] > 0.05 && Max[rows[[All, "relK1"]]] < 1.*^-8)
|>;
Export["Opsi2_CN_Dirac_Chi_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
