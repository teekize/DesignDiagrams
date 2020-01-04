from tkinter import *

root = Tk()

"""
we are creating a lable widget
"""
myLabel = Label(root, text="Hello wolrd")
myLabel2 = Label(root, text="my name is Teeka")
#then we place it on the root 

""" 
this is the grid system where things are arranged in rows and columns
with this grid we want to place the widget on the screen
"""

myLabel.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

"""
the eventloop. it does things as long as the event is still happaning
its in constant loop until its interrupted.
"""
root.mainloop()