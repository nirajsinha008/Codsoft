import tkinter as tk

# Create the main window
ws = tk.Tk()
ws.title("Simple Calculator")
ws.geometry('400x250+500+200')

# Global variable to store the expression
expression = ""

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalbutton():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar() is used to get the instance of the input field
equation = tk.StringVar()

# Create the text entry box for showing the expression
entry_box = tk.Entry(ws, textvariable=equation, font=('Arial', 20))
entry_box.grid(columnspan=6, ipadx=70)

# Create buttons and place them in the grid
button1 = tk.Button(ws, text=' 1 ', fg='black', bg='light gray',
                    command=lambda: press(1), height=2, width=7)
button1.grid(row=2, column=0)

button2 = tk.Button(ws, text=' 2 ', fg='black', bg='light gray',
                    command=lambda: press(2), height=2, width=7)
button2.grid(row=2, column=1)

button3 = tk.Button(ws, text=' 3 ', fg='black', bg='light gray',
                    command=lambda: press(3), height=2, width=7)
button3.grid(row=2, column=2)

button4 = tk.Button(ws, text=' 4 ', fg='black', bg='light gray',
                    command=lambda: press(4), height=2, width=7)
button4.grid(row=3, column=0)

button5 = tk.Button(ws, text=' 5 ', fg='black', bg='light gray',
                    command=lambda: press(5), height=2, width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(ws, text=' 6 ', fg='black', bg='light gray',
                    command=lambda: press(6), height=2, width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(ws, text=' 7 ', fg='black', bg='light gray',
                    command=lambda: press(7), height=2, width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(ws, text=' 8 ', fg='black', bg='light gray',
                    command=lambda: press(8), height=2, width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(ws, text=' 9 ', fg='black', bg='light gray',
                    command=lambda: press(9), height=2, width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(ws, text=' 0 ', fg='black', bg='light gray',
                    command=lambda: press(0), height=2, width=7)
button0.grid(row=5, column=0)

plus = tk.Button(ws, text=' + ', fg='black', bg='light gray',
                 command=lambda: press("+"), height=2, width=7)
plus.grid(row=2, column=3)

minus = tk.Button(ws, text=' - ', fg='black', bg='light gray',
                  command=lambda: press("-"), height=2, width=7)
minus.grid(row=3, column=3)

multiply = tk.Button(ws, text=' * ', fg='black', bg='light gray',
                     command=lambda: press("*"), height=2, width=7)
multiply.grid(row=4, column=3)

divide = tk.Button(ws, text=' / ', fg='black', bg='light gray',
                   command=lambda: press("/"), height=2, width=7)
divide.grid(row=5, column=3)

equal = tk.Button(ws, text=' = ', fg='black', bg='light gray',
                  command=equalpress, height=2, width=7)
equal.grid(row=5, column=2)

clear = tk.Button(ws, text='Clear', fg='black', bg='light gray',
                  command=clear, height=2, width=7)
clear.grid(row=5, column=1)

# Run the GUI loop
ws.mainloop()
