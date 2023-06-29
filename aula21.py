# operador and
# adiciona mais uma condição para o if.

entrar = input('[E]ntrar ou [S]air: ')
senha_entrada = '123456'
senha_digitada = input('Digite sua senha: ')
if entrar == 'E' and senha_digitada == senha_entrada:
    print('Entar')
elif entrar == 'S':
    print('Sair')
else:
    print('Usuário ou senha incorretos')