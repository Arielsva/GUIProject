import ttkbootstrap as ttk
from tkinter import *
from .add_guide import Add

class Edit(Add):
    def __init__(self, *args) -> None:
        
        for frame, name in zip(args, ['edit_frame', 'visual_frame_I',
                                      'visual_frame_II', 'student_frame',
                                      'class_frame']):
            globals()[name] = frame


        self.main = globals()['edit_frame']
        self.complement = globals()['visual_frame_I']
        self.options = globals()['visual_frame_II']
        self.student = globals()['student_frame']
        self.class_f = globals()['class_frame']

        self.main.grid(column=0, row=2, columnspan=7, sticky=NSEW)

        self.student.grid(column=0, row=1, columnspan=7, stick=NSEW)

        self.class_f.grid(column=0, row=1, columnspan=7, sticky=NSEW)

        def invoke(self):
            return super().__init__(frame=self.student, visual_frame_I=self.complement,
                                    visual_frame_II=self.options)


        def student(self):
            invoke(self)

            self.complement.grid(column=0, row=0, columnspan=5, sticky=NSEW)
            self.options.grid(column=5, row=0, columnspan=3, padx=50, pady=10, stick=NSEW)


        option_menu = ttk.Menu()

        option_menu.add_command(
            label='ALUNO(A)',
            command=lambda: student(self)
        )

        edit_option_menu = ttk.Menubutton(
            master=self.main,
            text='OPÇÃO',
            direction='below',
            menu=option_menu
        ).grid(column=0, row=0, ipadx=30, padx=10, pady=5, sticky=W)




