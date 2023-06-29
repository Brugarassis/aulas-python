# while/else
#recuso específico de python - o cara nao gosta muito de usar

nome = 'Bruno Garcia'
i=0
while i < len(nome):
    letra = nome[i]
    

    if letra == 'a':
        break

    print(letra)
    i += 1
else:
    print('Nemhum "a" encontrado')

print('Aqui está o primeiro "a" do seu nome')

# fazer um código para mostrar onde esta o primeiro a da frase.
