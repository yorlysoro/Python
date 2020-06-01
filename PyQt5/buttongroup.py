#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  buttongroup.py
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
		
		self.buttongroup = QButtonGroup()
		self.buttongroup.setExclusive(False)
		self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
		
		button = QPushButton("Button 1")
		self.buttongroup.addButton(button, 1)
		layout.addWidget(button)
		
		button = QPushButton("Button 2")
		self.buttongroup.addButton(button, 2)
		layout.addWidget(button)
		
	def on_button_clicked(self, id):
		for button in self.buttongroup.buttons():
			if button is self.buttongroup.button(id):
				print("%s was clicked!" % (button.text()))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
