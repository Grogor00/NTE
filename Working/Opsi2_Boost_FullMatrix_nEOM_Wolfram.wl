(* Full-matrix residual on flat gamma. ASCII. *)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261027];

id2 = IdentityMatrix[2];
sx = {{0, 1}, {1, 0}};
sy = {{0, -I}, {I, 0}};
sz = {{1, 0}, {0, -1}};
g0 = ArrayFlatten[{{id2, 0 id2}, {0 id2, -id2}}];
gammaI[s_] := ArrayFlatten[{{0 id2, s}, {-s, 0 id2}}];
gs = {gammaI[sx], gammaI[sy], gammaI[sz]};
alphas = Table[g0.gs[[i]], {i, 3}];
id4 = IdentityMatrix[4];

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

decomp[sg_, sf_, p_] := Module[{C, K, cI, cA, rest, pred, k, j, M, R},
  C = Cmat[sg, sf, p];
  K = Inverse[C];
  cI = Table[0., {3}];
  cA = Table[0., {3}, {3}];
  rest = Table[0., {3}];
  Do[
    M = sg^2 alphas[[k]].K.alphas[[k]];
    cI[[k]] = Re[Tr[M]/4];
    Do[cA[[k, j]] = Re[Tr[alphas[[j]].M]/4], {j, 3}];
    R = M - cI[[k]] id4;
    Do[R = R - cA[[k, j]] alphas[[j]], {j, 3}];
    rest[[k]] = Norm[R];
  , {k, 3}];
  pred = jammerI[sg, sf, p];
  <|"cI" -> cI, "cA" -> cA, "rest" -> Max[rest], "err" -> Max[Abs[cI - pred]]|>
];

drawP[] := Module[{p},
  p = RandomVariate[NormalDistribution[], 3];
  If[Norm[p] < 0.3, p = 0.3 p/Max[Norm[p], 10.^-8]];
  p
];

one[sg_, sf_, p_] := Module[{d, curI, curA, bracket, alphaVec, iMis, v, u, psi, dC, gp, i, k, j},
  d = decomp[sg, sf, p];
  curI = RandomVariate[NormalDistribution[], 3];
  curA = RandomVariate[NormalDistribution[], {3, 3}];
  psi = RandomVariate[NormalDistribution[], 4] + I RandomVariate[NormalDistribution[], 4];
  psi = psi/Norm[psi];
  gp = Sqrt[1. + p.p];
  u = Table[
    dC = sf (p[[i]]/gp) id4 - sf alphas[[i]];
    Re[Conjugate[psi].dC.psi]
  , {i, 3}];
  bracket = Table[
    d["cI"][[k]] curI[[k]] + Sum[d["cA"][[k, j]] curA[[j, k]], {j, 3}]
  , {k, 3}];
  alphaVec = Table[Sum[d["cA"][[k, j]] curA[[j, k]], {j, 3}], {k, 3}];
  iMis = (d["cI"] - sg) curI;
  v = bracket - sg curI;
  <|"resid" -> Norm[v],
    "alpha" -> Norm[alphaVec],
    "iPiece" -> Norm[iMis],
    "err" -> d["err"],
    "rest" -> d["rest"],
    "alphaCoeff" -> Max[Abs[Flatten[d["cA"]]]],
    "orth" -> If[Norm[v] < 10.^-12, 0., Norm[v - u (v.u)/Max[u.u, 10.^-18]]/Norm[v]]|>
];

n = 40;
boost = Table[one[RandomReal[{0.4, 2.}], RandomReal[{0.4, 2.}], drawP[]], {n}];
sf0 = Table[one[RandomReal[{0.4, 2.}], 0., drawP[]], {20}];
med[key_] := Median[boost[[All, key]]];
out = <|
  "engine" -> "wolfram",
  "n" -> n,
  "median_resid" -> med["resid"],
  "median_alpha_piece" -> med["alpha"],
  "median_I_piece" -> med["iPiece"],
  "median_orth_frac" -> med["orth"],
  "max_cI_err" -> Max[boost[[All, "err"]]],
  "max_rest" -> Max[boost[[All, "rest"]]],
  "sf0_max_resid" -> Max[sf0[[All, "resid"]]],
  "sf0_max_alpha" -> Max[sf0[[All, "alphaCoeff"]]]
|>;
Export["Opsi2_Boost_FullMatrix_nEOM_WOLFRAM.json", out, "JSON"];
