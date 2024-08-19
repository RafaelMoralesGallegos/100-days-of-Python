import random as random
from art import logo
print(logo)

HARD_GUESS = 5
EASY_GUESS = 10
NUMBER = random.randrange(0, 101)
game_over = False

def compare_guess(guess):
  if guess < NUMBER:
    print("Too low.")
    return False
  elif guess > NUMBER:
    print("Too high.")
    return False
  else:
    return True

print("Welcome to the Number Guessing Game!")
print("I'm thining of a number between 1 and 100")
# print(f"The number is {NUMBER}")
dif = input("Choose difficulty. Type 'easy' or 'hard': ")

if dif == "easy":
  guesses = EASY_GUESS
elif dif == "hard":
  guesses = HARD_GUESS

while not game_over:
  if guesses != 0:
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    game_over = compare_guess(guess)
    guesses -= 1
    if not game_over and guesses != 0:
      print("Guess again.")
  else:
    game_over = True

if guess == NUMBER:
  print(f"You got it! The answer was {NUMBER}")
else:
  print(f"You ran out of guesses, you lose. The answer was {NUMBER}")
