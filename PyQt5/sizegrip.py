#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sizegrip.py
#  
#  Copyright 2019 yorlysoro <yorlysoro@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#  
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("GroupBox")
		
		layout = QGridLayout()
		self.setLayout(layout)
		
		groupbox = QGroupBox("GroupBox Example")
		groupbox.setCheckable(True)
		layout.addWidget(groupbox)
		
		vbox = QVBoxLayout()
		groupbox.setLayout(vbox)
		
		radiobutton = QRadioButton("RadioButton 1")
		radiobutton.setChecked(True)
		vbox.addWidget(radiobutton)
		radiobutton = QRadioButton("RadioButton 2")
		vbox.addWidget(radiobutton)
		
		sizegrip = QSizeGrip(self)
		vbox.addWidget(sizegrip)
		
app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
