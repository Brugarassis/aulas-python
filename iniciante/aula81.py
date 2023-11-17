# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.
'''
lista_numeros = [1, 22, 4, 56, 39, 27, 27, 27]
lista_numeros.sort() # organiza os elementos da lista, caso o python saiba como.
x = sorted(lista_numeros) # cria uma lista nova (rasa) organizada.
print(lista_numeros) 
print(x)
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]

# ordenar por função:
# define uma função que ira organizar a lista 
# a ordenação é feita pela tabela unicode (ja definida) - ver na net.
'''
def order(item):
    return item['nome']

lista.sort(key=order)

for item in lista:
    print(item)
'''

# ordenar usando a função lambda:

#lista.sort(key=lambda item: item['nome']) 

def show(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

show(l1)
show(l2)
