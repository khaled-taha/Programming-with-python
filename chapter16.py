
# Chapter 16
from tkinter import *
root = Tk()
root.geometry("400x500")

# <<<<Frame>>>>

# How to create a frame?
myframe = Frame() # Like any component, you can put it in the main window by grid() method
myframe.grid(column=0, row=0)

# you can add any component to it
my_button = Button(myframe, text="Enter your age", bg="yellow")
my_button.grid(row=0, column=0)

scale = Scale(from_=1, to_=100, length=300, orient='horizontal')
scale.grid(row=1, column=0)

root.mainloop()

# ==================================================================================

# Colors:

# How to set the color for the label(for example.)
# you can set the color of the label by one of 2 ways:
    # Way 1: By Hex
my_label = Label(text="First Name", width=5, height=3, bg='#A202FF')
    # Way 2: name of color
my_label = Label(text="First Name", width=5, height=3, bg="yellow")

# ==================================================================================

# <<<<image>>>> 

# Can I replace the text of the ((Label of Button)) with an image in Tkinter ?
#  yes you can. But you can add an image with a type of GIF only in tkinter
# one solution is to use the Python Imaging Library

my_image = PhotoImage(file='me.gif')
image_label = Label(image=my_image)
image_button = Button(image=my_image)

# ==================================================================================

# <<<<Canvases>>>>

# Creates a canvas with a white background that is 200 × 200 pixels in size
my_canvas = Canvas(background='white', width=200, height=200)

# create a rectangle in this canvas with (20, 100) in upper laft, and (30, 150) in lower right, and fill it with red
my_canvas.create_rectangle(20, 100, 30, 150, fill='red')

my_canvas.grid(row=0, column=0)

# create oval
my_canvas.create_oval(20,100,70,180, fill='blue')
my_canvas.grid(row=1, column=1)

# create line
my_canvas.create_line(20,100,70,180, fill='green')
my_canvas.grid(row=2, column=2)

# create circle with redius:
def create_circle(x, y, r):
    my_canvas.create_oval(x-r, y-r, x+r, y+r)

# add images to a canvas. 
cheetah_image = PhotoImage(file='cheetahs.gif')
my_canvas.create_image(50,50, image=cheetah_image)
my_canvas.grid(row=3, column=3)

# ==================================================================================

# Check buttons
    # steps:
        # 1 - create a variable that store the state of the chack button
state = IntVar() # 0 -> unchecked, 1 -> checked
        #  you can change the state of the var
state.set(1)

        # 2 - create the check button and bind it with the var
my_check_button = Checkbutton(text="check button", var = state)
# ==================================================================================

# Radio buttons

from tkinter import *

root = Tk()

i = IntVar() #Basically Links Any Radio button With The Variable=i.
r1 = Radiobutton(root, text="option 1", value=1, variable=i)
r2 = Radiobutton(root, text="option 2", value=2, variable=i)
#
"""
If both values where equal, when one of the buttons
are pressed all buttons would be pressed.
If a button is pressed its value is true, or 1.
If you want to acess the data from the
radiobuttons, use a if statment like
"""
if (i.get() ==1):
       print("you picked option1")
else:
        print("you picked option2")
        
# :)

r1.pack()
r2.pack()

# ==================================================================================

# Create a textbox
textbox = Text(font=('Verdana', 16), height=6, width=40)

"""
textbox.get(1.0,END):  returns the contents of the text box
textbox.delete(1.0,END): deletes everything in the text box
textbox.insert(END,'Hello'): inserts text at the end of the text box
"""
# ==================================================================================

# create Scale bar (Progress)
scale = Scale(from_=1, to_=100, length=300, orient='horizontal')
# ==================================================================================
# GUI Events

# To bind between the component with any function when any key is pressed:
# component.bind(<Key_Name>, function)

# Program 1
from tkinter import *
def callback(event):
    print(event.keysym)
    # keysym: The name of the key that was pressed
root = Tk()
root.bind('<Key>', callback)
mainloop()

# Program 2
from tkinter import *
def callback1(event):
    print('You pressed the enter key.')
def callback2(event):
    print('You pressed the up arrow.')
root = Tk()
root.bind('<Return>', callback1)
root.bind('<Up>', callback2)
mainloop()

# ==================================================================================

