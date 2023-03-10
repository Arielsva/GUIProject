import ttkbootstrap as ttk
from tkinter import *
from .guides.view_guide import View
from .guides.add_guide import Add
from .guides.edit_guide import Edit


class Menu:
    def __init__(self, main:object, /, *args, **kwargs) -> None:
        self.main = main

        for arg, img in zip(args, ['visibility', 'add', 'edit', 'delete',
                               'alarm', 'calendar', 'settings']):
            globals()[img] = arg

        for frame, name in zip(list(*kwargs.values()), ['visibility_frame', 'add_frame', 'edit_frame',
                                                        'delete_frame', 'alarm_frame', 'calendar_frame',
                                                        'settings_frame', 'visual_frame_I', 'visual_frame_II',
                                                        'student_frame', 'class_frame']):
            globals()[name] = frame

        list_edit = (globals()['edit_frame'], globals()['visual_frame_I'],
                     globals()['visual_frame_II'], globals()['student_frame'],
                     globals()['class_frame'])

        view_button = ttk.Button(
            master=self.main,
            image=globals()['visibility'],
            bootstyle='light',
            command=lambda: View(globals()['visibility_frame'])
        ).grid(column=1, row=1, pady=10, padx=14, ipadx=10, ipady=5)
        add_button = ttk.Button(
            master=self.main,
            image=globals()['add'],
            bootstyle='light',
            command=lambda: Add(globals()['add_frame'], globals()['visual_frame_I'], globals()['visual_frame_II'])
        ).grid(column=2, row=1, pady=10, padx=14, ipadx=12, ipady=5)
        edit_button = ttk.Button(
            master=self.main,
            image=globals()['edit'],
            bootstyle='light',
            command=lambda:Edit(*list_edit)
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