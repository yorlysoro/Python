#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
	global entries
	window = Tk()
	window.title('People Shelve')
	form = Frame(window)
	form.pack()
	entries = {}
	for(ix, label) in enumerate(('key',)+fieldnames):
		lab = Label(form, text=label)
		ent = Entry(form)
		lab.grid(row=ix, column=0)
		ent.grid(row=ix, column=1)
		entries[label] = ent
	Button(window, text="Fetch", command=fetchRecord).pack(side=LEFT)
	Button(window, text="Update", command=updateRecord).pack(side=LEFT)
	Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
	return window
	
def fetchRecord():
	key = entries['key'].get()
	try:
		record = db[key]
	except:
		showerror(title='Error', message='No such key!')
	else:
		for field in fieldnames:
			entries[field].delete(0, END)
			entries[field].insert(0, repr(getattr(record, field)))
			
def updateRecord():
	key = entries['key'].get()
	if key in db:
		record = db[key]
	else:
		from person import Person
		record = Person(name='?', age='?')
	for field in fieldnames:
		setattr(record, field, eval(entries[field].get()))
	db[key] = record
	
db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()
			