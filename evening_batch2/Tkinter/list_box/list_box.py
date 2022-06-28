# =============================================================================
# listbox
# =============================================================================


from tkinter import *

import tkinter as tk

window = Tk()
window.title("school management")
lb = Listbox(window)

lb.insert(1, "student name")
lb.insert(2, "student fathername")
lb.insert(3, "student mothername")
lb.insert(4, "student class")
lb.insert(5, "student marks")
lb.pack()

window.mainloop()


# =============================================================================
# 
# =============================================================================

from tkinter import *

import tkinter as tk

window = Tk()
window.title("school management")
lb = Listbox(window)

lb.insert(1, "idle")
lb.insert(2, "dosa")
lb.insert(3, "poori")
lb.insert(4, "wada")
lb.insert(5, "upma")
lb.pack()

window.mainloop()
