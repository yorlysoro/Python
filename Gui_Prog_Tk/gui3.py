import sys
from tkinter import *

def quit():
	print('Hello, I must be going...')
	sys.exit()
	
widget = Button(None, text='Hello event World', command=quit)
widget.pack()
widget.mainloop()
