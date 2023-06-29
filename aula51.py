# Estrutura de desempacotamento 

nomes = ['Bruno', 'Rômulo', 'Rhaíssa', 'Gabi']

nome1, nome2, nome3, nome4 = nomes
print(nome2)

nome1, nome2, nome3, nome4 = ['Bruno', 'Rômulo', 'Rhaíssa', 'Gabi']
print(nome4)

nome1, nome2, *_ = nomes
print(nome1, nome2)
print(_)