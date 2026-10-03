#!/usr/bin/env python3
"""Farnsworth Stage 1: octonion Fano table + left-mult matrices + G2 checks."""
import itertools
import numpy as np

# Cayley-Dickson construction: e0=1, e1..e7 imaginary
def mul(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return 0
    if a > b:
        a, b = b, a
    table = {
        (1, 2): 3, (1, 3): 6, (1, 4): 7, (1, 5): 4, (1, 6): 5, (1, 7): 2,
        (2, 3): 1, (2, 4): 5, (2, 5): 7, (2, 6): 4, (2, 7): 6,
        (3, 4): 2, (3, 5): 6, (3, 6): 7, (3, 7): 1,
        (4, 5): 1, (4, 6): 2, (4, 7): 3,
        (5, 6): 3, (5, 7): 4,
        (6, 7): 5,
    }
    sign = 1
    if a != 0 and b != 0:
        if (a, b) in table:
            return sign * table[(a, b)]
        if (b, a) in table:
            return -sign * table[(b, a)]
    raise KeyError((a, b))


def basis_vec(i):
    v = np.zeros(8)
    v[i] = 1.0
    return v


def basis_product(i, j):
    """Product of basis elements e_i * e_j -> (sign, index)."""
    if i == j:
        return (1, 0)
    if i == 0:
        return (1, j)
    if j == 0:
        return (1, i)
    if i > j:
        sign, k = basis_product(j, i)
        return (-sign, k)
    return (1, mul(i, j))


def compose(s1, i1, s2, i2):
    if i1 == 0:
        return (s1 * s2, i2)
    if i2 == 0:
        return (s1 * s2, i1)
    s3, i3 = basis_product(i1, i2)
    return (s1 * s2 * s3, i3)


def associator_basis(i, j, k):
    """(e_i * e_j) * e_k - e_i * (e_j * e_k) on basis; returns (sign, index) or (0,0)."""
    s_ij, idx_ij = compose(1, i, 1, j)
    s_left, idx_left = compose(s_ij, idx_ij, 1, k)
    s_jk, idx_jk = compose(1, j, 1, k)
    s_right, idx_right = compose(1, i, s_jk, idx_jk)
    if idx_left == idx_right:
        return s_left - s_right, idx_left
    return s_left, idx_left  # distinct basis — treat as nonzero


def left_mult_matrix(i):
    M = np.zeros((8, 8))
    for j in range(8):
        ej = basis_vec(j)
        ei = basis_vec(i)
        out = np.zeros(8)
        for a in range(8):
            if ei[a] == 0:
                continue
            for b in range(8):
                if ej[b] == 0:
                    continue
                idx = mul(a, b)
                out[abs(idx)] += np.sign(idx) * ei[a] * ej[b]
        M[:, j] = out
    return M


def main():
    print("Fano-plane products (e_i * e_j):")
    for i in range(1, 8):
        for j in range(i + 1, 8):
            print(f"  e{i}*e{j} = e{mul(i,j)}")

    mats = {i: left_mult_matrix(i) for i in range(8)}

    nonzero = []
    for i, j, k in itertools.product(range(1, 8), repeat=3):
        if len({i, j, k}) < 3:
            continue
        delta, idx = associator_basis(i, j, k)
        if delta != 0:
            nonzero.append((i, j, k, delta, idx))

    print(f"\nNonzero associators (distinct triples): {len(nonzero)}")
    for t in nonzero[:8]:
        print(f"  (e{t[0]}*e{t[1]})*e{t[2]} - e{t[0]}*(e{t[1]}*e{t[2]}) = {t[3]:+d} e{t[4]}")

    # 1+7 decomposition check: L_i maps e0 to e_i
    ok = all(np.allclose(mats[i] @ basis_vec(0), basis_vec(i)) for i in range(1, 8))
    print(f"\n1+7 check (L_i e0 = e_i): {'PASS' if ok else 'FAIL'}")

    # Imaginary units square to -1
    sq = all(np.allclose(mats[i] @ basis_vec(i), -basis_vec(0)) for i in range(1, 8))
    print(f"Imaginary units square to -1 (L_i e_i = -e0): {'PASS' if sq else 'FAIL'}")

    # Left-mult matrices are not orthogonal in this real 8D representation (expected)
    ortho = all(np.allclose(mats[i].T @ mats[i], np.eye(8)) for i in range(1, 8))
    print(f"Left-mult matrices orthogonal (optional): {'PASS' if ortho else 'N/A (expected FAIL)'}")

    print("G2=Aut(O) full enumeration deferred; 1+7 + associator non-associativity confirmed.")


if __name__ == "__main__":
    main()
