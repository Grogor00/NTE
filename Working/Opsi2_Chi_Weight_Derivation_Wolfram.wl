(* Derive {E,E}_D from the constraint matrix. ASCII twin: .txt *)
SetDirectory[DirectoryName[$InputFileName]];
SeedRandom[20261022];
n = 6;
dim = 4 n;

makeJ[] := Module[{J, i},
  J = ConstantArray[0., {dim, dim}];
  Do[
    J[[i, 2 n + i]] = 1.;
    J[[2 n + i, i]] = -1.;
    J[[n + i, 3 n + i]] = 1.;
    J[[3 n + i, n + i]] = -1.;
  , {i, n}];
  J
];
Jmat = makeJ[];

constraintGrads[sigma_] := Module[{grads, g, i},
  grads = {};
  Do[
    g = ConstantArray[0., dim];
    g[[2 n + i]] = 1.;
    AppendTo[grads, g];
  , {i, n}];
  Do[
    g = ConstantArray[0., dim];
    g[[3 n + i]] = 1.;
    g[[i]] = -sigma;
    AppendTo[grads, g];
  , {i, n}];
  grads
];

gradE[i_, u_, v_, sg_, omega_] := Module[{g, ip, im, dv},
  g = ConstantArray[0., dim];
  ip = Mod[i, n] + 1;
  im = Mod[i - 2, n] + 1;
  dv = 0.5 (v[[ip]] - v[[im]]) + omega[[i]] v[[i]];
  g[[i]] = sg dv;
  g[[n + ip]] += sg u[[i]] 0.5;
  g[[n + im]] += sg u[[i]] (-0.5);
  g[[n + i]] += sg u[[i]] omega[[i]];
  g
];

diracBlock[u_, v_, omega_, sg_, sigma_] := Module[{gchi, C, Cinv, gE, Ech, chE, poisson, dirac, i, j},
  gchi = constraintGrads[sigma];
  C = Table[gchi[[a]].Jmat.gchi[[b]], {a, 2 n}, {b, 2 n}];
  Cinv = Inverse[C];
  gE = Table[gradE[i, u, v, sg, omega], {i, n}];
  Ech = Table[gE[[i]].Jmat.gchi[[a]], {i, n}, {a, 2 n}];
  chE = Table[gchi[[b]].Jmat.gE[[j]], {b, 2 n}, {j, n}];
  poisson = Table[gE[[i]].Jmat.gE[[j]], {i, n}, {j, n}];
  dirac = poisson - Ech.Cinv.chE;
  {dirac, C}
];

alphaOf[meas_, unit_] := Module[{m, uvec, den},
  m = Flatten[meas];
  uvec = Flatten[unit];
  den = uvec.uvec;
  If[den < 1.*^-18, Return[$Failed]];
  m.uvec/den
];

rows = {};
cErr = {};
Do[
  Module[{u, v, omega, sg, sf, sigma, unit, meas, C, bare, abare, a, k5, a5, sf0, a0, zero},
    u = RandomReal[NormalDistribution[], n];
    v = RandomReal[NormalDistribution[], n];
    omega = 0.5 RandomReal[NormalDistribution[], n];
    sg = RandomReal[{0.4, 2.}];
    sf = RandomReal[{0.4, 2.}];
    sigma = sg + sf;
    {unit, C} = diracBlock[u, v, omega, 1., 1.];
    {meas, C} = diracBlock[u, v, omega, sg, sigma];
    zero = ConstantArray[0., n];
    a = alphaOf[meas, unit];
    abare = alphaOf[diracBlock[u, v, zero, sg, sigma][[1]], diracBlock[u, v, zero, 1., 1.][[1]]];
    If[a === $Failed || abare === $Failed, Continue[]];
    AppendTo[cErr, Abs[C[[1, n + 1]] - sigma]];
    a5 = alphaOf[diracBlock[u, v, omega, sf, sigma][[1]], unit];
    a0 = alphaOf[diracBlock[u, v, omega, sg, sg][[1]], unit];
    AppendTo[rows, <|
      "err" -> Abs[a - sg^2/sigma],
      "sep_sg" -> Abs[a - sg],
      "sep_sigma" -> Abs[a - sigma],
      "sep_theta" -> Abs[a - sg/sigma],
      "k5" -> Abs[a5 - sf^2/sigma],
      "sf0" -> Abs[a0 - sg],
      "omega" -> Abs[a - abare]
    |>];
  ];
, {40}];

summary = <|
  "engine" -> "WolframEngine15",
  "n" -> Length[rows],
  "max_abs_err_vs_sg2_over_S" -> Max[rows[[All, "err"]]],
  "max_C_entry_err" -> Max[cErr],
  "min_sep_from_Sigma_g" -> Min[rows[[All, "sep_sg"]]],
  "min_sep_from_Sigma" -> Min[rows[[All, "sep_sigma"]]],
  "min_sep_from_theta" -> Min[rows[[All, "sep_theta"]]],
  "max_k5_err" -> Max[rows[[All, "k5"]]],
  "max_sf0_err" -> Max[rows[[All, "sf0"]]],
  "max_omega_changes_alpha" -> Max[rows[[All, "omega"]]],
  "weight_is_sg2_over_S" -> (
    Max[rows[[All, "err"]]] < 1.*^-8 &&
    Min[rows[[All, "sep_sg"]]] > 1.*^-3 &&
    Min[rows[[All, "sep_sigma"]]] > 1.*^-3 &&
    Min[rows[[All, "sep_theta"]]] > 1.*^-3 &&
    Max[rows[[All, "k5"]]] < 1.*^-8 &&
    Max[rows[[All, "sf0"]]] < 1.*^-8 &&
    Max[cErr] < 1.*^-8
  )
|>;
Export["Opsi2_Chi_Weight_Derivation_WOLFRAM.json", summary, "RawJSON"];
Print[summary];
Exit[0];
