# formatação de string
# s - string
# d - int
# f - float
# .<numero de digitos>f
# x ou X - hexadecimal
# (caractere) (><^) (Quantidade)
# > esquerda
# < direita
# ^ centro
# = força o sinal a aparecer antes dos zeros
# conversion flags !r !s !a
variavel = 'AB'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.045768098:>15.2f}')