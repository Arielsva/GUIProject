import ttkbootstrap as ttk
from tkinter import *

class View:
    def __init__(self, frame:object) -> None:
        self.main = frame

        self.main.grid(column=0, row=2, columnspan=8, sticky=NSEW)

        student_tree = ttk.Treeview(
            master=self.main,
        ).grid(column=0, row=0, padx=10, ipadx=220, rowspan=3, sticky=NSEW, pady=3)

        expand_tree = ttk.Button(
            master=self.main,
            bootstyle='solid-toolbutton'
        ).grid(column=1, row=0, ipadx=4, sticky=W, pady=3)

        search_tree = ttk.Entry(
            master=self.main,
        ).grid(column=1, row=0, ipadx=20, sticky=E, pady=3)

        search_menubutton = ttk.Menubutton(
            master=self.main,
        ).grid(column=1, row=1, sticky=NSEW, pady=3)

        class_tree = ttk.Treeview(
            master=self.main,
        ).grid(column=1, row=2, pady=3)