#1013
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maior = int(a + b + (a-b))//2

if maior < b and c < b:
    print(b, "eh o maior")
elif maior > c:
    print(maior, "eh o maior")

elif maior < c:
    maior = int(maior)
    print(c, "eh o maior")
