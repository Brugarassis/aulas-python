"""
Split and join  
split - divide uma str
join - une uma str
"""
# strip - retira espaços dos dois lados
# lstrip - retira espeços da esquerda
# r strip - retira espaços da direita

frase = '    Olha só   , que coisa interessante      '
lista_frase_crua = frase.split(',') # argumento - separar para separar a str.

lista_frase = []

for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

print(lista_frase_crua) # sem formatação
print(lista_frase)      # com formatação

# eu faço a primeira lista sem formatar para que consiga altera-la.
# assim fica a formatação automatica na segunda lista.

frases_unidas = ' * '.join(lista_frase) # argumento antes do join fica entre todos os índices da lista ou str.
print(frases_unidas)
