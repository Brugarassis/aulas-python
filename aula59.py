# Desempacotamento nas chamadas
# de métodos e funções

string = 'ABC'
lista = ['Bruno', 'Rômulo', 'Walfredo', 'Rosane','Rhaissa', 'Gabi', 'Emely']
tupla = 'Python', 'é', 'legal'
quartos = [

    ['Pai', 'Mãe'],
    ['Bruno', 'Rômulo'],
    ['Rhaíssa', 'Gabi'],
    ]

#p, b, *_, u = lista
#print(p,u)

print(*string)
print(*lista)
print(*tupla)
print(*quartos, sep='\n')
