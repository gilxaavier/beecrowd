#1018
num1 = int(input())
numero=num1
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0
contador7 = 0

while num1 >= 1:
    if num1 >= 100:
        num1 -= 100
        contador1 += 1

    elif num1 >= 50:
        num1 -= 50
        contador2 += 1

    elif num1 >= 20:
        num1 -= 20
        contador3 += 1

    elif num1 >= 10:
        num1 -= 10
        contador4 += 1

    elif num1 >= 5:
        num1 -= 5
        contador5 += 1

    elif num1 >= 2:
        num1 -= 2
        contador6 += 1
        
    elif num1 >= 1:
        num1 -= 1
        contador7 += 1
        
print(numero)
print(contador1, "nota(s) de R$ 100,00")
print(contador2, "nota(s) de R$ 50,00")
print(contador3, "nota(s) de R$ 20,00")
print(contador4, "nota(s) de R$ 10,00")
print(contador5, "nota(s) de R$ 5,00")
print(contador6, "nota(s) de R$ 2,00")
print(contador7, "nota(s) de R$ 1,00")
