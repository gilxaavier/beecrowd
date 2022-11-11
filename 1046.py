inicio, fim = input().split()
inicio = int(inicio)
fim = int (fim)

if inicio > fim:
    print(f"O JOGO DUROU {24 - (inicio - fim)} HORA(S)")

elif inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
    
elif inicio < fim:
    print(f"O JOGO DUROU {fim - inicio} HORA(S)")