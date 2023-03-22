# Leitura dos valores de entrada
hi, mi, hf, mf = map(int, input().split())

# Cálculo da duração do jogo
hora = minuto = 0

if hi == hf and mi == mf:  # Jogo com duração mínima
    hora = 24
elif hi == hf and mi < mf:
    hora = 0
    minuto = mf - mi
elif hi == hf and mi > mf:
    hora = 23
    minuto = 60 - (mi - mf)
elif hi < hf:
    hora = hf - hi
    if mi <= mf:
        minuto = mf - mi
    else:
        hora -= 1
        minuto = 60 - (mi - mf)
else:
    hora = 24 - (hi - hf)
    if mi <= mf:
        minuto = mf - mi
    else:
        hora -= 1
        minuto = 60 - (mi - mf)

# Saída do resultado
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
