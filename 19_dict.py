# diccionario: como un objecto en JS
my_dict = {}
print(type(my_dict))

my_dict = {
  "avión": "bla bla bla",
  "name": "Eloy",
  "last_name": "Bernardez",
  "age": 29
}
print(my_dict)

# cantidad de key/value
print(len(my_dict))

# indexing
print(my_dict["age"])
print(my_dict["last_name"])
# print(my_dict["unvalor"]) error

# alternativa: usar el método get(key) (si no existe el value, retorna None)
print(my_dict.get("age"))
print(
  my_dict.get("unvalor"))  # None. El hecho de no crashear, lo hace más útil

print("name" in my_dict)
print("otroqueno" in my_dict)