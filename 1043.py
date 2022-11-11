a, b, c = input().split()
a = float (a)
b = float (b)
c = float (c)

if b - c  < a < b + c:
    print(f"Perimetro = {a + b + c}")

else:
    print(f"Area = {((a + b)/ 2) * c}")
    