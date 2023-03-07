import ttkbootstrap as ttk
from tkinter import *


class Menu:
    def __init__(self, main:object, *args) -> None:
        self.main = main

        menu_frame = ttk.Frame(
            master=self.main
        ).grid(row=1, column=1)

        for arg, img in zip(args, ['visibility', 'add', 'edit', 'delete',
                               'alarm', 'calendar', 'settings']):
            globals()[img] = arg


        view_button = ttk.Button(
            master=menu_frame,
            image=globals()['visibility'],
            bootstyle='success',
            command=lambda: print('ok')
        ).grid(column=1, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        add_button = ttk.Button(
            master=menu_frame,
            image=globals()['add'],
            bootstyle='success',
        ).grid(column=2, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        edit_button = ttk.Button(
            master=menu_frame,
            image=globals()['edit'],
            bootstyle='success',
        ).grid(column=3, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        delete_button = ttk.Button(
            master=menu_frame,
            image=globals()['delete'],
            bootstyle='success',
        ).grid(column=4, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        time_button = ttk.Button(
            master=menu_frame,
            image=globals()['alarm'],
            bootstyle='success',
        ).grid(column=5, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        calendar_button = ttk.Button(
            master=menu_frame,
            image=globals()['calendar'],
            bootstyle='success',
        ).grid(column=6, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        config_button = ttk.Button(
            master=menu_frame,
            image=globals()['settings'],
            bootstyle='success',
        ).grid(column=7, row=1, pady=10, padx=14, ipadx=13, ipady=5)



    
    
    
    pass
