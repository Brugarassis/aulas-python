"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        #print(f'O total é de {total}.')
    return total
    

soma_10 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma_3 = soma(1, 2, 3)
print(soma_10)
print(soma_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
