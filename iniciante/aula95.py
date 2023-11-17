# Raise - lançando exceções


def divide(n, d):
    if d == 0:
        raise ZeroDivisionError("Divisão por zero nao pode")
