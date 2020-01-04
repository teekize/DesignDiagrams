from tkinter import *

root = Tk()

def login_fnc():
    myLable = Label(root, text="you can now login")
    myLable.grid(row=3, column= 2)

"""
we now create a button widget which we place it in the root window
it has some addition options which we can add to style the button better
"""
Submit=Button(root, text="Submit", padx=30, 
                pady= 20, background= "black", font = 15,foreground="#f1c40f")
""" 
In creating buttons colors can be in hexadecimal format. ie #ffffff
"""

Login =Button(root , text="Login", padx= 20, font =25, command=login_fnc)
Login.grid(row =1, column =2)
Submit.grid(row=0, column =0)

root.mainloop()