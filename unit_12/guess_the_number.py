from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Function to check user's guess again actual answer.


def check_answer(guess, answer, turns):
    """checks answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too High !!")
        return turns - 1
    elif guess < answer:
        print("Too Low !!")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}")

        # Choosing a random number between 1 and 100.


def set_difficulty():
    level = input("Choose a fifficulty. Type 'easy or 'hard : ")
    if level == 'easy':
        # global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print("Whlcome to the guessing game!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number. ")
    # Make function to set difficulty.

    # Let the user guess a number.
    guess = 0
    while guess != answer:
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        # Track the number of turns and reduce by 1 if they get it wrong.

        # Repeat the guessing functionality if they get it wrong.


game()
