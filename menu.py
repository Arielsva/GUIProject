import ttkbootstrap as ttk
from tkinter import *


class Menu:
    def __init__(self, main:object, button:object) -> None:
        self.main = main
        self.button = button

        view_button = ttk.Button(
            master=self.main,
        ).grid(column=0, row=1, pady=10, ipadx=10, ipady=4)
        add_button = ttk.Button(
            master=self.main,
        ).grid(column=1, row=1, pady=10, ipadx=10, ipady=4)
        edit_button = ttk.Button(
            master=self.main,
        ).grid(column=2, row=1, pady=10, ipadx=10, ipady=4)
        delete_button = ttk.Button(
            master=self.main,
        ).grid(column=3, row=1, pady=10, ipadx=10, ipady=4)
        time_button = ttk.Button(
            master=self.main,
        ).grid(column=4, row=1, pady=10, ipadx=10, ipady=4)
        calendar_button = ttk.Button(
            master=self.main,
        ).grid(column=5, row=1, pady=10, ipadx=10, ipady=4)
        config_button = ttk.Button(
            master=self.main,
        ).grid(column=6, row=1, pady=10, ipadx=10, ipady=4)



    
    
    
    pass