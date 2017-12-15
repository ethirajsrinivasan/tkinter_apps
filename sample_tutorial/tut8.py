from Tkinter import *


class TrakButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


    def printMessage(self):
        print("This worked")


root = Tk()
b = TrakButtons(root)
root.mainloop()
