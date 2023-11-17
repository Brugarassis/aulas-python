# enumerate - numera iteraveis - indices

lista = ['Bruno', 'Rômulo', 'Rhaíssa', 'Gabi']
lista.append('Emely')

"""
lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)
"""
for indice, nome in enumerate(lista):
    print(indice, nome)
    