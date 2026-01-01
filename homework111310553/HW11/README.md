# 常係數齊次常微分方程 (ODE) 通用求解器

本程式使用 `numpy.roots` 尋找特徵方程的根，並透過 `collections.Counter` 處理重根邏輯，同時解決了數值計算中常見的微小浮點數誤差問題。

## 1. 程式碼實作

```python
import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次常微分方程: a_n y^(n) + ... + a_1 y' + a_0 y = 0
    參數 coefficients: [a_n, a_n-1, ..., a_0] 係數列表
    """
    # 1. 求特徵方程的根 (lambda)
    roots = np.roots(coefficients)
    
    # 2. 數值清理：處理浮點數微小誤差
    # 將極小的項歸零，並四捨五入到小數點後 6 位以利於 Counter 統計重根
    refined_roots = []
    for r in roots:
        real_part = round(r.real, 6)
        imag_part = round(r.imag, 6)
        # 虛部若極小則視為實根
        if abs(imag_part) < 1e-8:
            refined_roots.append(real_part + 0j)
        else:
            refined_roots.append(real_part + imag_part * 1j)
    
    # 3. 統計每個根的重數 (Multiplicity)
    root_counts = Counter(refined_roots)
    
    # 4. 根據根的性質建構通解字串
    processed_roots = set()
    terms = []
    c_idx = 1
    
    # 排序：實根在前，複數根在後
    sorted_unique_roots = sorted(root_counts.keys(), key=lambda x: (abs(x.imag) > 1e-5, x.real, x.imag))

    for r in sorted_unique_roots:
        if r in processed_roots:
            continue
            
        m = root_counts[r] # 重數
        
        # --- 情況 A: 實根 ---
        if abs(r.imag) < 1e-5:
            val = r.real
            for i in range(m):
                # 處理 x 的次方
                x_pow = "" if i == 0 else ("x" if i == 1 else f"x^{i}")
                # 處理指數部分
                exp_part = "1" if val == 0 and i == 0 else f"e^({val}x)"
                if val == 0 and i > 0: exp_part = "" # y = C_1 + C_2x ...
                
                terms.append(f"C_{c_idx}{x_pow}{exp_part}")
                c_idx += 1
            processed_roots.add(r)
            
        # --- 情況 B: 複數共軛根 (alpha +/- beta*i) ---
        else:
            alpha = r.real
            beta = abs(r.imag)
            conj_root = complex(alpha, -beta)
            
            for i in range(m):
                x_pow = "" if i == 0 else ("x" if i == 1 else f"x^{i}")
                exp_part = f"e^({alpha}x)" if alpha != 0 else ""
                
                # 加入 cos 項
                terms.append(f"C_{c_idx}{x_pow}{exp_part}cos({beta}x)")
                c_idx += 1
                # 加入 sin 項
                terms.append(f"C_{c_idx}{x_pow}{exp_part}sin({beta}x)")
                c_idx += 1
                
            processed_roots.add(r)
            processed_roots.add(conj_root)

    return "y(x) = " + " + ".join(terms)

# --- 測試主程式 ---
if __name__ == "__main__":
    test_cases = [
        ("實數單根", [1, -3, 2]),           # y'' - 3y' + 2y = 0
        ("實數重根", [1, -4, 4]),           # y'' - 4y' + 4y = 0
        ("複數共軛根", [1, 0, 4]),          # y'' + 4y = 0
        ("複數重根", [1, 0, 2, 0, 1]),      # (D^2 + 1)^2 y = 0
        ("高階重根", [1, -6, 12, -8])       # (D - 2)^3 y = 0
    ]

    for name, coeffs in test_cases:
        print(f"--- {name} ---")
        print(f"方程係數: {coeffs}")
        print(solve_ode_general(coeffs), "\n")
