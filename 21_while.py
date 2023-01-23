'''
while True:
  print("se ejecutó")


counter =0
while counter < 10:
  counter +=1
  print("se ejecuta")

# break: corta el flujo del programa
counter = 0
while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''

# continue: salta a la próxima iteración, saltándose lo que quede dentro de la instrucción restante
counter = 0
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)
