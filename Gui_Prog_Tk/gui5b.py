from gui5 import HelloButton

class MyButton(HelloButton):
	def callback(self):
		print('Ignoring Press!...')

MyButton(None, text='Hello subclass world').mainloop()
