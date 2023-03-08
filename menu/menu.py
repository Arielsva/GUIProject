import ttkbootstrap as ttk
from tkinter import *
from .guides.view_guide import View

class Menu:
    def __init__(self, main:object, frame:object, *args) -> None:
        self.main = main
        self.frame = frame

        for arg, img in zip(args, ['visibility', 'add', 'edit', 'delete',
                               'alarm', 'calendar', 'settings']):
            globals()[img] = arg


        view_button = ttk.Button(
            master=self.main,
            image=globals()['visibility'],
            bootstyle='light',
            command=lambda: View(self.frame)
        ).grid(column=1, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        add_button = ttk.Button(
            master=self.main,
            image=globals()['add'],
            bootstyle='light',
        ).grid(column=2, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        edit_button = ttk.Button(
            master=self.main,
            image=globals()['edit'],
            bootstyle='light',
        ).grid(column=3, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        delete_button = ttk.Button(
            master=self.main,
            image=globals()['delete'],
            bootstyle='light',
        ).grid(column=4, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        time_button = ttk.Button(
            master=self.main,
            image=globals()['alarm'],
            bootstyle='light',
        ).grid(column=5, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        calendar_button = ttk.Button(
            master=self.main,
            image=globals()['calendar'],
            bootstyle='light',
        ).grid(column=6, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        config_button = ttk.Button(
            master=self.main,
            image=globals()['settings'],
            bootstyle='light',
        ).grid(column=7, row=1, pady=10, padx=14, ipadx=13, ipady=5)