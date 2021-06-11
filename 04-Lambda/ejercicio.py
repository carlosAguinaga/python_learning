# Vamos a hacer un jerecicio para saber si una palabra es palíndromo o no

# Empleamos lambda:
variable_contenedora = lambda argumento: argumento == argumento[::-1]
print(variable_contenedora('ana'))

# Empleamos una función normal:
def fun(arg):
    return arg == arg[::-1]

print(fun('ana'))

