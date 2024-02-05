import tkinter as tk
from tkinter.constants import W

def convert_temperature():
    try:
        temperature = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result.set(f"{(temperature * 9/5) + 32:.2f} °F")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result.set(f"{temperature + 273.15:.2f} K")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result.set(f"{(temperature - 32) * 5/9:.2f} °C")
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result.set(f"{(temperature - 32) * 5/9 + 273.15:.2f} K")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result.set(f"{temperature - 273.15:.2f} °C")
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result.set(f"{(temperature - 273.15) * 9/5 + 32:.2f} °F")
        else:
            result.set("Invalid conversion")

    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create labels
label1 = tk.Label(root, text="Enter Temperature:")
label1.grid(row=0, column=0, columnspan=2, sticky=W)

# Create an entry widget for temperature input
entry = tk.Entry(root)
entry.grid(row=0, column=2, columnspan=2, sticky=W)

# Create labels for unit selection
label2 = tk.Label(root, text="From Unit:")
label2.grid(row=1, column=0, sticky=W)

label3 = tk.Label(root, text="To Unit:")
label3.grid(row=2, column=0, sticky=W)

# Create variables for unit selection
from_unit_var = tk.StringVar()
to_unit_var = tk.StringVar()

from_unit_var.set("Celsius")  # Default from unit
to_unit_var.set("Fahrenheit")  # Default to unit

# Create option menus for unit selection
from_unit_menu = tk.OptionMenu(root, from_unit_var, "Celsius", "Fahrenheit", "Kelvin")
from_unit_menu.grid(row=1, column=1, sticky=W)

to_unit_menu = tk.OptionMenu(root, to_unit_var, "Celsius", "Fahrenheit", "Kelvin")
to_unit_menu.grid(row=2, column=1, sticky=W)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=1, sticky=W)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, foreground="green")
result_label.grid(row=4, column=0, columnspan=4, sticky=W)

# Start the Tkinter main loop
root.mainloop()


# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
