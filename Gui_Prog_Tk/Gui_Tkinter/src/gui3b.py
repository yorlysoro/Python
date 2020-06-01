import sys
from tkinter import *

widget = Button(None, 
				text='Hello event world',
				command=(lambda: print('hello lambda wordl') or sys.exit()) )

widget.pack()
widget.mainloop()
