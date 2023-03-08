import ttkbootstrap as ttk
from tkinter import *

class Add:
    def __init__(self, frame:object, visual_frame:object) -> None:
        self.main = frame
        self.options = visual_frame

        self.main.configure(width=400, height=200)
        self.main.grid(column=0, row=2, columnspan=5, sticky=NSEW)

        
        name_entry = ttk.Entry(
            master=self.main,

            ).grid(column=0, row=0, padx=30, pady=10, ipadx=170, columnspan=2, sticky=EW)

        email_entry = ttk.Entry(
            master=self.main,

        ).grid(column=0, row=1, padx=30, pady=10, ipadx=170, columnspan=2, sticky=EW)
        
        phone_entry = ttk.Entry(
            master=self.main,

        ).grid(column=0, row=2, padx=30, pady=10, sticky=EW)

        id_view = ttk.Entry(
            master=self.main,
            state='readonly',
            width=5
        ).grid(column=1, row=2, pady=10)

        cancel_button = ttk.Button(
            master=self.main,
            text='CANCELAR'
        ).grid(column=0, row=3, padx=20, pady=10, sticky=E)

        add_button = ttk.Button(
            master=self.main,
            text='ADICIONAR'
        ).grid(column=1, row=3, padx=20, pady=10, sticky=W)
        
        
        #

        self.options.configure(bootstyle='secondary')
        self.options.grid(column=5, row=2, columnspan=3, padx=50, pady=10, stick=NSEW)


        class_button = ttk.Menubutton(
            master=self.options,
            bootstyle='light'
        ).grid(column=0, row=0, padx=10, pady=10, ipadx=10, columnspan=2, sticky=EW)     

        id_button = ttk.Checkbutton(
            master=self.options,
            bootstyle='warning',
            text='ID'
        ).grid(column=0, row=1, pady=5)

        level_state_button = ttk.Checkbutton(
            master=self.options,
            bootstyle='warning',
            text='NÍVEL'
        ).grid(column=1, row=1, pady=5)

        level_button = ttk.Menubutton(
            master=self.options,
            bootstyle='light'
        ).grid(column=0, row=2, padx=10, pady=10, ipadx=10, columnspan=2, sticky=EW)

        date_entry = ttk.DateEntry(
            master=self.options,
            bootstyle='warning'
        ).grid(column=0, row=3, padx=10, pady=10, ipadx=27, columnspan=2, sticky=EW)

        
