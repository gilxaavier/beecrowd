values = int(input(""))
outside = 0
inside = 0
for i in range(values):
    number = int(input())
    if number > 9 and number<= 20:
        inside +=1
    else:
        outside +=1
        
print(inside, "in")
print(outside, "out")