# Import the 'random' module which allows us to use functions for generating random numbers
import random

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
        print(f"You win, it was {result}")
    else:
        # If they don't match, print a losing message.
        print(f"You lose, it was {result}")

# Check if this script is being run directly (not being imported)
if __name__ == '__main__':
    # If the script is run directly, call the coin_toss function to start the game.
    coin_toss()
