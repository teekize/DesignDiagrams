"""
this module creates an image view application where you can view your appplications.
"""
from tkinter import *
from PIL import ImageTk , Image
import os

imgs =os.listdir(r"C:\Users\ELVIS LEMEIN\Pictures\2018-08-06")
def img_(imgs):
    """
    this function gets the list of images 
    and opens the files and retuns the images as a list 
    """
    l=[]
    for img in imgs:

        my_img =ImageTk.PhotoImage(Image.open(rf"C:\Users\ELVIS LEMEIN\Pictures\2018-08-06\{img}"))
        l.append(my_img)
    return l

def back(num):
    """
    this goes back 
    """
    global my_label
    global next_
    global back

    my_label.grid_forget()
    my_label =Label(image=image[num -1])
    my_label.grid(row =0, column =0, columnspan =3)
    next_bt = Button(root, text=">>", command =lambda: next_(num +1))
    back_bt = Button(root, text="<<", command =lambda: back(num-1))

    if num == 0:
        back_bt = Button(root, text= "<<",  state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    next_bt.grid(row=1, column=2)
    back_bt.grid(row=1, column=0)

    return

def next_(num):
    """
    this function gives a next image to be displayed on the screen
    it will be passed a number for which it will increment the number 
    so that it can be added to the screen
    """
    global my_label
    global next_
    global back
    
    #we first clear the screen
    my_label.grid_forget()
    my_label =Label(image=image[num  +1])
    my_label.grid(row =0, column =0, columnspan =3)
    next_bt = Button(root, text=">>", command =lambda: next_(num +1))
    back_bt = Button(root, text="<<", command =lambda: back(num-1))

    if num == len(imgs) - 2:
        next_bt = Button(root, text=">>", state =DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    next_bt.grid(row=1, column=2)
    back_bt.grid(row=1, column=0)

root =Tk()
root.title("Image viewer")
root.iconbitmap(r"C:\Users\ELVIS LEMEIN\Documents\ALL PYTHON PROJECTS\GUI-py\school.ico")

image =img_(imgs)
my_label =Label(image=image[0])
my_label.grid(row =0, column =0, columnspan =3)

back_bt = Button(root, text= "<<", command= back, state=DISABLED)
next_bt = Button(root, text= ">>", command =lambda: next_(0))
exit_ =Button(root, text= "Exit", command= root.quit)

back_bt.grid(row =1, column=0)
next_bt.grid(row=1, column =2)
exit_.grid(row=1, column=1)

root.mainloop()