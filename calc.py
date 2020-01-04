from tkinter import *

root =Tk()
root.title("Simple calculator")

dt_ent= Entry(root, width=40, borderwidth=5)
dt_ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # l =[]
    # l.append(number)
    current =dt_ent.get()
    # for number in l:
    dt_ent.delete(0, END)

    dt_ent.insert(0, str(current) + str(number))
    

def button_clear():
    dt_ent.delete(0, END)

def button_add():
    tst_num =dt_ent.get()
    global f_num
    global math
    math ="addition"
    f_num =int(tst_num)
    dt_ent.delete(0, END)

def button_equal():
    second_numb =dt_ent.get()
    dt_ent.delete(0, END)
    if math == "addition":
        dt_ent.insert(0, f_num + int(second_numb))
    elif math == "subtraction":
        dt_ent.insert(0, f_num - int(second_numb))
    elif math == "division":
        dt_ent.insert(0, f_num / int(second_numb))
    else :
        dt_ent.insert(0, f_num * int(second_numb))

def subtract():
    tst_num =dt_ent.get()
    global f_num
    global math
    math ="subtraction"
    f_num =int(tst_num)
    dt_ent.delete(0, END)
    return

def multiply():
    tst_num =dt_ent.get()
    global f_num
    global math
    math ="multiplication"
    f_num =int(tst_num)
    dt_ent.delete(0, END)
    return
def divide():
    tst_num =dt_ent.get()
    global f_num
    global math
    math ="division"
    f_num =int(tst_num)
    dt_ent.delete(0, END)
    return
#define buttons
button_1 = Button(root, text ="1", padx =40, pady =20, command =lambda: button_click(1))
button_2 = Button(root, text ="2", padx =40, pady =20, command =lambda:button_click(2))
button_3 = Button(root, text ="3", padx =40, pady =20, command =lambda:button_click(3))
button_4 = Button(root, text ="4", padx =40, pady =20, command =lambda:button_click(4))
button_5 = Button(root, text ="5", padx =40, pady =20, command =lambda:button_click(5))
button_6 = Button(root, text ="6", padx =40, pady =20, command =lambda:button_click(6))
button_7 = Button(root, text ="7", padx =40, pady =20, command =lambda:button_click(7))
button_8 = Button(root, text ="8", padx =40, pady =20, command =lambda:button_click(8))
button_9 = Button(root, text ="9", padx =40, pady =20, command =lambda:button_click(9))
button_0 = Button(root, text ="0", padx =40, pady =20, command =lambda:button_click(0))
button_add = Button(root, text ="+", padx =39, pady =20, command =button_add)
button_clear = Button(root, text ="C", padx =91, pady =20, command =button_clear)
button_equal = Button(root, text ="=", padx =91, pady =20, command =button_equal)

button_sub = Button(root, text ="-", padx =42, pady =20, command =subtract)
button_mult = Button(root, text ="*", padx =42, pady =20, command =multiply)
button_div = Button(root, text ="/", padx =42, pady =20, command =divide)

#button the buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan =2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan =2)
button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)
root.mainloop()