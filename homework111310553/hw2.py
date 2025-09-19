import cmath

def root2(a, b, c):
    D = cmath.sqrt(b**2 - 4*a*c) 
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    return x1, x2

a, b, c = 1, -3, 2 
r1, r2 = root2(a, b, c)
print("Roots:", r1, r2)
print("f(r1) =", a*r1**2 + b*r1 + c)
print("f(r2) =", a*r2**2 + b*r2 + c)

a, b, c = 1, 2, 5   
r1, r2 = root2(a, b, c)
print("\nRoots:", r1, r2)
print("f(r1) =", a*r1**2 + b*r1 + c)
print("f(r2) =", a*r2**2 + b*r2 + c)
