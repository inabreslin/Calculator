from tkinter import *

#define window
window = Tk()
window.title("Calculator")

#define top entry box
Entry_Box = Entry(window, font = "calibri 18",  width = 20)

#define entry box postion
Entry_Box.grid(row = 0, column = 0, columnspan = 3)

#define global variables
global current_operation
current_operation = "none"

#function definitions
def num_button_click(number):

    current = Entry_Box.get()
    button_clear()
    Entry_Box.insert(0, current + str(number))

def button_equal():
    global first_number
    global current_operation
    current_num = Entry_Box.get()
    button_clear()
    if current_operation == "addition":
        Entry_Box.insert(0, first_number + float(current_num))
    elif current_operation == "subtract":
        Entry_Box.insert(0, first_number - float(current_num))
    elif current_operation == "multiply":
        Entry_Box.insert(0, first_number * float(current_num))
    elif current_operation == "divide":
        Entry_Box.insert(0, first_number / float(current_num))
    current_operation = "none"

def operator():
    global first_number
    if current_operation != "none":
        button_equal()
    first_number = float(Entry_Box.get())

def button_add():
    operator()
    global current_operation
    current_operation = "addition"
    button_clear()

def button_subtract():
    operator()
    global current_operation
    current_operation = "subtract"
    button_clear()

def button_multiply():
    operator()
    global current_operation
    current_operation = "multiply"
    button_clear()

def button_divide():
    operator()
    global current_operation
    current_operation = "divide"
    button_clear()

def button_clear():
    Entry_Box.delete(0, END)

def button_exit():
    window.destroy()
    return


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

Equal_Button = Button(window, width = 5, text = "=", activebackground = "steel blue", bg = "deep sky blue", bd = 3, padx = 20, pady = 20, command = button_equal)

Add_Button = Button(window, width = 5, text = "+", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_add)
Subtract_Button = Button(window, width = 5, text = "-", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_subtract)
Multiply_Button = Button(window, width = 5, text = "*", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_multiply)
Divide_Button = Button(window, width = 5, text = "/", activebackground = "steel blue", bg = "sky blue", bd = 3, padx = 21, pady = 20, command = button_divide)

Clear_Button = Button(window, width = 5, text = "Clear", activebackground = "steel blue", bg = "deep sky blue", bd = 3, padx = 20, pady = 20, command = button_clear)

Exit_Button = Button(window, width = 5, text = "Exit", activebackground = "red3", bg = "red", bd = 3, padx = 21, pady = 20, command = button_exit)

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

Equal_Button.grid(row = 4, column = 2)

Add_Button.grid(row = 1, column = 3)
Subtract_Button.grid(row = 2, column = 3)
Multiply_Button.grid(row = 3, column = 3)
Divide_Button.grid(row = 4, column = 3)

Clear_Button.grid(row = 4, column = 0)

Exit_Button.grid(row = 0, column = 3)

window.mainloop()
