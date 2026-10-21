(* Dirac matrices: aligned coefficient, boost closed form. ASCII twin: .txt *)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261022];

id2 = IdentityMatrix[2];
sx = {{0, 1}, {1, 0}};
sy = {{0, -I}, {I, 0}};
sz = {{1, 0}, {0, -1}};
g0 = ArrayFlatten[{{id2, 0 id2}, {0 id2, -id2}}];
gammaI[s_] := ArrayFlatten[{{0 id2, s}, {-s, 0 id2}}];
gs = {gammaI[sx], gammaI[sy], gammaI[sz]};
alphas = Table[g0.gs[[i]], {i, 3}];
id4 = IdentityMatrix[4];

alphaSqErr = Max[Table[Norm[alphas[[k]].alphas[[k]] - id4], {k, 3}]];

Cmat[sg_, sf_, p_] := Module[{gp, M},
  gp = Sqrt[1. + p.p];
  M = (sg + sf gp) id4;
  Do[M = M - sf p[[i]] alphas[[i]], {i, 3}];
  M
];

jammerI[sg_, sf_, p_] := Module[{gp, den},
  gp = Sqrt[1. + p.p];
  den = sg^2 + 2 gp sg sf + sf^2;
  sg^2 (sg + sf gp)/den
];

channel[sg_, sf_, p_] := Module[{C, K, M, cI, cA, pred, k},
  k = 1;
  C = Cmat[sg, sf, p];
  K = Inverse[C];
  M = sg^2 alphas[[k]].K.alphas[[k]];
  cI = Re[Tr[M]/4];
  cA = Table[Re[Tr[alphas[[j]].M]/4], {j, 3}];
  pred = jammerI[sg, sf, p];
  <|"cI" -> cI, "cA" -> Max[Abs[cA]], "pred" -> pred,
    "err" -> Abs[cI - pred],
    "alignedTarget" -> If[sg + sf == 0, sg, sg^2/(sg + sf)],
    "distI" -> Norm[M - cI id4]|>
];

rowsA = {}; rowsB = {}; rows0 = {};
Do[
  Module[{sg, sf, p, ra, rb, r0},
    sg = RandomReal[{0.4, 2.}];
    sf = RandomReal[{0.4, 2.}];
    ra = channel[sg, sf, {0., 0., 0.}];
    p = RandomReal[NormalDistribution[], 3];
    If[Norm[p] < 0.3, p = 0.3 p/Max[Norm[p], 10.^-8]];
    rb = channel[sg, sf, p];
    r0 = channel[sg, 0., p];
    AppendTo[rowsA, ra];
    AppendTo[rowsB, <|"sg" -> sg, "sf" -> sf, "rb" -> rb|>];
    AppendTo[rows0, <|"sg" -> sg, "r0" -> r0|>];
  ];
, {60}];

alErr = Max[Table[Abs[rowsA[[i]]["cI"] - rowsA[[i]]["alignedTarget"]], {i, Length[rowsA]}]];
alA = Max[rowsA[[All, "cA"]]];
alDist = Max[rowsA[[All, "distI"]]];
boErr = Max[Table[rowsB[[i]]["rb"]["err"], {i, Length[rowsB]}]];
boDep = Min[Table[Abs[rowsB[[i]]["rb"]["cI"] - rowsB[[i]]["sg"]^2/(rowsB[[i]]["sg"] + rowsB[[i]]["sf"])], {i, Length[rowsB]}]];
boA = Median[Table[rowsB[[i]]["rb"]["cA"], {i, Length[rowsB]}]];
sep = Min[Table[Abs[rowsB[[i]]["rb"]["cI"] - rowsB[[i]]["sg"]], {i, Length[rowsB]}]];
sf0Err = Max[Table[Abs[rows0[[i]]["r0"]["cI"] - rows0[[i]]["sg"]], {i, Length[rows0]}]];
sf0A = Max[Table[rows0[[i]]["r0"]["cA"], {i, Length[rows0]}]];

summary = <|
  "engine" -> "WolframEngine15",
  "n" -> 60,
  "alpha_sq_err" -> alphaSqErr,
  "aligned_pass" -> (alErr < 10.^-8 && alA < 10.^-8 && alDist < 10.^-8),
  "aligned_max_err_vs_sg2_over_S" -> alErr,
  "aligned_max_alpha_channel" -> alA,
  "aligned_max_dist_to_I" -> alDist,
  "boost_max_err_vs_closed_form" -> boErr,
  "boost_min_departure_from_sg2_over_S" -> boDep,
  "boost_median_alpha_channel" -> boA,
  "boost_min_sep_cI_from_Sigma_g" -> sep,
  "boost_changes_weight" -> (boDep > 10.^-3 && boErr < 10.^-8),
  "sf0_max_err_vs_sg" -> sf0Err,
  "sf0_max_alpha_channel" -> sf0A
|>;
Export["Opsi2_Gamma_Matrix_Coefficient_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
