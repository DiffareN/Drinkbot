##############################################################
# Drinkbot by Fredrik "Diffe" Sandstrom and Rikard Johansson #
# Feel free to use the code as long as this text stays intact#
##############################################################
from tkinter import *

def sel():
   selection = "Du har valt " + str(var.get()) + " cl"
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="4 cl", indicatoron=0, variable=var, value=4, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="6 cl", indicatoron=0, variable=var, value=6, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="8 cl", indicatoron=0, variable=var, value=8, command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
