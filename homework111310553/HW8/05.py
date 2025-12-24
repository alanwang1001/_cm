import numpy as np

# 定義生成矩陣 G (4x7)
# 前 4 欄為單位矩陣 (Identity)，後 3 欄為校驗位元生成邏輯
G = np.array([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
])

H = np.array([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
])

def encode(data_bits):
    """將 4 位元資料編碼為 7 位元"""
    codeword = np.dot(data_bits, G) % 2
    return codeword

def decode(received_bits):
    """解碼並修正 1 位元錯誤"""
    syndrome = np.dot(received_bits, H.T) % 2

    error_idx = -1
    for i in range(H.shape[1]):
        if np.array_equal(syndrome, H[:, i]):
            error_idx = i
            break
            
    corrected_bits = received_bits.copy()
    if error_idx != -1:
        print(f"偵測到錯誤！錯誤發生在位置: {error_idx}")
        corrected_bits[error_idx] = (corrected_bits[error_idx] + 1) % 2
    else:
        print("未偵測到錯誤。")
    return corrected_bits[:4]

# --- 測試程式 ---
data = np.array([1, 0, 1, 1])
print(f"原始資料: {data}")
encoded = encode(data)
print(f"編碼後 (7位元): {encoded}")
received = encoded.copy()
received[2] = (received[2] + 1) % 2 
print(f"收到的資料 (含錯誤): {received}")

# 解碼與修正
decoded_data = decode(received)
print(f"修正後的原始資料: {decoded_data}")
