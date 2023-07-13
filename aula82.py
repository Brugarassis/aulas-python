def execute(funçao, *args):
    return funçao(*args)

def sum(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
print(duplica(3))



'''
print(
    execute(sum, 12, 14),
    execute (lambda x, y: x + y, 2, 4),
    sum(2,3)
)
'''