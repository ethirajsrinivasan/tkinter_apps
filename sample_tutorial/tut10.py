from Tkinter import *

def doNothing():
    print("OK  i wont")


root = Tk()

# ***** Main Menu *****
menuTrak = Menu(root)
root.config(menu=menuTrak)

subMenu = Menu(menuTrak)
menuTrak.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New project...", command=doNothing)
subMenu.add_command(label="Now .", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

subEditMenu = Menu(menuTrak)
menuTrak.add_cascade(label="Edit", menu=subEditMenu)
subEditMenu.add_command(label="Redo", command=doNothing)

# ***** toolbar *****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP,fill=X)
root.mainloop()

















