import ttkbootstrap as ttk
from tkinter import *

class Add:
    def __init__(self, frame:object, visual_frame_I:object, visual_frame_II:object) -> None:
        self.main = frame

        self.complement = visual_frame_I
        self.options = visual_frame_II

        self.complement = ttk.Frame(master=self.main)
        self.options = ttk.Frame(master=self.main)

        self.main.grid(column=0, row=2, columnspan=7, sticky=NSEW)

        self.complement.grid(column=0, row=0, sticky=NSEW)

        
        name_entry = ttk.Entry(
            master=self.complement,

            ).grid(column=0, row=0, padx=30, pady=10, ipadx=170, columnspan=2, sticky=EW)

        email_entry = ttk.Entry(
            master=self.complement,

        ).grid(column=0, row=1, padx=30, pady=10, ipadx=170, columnspan=2, sticky=EW)
        
        phone_entry = ttk.Entry(
            master=self.complement,

        ).grid(column=0, row=2, padx=30, pady=10, sticky=EW)

        id_view = ttk.Entry(
            master=self.complement,
            state='readonly',
            width=5
        ).grid(column=1, row=2, pady=10)

        cancel_button = ttk.Button(
            master=self.complement,
            text='CANCELAR',
            command=lambda: clear_grid(self)
        ).grid(column=0, row=3, padx=20, pady=10, sticky=E)

        add_button = ttk.Button(
            master=self.complement,
            text='ADICIONAR'
        ).grid(column=1, row=3, padx=20, pady=10, sticky=W)
        
        
        #

        self.options.configure(bootstyle='secondary')
        self.options.grid(column=1, row=0, padx=50, stick=NSEW)


        class_button = ttk.Menubutton(
            master=self.options,
            bootstyle='light'
        ).grid(column=0, row=0, padx=10, pady=10, ipadx=10, columnspan=2, sticky=EW)     

        id_button = ttk.Checkbutton(
            master=self.options,
            bootstyle='dark',
            text='ID'
        ).grid(column=0, row=1, pady=5)

        level_state_button = ttk.Checkbutton(
            master=self.options,
            bootstyle='dark',
            text='NÍVEL'
        ).grid(column=1, row=1, pady=5)

        level_button = ttk.Menubutton(
            master=self.options,
            bootstyle='light'
        ).grid(column=0, row=2, padx=10, pady=10, ipadx=10, columnspan=2, sticky=EW)

        date_entry = ttk.DateEntry(
            master=self.options,
            bootstyle='default'
        ).grid(column=0, row=3, padx=10, pady=10, ipadx=27, columnspan=2, sticky=EW)

        def clear_grid(self):
            self.complement.grid_remove()
            self.options.grid_remove()