# Generator expression - funções que sabem pausar

import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)

lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

# a lista esta toda na memoria
# generator acessa um valor por vez. Por isso nao podemos acessar indices e nem o len
