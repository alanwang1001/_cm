import math

def calculate_log_probability(p, n):
    # 計算常用對數 log10(p^n) = n * log10(p)
    log10_val = n * math.log10(p)
    
    # 計算自然對數 ln(p^n) = n * ln(p)
    ln_val = n * math.log(p)
    
    return log10_val, ln_val

# 設定參數
p = 0.5
n = 10000

log10_result, ln_result = calculate_log_probability(p, n)

print(f"對於 p={p}, n={n}:")
print("-" * 30)
print(f"1. 自然對數 ln(p^n)      = {ln_result:.4f}")
print(f"2. 常用對數 log10(p^n)   = {log10_result:.4f}")
print("-" * 30)

# 解析結果含義
mantissa = 10 ** (log10_result % 1)
exponent = int(log10_result // 1)
print(f"科學計數法表示：{mantissa:.2f} * 10^{exponent}")
