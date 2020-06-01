#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  record.py
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
import warnings

class metaMetaBunch(type):
	def __new__(cls, classname, bases, classdict):
	
		def __init__(self, **kw):
			for k in self.__dflts__: 
				setattr(self, k, self.__dflts__[k])
			for k in kw: 
				setattr(self, k, kw[k])
		def __repr__(self):
			rep = ['%s = %r' % (k, getattr(self,k)) for k in self.__dflts__
			if getattr(self,k) != self.__dflts__[k]]
			return '%s(%s)' % (classname, ', '.join(rep))
			
			newdict = {'__slots__':[], '__dflts__':{}, '__init__':__init__,'__rep__':__repr__}
			
			for k in classdict:
				if k.startswith('__'):
					if k in newdict:
						warnings.warn("can't set attr %r in bunch-class %r" %(k, classname))
					else:
						newdict[k] = classdict[k]
				else:
					newdict['__slots__'].append(k)
					newdict['__dflts__'][k] = classdict[k]
				return type.__new__(cls, classname, bases, newdict)
			
class record(object):
	__metaclass__ = metaMetaBunch
	
if __name__ == "__main__":
	  class Point(record):
		  x = 0.0
		  y = 0.0
		  color = 'gray'
		  
		q = Point()
		return q
		
		p = Point(x = 1.2, y = 3.4)
		print p
		
		r = Point(x = 2.0, color = 'blue')
		print r
		print r.x, r.y


