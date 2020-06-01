from tkinter import *
from tkinter.messagebox import *

def callback():
	if askyesno('Verificar', 'Desea salir?'):
		showwarning('Si', 'Salir no implementado')
	else:
		showinfo('No', 'Salida cancelada')

errmsg = 'Sorry, no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('spam', errmsg))).pack(fill=X)
mainloop()
