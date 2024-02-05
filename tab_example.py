import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Tab Example")

# Create a Tab Control
tab_control = ttk.Notebook(root)

# Create the first tab
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")

# Create content for the first tab
label1 = tk.Label(tab1, text="This is Tab 1")
label1.pack(padx=20, pady=20)

# Create the second tab
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")

# Create content for the second tab
label2 = tk.Label(tab2, text="This is Tab 2")
label2.pack(padx=20, pady=20)

# Pack the tab control to the main window
tab_control.pack(expand=1, fill="both")

# Start the Tkinter main loop
"""root.mainloop()"""
