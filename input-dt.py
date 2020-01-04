from tkinter import *

root = Tk()

def fetch():
    lable = Label(root, text=data_ent.get())
    lable.grid(row=5, column =4)

"""
we create the inputs for getting data with the Entry class
to get the data form the input widget we use the get method

"""
data_ent =Entry(root, width=50 )
data_ent.insert(0, "Enter your name: ")
data_ent.grid(row=2, column =1)

click = Button(root, text ="Submit", command= fetch)
click.grid(row=2, column =4)

root.mainloop()
