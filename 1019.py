#1019
valor = int(input())
contador_hora = 0
contador_min = 0
contador_seg = 0

while valor > 0:
    if valor >= 3600:
        contador_hora += 1
        valor -= 3600
    elif valor < 3600 and valor >= 60:
        contador_min += 1
        valor -= 60
    elif valor < 60:
        contador_seg += 1
        valor -= 1

print(f"{contador_hora}:{contador_min}:{contador_seg}")

