# 1012
valor = input().split()
a, b, c = valor
a = float(a)
b = float(b)
c = float(c)
print(f"TRIANGULO: {(a*c) / 2:.3f}")
print(f"CIRCULO: {3.14159 * (c ** 2):.3f}")
print(f"TRAPEZIO: {(a + b) * c/2:.3f}")
print(f"QUADRADO: {b**2:.3f}")
print(f"RETANGULO: {a*b:.3f}")
