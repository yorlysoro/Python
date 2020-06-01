#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  peopleinteract_update.py
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
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
	key = input('\nKey? => ')
	if not key: break
	if key in db:
		record = db[key]
	else:
		record = Person(name = '?', age='?')
	for field in fieldnames:
		currval = getattr(record, field)
		newtext = input('\t[%s] = %s\n\t\tnew?=>' %(field, currval))
		if newtext:
			setattr(record, field, eval(newtext))
	db[key] = record
db.close()
