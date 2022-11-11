# 1154
age = 0
contador = 0
acumulador = age
while age >= 0:
    age = int(input())
    if age > 0:
        contador += 1
        acumulador += age

print(f"{acumulador / contador:.2f}")
