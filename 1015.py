# 1015
import math
num1 = input().split()
num2 = input().split()
x1, y1 = num1
x2, y2 = num2
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt((((x2 - x1)*(x2 - x1)) + ((y2 - y1))*(y2 - y1)))
print(f"{distancia:.4f}")
