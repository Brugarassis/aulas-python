# List comprehension

# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]
# print(lista)

lista = [numero * 2 for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {
        "nome": "p1",
        "preco": 20,
    },
    {
        "nome": "p2",
        "preco": 10,
    },
    {
        "nome": "p3",
        "preco": 30,
    },
]

novos_produtos = [produto["nome"] for produto in produtos]
# print(novos_produtos)

novos_precos = [{**produto, "preco": produto["preco"] * 1.05} for produto in produtos]
print(novos_precos, sep="\n")
