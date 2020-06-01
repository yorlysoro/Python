#!/usr/bin/env python2
import sys
from Tkinter import *

raiz = Tk()
raiz.title("Mi Primera ventana")
etiqueta = Label(raiz,text="Hola mundo!")
boton = Button(raiz,text="Click!")
etiqueta.pack()
boton.pack()
raiz.mainloop()
