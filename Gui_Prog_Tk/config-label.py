from tkinter import *

root = Tk()
labelfont = ('times', 20, 'bold italic underline')
widget = Label(root, text='Hello config world')
widget.config(bg='#af4e12', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
