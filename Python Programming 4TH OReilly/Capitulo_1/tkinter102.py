#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tkinter102.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
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
from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		button = Button(self, text='press', command=self.reply)
		button.pack()
	def reply(self):
		showinfo(title='popup', message='Button pressed!')
	
	
if __name__ == '__main__':
	window = MyGui()
	window.pack()
	window.mainloop()
