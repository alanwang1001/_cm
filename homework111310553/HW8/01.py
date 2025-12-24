from decimal import Decimal, getcontext

# 設定足夠的精度（有效數位）
getcontext().prec = 10 

# 計算 (1/2)^10000
p = Decimal('0.5')
result = p ** 10000

print(f"連續 10,000 次正面的精確機率約為：")
print(f"{result:.2e}") # 以科學計數法顯示
