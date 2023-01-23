import random  # para que se devuelva un nro aleatorio

options = ("piedra", "papel", "tijera")

rounds = 0
user_wins = 0
computer_wins = 0
while abs(user_wins - computer_wins) < 2:

  print("*" * 10)
  print("ROUND", rounds + 1)
  print("*" * 10)
  print("user wins =>", user_wins)
  print("computer wins =>", computer_wins)

  user_option = input("piedra, papel o tijera => ").lower()
  if (not user_option in options):
    print("Esa opción no es válida")
    continue

  rounds += 1
  computer_option = random.choice(options)
  '''
  random.choice(seq)
  Return a random element from the non-empty sequence seq
  '''

  print("Su elección =>", user_option)
  print("CPU ha elegido =>", computer_option)

  if (user_option == computer_option):
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("Ud. ha ganado!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("Ud. ha perdido!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("tijera gana a papel")
      print("Ud. ha perdido!")
      computer_wins += 1
    else:
      print("papel gana a piedra")
      print("Ud. ha ganado!")
      user_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("Ud. ha ganado!")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("Ud. ha perdido")
      computer_wins += 1
if user_wins > computer_wins:
  print("El ganador definitivo es Ud. :D")
else:
  print("El ganador definitivo fue CPU u.u")
