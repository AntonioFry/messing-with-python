print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
  print("You are old enough!")

  wants_to_play = input("Do you want to play? ")
  if wants_to_play == "yes":
    print("Let's play!")

else:
  print("You are not old enough to play.")

