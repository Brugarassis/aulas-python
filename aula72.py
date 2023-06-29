# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# 1º

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros_ate_10 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
mult_ate_10 = multiplicar(*numeros_ate_10)
print(f'A mutiplicação de {numeros_ate_10} é igual a {mult_ate_10}')
#print(1*2*3*4*5*6*7*8*9*10)

"""
2º - Crie uma função que mostre se um número é par ou impar.
     imprima se é par ou impar
"""


numero = input('Digite um número inteiro: ')


def par_impar(n):
    numero_int = int(n)
    if numero_int % 2 ==0:
        print(f'O número {n} é Par')
    else:
        print(f'O número {n} é impar')

  
par_impar(numero)
   