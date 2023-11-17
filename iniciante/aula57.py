# listas dentro de listas

quartos = [

    ['Pai', 'Mãe'],
    ['Bruno', 'Rômulo'],
    ['Rhaíssa', 'Gabi'],
    ]

#print(quartos[0])
#print(quartos[1][1])
#print(quartos[0][1])

for quarto in quartos:
    for pessoas in quarto:
        print(pessoas)
        
