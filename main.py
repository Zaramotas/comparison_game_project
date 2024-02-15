from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guesss, follower_1, follower_2):
    """Use if statement to check if user is correct."""
    if follower_1 > follower_2:
        return guesss == 'a'
    else:
        return guesss == 'b'



def game():
    print(logo)
    account_b = random.choice(data)
    points = 0
    while True:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            points += 1
            print(f"You're right! Current score: {points}")
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            break

game()
while True:
    play_again = input("Play Again? Type 'Y' or 'N': ").lower()
    if play_again == 'y':
        game()
    elif play_again == 'n':
        print("Game over")
        break
    else:
        print("Wrong input")
