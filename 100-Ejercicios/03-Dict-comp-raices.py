# Crear, con un dictionary comprehension, un diccionario cuyas llaves sean los 1000 primeros números naturales con sus raíces cuadradas como valores.

# [salida ciclo condición]

# list_one = []

# for num in range(1, 101):
#     if num % 3 != 0:
#         list_one.append(num)

# print(list_one)


print([num for num in range(1, 101) if num % 5 != 0 ])


