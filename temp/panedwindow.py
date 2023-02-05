from tkinter import *

m1 = PanedWindow(background='grey', sashpad=10, width=400)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane", background='grey')
m1.add(left)

m2 = PanedWindow(orient=VERTICAL, background='grey20')
m1.add(m2)

top = Label(m2, text="top pane", background='grey20')
m2.add(top)

bottom = Label(m2, text="bottom pane", background='grey40')
m2.add(bottom)

mainloop()