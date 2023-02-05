import ttkbootstrap as ttk
from tkinter import *
from PIL import Image, ImageTk
from roundbutton import RoundButton
from images.LISTA import *
from menu import Menu

class App:

    global root
    root = ttk.Window(themename='solar')
    # root.geometry('500x400')

    GERENCIAR_D = ImageTk.PhotoImage(Image.open(GERENCIAR_DEFAULT))
    MENU_D = ImageTk.PhotoImage(Image.open(MENU_DEFAULT))
    FINANCEIRO_D = ImageTk.PhotoImage(Image.open(FINANCEIRO_DEFAULT))

    IMAGE_LABEL = Label(
        master=root
    ).grid(column=0, row=0, padx=30)


    GERENCIAR_BUTTON = Button(
            master=root,
            image=GERENCIAR_D,
            autostyle=False,
            border=0,
            background='#002B36',
            activebackground='#002B36',
            command=lambda: print('OK')
        )

    RoundButton(GERENCIAR_FRONT, GERENCIAR_DEFAULT, GERENCIAR_PRESSED, GERENCIAR_BUTTON)
    GERENCIAR_BUTTON.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

    MENU_BUTTON = Button(
        master=root,
        image=MENU_D,
        autostyle=False,
        border=0,
        background='#002B36',
        activebackground='#002B36',
        command=lambda: Menu(root, App.MENU_BUTTON)
        )
    
    RoundButton(MENU_FRONT, MENU_DEFAULT, MENU_PRESSED, MENU_BUTTON)
    MENU_BUTTON.grid(column=3, row=0, padx=10, pady=5, columnspan=2)
    # MENU_BUTTON.

    FINANCEIRO_BUTTON = Button(
        master=root,
        image=FINANCEIRO_D,
        autostyle=False,
        border=0,
        background='#002B36',
        activebackground='#002B36',
        command=lambda: print('OK')
        )
    
    RoundButton(FINANCEIRO_FRONT, FINANCEIRO_DEFAULT, FINANCEIRO_PRESSED, FINANCEIRO_BUTTON)
    FINANCEIRO_BUTTON.grid(column=5, row=0, padx=10, pady=5, columnspan=2)

root.mainloop()

class Gerenciar:
    pass