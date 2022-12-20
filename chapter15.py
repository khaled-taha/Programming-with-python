
# Chapter 15

from tkinter import *

# craete a window
root = Tk()
# your code and components
root.mainloop()

# ============================================================================

from tkinter import *

# craete a window
root = Tk()
root.geometry("500x500")
# <<<<Label>>>>
# How to create a label in the window

# Way 1:
    # create the label with (Text, font, backgroud, forground)
my_label = Label(text = "Enter your name", font = ("Arial", 30), bg = "red", fg = "black", width=20, height=5)
    # Put this label in the window
my_label.grid(column=0, row=0)

#Way2:
    # create the label with (Text, font, backgroud, forground), and make a link with the window
my_label = Label(root, text = "Enter your name", font = ("Arial", 30), bg = "red", fg = "black", width=20, height=5)
    # Put this label in the window
my_label.pack(side=BOTTOM)

# Note: We cannot use gird with pack
# How to change the content of the label later? 

my_label.configure(text="Changes")

a = 1
b = 2
my_label.configure(text='a = {}, b = {}'.format(a, b))

root.mainloop()
# ============================================================================

# <<<<Inputs>>>>
# How to create an input ? with Entry
    # Steps:
        # 1 - Create the entry
my_input = Entry()
        # 2 - put it in the Window
my_input.grid(column=0, row=1)
        # 3 - During Running, you can get the input from Entry by get() method as a (((String value)))
String_val = my_input.get()
num_val = eval(String_val)

# ============================================================================

# How to create a Button
    # Steps: 
        # CREATE the command that you want to execute by the button
def sayHello():
    print("Hello")
        # create the button with the internal text and (the comman)
sayHello_btn = Button(text="Print Hello in the terminal", command = sayHello)
        # put it in the window
sayHello_btn.grid(column=0, row=2)


# Program to create a list of buttons form A to Z
from tkinter import *
root = Tk()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
label = Label()
label.grid(column = 1, row = 1, columnspan = 26)

def command(x):
    label.configure(text = 'Buttom {} clicked'.format(alpha[x]))

buttons = [0] * 26 # list with 26 things. they will be replaced with buttons
for i in range(26):
    buttons[i] = Button(text = alpha[i], command = lambda x = i:command(x))
    buttons[i].grid(row = 0, column = i)

root.mainloop()

# ============================================================================

# create a program that count the time of clicks 

from tkinter import *
root = Tk()

label = Label()
label.grid(column=0, row = 0)

counter = 0

def click():
    global counter
    counter += 1
    label.configure(text = 'Clicked {} times'.format(counter))
    
button = Button(text = "click", command = click)
button.grid(column=0, row=1)

root.mainloop()

# ============================================================================
