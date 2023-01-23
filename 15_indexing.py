text = "Ella sabe Python"
print(text[0])
print(text[1])
#print(text[999])

# último caracter
print(text[-1])

# otra forma de obtener el último caracter
size = len(text)
print("size => ", size)
print(text[size - 1])

# slicing
print(text[0:5])
print(text[10:16])
print(text[:10])  # es igual a print(text[0:10])
print(text[3:])  # es igual a print(text[3:size-1])
print(text[:])  # devuelve el mismo string
print(text[10:16:1])  # el último dato me indica el nro de saltos
print(text[10:16:2])  # de a 2 saltos
print(text[::2])