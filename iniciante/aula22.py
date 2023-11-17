# operador or
# Qaulquer operação verdadeira, valida todas.
# diferente do and q qualquer falsa, desvalida.
entrar = input('[E]ntrar ou [S]air: ')
senha_entrada = '123456'
senha_digitada = input('Digite sua senha: ')
if (entrar == 'E' or entrar == 'e') and senha_digitada == senha_entrada:
    print('Entar')
else:
    print('Sair')
