x = int(input())
y = int(input())

# Garantir que x seja menor que y
if x > y:
    x, y = y, x

for num in range(x+1, y):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
