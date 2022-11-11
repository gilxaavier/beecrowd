#1073
number1 = int(input())
contador = 1
while contador <= number1:
    if contador % 2 ==0:
        print(f"{contador}^2 = {contador**2}")
    contador += 1
