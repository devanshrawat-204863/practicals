# Importing dependencies
from random import randint


def print_message(has_won):
    """
    PROTOTYPE:
        print_message()
        Arguments -> (bool) has_won
        Return values -> None
    DESCRIPTION:
        Takes a boolean argument has_won as argument and prints message to the console appropriately.
    USAGE:
        print_message(True) -> "You win!"
        print_message(False) -> "Better luck next time."
    """
    if has_won:
        print("You win !")
    else:
        print("Better luck next time.")


def draw():
    """
    PROTOTYPE:
        draw()
        Arguments -> None
        Return values -> None
    DESCRIPTION:
        Simulates a draw situation.
    ADDITIONALS:
        The rules of the draw are as follows:
            -> A lucky number is chosen randomly by the computer.
            -> The user inputs a guess.
            -> If the number the user entered is the same as the one selected randomly, he/she wins.
               Else, he loses.
    """
    lucky_number = randint(1, 600)
    user_guess = int(input("Choose a number between 1 and 600: "))

    print("Lucky number: " + str(lucky_number))
    print("Your guess: " + str(user_guess))

    if lucky_number == user_guess:
        has_won = True
    else:
        has_won = False

    print_message(has_won)


def main():
    print("--- ABC School Lucky Draw ---")
    draw()


# print(draw.__doc__)
# print(print_message.__doc__)


if __name__ == "__main__":
    main()
