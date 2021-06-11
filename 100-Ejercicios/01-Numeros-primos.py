# Para un futuro explica porque determinado número no es primo.


# Definir si un número es primo o no:

numero = int(input('Escribe un número: '))

def es_primo(num):

    for divisor in range(2, num - 1):
        if num % divisor == 0:
            print(f'El número {num} no es primo.')
            return False
        else:
            continue
    
    print(f'El número {num} sí es primo.')
    return True    


es_primo(numero)
   




