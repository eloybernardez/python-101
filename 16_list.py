numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ["do the dishes", "play videogames"]
print(tasks)

types = [1, True, "Hola"]
print(types)

print(numbers[0])
print(tasks[0])

text = "Hola"
#text[0] = "W"  # strings no son mutables

tasks[0] = "watch platzi courses"  # las listas si son mutables
print(tasks)

tasks[0] = "do the dishes"
print(tasks)

# se puede hacer slicing
print(numbers[:3])

# se puede usar in
print(True in types)
print("Hola" in types)