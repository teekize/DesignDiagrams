from tkinter import *
from PIL import Image
from PIL import ImageTk
"""
in this file we learn how to create an icon in tkinter
an .ico file you can get some free icons from the website 
https://icon-icons.com/

be keen on thespelling of ImageTk not ImageTK.
"""

root = Tk()

root.title("Blessed Schools Narok")
root.iconbitmap(r'C:\Users\ELVIS LEMEIN\Documents\ALL PYTHON PROJECTS\GUI-py\school.ico')

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\ELVIS LEMEIN\Pictures\focus.jpg"))
my_label =Label(image= my_img)
my_label.pack()















exit_bt =Button(root, text="Exit", command =root.quit)
exit_bt.pack()
root.mainloop()