import random

random_integer = random.randint(1, 3)

usr_input = int(input ("Choose 1 to rock, 2 for paper, 3 for scissors: "))

words = ["rock", "paper", "scissors"]

if (usr_input == random_integer ):
    print(f"Tie, both choosed {words[random_integer]}")
else:
    if (usr_input == 2 & random_integer == 3):
        print(f"Your rival won, he choosed scissors, number:{random_integer}")
    else:
        if(usr_input == 3 & random_integer == 1):
            print(f"Your rival won, he choosed rock, number:{random_integer}")
        else:
            if (usr_input == 1 & random_integer == 2):
                print(f"Your rival won, he choosed paper, number:{random_integer}")
            else:   
                print(f"You won, congrats, because your oponent choosed {words[random_integer]}, number:{random_integer}")