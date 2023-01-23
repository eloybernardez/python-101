name = "Eloy"
last_name = "Bernardez"
my_age = 29
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Eloy"
print(quote)

quote2 = " She said 'Hello'  "
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1 (concatenación) =>", template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2 (con format) =>", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3 (con f) =>", template)

# reto
template2 = f"Hola, mi nombre es {name} {last_name} y mi edad es {my_age}"
print("reto", template2)
