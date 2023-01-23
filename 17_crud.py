# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]

# Read
print(numbers[1])

# Update
numbers[-1] = 10
print(numbers)

# Create (metodo append para agregar al final de la lista (como push en JS))
numbers.append(700)
print(numbers)
# método insert para agregar en una posición específica
numbers.insert(0, "hola")
print(numbers)

numbers.insert(
  3, "change"
)  # no borrará al elemento en el index 3, simplemente lo mueve al siguiente

print(numbers)

# unir listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

# find index
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

# Delete
new_list.remove("todo 1")
print(new_list)

# elimina el último elemento
new_list.pop()
print(new_list)

# elimina también si indicamos el índice
new_list.pop(2)
print(new_list)

# invertir array
new_list.reverse()
print(new_list)

# ordenar de menor a mayor
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

# para strings (alfabéticamente)
strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

# no se puede ordenar listas con tipos mezclados