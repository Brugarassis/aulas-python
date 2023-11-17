contador = 0

while contador < 100:
    contador += 1

    if contador == 10:
        print('Oi')
        continue
    if contador > 10 and contador< 20:
        print('Bruno')
        continue
    print(contador)
    
    if contador == 40:
        break
print('Acabou')
