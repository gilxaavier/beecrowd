x, y, z = input().split()
x = int(x)
y = int (y)
z = int (z)

if x < y and x < z:
    if y < z:
        print(x)
        print(y)
        print(z)
    else:
        print(x)
        print(z)
        print(y)
        
if y < x and y < z:
    if x < z:
        print(y)
        print(x)
        print(z)
    else:
        print(y)
        print(z)
        print(x)
        
    
if z < y and z < x:
    if y < x:
        print(z)
        print(y)
        print(x)
    else:
        print(z)
        print(x)
        print(y)
print()
print(x)
print(y)
print(z)