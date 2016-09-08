##############################################################
# Drinkbot by Fredrik "Diffe" Sandstrom and Rikard Johansson #
# Feel free to use the code as long as this text stays intact#
##############################################################
from tkinter import *
from drinkar.py import *

	
def sel():
	selection = "Du har valt " + str(var.get()) + " cl"
	label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="4 cl", indicatoron=0, width=10, variable=var, value=4,
                  command=sel)
R1.pack( side = LEFT )

R2 = Radiobutton(root, text="6 cl", indicatoron=0, width=10, variable=var, value=6,
                  command=sel)
R2.pack( side = LEFT )

R3 = Radiobutton(root, text="8 cl", indicatoron=0, width=10, variable=var, value=8,
                  command=sel)
R3.pack( side = LEFT )

label = Label(root)
label.pack()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()
