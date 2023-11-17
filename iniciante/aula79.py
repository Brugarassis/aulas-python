# exemplos de uso de sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('show')
        break

    print(letras)
