# Crear, con list comprehension, una lista de todos los múltiplos de 4 que a la vez también son
# múltiplos de 6 y de 9, hasta 5 dígitos.

def run():
    multiples = [multiple for multiple in range(1, 100_000) if multiple % 36 == 0]
    print(multiples)


if __name__ == '__main__':
    run()