from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Quadratische Gleichungen")
root.configure(bg="#3a3a3a")
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()