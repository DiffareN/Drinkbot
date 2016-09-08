##############################################################
# Drinkbot by Fredrik "Diffe" Sandstrom and Rikard Johansson #
# Feel free to use the code as long as this text stays intact#
##############################################################
##############################################################
# Drinkbot by Fredrik "Diffe" Sandstrom and Rikard Johansson #
# Feel free to use the code as long as this text stays intact#
##############################################################
from tkinter import *
from drinkar import * 
	
def sel():
	if str(drink.get()) == '1':
		drinknamn = "Redbull & vodka"
	elif str(drink.get()) == '2':
		drinknamn = "Sangria"
	elif str(drink.get()) == '3':
		drinknamn = "Tequila sunrise"
	else:
		drinknamn = "Du har inte valt en drink!"
		
	selection = "Du har valt " + str(var.get()) + " cl och " + drinknamn
	label.config(text = selection)

root = Tk()
drink = IntVar()
D1 = Radiobutton(root, text="Redbull & Vodka", indicatoron=0, width=25, variable=drink, value=1,
                  command=sel)
D1.place(x=30, y=0)

D2 = Radiobutton(root, text="Sangria", indicatoron=0, width=25, variable=drink, value=2,
                  command=sel)
D2.place(x=280, y=0)

D3 = Radiobutton(root, text="Tequila sunrise", indicatoron=0, width=25, variable=drink, value=3,
                  command=sel)
D3.place(x=530, y=0)



#HÄR SKA VA RADBRYTNING


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
root.overrideredirect(1)
root.geometry("800x480")
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()

