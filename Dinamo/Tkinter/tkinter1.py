#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter.py
#  
#  Copyright 2017 yorlys <yorlys@debian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import tkinter

class Application(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()
	def create_widgets(self):
		self.hi_there = tkinter.Button(self)
		self.hi_there["text"] = "Hello World\n(Click Me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.quit = tkinter.Button(self, text="QUIT", fg="red",
								command=root.destroy)
		self.quit.pack(side="bottom")
	def say_hi(self):
		print("hi there, everyone!")
	
root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
