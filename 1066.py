positivo = 0
negativo = 0
par = 0 
impar = 0
for i in range(5):
    num = float(input(""))
    if num > 0:
        positivo +=1
    elif num < 0:
        negativo +=1
    elif num % 2 ==0:
        par +=1
    elif num % 2 == 1:
        impar +=1

print(par, "valor(es) par(es)") 
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
