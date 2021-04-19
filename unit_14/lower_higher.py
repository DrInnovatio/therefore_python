from art import logo, vs
from game_data import data
from replit import clear
import random
# Display the art


def format_data(account):
    # Format the account data into printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data.
while game_should_continue:

    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")
    # Ask user for a guess.
    guess = input("Who has more followers ? Type 'A' or 'B' : ").lower()

    # Check if user is correct.
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Use if statement to check if user is correct.
    clear()

    if is_correct:
        score += 1
        print(f"YOU ARE RIGHT! The current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. The final score : {score}.")

    # Give user feedback on their guess.

    # score keeping.

    # Make the game repeatable.

    # Clear the screen between rounds.


# git test in PyCharm
# git test in PyCharm

