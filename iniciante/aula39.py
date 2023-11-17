# exercício
nome = 'Bruno Garcia de Assis'

indice = 0
novo_nome =''

while indice <len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
#add o ultimo asterisco fora do while
novo_nome += '*'
print(novo_nome)
print(len(nome))