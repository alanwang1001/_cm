import cmath

def root3(a, b, c, d):
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    delta = (q/2)**2 + (p/3)**3
    
    # 取得 u 的其中一個立方根
    u = (-q/2 + cmath.sqrt(delta))**(1/3)

    if abs(u) != 0:
        v = -p / (3 * u)
    else:
        v = (-q)**(1/3)

    w = cmath.exp(2j * cmath.pi / 3)
    
    roots_t = [
        u + v,
        u*w + v*w**2,
        u*w**2 + v*w
    ]

    return [t - b/(3*a) for t in roots_t]

# 驗證
a, b, c, d = 1, -6, 11, -6
roots = root3(a, b, c, d)

print(f"求得根: {roots}")
for r in roots:
    # 檢查 f(r) 是否接近 0
    val = a*r**3 + b*r**2 + c*r + d
    print(f"f({r:.2f}) ≈ 0: {cmath.isclose(val, 0, abs_tol=1e-9)}")
