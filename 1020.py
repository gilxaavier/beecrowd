#1020
dias = int(input())
contador_ano = 0
contador_mes = 0
contador_dia = 0

while dias > 0:
    if dias >= 365:
        contador_ano += 1
        dias -= 365
    elif dias < 365 and dias >= 30:
        contador_mes += 1
        dias -= 30
    elif dias < 30:
        contador_dia += 1
        dias -= 1
print(f"{contador_ano} ano(s)")
print(f"{contador_mes} mes(es)")
print(f"{contador_dia} dia(s)")
