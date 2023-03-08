import ttkbootstrap as ttk
from tkinter import *
from menu.menu import Menu
from PIL import Image, ImageTk
from images.img import *

class App:

    global root
    root = ttk.Window()

    style = ttk.Style(theme='darkly')

    IMAGE_LABEL = Label(
        master=root
    ).grid(column=0, row=0, padx=50)
    
    buttons_menu_frame = ttk.Frame(
        master=root,
        # bootstyle='light'
    )


class MainManage(App):

    MANAGE_BUTTON = ttk.Button(
            master=root,
            text='GERENCIAR',
            bootstyle='light-outline-toolbutton',
            state='focus',
            command=lambda: print('OK')
        )
    MANAGE_BUTTON.grid(column=1, row=0, padx=10, pady=5, ipadx=60,columnspan=2)


class MainMenu(App):

    visibility = ImageTk.PhotoImage(Image.open(visibility_img))
    add = ImageTk.PhotoImage(Image.open(add_img))
    edit = ImageTk.PhotoImage(Image.open(edit_img))
    delete = ImageTk.PhotoImage(Image.open(delete_img))
    alarm = ImageTk.PhotoImage(Image.open(alarm_img))
    calendar = ImageTk.PhotoImage(Image.open(calendar_img))
    settings = ImageTk.PhotoImage(Image.open(settings_img))

    img_list = (visibility, add, edit, delete, alarm, calendar, settings)

    visibility_frame = ttk.Frame(master=root)
    add_frame = ttk.Frame(master=root)
    edit_frame = ttk.Frame(master=root)
    delete_frame = ttk.Frame(master=root)
    alarm_frame = ttk.Frame(master=root)
    calendar_frame = ttk.Frame(master=root)
    settings_frame = ttk.Frame(master=root)

    visual_frame = ttk.Frame(master=root)

    frame_list = (visibility_frame, add_frame, edit_frame, delete_frame,
                  alarm_frame, calendar_frame, settings_frame, visual_frame)
    
    MENU_BUTTON = ttk.Button(
        master=root,
        text='MENU',
        bootstyle='light-outline-toolbutton',
        command=lambda: Menu(root, *MainMenu.img_list, **{'list':MainMenu.frame_list})
        )
    MENU_BUTTON.grid(column=3, row=0, padx=50, pady=5, ipadx=80, columnspan=3)


class MainFinancial(App):

    FINANCEIRO_BUTTON = ttk.Button(
        master=root,
        text='FINANCEIRO',
        bootstyle='light-outline-toolbutton',
        command=lambda: print('OK')
        )
    FINANCEIRO_BUTTON.grid(column=6, row=0, padx=10, pady=5, ipadx=60, columnspan=2)



if __name__ == '__main__':
        root.mainloop()