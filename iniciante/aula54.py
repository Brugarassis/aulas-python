#Exercicio criar uma lista interativa

import os

lista = []

while True:
    print('Selecione uma opção')
    opçao = input('[i]nserir, [a]pagar, [l]istar: ')
  

    if opçao == 'i':
        os.system('cls')
        valor = input('insira um item a lista: ')
        lista.append(valor)

    elif opçao == 'a':
        os.system('cls')
        item_str = input('Qual item você deseja apagar? ')
                 
        try:
            item = int(item_str) 
            del lista[item]
        except ValueError:
                print('Erro - por favor digite o número do item na lista')
        except IndexError:
                print('Erro - Esse item não existe na lista')
        except Exception:
                print('Erro não identificado')        


    elif opçao == 'l':
        os.system('cls')
                
        if len(lista) == 0:
            print('Nada a listar')

        for i, valor in enumerate(lista): 
            print(i, valor)

    else:
        print('Selecione apenas i, a ou l')

