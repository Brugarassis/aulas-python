
import random

for _ in range (10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10
    soma_multiplicacao_1 = 0
    for digito in nove_digitos:
        soma_multiplicacao_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    resto_1 = (soma_multiplicacao_1 * 10) % 11
    primeiro_digito = 0 if resto_1 > 9 else resto_1

    dez_digitos = nove_digitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    soma_multiplicacao_2 = 0

    for digito in dez_digitos:
        soma_multiplicacao_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    resto_2 = (soma_multiplicacao_2 * 10) % 11
    segundo_digito = 0 if resto_2 > 9 else resto_2

    cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    print(cpf_gerado)
