# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


# Copy
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3],
}

#d2 = d1 # altero o d1
#d2 = d1.copy() # apenas copia os valores imutaveis de d1, sem o altera-lo
               # ja os valores mutaveis, como listas, sao alterados nos dois dicionários (shalow copy)
               # para fazer uma copia total tem q importar metodo - copy.

# d2 = copy.copy(d1) # Shalow copy
d2 = copy.deepcopy(d1) # deep copu - copia total

d2['c1'] = 1000 
d2['l1'][1] = 999

print(d1)
print(d2)
"""
# pop
p1 = {
    'nome': 'Bruno',
    'sobrenome': 'Garcia de Assis',

    }

#nome = p1.pop('nome')
#print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

# update pode ser feito de 3 formas

#p1.update ({
#    'nome': 'Romulo',
#    'idade': 26,
#})
 
#p1.update(nome = 'Walfredo', idade = 59)
lista = [['nome', 'Emely'], ['idade', 25]]
p1.update(lista)
print(p1)