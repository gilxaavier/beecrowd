# 1037
number1 = float(input())

if number1 >= 25.01 and number1 <= 50.00:
    print("Intervalo (25,50]")
elif number1 >= 0.00 and number1 <= 25.00:
    print("Intervalo [0,25]")
elif number1 >= 75.00 and number1 <= 100.00:
    print("Intervalo (75,100]")
elif number1 < 0 or number1 > 100:
    print("Fora de intervalo")
