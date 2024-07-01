import math
import tkinter as tk

def addition(a,b):
    return (a + b)

def subtraction(a,b):
    return (a - b)

def devision(a,b):
    return (a / b)

def multiplication(a,b):
    return (a * b)

def button_clicker():
    pass

calculator = tk.Tk()
calculator.title("Simple Calculator")
calculator.geometry("300x400")

#create a frame
frame = tk.Frame(calculator, bd=10, relief="ridge", padx=20, pady=20, bg="#F5DEB3")
frame.pack(fill="both", expand=True)

num_rows = 3
num_cols = 3
count = 1
# Loop through rows and columns to create buttons
for row in range(num_rows):
    for col in range(num_cols):
        # Create a button with a unique identifier
        button_nr = f"{count}"
        button = tk.Button(frame, text=button_nr)
        count += 1
        
        # Place the button in the grid
        button.grid(row=row, column=col, padx=10, pady=10)

calculator.mainloop()
