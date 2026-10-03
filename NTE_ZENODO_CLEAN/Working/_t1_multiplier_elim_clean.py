# -*- coding: utf-8 -*-
"""T-1 clean verification: Door-A multiplier elimination (old C9 action)."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from sympy import (
    symbols, Function, diff, simplify, expand, solve, sqrt, together, collect
)

t = symbols('t', real=True)
n = Function('n')(t)
a = Function('a')(t)
Phi = Function('Phi')(t)
mu = Function('mu')(t)

M, beta, lam = symbols('M beta lam', real=True, positive=True)

ad = diff(a, t)
Phid = diff(Phi, t)
Phidd = diff(Phi, t, 2)
add = diff(a, t, 2)

F = M**2 + Phi**2/6
Fd = Phi*Phid/3

def L_build(measure, Vexpr, k_val):
    L0 = (
        -3*F*a*ad**2/n
        -3*a**2*ad*Fd/n
        + a**3*Phid**2/(2*n)
        - n*a**3*Vexpr
        + 3*F*k_val*a*n
    )
    if measure == 'sqrtg':
        Lmu = mu*(a**2*ad - n*a**3*beta*Phi**2)
    else:
        Lmu = mu*(ad/a - n*beta*Phi**2)
    return L0 + Lmu

def el_phi(L):
    return simplify(diff(L.diff(Phid), t) - L.diff(Phi))

def on_shell_constraint(measure, Vexpr, k_val, label):
    L = L_build(measure, Vexpr, k_val)
    EPhi = expand(el_phi(L))
    mu_sol = simplify(solve(EPhi, mu)[0])
    Cn = L.diff(n)
    C = Cn.subs(mu, mu_sol).subs(n, 1)

    Hs, Hds, Hdds = symbols('H Hd Hdd', real=True)
    H_fun = ad/a
    Hd_fun = diff(H_fun, t)
    Hdd_fun = diff(Hd_fun, t)
    Phid_c = Hd_fun/(2*beta*Phi)
    Phidd_c = Hdd_fun/(2*beta*Phi) - Phid_c**2/Phi

    C2 = C.subs({Phidd: Phidd_c, Phid: Phid_c})
    C2 = expand(C2.subs(add, a*(Hd_fun + H_fun**2)))
    C2 = expand(C2.subs(ad, H_fun*a))

    for _ in range(10):
        C2 = expand(C2.subs(Phi**2, H_fun/beta))
    C2 = together(C2)
    num, den = C2.as_numer_denom()
    num = expand(num)
    den = expand(den)
    for _ in range(10):
        num = expand(num.subs(Phi**2, H_fun/beta))
        den = expand(den.subs(Phi**2, H_fun/beta))
    if num.has(Phi):
        num = expand(num.subs(Phi, sqrt(H_fun/beta)))
    if den.has(Phi):
        den = expand(den.subs(Phi, sqrt(H_fun/beta)))
    R = simplify(num/den)

    R = R.subs(a.diff(t, 3), a*(Hdds + 3*Hs*Hds + Hs**3))
    R = R.subs(a.diff(t, 2), a*(Hds + Hs**2))
    R = R.subs(a.diff(t), Hs*a)
    R = expand(R)
    R = R.subs(ad, Hs*a)
    R = expand(simplify(R))

    Ra = simplify(R / a**3)
    Ra = expand(Ra)
    # Final sweep: any leftover Derivative(a,t) -> H a
    Ra = expand(Ra.subs(a.diff(t), Hs*a))
    Ra = simplify(Ra)

    print('====', label, '====')
    print('constraint/a^3 =', Ra)

    dS = simplify(Ra.subs({Hds: 0, Hdds: 0}))
    dS = expand(simplify(dS.subs(a.diff(t), Hs*a)))
    print('dS:', dS)
    print('dS collected:', collect(expand(dS), Hs))

    mu1 = mu_sol.subs(n, 1)
    mu1 = mu1.subs({Phid: 0, Phidd: 0, ad: Hs*a, add: a*Hs**2})
    for _ in range(8):
        mu1 = expand(mu1.subs(Phi**2, Hs/beta))
    if mu1.has(Phi):
        mu1 = mu1.subs(Phi, sqrt(Hs/beta))
    mu1 = simplify(mu1)
    print('mu_dS =', mu1)

    # Drop-mu (mu=0) dS comparison
    Cn0 = L.diff(n).subs(mu, 0).subs(n, 1)
    C0 = expand(Cn0.subs({Phid: 0, Phidd: 0, add: a*Hs**2, ad: Hs*a}))
    for _ in range(8):
        C0 = expand(C0.subs(Phi**2, Hs/beta))
    if C0.has(Phi):
        C0 = C0.subs(Phi, sqrt(Hs/beta))
    C0 = simplify(C0 / a**3)
    C0 = expand(simplify(C0.subs(a.diff(t), Hs*a)))
    print('dS drop-mu Cn/a3:', C0)
    print()
    return Ra, dS, mu1, C0


V_quart = lam * Phi**4
V_full = 3*beta**2*M**2 * Phi**4 - (beta**2/8)*Phi**6

for measure in ['sqrtg', 'dN']:
    for name, Vexpr in [('quart', V_quart), ('full', V_full)]:
        for k_val in [0, 1]:
            on_shell_constraint(measure, Vexpr, k_val, f'{measure}|{name}|k={k_val}')

print('==== NUMERIC dS BOUND ====')
beta_n = 2.38e-47
M_n = 2.435e18
Hmax0 = 4 * beta_n * M_n**2
rhomax0 = 3*M_n**2*Hmax0**2 - Hmax0**3/(2*beta_n)
print('lam=0: H_max =', Hmax0, 'GeV')
print('lam=0: rho_max^(1/4) =', rhomax0**0.25, 'GeV = ', rhomax0**0.25/1000, 'TeV')

lam_n = 3 * beta_n**2 * M_n**2
Hmax1 = 8 * beta_n * M_n**2
rhomax1 = 6*M_n**2*Hmax1**2 - Hmax1**3/(2*beta_n)
print('lam=3 beta^2 M^2: H_max =', Hmax1, 'GeV')
print('lam=3 beta^2 M^2: rho_max^(1/4) =', rhomax1**0.25, 'GeV =', rhomax1**0.25/1000, 'TeV')
print('H_x = 6 beta M^2 =', 6*beta_n*M_n**2, 'GeV')

# Full V analytic dS bound: from expected form
# After run we will read off dS for full V
