#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  moreplus.py
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
import sys

def getreply():
	if sys.stdin.isatty():
		return input('?')
	else:
		if sys.platform[:3] == 'win':
			import msvcrt
			msvcrt.putch(b'?')
			key = msvcrt.getche()
			msvcrt.putch(b'\n')
			return key
		else:
			assert False, 'Platform not supported'
			#linux?: open('/dev/tty').readline()[:-1]

def more(text, numlines=10):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk: print(line)
		if lines and getreply() not in [b'y', b'Y']: break
		
if __name__ == '__main__':
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())
