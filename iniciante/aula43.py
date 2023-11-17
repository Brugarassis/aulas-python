# for
# while é utilizado para codigos q nao sabemos quantas repetições vão acontecer - exemplo usuário add senha.
# for é utilizado quando sabemos quantas repetiçoes vão acontecer.

texto = 'Bruno Garcia de Assis'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')

