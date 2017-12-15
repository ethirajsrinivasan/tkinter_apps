from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo('Window Title', 'Monkeys can live upto 300 years')

answer = tkMessageBox.askquestion("Question 1", 'Do you like Batman?')

if answer == 'yes':
    print("The batman")
root.mainloop()