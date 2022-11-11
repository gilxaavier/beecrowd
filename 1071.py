# 1071
x = int(input())
y = int(input())

maior = 0
menor = 0

if x > y:
    maior = x
if y > x:
    maior = y
if x < y:
    menor = x
if y < x:
    menor = y

menor += 1
soma = 0

while menor < maior:
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)