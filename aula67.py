# podemos dar valores padrao para parametros.
# caso um valor nao seja enviado como argumento, o padrao sera utilizado.

# refatorar - editar o codigo
# ex -  código pronto, mas quero add um valor a uma função

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=} | x + y =', x+y)

soma(1, 2)
soma(1, 2, 3)
soma(z=4, y=3, x=6)
