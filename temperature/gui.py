import tkinter as tk

def convert_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Create a Tkinter window
window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")

# Create labels and entry field
instruction_label = tk.Label(window, text="Enter temperature in Celsius:")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="")
result_label.pack()

convert_button = tk.Button(window, text="Convert", command=convert_to_fahrenheit)
convert_button.pack()

# Start the Tkinter event loop
window.mainloop()
