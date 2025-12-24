import numpy as np

def cross_entropy(P, Q):
    epsilon = 1e-12
    return -np.sum(P * np.log2(Q + epsilon))

P = np.array([0.1, 0.7, 0.2])
h_pp = cross_entropy(P, P)

print(f"真實分佈 P: {P}")
print(f"H(P, P) [即 Entropy H(P)]: {h_pp:.6f}")
print("-" * 40)
print(f"{'分佈 Q':<25} | {'H(P, Q)':<10} | {'是否 > H(P, P)?'}")
print("-" * 40)

test_qs = [
    [0.3, 0.4, 0.3],
    [0.1, 0.6, 0.3],
    [0.8, 0.1, 0.1],
    [0.33, 0.33, 0.34],
]
for q_list in test_qs:
    Q = np.array(q_list)
    h_pq = cross_entropy(P, Q)
    print(f"{str(q_list):<25} | {h_pq:.6f}   | {h_pq > h_pp}")
