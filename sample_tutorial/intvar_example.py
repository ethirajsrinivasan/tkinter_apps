from Tkinter import Entry, IntVar, Tk

root = Tk()

data = IntVar()

entry = Entry(textvariable=data)
entry.grid()

def click(event):
    # Get the number, add 1 to it, and then print it
    print data.get() + 1

# Bind the entrybox to the Return key
entry.bind("<Return>", click)

root.mainloop()