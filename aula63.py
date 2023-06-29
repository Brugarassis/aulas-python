# Procurando problemas e refinando o código

import re
import sys

while True:
    entrada = input('Digite seu CPF: ')

    cpf_enviado = re.sub(
        r'[^0-9]',
        '',
        entrada
    )
    numeros_repitidos = entrada == entrada[0] * len(entrada)

    if numeros_repitidos:
        print('Esse cpf é inválido')
        sys.exit()


    nove_diigitos = cpf_enviado[:9]
    contador_regressivo_2 = 10
    soma_multiplicacao_2 = 0

    for digito in nove_diigitos:
        soma_multiplicacao_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1


    resto = (soma_multiplicacao_2 * 10) % 11
    primeiro_digito = 0 if resto > 9 else resto

    dez_diigitos = nove_diigitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    soma_multiplicacao_2 = 0

    for digito in dez_diigitos:
        soma_multiplicacao_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1


    resto_2 = (soma_multiplicacao_2 * 10) % 11
    segundo_digito = 0 if resto_2 > 9 else resto_2

    #print(f'O primeiro digito do seu cpf é: {primeiro_digito}')
    #print(f'O segundo digito do seu cpf é:{segundo_digito}')

    cpf_gerado = f'{nove_diigitos}{primeiro_digito}{segundo_digito}'

    if cpf_enviado == cpf_gerado:
        print('Cpf válido')
        break
    
    else:
        print('Cpf inválido, digite novamente')
        continue
        
