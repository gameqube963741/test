def click1():
    textvar.set('Pressed the button')

import tkinter as tk

win = tk.Tk()

textvar = tk.StringVar()
button1 = tk.Button(win, textvariable = textvar, command=click1)
textvar.set('button')
button1.pack()
win.mainloop()