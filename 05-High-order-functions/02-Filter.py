# Obtener en otra lista unicamente números impares:

my_list = [1, 4, 5, 6, 9, 13, 19, 21]

# Vamos a hacer una list comprehension:
lista_impares = [num for num in my_list if num % 2 != 0]
print(my_list)
print(lista_impares)
print('')


# Vamos a usar filter:
lista_pares = list(filter(lambda x: x % 2 == 0 , my_list))
print(my_list)
print(lista_pares)
