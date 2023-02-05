from PIL import Image, ImageTk

class RoundButton:
    
    def __init__(self, FRONT:str, DEFAULT:str, PRESSED:str, BUTTON):
        self.FRONT:str = FRONT
        self.DEFAULT:str = DEFAULT
        self.PRESSED:str = PRESSED
        self.button = BUTTON

        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)
        self.button.bind("<ButtonPress>", self.to_press)
        # self.button.bind("<ButtonRelease-1>", self.on_enter)
        # self.button.bind("<ButtonPress>", self.to_press(any))

    def on_enter(self, event):
        self.frame = ImageTk.PhotoImage(Image.open(self.FRONT))
        self.button['image'] = self.frame

    def on_leave(self, event):
        self.frame = ImageTk.PhotoImage(Image.open(self.DEFAULT))
        self.button['image'] = self.frame

    def to_press(self, event):
        self.frame = ImageTk.PhotoImage(Image.open(self.PRESSED))
        self.button['image'] = self.frame