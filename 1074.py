number = int(input())

for i in range(number):
    n = int(input())
    if n <0 and n % 2 == 0:
        print("EVEN NEGATIVE")
    
    elif n <0 and n % 2 == 1:
        print("ODD NEGATIVE")
    
    elif n == 0:
        print("NULL")
    
    if n >0 and n % 2 == 0:
        print("EVEN POSITIVE")
    
    elif n >0 and n % 2 == 1:
        print("ODD POSITIVE")