"""
      Argumentos
Argumento nomeado - Tem um nome - depois um sinal de igual.
Argumento não nomeado - Chamado de posicional - recebe apenas o valor.
n nomeado precisa ser passado na ordem em que os parametros
"""

def soma(x, y, z):
    print(f'{x=} {y=} {z=} | x + y + z = ', x + y + z)

soma(1,2,3) # nao nomeada - preciso por em ordem
soma(y=5, x=4, z=1) #nomeada - possp colocar em qualquer ordem

# se eu nomear um argumento, todos os outros que vierem depois devem ser nomeados.


 