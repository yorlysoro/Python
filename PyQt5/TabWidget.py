#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TabWidget.py
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
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		
		layout = QGridLayout()
		self.setLayout(layout)
		
		label1 = QLabel("Example content contained in a tab.")
		label2 = QLabel("More example text in the second tab.")
		
		tabwidget = QTabWidget()
		tabwidget.addTab(label1, "Tab 1")
		tabwidget.addTab(label2, "Tab 2")
		layout.addWidget(tabwidget, 0, 0)
	
	
app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
