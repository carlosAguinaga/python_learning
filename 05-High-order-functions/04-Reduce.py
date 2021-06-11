from functools import reduce
# Multiplica cada uno de los elementos de la siguiente lista:

my_list = [2, 2, 2, 2, 2]

# Empleamos For:
acu = 1

for num in my_list:
    acu *= num

print(f'Producto de un For obtenemos: {acu}')


# Empleamos Reduce:
todo_multiplicado = reduce(lambda a, b: a * b, my_list)
print(f'Producto de Reduce obtenemos: {todo_multiplicado}')
