
from art import logo, Vursus
from game_data import data
import random

import os
clear = lambda: os.system('cls')  


def format_data(account):
    """Take the account data and return the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, {account_description}, {account_country}"

#score keeping.
def check_answer(guess, A_follower_count, B_follower_count):
    """Take the user guess and follower counts andreturn if they got it right"""
    if A_follower_count > B_follower_count:
        return guess == "A"
    else:
        return guess == "B"


SCORE = 0
print(logo)
account_B = random.choice(data)

is_game_over = False
while not is_game_over:
#Generate a random from the game data
    account_A = account_B
    account_B = random.choice(data)
    while account_B == account_A:
        account_B = random.choice(data)
        
        
    A_follower_count = account_A['follower_count']
    B_follower_count = account_B['follower_count']

### check  
# print(logo)
# print(f"Compare A: {format_data(account_A)}.\n", "\n")
# print(Vursus)
# print(f"Against B: {format_data(account_B)}.")
# guess = input("Who has more follower? Type 'A' or 'B': ").upper()


#display logo and art
    print(f"Compare A: {format_data(account_A)}.\n", "\n")
    print(Vursus)
    print(f"Against B: {format_data(account_B)}.")
#Ask user for a guess 
    
    guess = input("Who has more follower? Type 'A' or 'B': ").upper()
    is_correct = check_answer(guess, A_follower_count, B_follower_count)
    if is_correct:
        SCORE += 1
        clear()
        print(logo)
        print(f"You're right!. Current score: {SCORE}")
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        is_game_over = True