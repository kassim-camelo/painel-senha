"""a = input("ASSUNTO")
b = input("PRIORIDADE")
c = '001'

print(f"{a.upper()}-{b.upper()}{c}")"""


"""from tkinter import *
from tkinter import ttk
root = Tk()
root.state('zoomed')
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)
ttk.Label(frm, text="Hello World!").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=1)
root.mainloop()"""

from tkinter import Tk, Label, Frame

root = Tk()

my_frame = Frame(root, bg="#f0f0f0", width=200, height=100, padx=10, pady=10)
my_frame.pack()

my_label = Label(my_frame, text="Hello, World!", font=("Arial", 16), fg="blue")
my_label.pack()

root.mainloop()

