#imprecisão de ponto flutuante
# 3 formas de contornar esse erro


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2)) # segundo argumento são as casas depois da vírgula.

#vc tbm pode importar fução decimal - geralmente utilizado para precisão maior 
# (números muito grandes depois da virgula). utiliza com str

import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))