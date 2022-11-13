par = 0
impar = 0
positivo = 0
negativo = 0
numeros = []

for i in range(5):
    num = int(input())
    numeros.append(num)
print(numeros)

for i in numeros:
    if i % 2 == 0 :
        par += 1
        
    if i % 2 == 1:
        impar += 1
        
    if i >  0:
        positivo += 1
    if i <0:
        negativo+=1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")