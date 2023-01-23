name = "Eloy"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Eloy" + " Bernardez")
print(10 + 20)
#print("Eloy" + 12)  #error
print("Eloy " + "29")  # funciona

age = 29
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

# Calcula tu edad en 10 años
age = input("Escribe tu edad => ")  # age es string
print(type(age))
age = int(age)  # transformar a int
print(f"Tu edad en 10 años será { age+ 10}")
