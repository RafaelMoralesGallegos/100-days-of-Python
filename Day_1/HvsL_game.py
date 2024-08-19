import random as random
from os import system

from art import logo, vs
from game_data import data  # There are 50 data points in file

score = 0
data_list = random.sample(range(0, len(data)), 2)
A_data = data[data_list[0]]
B_data = data[data_list[1]]
game_over = False


def game():
    """Starts the game of Higher and Lower"""
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(
        f"Compare A: {A_data['name']}, a {A_data['description']},"
        f" from {A_data['country']}, {A_data['follower_count']}"
    )
    print(vs)
    print(
        f"Againts B: {B_data['name']}, a {B_data['description']},"
        f" from {B_data['country']}, {B_data['follower_count']}"
    )
    followers = input("Who has more followers? Type 'A' or 'B': ").upper()
    if followers == "A":
        return A_data["follower_count"], B_data["follower_count"]
    elif followers == "B":
        return B_data["follower_count"], A_data["follower_count"]
    else:
        return 0, 1


def new_data():
    """Generates New Data for Game"""
    B_actual = data_list[1]
    B_new = random.randint(0, 49)
    while B_actual == B_new:
        B_new = random.randint(0, 49)
    return B_actual, B_new


while not game_over:
    stats = game()  # Begin Game
    if stats[0] > stats[1]:
        score += 1
        data_list = new_data()
        A_data = data[data_list[0]]
        B_data = data[data_list[1]]
        system("clear")
    else:
        system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
