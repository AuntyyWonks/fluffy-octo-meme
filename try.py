from tkinter import *
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.insert(END, str(result))
        except Exception as e:
            display.insert(END, "Error\n" + str(e))
    elif text == "C":
        display.delete(0, END)
    else:
        display.insert(END, text)

root = Tk()
root.title("Scientific Calculator")

display = Entry(root, width=40, bd=8, font=('arial', 20, 'bold'), justify='right')
display.grid(row=0, column=0, columnspan=4)

for i in range(9):
    Button(root, text=str(i), width=5, command=lambda i=i: click(i)).grid(row=(i//3)+1, column=i%3)

operators = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/"
}

# Define a mapping for operators to columns
operator_columns = {"+": 1, "-": 2, "*": 3, "/": 4}

for op in operators:
    Button(root, text=op, width=5, command=lambda op=op: click(op)).grid(row=4, column=operator_columns[op])

buttons = ["sin", "cos", "tan", "log", "log10", "exp", "pi", "e"]
for i, func in enumerate(buttons):
    Button(root, text=func, width=5, command=lambda func=func: click(func)).grid(row=5, column=i % 4)

root.mainloop()
