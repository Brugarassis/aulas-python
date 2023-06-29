# Operações condicionais.
# if(se)/ elif(se não se)/ else(se não)
entrada = input('Você quer entrar ou sair? ')
if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar nem sair')

# if pode vir sozinho
# elif e else só sao empregados depois do if
# posso utilizar apenas o if e o else
# o elif pode se repetir várias vezes, mas sempre depois dele vem o else
