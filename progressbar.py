from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('200x200')

progress = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate')

def bar():
    import time
    progress['value'] = 20 #shows 20% progress
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 25
    root.update_idletasks()
    time.sleep(1.25)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 59
    root.update_idletasks()
    time.sleep(0.25)

    progress['value'] = 63
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 84
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    root.update_idletasks()


progress.pack(pady = 50)
Button(root, text = 'Start', command= bar).pack(pady = 10)
root.mainloop()
