alcool = 0
diesel = 0
gasolina = 0
while True:
    num = int(input())
    if num == 1:
        alcool +=1
    elif num ==2 :
        gasolina += 1
    elif num == 3:
        diesel += 1
    elif num == 4:
        break
    else:
       continue


print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', diesel)
