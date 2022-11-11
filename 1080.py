#1080
numero = int(input())
maior = 0
contador = 1
while contador < 100:
    numero = int(input())
    contador += 1
    if numero > maior:
        maior = numero
        posicao = contador
print(maior)
print(posicao)
