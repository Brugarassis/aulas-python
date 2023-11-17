"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
""" 
# primeiro digito

cpf_enviado = '74682489070'
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

print(f'O primeiro digito do seu cpf é: {primeiro_digito}')
print(f'O segundo digito do seu cpf é:{segundo_digito}')

cpf_gerado = f'{nove_diigitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado == cpf_gerado:
    print('Cpf válido')
else:
    print('Cpf inválido, digite novamente')
    