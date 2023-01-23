'''
for element in range(
    1, 21):  # range returns a sequence of integers from i to j-1, one by one
  print(element)

'''

# For y listas
my_list = [23, 45, 67, 89, 43]

for element in my_list:
  print(element)

# For y tuplas
my_tuple = ("nico", "juli", "santi")
for element in my_tuple:
  print(element)

product = {"name": "camisa", "price": 100, "stock": 89}

# For y diccionarios
for key in product:
  print(key, "=>", product[key])

# alternartiva + elegante
for key, value in product.items():
  print(key, "=>", value)

# For y lista de diccionarios
people = [{
  "name": "Nico",
  "age": 34
}, {
  "name": "Eloy",
  "age": 29
}, {
  "name": "Santi",
  "age": 4
}]

for person in people:
  print("name =>", person["name"])
