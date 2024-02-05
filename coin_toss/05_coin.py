import tkinter as tk
import random

def coin_toss():
    coin_sides = ('heads', 'tails')
    result = random.choice(coin_sides)
    user_guess = user_input.get().lower().strip()

    if result[0] == user_guess[0]:
        result_label.config(text=f"You win, it was {result}", foreground="green")
    else:
        result_label.config(text=f"You lose, sorry, it was {result}", foreground="red")

def play_again():
    coin_toss()
    user_input.delete(0, 'end')

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Coin Toss Game")

    # Create and configure widgets
    user_input_label = tk.Label(root, text="Heads or Tails?")
    user_input = tk.Entry(root)
    result_label = tk.Label(root, text="")

    toss_button = tk.Button(root, text="Toss Coin", command=coin_toss)
    play_again_button = tk.Button(root, text="Play Again", command=play_again)

    # Grid layout
    user_input_label.grid(row=0, column=0)
    user_input.grid(row=0, column=1)
    toss_button.grid(row=1, column=0, columnspan=2)
    result_label.grid(row=2, column=0, columnspan=2)
    play_again_button.grid(row=3, column=0, columnspan=2)

    root.mainloop()