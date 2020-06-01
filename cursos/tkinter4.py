import sys
from Tkinter import *

def hacer_click():
	try:
		__valor = int(entrada_txt.get())
		__valor = __valor*10
		etiqueta.config(text=__valor)
	except ValueError:
		etiqueta.config(text='Introduce un numero!')
	

app = Tk()
app.title("Mi primera ventana")
vp = Frame(app)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta = Label(vp,text="Escribe algo:")
etiqueta.grid(column=1,row=1)

boton = Button(vp,text="Click!",command=hacer_click)
boton.grid(column=2,row=2)

valor=""
entrada_txt = Entry(vp,width=10,textvariable=valor)
entrada_txt.grid(column=3,row=1)

app.mainloop()
