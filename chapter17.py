
# Chapter 17
from tkinter import *
root = Tk()
root.geometry("400x500")

# How to change the title of the window ?
root.title("My Window")

# =====================================================================================

# How to disable or enable the button ?
# A/ By change the state 

# NORMAL -> Enable
# DISABLED -> Disable

label = Label(text='Your label')
label.pack()

def function():
    print('command')
my_button = Button(text="Calc", width=5, height=5, command=function, state= DISABLED)
my_button.pack()

# you can change the state later by:
my_button.configure(state=NORMAL)

# =====================================================================================

# How to display the properties of the component ?
# By cget('the property')

# Button
print(my_button.cget('text'))
print(my_button.cget('state'))
print(my_button.cget('bg'))
print(my_button.cget('fg'))

# Label
print(label.cget('text'))
print(label.cget('state'))
print(label.cget('bg'))
print(label.cget('fg'))

# This can be used with buttons, canvases, etc
# Tkinter overrides the [] operators, so that label['text'] accomplishes the same thing as the example above.
# =====================================================================================

# <<<<Messagebox>>>>
# How to create a Messagebox ?
# At first, ask your self: What is the type of the messageBox that you want to create ?

from tkinter.messagebox import *
"""
showinfo          :OK button
askokcancel       :OK and Cancel buttons
askquestion       :Yes and No buttons
askretrycancel    :Retry and a Cancel buttons
askyesnocancel    :Yes, No, and Cancel buttons
showerror         :An error icon and an OK button
showwarning       :A warning icon an an OK button

"""

showinfo(title = 'Message for you', message='Hi there!')
askquestion(title='Quit?', message='Do you really want to quit?')
showwarning(title='Warning', message='Unsupported format')

# How to catch the returned value form this messagebox ?
from tkinter import *
from tkinter.messagebox import *

def quitter_function():
    answer = askquestion(title='Quit?', message='Really quit?')
    if answer=='yes':
        root.destroy()

root = Tk()
root.protocol('WM_DELETE_WINDOW', quitter_function)
mainloop()

"""
showinfo          :Always returns 'ok'
askokcancel       :OK—True Cancel or window closed—False
askquestion       :Yes—'yes' No—'no'
askretrycancel    :Retry—True Cancel or window closed—False
askyesnocancel    :Yes—True No—False anything else—None
showerror         :Always returns 'ok'
showwarning       :Always returns 'ok'

"""

# Note: you can destroy any thing by destroy() method.
root.destroy()
my_button.destroy()
# =====================================================================================
# <<<<dialog>>>>

# How to create dialog boxes that allow the user to pick a file to open or to save a file.
from tkinter.filedialog import *

"""
askopenfilename      :Opens a typical file chooser dialog
askopenfilenames     :Like previous, but user can pick more than one file
asksaveasfilename    :Opens a typical file save dialog
askdirectory         :Opens a directory chooser dialog

"""

# In dialog, You can set initialdir to the directory you want the dialog to start in and specify the file types.
"""Here is an example that opens a file dialog that allows you to select a text file.
The program then displays the contents of the file in a textbox"""

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *

root = Tk()
my_textbox = ScrolledText()
my_textbox.grid(row=0, column=0)

fileName = ''
s = ""

def openfile():
    global fileName, s
    fileName = askopenfilename(initialdir='E:\4th-Dep\python', filetypes=[('Text files', '.txt'),('All files', '*')])
    s = open(fileName).read()
    my_textbox.insert(1.0, s)

openfile_btn = Button(text='open file', command=openfile)
openfile_btn.grid(row=0, column=0)


root.mainloop()
# =====================================================================================

# <<<<Open New Window>>>>
from tkinter import *

root = Tk()


def openNewWindow():
    new_window = Toplevel()
    label = Label(new_window, text="New Window")
    

btn = Button(text='open window', command=openNewWindow)
btn.grid(row=0, column=0)


root.mainloop()

# =====================================================================================

# other points:
# 1 - Menu bars
# 2 - update the window
# 3 - StringVar

