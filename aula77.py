# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Qual a capital do Brasil?',
        'Opções': ['São Paulo', 'Curitiba', 'Brasília', 'Rio de Janeiro'],
        'Resposta': 'Brasília',
    },
    {
        'Pergunta': 'Em que ano foi abolida a escravidão no Brasil?',
        'Opções': ['1888', '1889', '1600', '1900'],
        'Resposta': '1888',
    },
    {
        'Pergunta': 'Qual é o atual Presidente do Brasil?',
        'Opções': ['Ciro Gomes', 'Bolsonaro', 'Dilma', 'Lula'],
        'Resposta': 'Lula',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    print('Opções:')


    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
         
    print()
    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
             if opcoes[escolha_int] == pergunta['Resposta']:
                 acertou = True

    print()             
    if acertou:
        qtd_acertos += 1
        print('Acertou :)')
    else:
        print('Errou :(')

    print()
print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')



  
