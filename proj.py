import random
player_guess = input("Guess the temprature: ")
real_temprature = random.choice(["Cold", "Warm", "Hot"])
tries = 0
if player_guess == real_temprature:
  print("You Won!")
  quit()
else:
    print("You Lost!")
    tries += 1
    while tries < 5:
      player_guess = input("Guess the temprature: ")
      real_temprature = random.choice(["Cold", "Warm", "Hot"])
      tries = 0
      if player_guess == real_temprature:
        print("You Won!")
        quit()
      else:
        print("You Lost!")
        tries += 1
