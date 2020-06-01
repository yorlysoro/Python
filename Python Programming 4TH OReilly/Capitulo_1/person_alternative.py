#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  person_alternative.py
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
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)
	def __str__(self):
		return ('<%s => %s: %s, %s>' %( \
		self.__class__.__name__, self.name, self.job, self.pay))
		

class Manager(Person):
	def __init__(self, name, age, pay):
		Person.__init__(self, name, age, pay, 'manager')
	def giveRaise(self, percent, bonus=0.1):
		Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
	bob = Person('Bob Smith', 44)
	sue = Person('Sue Jones', 47, 40000, 'hardware')
	tom = Manager(name='Tom Due', age=50, pay=50000)
	print(sue, sue.pay, sue.lastName())
	for obj in (bob, sue, tom):
		obj.giveRaise(.10)
		print(obj)
