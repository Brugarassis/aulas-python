frase = 'Bruno tem 26 anos e está iniciando seus estudos em programação.' \
    'Ele é um cara inteligente e bonito.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue


    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print(f'A letra que apareceu mais foi a "{letra_apareceu_mais_vezes}", com um total de {qtd_apareceu_mais_vezes}x.')