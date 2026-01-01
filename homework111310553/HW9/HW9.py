import numpy as np
from scipy.linalg import lu, eig, svd

# ---------------------------------------------------------
# 1. 遞迴計算行列式 (Recursive Determinant)
# ---------------------------------------------------------
def recursive_det(M):
    # 基本情況：1x1 或 2x2 矩陣
    n = M.shape[0]
    if n == 1:
        return M[0, 0]
    if n == 2:
        return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    
    det = 0
    for j in range(n):
        # 取得餘因子矩陣 (Minor): 刪除第 0 列與第 j 欄
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        # 代數餘子式公式
        det += ((-1)**j) * M[0, j] * recursive_det(minor)
    return det

# ---------------------------------------------------------
# 2. LU 分解計算行列式
# ---------------------------------------------------------
def det_via_lu(M):
    # P: 置換矩陣, L: 下三角 (對角線為1), U: 上三角
    P, L, U = lu(M)
    # 行列式 = det(P) * det(L) * det(U)
    # det(L) = 1, det(U) = 對角線乘積
    # det(P) 取決於交換次數 (1 或 -1)
    det_P = np.linalg.det(P) 
    det_U = np.prod(np.diag(U))
    return det_P * det_U

# ---------------------------------------------------------
# 測試數據準備
# ---------------------------------------------------------
A = np.array([[4, 3, 2],
              [3, 2, 1],
              [2, 1, 3]], dtype=float)

print(f"原始矩陣 A:\n{A}\n")
print(f"1. 遞迴行列式結果: {recursive_det(A)}")
print(f"2. LU 分解行列式結果: {det_via_lu(A)}")
print("-" * 30)

# ---------------------------------------------------------
# 3. 驗證矩陣分解重構 (Reconstruction)
# ---------------------------------------------------------
# (a) LU 分解
P, L, U = lu(A)
print("LU 驗證 (P*L*U):", np.allclose(A, P @ L @ U))

# (b) 特徵值分解 (Eigen Decomposition)
evals, evecs = eig(A)
# A = Q \Lambda Q^-1
A_eig_recon = evecs @ np.diag(evals) @ np.linalg.inv(evecs)
print("特徵值分解驗證:", np.allclose(A, A_eig_recon))

# (c) SVD 分解
u_mat, s_vec, vt_mat = svd(A)
# A = U \Sigma V^T
A_svd_recon = u_mat @ np.diag(s_vec) @ vt_mat
print("SVD 驗證:", np.allclose(A, A_svd_recon))
print("-" * 30)

# ---------------------------------------------------------
# 4. 用特徵值分解實作 SVD
# ---------------------------------------------------------
def svd_via_eigen(M):
    # 1. 計算 M^T M 的特徵值與特徵向量得到 V
    w_v, v = np.linalg.eigh(M.T @ M)
    # 排序（特徵值由大到小）
    idx = w_v.argsort()[::-1]
    w_v, v = w_v[idx], v[:, idx]
    
    # 2. 奇異值是特徵值的平方根
    s = np.sqrt(np.maximum(w_v, 0))
    
    # 3. 計算 U = M * V * Sigma^-1
    # 這裡簡化處理，實際需考慮 s=0 的情況
    u = M @ v / s
    return u, s, v.T

u_custom, s_custom, vt_custom = svd_via_eigen(A)
print("自定義 SVD 奇異值:", s_custom)
print("-" * 30)

# ---------------------------------------------------------
# 5. 主成分分析 (PCA) 實作
# ---------------------------------------------------------
def run_pca(data, k):
    # 1. 中心化 (Zero-mean)
    mean_vec = np.mean(data, axis=0)
    centered_data = data - mean_vec
    
    # 2. SVD 分解 (對中心化後的數據)
    # data = U * S * V^T, V 的每一行就是主成分
    U, S, Vt = svd(centered_data)
    
    # 3. 投影到前 k 個主成分
    # 投影結果 = Data * V[:, :k]
    principal_components = Vt[:k, :].T
    projected_data = centered_data @ principal_components
    
    return projected_data, principal_components

# 模擬 5 筆 3 維數據進行 PCA 降到 2 維
sample_data = np.random.rand(5, 3)
reduced_data, components = run_pca(sample_data, 2)
print("PCA 降維後的數據 (5x2):\n", reduced_data)
