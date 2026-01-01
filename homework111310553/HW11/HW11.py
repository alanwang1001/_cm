import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    # 1. 求特徵方程的根
    roots = np.roots(coefficients)
    
    # 2. 處理數值誤差：將極小的虛部捨去，並對根進行四捨五入以便統計重根
    # 使用 round 處理到小數點後 6 位，這足以區分不同的根並合併數值誤差產生的微小差異
    rounded_roots = []
    for r in roots:
        real_part = round(r.real, 6)
        imag_part = round(r.imag, 6)
        # 如果虛部極小，視為實根
        if abs(imag_part) < 1e-8:
            rounded_roots.append(real_part + 0j)
        else:
            rounded_roots.append(real_part + imag_part * 1j)
    
    # 3. 統計每個根出現的次數（重根數）
    root_counts = Counter(rounded_roots)
    
    # 4. 由於複數根總是成對出現 (a + bi, a - bi)，我們只處理虛部 > 0 的部分
    # 我們將處理過的根記錄下來，避免重複處理共軛複數
    processed_roots = set()
    terms = []
    c_idx = 1
    
    # 排序根，讓輸出結果更有規律（先實根後複根，或按大小排）
    unique_roots = sorted(root_counts.keys(), key=lambda x: (x.imag != 0, x.real, x.imag))

    for root in unique_roots:
        if root in processed_roots:
            continue
            
        multiplicity = root_counts[root]
        
        if root.imag == 0:
            # 實根處理: (C_1 + C_2x + ... + C_mx^n) * e^(rx)
            r = root.real
            for i in range(multiplicity):
                x_part = f"x^{i}" if i > 0 else ""
                # 簡化顯示：x^1 寫成 x
                if i == 1: x_part = "x"
                terms.append(f"C_{c_idx}{x_part}e^({r}x)")
                c_idx += 1
            processed_roots.add(root)
            
        else:
            # 複數根處理: e^(ax) * [ (C_1 + C_2x...)cos(bx) + (C_k + C_k+1x...)sin(bx) ]
            alpha = root.real
            beta = abs(root.imag)
            # 找到對應的共軛根
            conj_root = complex(alpha, -beta)
            
            # 複數重根的處理
            for i in range(multiplicity):
                x_part = f"x^{i}" if i > 0 else ""
                if i == 1: x_part = "x"
                
                # 構造 cos 和 sin 項
                exp_part = f"e^({alpha}x)" if alpha != 0 else ""
                
                terms.append(f"C_{c_idx}{x_part}{exp_part}cos({beta}x)")
                c_idx += 1
                terms.append(f"C_{c_idx}{x_part}{exp_part}sin({beta}x)")
                c_idx += 1
            
            processed_roots.add(root)
            processed_roots.add(conj_root)

    return "y(x) = " + " + ".join(terms)

# --- 測試主程式 (使用你提供的範例) ---
if __name__ == "__main__":
    print("--- 實數單根範例 ---")
    coeffs1 = [1, -3, 2]
    print(f"方程係數: {coeffs1}")
    print(solve_ode_general(coeffs1))

    print("\n--- 實數重根範例 ---")
    coeffs2 = [1, -4, 4]
    print(f"方程係數: {coeffs2}")
    print(solve_ode_general(coeffs2))

    print("\n--- 複數共軛根範例 ---")
    coeffs3 = [1, 0, 4]
    print(f"方程係數: {coeffs3}")
    print(solve_ode_general(coeffs3))

    print("\n--- 複數重根範例 ---")
    coeffs4 = [1, 0, 2, 0, 1]
    print(f"方程係數: {coeffs4}")
    print(solve_ode_general(coeffs4))

    print("\n--- 高階重根範例 ---")
    coeffs5 = [1, -6, 12, -8]
    print(f"方程係數: {coeffs5}")
    print(solve_ode_general(coeffs5))
