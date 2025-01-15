import random

from art import logo_blackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []
player_count = 0
dealer_count = 0
finished = False


def get_card():
    global player_count
    global player
    player.append(random.choice(cards))
    player_count = sum(player)
    if player_count > 21 and (11 in player):
        player[player.index(11)] = 1
        player_count = sum(player)
    print(f"Your cards: {player}, current score: {player_count}")


def give_dealer():
    global dealer_count
    while dealer_count < 22:
        if dealer_count < 17:
            dealer.append(random.choice(cards))
            dealer_count = sum(dealer)
        else:
            break
    print(f"Computer's final hand: {dealer}, final score: {dealer_count}")


def blackjack():
    global player
    global dealer
    print(logo_blackjack)
    player = random.choices(cards, k=2)
    player_count = sum(player)
    dealer = random.choices(cards, k=2)
    dealer_count = sum(dealer)
    print(f"Your cards: {player}, current score: {player_count}")
    print(f"computer's first card: {dealer[0]}")

    while True:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == "y":
            get_card()
            if player_count > 21:
                give_dealer()
                break
        else:
            give_dealer()
            break

    if player_count > 21:
        print("You went over. You Lose!")
    elif dealer_count > 21:
        print("Opponent went over. You Win!")
    elif player_count == dealer_count:
        print("Draw")
    elif player_count < dealer_count:
        print("You Lose!")
    else:
        print("You Win!")

    playing = input("Do you want to play a game of Blackjack? Type 'y' or 'no' ")
    if playing == "y":
        blackjack()


playing = input("Do you want to play a game of Blackjack? Type 'y' or 'no' ")
if playing == "y":
    blackjack()
