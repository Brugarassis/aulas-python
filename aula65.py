# Funções são trechos de código usados para replicar determinada ação ao longo do código.
# podemos dar valores (argumesntos) a elas
# por padrão retornam none(nada)

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}. Tudo bem?')

saudacao('Bruno')
saudacao('Rômulo')
saudacao('Walfredo')

