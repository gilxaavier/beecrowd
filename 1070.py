#1070
num1 = int(input())
contador = 1
i = 0
if num1 % 2 == 0:
    num1 += 1

    while contador <= 6:
        print(num1)
        num1 += 2
        contador += 1
elif num1 % 2 == 1:

    while contador <= 6:
        print(num1)
        num1 += 2
        contador += 1
