(* Q-Stage3 algebraic excess — Wolfram Engine *)
SetDirectory[DirectoryName[$InputFileName]];

hg = DiagonalMatrix[Array[hgS, 3]];
X  = DiagonalMatrix[Array[xS, 3]];
G  = hg.X;
hf = hg.X.X;
W  = hg.(IdentityMatrix[3] - X).(IdentityMatrix[3] - X);
Wdiff = Simplify[W - (hg + hf - 2*G)];

pig = Array[pgS, 3];
p   = Array[pS, 3];
rem  = Simplify[hg.pig + hf.(-pig - p) + W.p];
rem0 = Simplify[hg.pig + hf.(-pig)];
excess = Simplify[rem - rem0];

e1 = Simplify[excess - (W - hf).p];
e2 = Simplify[excess - hg.(IdentityMatrix[3] - 2*X).p];
k1 = Simplify[excess /. {xS[1]->1, xS[2]->1, xS[3]->1}];

wOK = PossibleZeroQ[Together[Tr[Wdiff.Wdiff]]];
e1OK = PossibleZeroQ[Together[excess.excess - ((W-hf).p).((W-hf).p)]] && PossibleZeroQ[Together[Norm[e1]^2]];
(* simpler: *)
e1OK = PossibleZeroQ[Together[e1.e1]];
e2OK = PossibleZeroQ[Together[e2.e2]];
k1OK = PossibleZeroQ[Together[k1.k1]];

(* Dirac matrix det identity — symbolic *)
a = Symbol["aSC"]; b = Symbol["bSC"]; c = Symbol["cSS"];
det = Simplify[a*c + b^2];
detIfC0 = Simplify[det /. c -> 0];

out = {
  {"W_equals_hg_hf_minus_2G", wOK},
  {"excess_equals_W_minus_hf_times_p", e1OK},
  {"excess_equals_hg_I_minus_2X_times_p", e2OK},
  {"K1_excess_vanishes_at_X_I", k1OK},
  {"dirac_det", ToString[det, InputForm]},
  {"dirac_det_if_c_0", ToString[detIfC0, InputForm]},
  {"excess_vector_InputForm", ToString[excess, InputForm]}
};

stream = OpenWrite["Opsi2_QStage3_WOLFRAM_RESULTS.txt"];
Scan[WriteString[stream, #[[1]], " = ", ToString[#[[2]], InputForm], "\n"] &, out];
Close[stream];
Print[out];
Exit[0];
