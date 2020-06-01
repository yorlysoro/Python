from tkinter import *
from dialogTable import demos
from Quitter import Quitter

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text="Basic Demos").pack()
		for (key, value) in demos.items():
			Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
		Quitter(self).pack(side=TOP, fill=BOTH)
		
Demo().mainloop()
