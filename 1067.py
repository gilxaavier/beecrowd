# 1067
number1 = int(input())
contador = 1
if number1 % 2 == 0:
    while contador < number1:
        print(contador)
        contador += 2

if number1 % 2 != 0:
    while contador <= number1:
        print(contador)
        contador += 2
