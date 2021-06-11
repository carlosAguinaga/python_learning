# Crea un objeto con llaves nombradas del 1 al 100 y con valores de esos mismos numeros elevados al cubo; sin embargo los números solo deben agregarse al diccionario si no son divisibles entre 3.

# Empleamos bucles:
# def run():

    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 == 0:
    #         continue

    #     my_dict[i] = i ** 3

    # return my_dict
    # ------------------------------------------------------------------

# Empleamos Dictionary comprehensions:
def dict_comp():
    my_dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    return my_dict



if __name__ == '__main__':
    # print(run())
    print(dict_comp())
    
