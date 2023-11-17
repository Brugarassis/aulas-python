# cuidados com dados mutáveis.
# dados imutáveis - se vc usa o = vc apenas copia o valor
# dados mutáveis - aponta para o mesmo valor na memória

lista_a =['Bruno', 'Rômulo']
lista_b = lista_a
lista_c = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_c)
print(lista_a)

lista = ['Bruno', 'Rômulo', 'Rhaíssa', 'Gabi']
 
for nome in lista:
    print(nome, type(nome))