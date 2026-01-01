import math

def generate_fibonacci_analysis(n_terms):
    """
    產生費波那契數列並計算相鄰兩項的比值
    """
    if n_terms < 2:
        return "請輸入大於 2 的項數"

    fib_sequence = [0, 1]
    ratios = []

    print(f"{'項次':<5} | {'費波那契數':<15} | {'與前項比值 (趨近黃金比例)':<20}")
    print("-" * 50)
    print(f"{0:<5} | {0:<15} | {'N/A'}")
    print(f"{1:<5} | {1:<15} | {'N/A'}")

    for i in range(2, n_terms):
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
        
        # 計算相鄰兩項的比值
        ratio = fib_sequence[i] / fib_sequence[i-1]
        ratios.append(ratio)
        
        print(f"{i:<5} | {next_val:<15} | {ratio:.10f}")

    phi = (1 + math.sqrt(5)) / 2
    print("-" * 50)
    print(f"理論黃金比例 φ ≈ {phi:.10f}")
    print(f"最後一項計算誤差: {abs(ratios[-1] - phi):.10e}")

if __name__ == "__main__":
    print("--- 費波那契數列與黃金比例驗證程式 ---")
    try:
        terms = int(input("請輸入想要生成的項數 (建議 15-30): "))
        generate_fibonacci_analysis(terms)
    except ValueError:
        print("請輸入有效的整數")
