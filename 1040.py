#1040
notas = input().split()
n1, n2, n3, n4 = notas
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n1 *= 2
n2 *= 3
n3 *= 4
n4 *= 1
media = (n1 + n2 + n3 + n4) / 10

print(f"Media: {media:.1f}")
if 5.00 > media:
    print("Aluno reprovado.")


elif media >= 5.00 and media <= 6.9:
    exame = float(input())
    media_final = (media + exame) / 2
    print("Aluno em exame.")
    print(f"Nota do exame: {exame:.1f}")
    print("Aluno aprovado.")
    print(f"Media final: {media_final:.1f}")


elif media >= 7.00:
    print("Aluno aprovado.")

