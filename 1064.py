positivos = 0
media = []
for num in range(6):
    num = float(input(""))
    if num > 0:
        positivos +=1
        media.append(num)
        
print(f"{positivos} valores positivos")
print(f"{sum(media) / len(media):.1f}") 