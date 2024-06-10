import tkinter as tk
from tkinter.constants import SUNKEN
import tkinter.messagebox
import math

# Function to handle button click
def myclick(number):
    if number == '^':
        entry.insert(tk.END, '**2')  # Append **2 for squaring
    else:
        entry.insert(tk.END, number)

# Function to evaluate the expression
def equal():
    try:
        expression = entry.get().replace('√', 'math.sqrt')
        y = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to dynamically update the font size based on the window size
def update_font(event):
    new_width = event.width
    new_height = event.height
    # Ensure the font size scales up with the window size, but limit the size
    new_font_size = max(10, min(new_width // 15, new_height // 15))
    new_font = ('Arial', new_font_size)
    entry.config(font=new_font)
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(font=new_font)

# List of colors for the buttons
button_colors = [
    '#FF6666', '#FFB266', '#FFFF66', '#B2FF66',
    '#66FF66', '#66FFB2', '#66FFFF', '#66B2FF',
    '#6666FF', '#B266FF', '#FF66FF', '#FF66B2',
    '#FFC266', '#C2FF66', '#66FFC2', '#C266FF',
    '#FF6666', '#FFB266', '#FFFF66', '#B2FF66'
]

# Main window setup
window = tk.Tk()
window.title('Dynamic Calculator ')

frame = tk.Frame(master=window, padx=10, pady=10)
frame.pack(expand=True, fill='both')

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=5, ipady=5, pady=5, sticky='nsew')

# Create buttons with different colors
buttons = [
    '1', '2', '3', '+', '(',
    '4', '5', '6', '-', ')',
    '7', '8', '9', '*', '^',
    'C', '0', '=', '/', '√'
]

row = 1
col = 0
for i, button in enumerate(buttons):
    action = lambda x=button: myclick(x) if x not in ('C', '=', '√') else clear() if x == 'C' else equal() if x == '=' else myclick('√(')
    b = tk.Button(master=frame, text=button, padx=15, pady=5, command=action, bg=button_colors[i % len(button_colors)])
    b.grid(row=row, column=col, pady=2, padx=2, sticky='nsew')
    col += 1
    if col > 4:
        col = 0
        row += 1

# Configure grid weights to make the UI dynamically resizable
for i in range(5):
    frame.columnconfigure(i, weight=1)
for i in range(row + 1):
    frame.rowconfigure(i, weight=1)

# Bind the <Configure> event to the update_font function
window.bind('<Configure>', update_font)

# Main loop
window.mainloop()
