# Exercício
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'anime'
tentativas_acertadas = ''
numero_tentativas = 0
while True:
    tentativa = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(tentativa) > 1:
        print('Digite apenas uma letra.')
        continue

    if tentativa in palavra_secreta:
        tentativas_acertadas += tentativa

    palavra_formada = ''
    for acertos in palavra_secreta:
        if acertos in tentativas_acertadas:
            palavra_formada += acertos
        else:
            palavra_formada += '*'

    print(f'Palavra secreta: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns, você ganhou.')
        print(f'O numero de tentativas foi de: {numero_tentativas}')
        tentativas_acertadas = ''
        numero_tentativas = 0





        
    

