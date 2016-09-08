##############################################################
# Drinkbot by Fredrik "Diffe" Sandstrom and Rikard Johansson #
# Feel free to use the code as long as this text stays intact#
##############################################################
from tkinter import *
from drinkar.py import *
	
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
D1.pack( side = LEFT )

D2 = Radiobutton(root, text="Sangria", indicatoron=0, width=25, variable=drink, value=2,
                  command=sel)
D2.pack( side = LEFT )

D3 = Radiobutton(root, text="Tequila sunrise", indicatoron=0, width=25, variable=drink, value=3,
                  command=sel)
D3.pack( side = LEFT )


#HÄR SKA VA RADBRYTNING
print ("Välj styrka på drinken:")

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
