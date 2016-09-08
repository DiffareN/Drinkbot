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

	selection = "Du har valt " + str(var.get()) + " cl och " + drinknamn
	label.config( text = selection)
	label.configure(background = 'white')

root = Tk()
drink = IntVar()
D1 = Radiobutton(root, text="Redbull & Vodka", indicatoron=0, width=25, variable=drink, value=1,
                  command=sel)
D1.place(x=50, y=30)

D2 = Radiobutton(root, text="Sangria", indicatoron=0, width=25, variable=drink, value=2,
                  command=sel)
D2.place(x=300, y=30)

D3 = Radiobutton(root, text="Tequila sunrise", indicatoron=0, width=25, variable=drink, value=3,
                  command=sel)
D3.place(x=550, y=30)



#HÄR SKA VA RADBRYTNING


var = IntVar()
R1 = Radiobutton(root, text="4 cl", indicatoron=0, width=10, variable=var, value=4,
                  command=sel)
R1.place(x=135, y=300)

R2 = Radiobutton(root, text="6 cl", indicatoron=0, width=10, variable=var, value=6,
                  command=sel)
R2.place(x=335, y=300)

R3 = Radiobutton(root, text="8 cl", indicatoron=0, width=10, variable=var, value=8,
                  command=sel)
R3.place(x=535, y=300)

label = Label(root)
label.place(x=285, y=0)
label.configure(background='#533B9D')
root.overrideredirect(1)
root.configure(background='#533B9D')
root.geometry("800x480")
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()
