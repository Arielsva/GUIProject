import ttkbootstrap as ttk
from tkinter import *
from menu.menu import Menu
from PIL import Image, ImageTk
from images.img import *

class App:

    global root
    root = ttk.Window()

    visibility = ImageTk.PhotoImage(Image.open(visibility_img))
    add = ImageTk.PhotoImage(Image.open(add_img))
    edit = ImageTk.PhotoImage(Image.open(edit_img))
    delete = ImageTk.PhotoImage(Image.open(delete_img))
    alarm = ImageTk.PhotoImage(Image.open(alarm_img))
    calendar = ImageTk.PhotoImage(Image.open(calendar_img))
    settings = ImageTk.PhotoImage(Image.open(settings_img))

    img_list = (visibility, add, edit, delete, alarm, calendar, settings)

    style = ttk.Style(theme='darkly')

    IMAGE_LABEL = Label(
        master=root
    ).grid(column=0, row=0, padx=50)

    #MenuFrames
    
    visibility_frame = ttk.Frame(
        master=root,
        # bootstyle='light'
    )

    GERENCIAR_BUTTON = ttk.Button(
            master=root,
            text='GERENCIAR',
            bootstyle='light-outline-toolbutton',
            state='focus',
            command=lambda: print('OK')
        )
    GERENCIAR_BUTTON.grid(column=1, row=0, padx=10, pady=5, ipadx=60,columnspan=2)

    MENU_BUTTON = ttk.Button(
        master=root,
        text='MENU',
        bootstyle='light-outline-toolbutton',
        command=lambda: Menu(root, App.visibility_frame, *App.img_list)
        )
    MENU_BUTTON.grid(column=3, row=0, padx=50, pady=5, ipadx=80, columnspan=3)

    FINANCEIRO_BUTTON = ttk.Button(
        master=root,
        text='FINANCEIRO',
        bootstyle='light-outline-toolbutton',
        command=lambda: print('OK')
        )
    FINANCEIRO_BUTTON.grid(column=6, row=0, padx=10, pady=5, ipadx=60, columnspan=2)

root.mainloop()

