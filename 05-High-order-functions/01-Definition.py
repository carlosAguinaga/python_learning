# Función de orden superior: es una función que recibe como parámetro a otra función.

# Saludo es una función de orden superior.
def saludo(fun):
    fun()

def hola():
    nombre = input('Escribe tu nombre: ')
    print(f'Hola, {nombre}')


def adios():
    nombre = input('Escribe tu nombre: ')
    print(f'Adios, {nombre}')

saludo(hola)
saludo(adios)