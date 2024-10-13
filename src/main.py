import random

while True:
  play = input("Roll the dice? (y,n) : ")
  if play.lower() == 'y':
    num_1 = random.randint(1,6)
    num_2 = random.randint(1,6)
    Outcome = (num_1, num_2)
    print(Outcome)
  elif play.lower() == 'n':
    print("Thanks for playing")
    break
  else:
    print('Unknown Command')
      