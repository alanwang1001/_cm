import cmath

def dft(x):
    """
    離散傅立葉正轉換 (DFT)
    :param x: 輸入訊號 (List of numbers)
    :return: 頻率域表示 (List of complex numbers)
    """
    N = len(x)
    X = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # 尤拉公式 e^(-i*2*pi*k*n/N)
            angle = -2j * cmath.pi * k * n / N
            sum_val += x[n] * cmath.exp(angle)
        X.append(sum_val)
    return X

def idft(X):
    """
    離散傅立葉逆轉換 (IDFT)
    :param X: 頻率域訊號 (List of complex numbers)
    :return: 時間域表示 (List of complex numbers)
    """
    N = len(X)
    x = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # 尤拉公式 e^(i*2*pi*k*n/N)
            angle = 2j * cmath.pi * k * n / N
            sum_val += X[k] * cmath.exp(angle)
        # 逆轉換需要除以 N
        x.append(sum_val / N)
    return x

# --- 測試程式碼 ---
if __name__ == "__main__":
    # 定義一個簡單的訊號
    original_signal = [1.0, 2.0, 3.0, 4.0]
    print(f"原始訊號: {original_signal}")

    # 執行 DFT
    fft_result = dft(original_signal)
    print("\nDFT 結果 (頻率域):")
    for i, val in enumerate(fft_result):
        print(f"  bin {i}: {val:.2f}")

    # 執行 IDFT 回推
    recovered_signal = idft(fft_result)
    print("\nIDFT 回推訊號 (應與原始訊號接近):")
    # 只取實部，因為逆轉換後的虛部通常趨近於 0
    formatted_recovered = [round(val.real, 2) for val in recovered_signal]
    print(formatted_recovered)
