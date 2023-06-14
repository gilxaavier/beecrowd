notas = []
cont = 0

while cont <2:
    nota = float(input())
    if nota <0 or nota > 10:
        print('nota invalida')
    else:
        notas.append(nota)
        cont+=1

print(f'media = {sum(notas) / len(notas)}')