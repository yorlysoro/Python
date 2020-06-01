#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  person_start.py
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
class Person(object):
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
		

if __name__ == '__main__':
	bob = Person('Bob Smith', 42, 30000, 'software')
	sue = Person('Sue Jones', 45, 40000, 'hardware')
	print(bob.name, sue.pay)
	
	print(bob.name.split()[-1])
	sue.pay *= 1.10
	print(sue.pay)
