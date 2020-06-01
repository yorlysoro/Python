#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  manager.py
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
from person import Person

class Manager(Person):
	def giveRaise(self, percent, bonus=0.1):
		self.pay *= (1.0 + percent + bonus)
	
	
if __name__ == '__main__':
	tom = Manager(name="Tom Doe", age=50, pay=50000)
	print(tom.lastName())
	tom.giveRaise(.20)
	print(tom.pay)
