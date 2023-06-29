# exercício
'''
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo.')
elif primeiro_valor == segundo_valor:
    print('Os dois valores são iguais')
else:
    print('O segundo valor é maior que o primeiro.')

'''

# aparecendo as variáveis
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=} ')
else:
    print(f'{primeiro_valor=} é menor que {segundo_valor=}')

