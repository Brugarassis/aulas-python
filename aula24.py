 # operadorea in e not in
# entre coisas e nao esta entre.
# strings no python são interáveis.
# 0 1 2 3 4 
# B r u n o
#-5-4-3-2-1
'''
nome = 'Bruno'
print(nome [1])
print(nome [-4])
print('B' in nome)
print('run' in nome)
print('z' in nome)
print('zero' in nome)
'''
nome2 = input('Digite seu nome: ')
encontrar = input('O que você quer encontrar? ')
if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')
