'''
Introdução ao try/except
try -> tenta executar o código
except -> é executado caso haja um erro no try
'''
numero_str = input('Digite o número que você deseja dobrar: ')
try:
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
    