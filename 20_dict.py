person = {
  "name": "Eloy",
  "last_name": "Bernardez",
  "languages": ["Python", "JavaScript"],
  "age": 29
}

print(person)

person["name"] = "Santiago"
person["age"] -= 20
person["languages"].append("Rust")
print(person)

# Delete key/value
del person["last_name"]
person.pop("age")
print(person)

# get items / keys / values
print("-------items---------"
      )  # -> retorna tuplas con los key / values en ellas
print(person.items())
print("-------keys---------")  # -> retorna tuplas con las keys
print(person.keys())
print("-------values---------")  # -> retorna tuplas con los values
print(person.values())