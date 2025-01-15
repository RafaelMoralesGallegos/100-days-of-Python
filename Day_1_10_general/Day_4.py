import random

import modpi as mmod

random_interger = random.randint(0, 4)
random_float = random.random()
random_number = random_interger + random_float
print(random_number)
random_number_2 = random_float * 5
print(random_number_2)

# Perzonalized Module created by new python3 and downloading as .py file and deleting other.
print(mmod.pi)

# Part 3
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

game_icons = [rock, paper, scissors]
game_name = ["Rock", "Paper", "Scissors"]

player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
print(f"You chose {game_name[player]}\n{game_icons[player]}")

computer = random.randint(0, 2)
print(f"The computer chose {game_name[computer]}\n{game_icons[computer]}")

if player >= 3 or player < 0:
    print("You broke the rules, You lose.")
elif player == computer:
    print("You Draw.")
elif player == 2 and computer == 0:
    print("You Lose :(")
elif player == 0 and computer == 2:
    print("You Win :)")
elif player < computer:
    print("You Lose :(")
elif player > computer:
    print("You Win :)")

for icon in game_name:
    print(icon)
    print(icon + " pie")
