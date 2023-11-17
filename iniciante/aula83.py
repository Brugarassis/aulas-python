# kwargs - desempacotando dicionários


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


pessoa = {"nome": "Bruno", "idade": 27, "peso": 72, "altura": 1.75}


mostro_argumentos_nomeados(nome="Bruno", idade=27)
mostro_argumentos_nomeados(**pessoa)
