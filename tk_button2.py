def clickme():
    global count
    count += 1
    labeltext.set("click " + str(count) + " 次了！")
    if(btntext.get() == "click me！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("click me！")

import tkinter as tk

win = tk.Tk()
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg="red", textvariable=labeltext)
labeltext.set("welcome Tkinter！")
label1.pack()
button1 = tk.Button(win, textvariable=btntext, command=clickme)
btntext.set("click me！")
button1.pack()
win.mainloop()