import numpy as np

# 假設多項式為 x^5 - 10x^4 + 35x^3 - 50x^2 + 24x (根為 0, 1, 2, 3, 4)
# 係數由高次到低次排列
c = [1, -10, 35, -50, 24, 0]

roots = np.roots(c)
print(f"多項式的根為：\n{roots}")
