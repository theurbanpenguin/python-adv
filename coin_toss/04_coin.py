# Import the 'random' module which allows us to use functions for generating random numbers
import random

# import the local color module and the Color class, allowing access to the variables
from color import Colors

# Initialize a variable to control the game loops_coin_again=True
toss_coin_again=True

# Define a function named 'coin_toss'
def coin_toss():
    # Define a tuple containing the two possible outcomes of a coin toss: 'heads' and 'tails'
    coin_sides = ('heads', 'tails')

    # Randomly choose one of the outcomes using random.choice()
    result = random.choice(coin_sides)

    # Ask the user to guess the outcome and store the input.
    # Convert the input to lowercase and remove whitespace from both ends for consistent comparison.
    user_guess = input("Enter heads or tails: ").lower().strip()

    # Compare the first character of the user's guess and the result.
    # This allows the user to enter any string as long as it starts with 'h' (for heads) or 't' (for tails).
    if result[0] == user_guess[0]:
        # If the first characters match, print a winning message.
        print(f"{Colors.GREEN}You win, it was {result}{Colors.RESET}")
    else:
        # If they don't match, print a losing message.
        print(f"{Colors.RED}You lose, it was {result}{Colors.RESET}")

# Convert a single character input ('y' or 'n') to a boolean value
# 'y' becomes True, anything else becomes False
def get_boolean_input(input):
    if input == 'y':
        return True
    else:
        return False


# Check if this script is being run directly (not being imported)
if __name__ == '__main__':
    # Game loop
    while toss_coin_again:
        # Call the coin_toss function to start the game.
        coin_toss()
        # Ask user if they want to continue, only 'y' will allow the game to continue.
        user_continue=input("Do you want to toss again, enter y or n: ").lower()
        toss_coin_again = get_boolean_input(user_continue)

