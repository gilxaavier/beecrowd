n = int(input())

for _ in range(n):
    x, y = map(int, input().split())  

    menor = min(x, y)
    maior = max(x, y)


    soma = 0

    for num in range(menor, maior + 1):
      
        if num % 2 != 0:
            soma += num 

    print(soma) 
