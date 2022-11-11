#1044
a, b = input().split()
a = int(a)
b = int(b)
c = 0
if a > b:
    c = a
    a = b
    b = c

if b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")