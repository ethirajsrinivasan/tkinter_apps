from Tkinter import *
from PIL import Image, ImageTk




root =Tk()

image = Image.open("save.png")
photo = ImageTk.PhotoImage(image)

# photo = PhotoImage(file='download.jpg')
label = Label(root, image=photo)
label.pack()

root.mainloop()