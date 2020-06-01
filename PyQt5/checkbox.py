#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  checkbox.py
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
		
		layout = QGridLayout()
		self.setLayout(layout)
		
		self.checkbox1 = QCheckBox("Kestrel")
		self.checkbox1.setChecked(True)
		self.checkbox1.toggled.connect(self.checkbox_toggled)
		layout.addWidget(self.checkbox1, 0, 0)
		
		self.checkbox2 = QCheckBox("Sparrowhawk")
		self.checkbox2.toggled.connect(self.checkbox_toggled)
		layout.addWidget(self.checkbox2, 1,0)
		
		self.checkbox3 = QCheckBox("Hobby")
		self.checkbox3.toggled.connect(self.checkbox_toggled)
		layout.addWidget(self.checkbox3, 2, 0)
		
	def checkbox_toggled(self):
		
		selected = []
		
		if self.checkbox1.isChecked():
			selected.append("Kestrel")
			
		if self.checkbox2.isChecked():
			selected.append("Sparrowhawk")
			
		if self.checkbox3.isChecked():
			selected.append("Hobby")
			
		print("Selected: %s" % (" ".join(selected)))
		
app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
