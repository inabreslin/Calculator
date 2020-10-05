from tkinter import *
from math import *

#define window
window = Tk()
window.title("Calculator")
window.iconbitmap(r"C:\Users\Proteus\Desktop\Calculator\calculator.ico")

#define top entry box
Entry_Box = Entry(window, font = "calibri 18",  width = 20)

#define entry box postion
Entry_Box.grid(row = 0, column = 0, columnspan = 3)

#define global variables
global new
new = 0

#function definitions
def num_button_click(number):
    global new
    current = Entry_Box.get()
    button_clear()
    if new == 0:
        Entry_Box.insert(0, str(number))
        new = 1
    else:
        Entry_Box.insert(0, current + str(number))
    

def button_equal():
    global new
    current_equation = Entry_Box.get()
    button_clear()
    Entry_Box.insert(0, eval(current_equation))
    new = 0


def button_dot():
    Entry_Box.insert(END, ".")

def button_open_bracket():
    Entry_Box.insert(END, "(")

def button_close_bracket():
    Entry_Box.insert(END, ")")

def button_minus():
    Entry_Box.insert(END, "-")

def button_reciprocal():
    current = float(Entry_Box.get())
    button_clear()
    Entry_Box.insert(0, 1/current)

def button_root():
    current = float(Entry_Box.get())
    button_clear()
    Entry_Box.insert(0, sqrt(current))

def button_factorial():
    current = int(Entry_Box.get())
    button_clear()
    factorial = 1
    if current != 1:
        for i in range(1, current+1):
            factorial = factorial * i
    Entry_Box.insert(0, float(factorial))

def button_add():
    Entry_Box.insert(END, "+")

def button_subtract():
    Entry_Box.insert(END, "-")

def button_multiply():
    Entry_Box.insert(END, "*")

def button_divide():
    Entry_Box.insert(END, "/")

def button_backspace():
    current = Entry_Box.get()
    length = len(current)
    if (length != 0):
        Entry_Box.delete(length-1, END)

def button_clear():
    Entry_Box.delete(0, END)


#define buttons
Button0 = Button(window, width = 5, text = "0", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(0))
Button1 = Button(window, width = 5, text = "1", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(1))
Button2 = Button(window, width = 5, text = "2", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(2))
Button3 = Button(window, width = 5, text = "3", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(3))
Button4 = Button(window, width = 5, text = "4", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(4))
Button5 = Button(window, width = 5, text = "5", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(5))
Button6 = Button(window, width = 5, text = "6", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(6))
Button7 = Button(window, width = 5, text = "7", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(7))
Button8 = Button(window, width = 5, text = "8", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(8))
Button9 = Button(window, width = 5, text = "9", activebackground = "light steel blue", bg = "light blue", bd = 3, padx = 20, pady = 20, command = lambda: num_button_click(9))

Equal_Button = Button(window, width = 5, text = "=", activebackground = "steel blue", bg = "deep sky blue", bd = 3, padx = 21, pady = 20, command = button_equal)
Dot_Button = Button(window, width = 5, text = ".", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_dot)
Open_Bracket_Button = Button(window, width = 5, text = "(", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_open_bracket)
Close_Bracket_Button = Button(window, width = 5, text = ")", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_close_bracket)
Minus_Button = Button(window, width = 5, text = "(-)", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_minus)


Reciprocal_Button = Button(window, width = 5, text = "1/X", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_reciprocal)
Root_Button = Button(window, width = 5, text = "sqrt(X)", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 20, pady = 20, command = button_root)
Factorial_Button = Button(window, width = 5, text = "X!", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_factorial)

Add_Button = Button(window, width = 5, text = "+", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_add)
Subtract_Button = Button(window, width = 5, text = "-", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_subtract)
Multiply_Button = Button(window, width = 5, text = "*", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_multiply)
Divide_Button = Button(window, width = 5, text = "/", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_divide)

Backspace_Button = Button(window, width = 5, text = "Backspace", activebackground = "steel blue", bg = "deep sky blue", bd = 3, padx = 20, pady = 20, command = button_backspace)
Clear_Button = Button(window, width = 5, text = "Clear", activebackground = "steel blue", bg = "deep sky blue", bd = 3, padx = 20, pady = 20, command = button_clear)

Exit_Button = Button(window, width = 5, text = "Exit", activebackground = "red3", bg = "red", bd = 3, padx = 21, pady = 20, command = window.quit)

#button positioning
Button0.grid(row = 4, column = 1)
Button1.grid(row = 3, column = 0)
Button2.grid(row = 3, column = 1)
Button3.grid(row = 3, column = 2)
Button4.grid(row = 2, column = 0)
Button5.grid(row = 2, column = 1)
Button6.grid(row = 2, column = 2)
Button7.grid(row = 1, column = 0)
Button8.grid(row = 1, column = 1)
Button9.grid(row = 1, column = 2)

Equal_Button.grid(row = 6, column = 3)
Dot_Button.grid(row = 4, column = 0)
Open_Bracket_Button.grid(row = 6, column = 0)
Close_Bracket_Button.grid(row = 6, column = 2)
Minus_Button.grid(row = 4, column = 2)

Reciprocal_Button.grid(row = 5, column = 1)
Root_Button.grid(row = 6, column = 1)
Factorial_Button.grid(row = 5, column = 3)

Add_Button.grid(row = 1, column = 3)
Subtract_Button.grid(row = 2, column = 3)
Multiply_Button.grid(row = 3, column = 3)
Divide_Button.grid(row = 4, column = 3)

Backspace_Button.grid(row = 5, column = 0)
Clear_Button.grid(row = 5, column = 2)

Exit_Button.grid(row = 0, column = 3)

window.mainloop()
