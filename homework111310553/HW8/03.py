import numpy as np

def calculate_information_metrics(P, Q):
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)
    P /= P.sum()
    Q /= Q.sum()
    epsilon = 1e-12
    P_eps = P + epsilon
    Q_eps = Q + epsilon
    entropy = -np.sum(P * np.log2(P_eps))
    cross_entropy = -np.sum(P * np.log2(Q_eps))）
    kl_divergence = np.sum(P * np.log2(P_eps / Q_eps))

    return entropy, cross_entropy, kl_divergence

P = [0.1, 0.2, 0.7] 
Q = [0.3, 0.3, 0.4] 
h, ce, kl = calculate_information_metrics(P, Q)

print(f"1. 熵 (Entropy): {h:.4f} bits")
print(f"2. 交叉熵 (Cross Entropy): {ce:.4f} bits")
print(f"3. KL 散度 (KL Divergence): {kl:.4f} bits")
print(f"驗證 H(P, Q) = H(P) + D_KL(P||Q): {h + kl:.4f}")
