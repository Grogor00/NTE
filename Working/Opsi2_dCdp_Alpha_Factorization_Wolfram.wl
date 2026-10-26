(* Project Delta = M - sg I onto span{dC/dp_i}. *)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261026];
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

dCs[sf_, p_] := Module[{gp},
  gp = Sqrt[1. + p.p];
  Table[sf (p[[i]]/gp) id4 - sf alphas[[i]], {i, 3}]
];

vec[m_] := Flatten[m];
relProj[target_, cols_] := Module[{A, coef, nrm},
  nrm = Norm[vec[target]];
  If[nrm < 10.^-18, Return[0.]];
  A = Transpose[vec /@ cols];
  coef = PseudoInverse[A].vec[target];
  Norm[vec[target] - A.coef]/nrm
];

one[sg_, sf_, p_] := Module[{C, gp, K, M, Delta, dlist, p2, C2, fd},
  C = Cmat[sg, sf, p];
  gp = Sqrt[1. + p.p];
  K = Inverse[C];
  M = sg^2 alphas[[1]].K.alphas[[1]];
  Delta = M - sg id4;
  dlist = dCs[sf, p];
  p2 = p; p2[[1]] = p2[[1]] + 10.^-6;
  C2 = Cmat[sg, sf, p2];
  fd = Norm[(C2 - C)/10.^-6 - dlist[[1]]];
  <|
    "rel_dC" -> relProj[Delta, dlist],
    "rel_C" -> relProj[M, {C}],
    "abs_Delta" -> Norm[vec[Delta]],
    "fd" -> fd
  |>
];

gen = {}; zero = {}; sf0 = {};
Do[
  Module[{sg, sf, p, r},
    sg = RandomReal[{0.4, 2.}];
    sf = RandomReal[{0.4, 2.}];
    p = RandomReal[NormalDistribution[], 3];
    If[Norm[p] < 0.3, p = 0.3 p/Max[Norm[p], 10.^-8]];
    AppendTo[gen, one[sg, sf, p]];
    AppendTo[zero, one[sg, sf, {0., 0., 0.}]];
    AppendTo[sf0, one[sg, 0., p]];
  ];
, {60}];

med = Median[gen[[All, "rel_dC"]]];
mn = Min[gen[[All, "rel_dC"]]];
p0min = Min[zero[[All, "rel_dC"]]];
sf0max = Max[sf0[[All, "abs_Delta"]]];
fdmax = Max[gen[[All, "fd"]]];
summary = <|
  "engine" -> "WolframEngine15",
  "n" -> 60,
  "median_rel_resid_dCdp" -> med,
  "min_rel_resid_dCdp" -> mn,
  "median_rel_resid_onto_C" -> Median[gen[[All, "rel_C"]]],
  "min_rel_resid_onto_C" -> Min[gen[[All, "rel_C"]]],
  "p0_min_rel_dCdp" -> p0min,
  "sf0_max_abs_Delta" -> sf0max,
  "max_fd_err" -> fdmax,
  "escape_fails" -> (med > 10.^-2 && p0min > 10.^-2 && sf0max < 10.^-8 && fdmax < 10.^-6)
|>;
Export["Opsi2_dCdp_Alpha_Factorization_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
