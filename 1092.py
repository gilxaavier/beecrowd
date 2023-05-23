n = int(input())
c,r,s = 0, 0 ,0

for i in range(n):
    qtd,tp= input().split()
    qtd = int(qtd)
    if tp == "C":
        c += qtd
    elif tp == "R":
        r+= qtd
    elif tp == "S":
        s+= qtd
    
total = (c + r + s)

print("Total:" ,total, "cobaias")

print("Total de coelhos:", c)
print("Total de ratos:", r)
print("Total de sapos:", s)
print(f"Percentual de coelhos: {(c / total )* 100:.2f} %") 
print(f"Percentual de ratos: {(r / total )* 100:.2f} %" ) 
print (f"Percentual de sapos: {(s / total )* 100 :.2f} %") 
