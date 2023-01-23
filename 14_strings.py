text = "Ella sabe programar en Python"

# metodo de Strings así como string.includes() en JS
'''
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
  print("Elegiste bien!!")
else:
  print("También elegiste bien :)")
'''

# como string.length
size = len(text)
print(size)

print(text)
# string.toUpperCase()
print(text.upper())

# string.toLowerCase()
print(text.lower())

# Cuenta las veces que aparece el string que introducimos
print(text.count("a"))

# pasa minúsculas a mayúsculas y viceversa
print(text.swapcase())

# retorna booleano si el string empieza con el texto ingresado
print(text.startswith("Ella"))
print(text.endswith("Rust"))

# string.replace()
print(text.replace("Python", "Go"))

text_2 = "este es un título"
print(text_2)

# primer caracter se pasa a mayúscula
print(text_2.capitalize())

# convierte cada letra de cada palabra en mayúscula
print(text_2.title())

# vemos si el string podría ser un int
print(text_2.isdigit())
print("398".isdigit())