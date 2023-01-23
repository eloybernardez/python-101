# tuplas: estructura de dato incorporada en Python. Es un contenedor para el almacenamiento de una colección ordenada de uno o más elementos, accesibles mediante indexación
numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD (diferencia enre tupla y lista => en una tupla no podemos AGREGAR elementos ni eliminarlos => una tupla es INMUTABLE)
#numbers.append(10) error
print(numbers)
#numbers[1] = "change" error

# Métodos
print(strings)
print(strings.index("zule"))
print(strings.count("nico"))

# Transformación de tupla en lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = "juli"
print(my_list)

# Transformación de lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))