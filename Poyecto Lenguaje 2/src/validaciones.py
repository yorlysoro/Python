import re, time, string
__name__ = "validaciones"
class Validaciones(object):

	def fecha(self, fecha):
		validarFecha = re.search("[a-zA-Z%s]" %(string.punctuation), fecha)
		if(validarFecha or fecha == ""):
			return True
		else:
			try:
				dia, mes, anio = fecha.split()
				anioActual = time.strftime("%Y")
				if(dia < "1" or dia > "31" or mes < "1" or mes > "12" or anio < anioActual or anio > anioActual or len(dia) > 2 or len(mes) > 2 or len(anio) > 4 or len(anio) < 4 ):
					return True
				else:
					return False
			except Exception as e:
				return True
	
	def __validar_fecha(self, fecha):
		try:
			result = time.strptime(fecha,"%d%m%Y")
			return False
		except:
			return True

	def Respuestas(self, resp):
		validarResp = re.search("[0-9%s%s]" %(string.punctuation, string.whitespace),resp)
		if(validarResp or resp == "" or len(resp) > 2):
			return " "
		else:
			if(resp == "S" or resp == "SI"):
				return "S"
			elif(resp == "N" or resp == "NO"):
				return "N"
			else:
				return " "

	def validarCedula(self, CI):
		validarCI = re.search("[a-zA-Z%s%s]" % (string.punctuation, string.whitespace), CI)
		if(validarCI or CI == "" or len(CI) < 7):
			return True
		else:
			return False

	def validarNombreApellido(self, cadena):
		validar = re.search("[0-9%s]"%(string.punctuation), cadena)
		if(validar or cadena == "" or len(cadena) < 4):
			return True
		else:
			return False

	def validarAnio(self, anio):
		anioActual = time.strftime("%Y")
		validar = re.search("[a-zA-Z%s%s]" %(string.punctuation, string.whitespace), anio)
		if(anio == "" or validar or len(anio) < 4 or len(anio) > 4 or anio != anioActual ):
			return True
		else:
			return False

	def validarSueldo(self, sueldo):
		validar = re.search("[a-zA-Z%s%s]" %(string.punctuation, string.whitespace), sueldo)
		if(validar or sueldo == ""):
			return 0.00
		else:
			try:
				sueldo = float(sueldo)
				return sueldo
			except:
				return 0.00
	def validarNumero(self, numero):
		validar = re.search("[a-zA-Z%s%s]" %(string.punctuation, string.whitespace), numero)
		if(validar or numero == "" or len(numero) > 2 or numero <= "0"):
			return True
		else:
			try:
				numero = int(numero)
				return False
			except:
				return True
	def validarEdad(self, edad):
		validar = re.search("[a-zA-Z%s%s]" %(string.punctuation, string.whitespace), edad)
		if(validar or edad == "" or len(edad) > 2 or edad <= "0" or edad > "100"):
			return True
		else:
			try:
				edad = int(edad)
				return False
			except:
				return True

	def validarOpcion(self, numero, tipo, cant):
		validar = re.search("[a-zA-Z%s%s]"%(string.punctuation, string.whitespace), numero)
		if(tipo == "nivel"):
			if(validar or numero == "" or len(numero) > 1 or numero <= "0" or numero > "5"):
				return True
			else:
				return False
		elif(tipo == "cargo"):
			if(validar or numero == "" or len(numero) > 1 or numero <= "0" or numero > "3"):
				return True
			else:
				return False
		elif(tipo == "menu"):
			if(validar or numero == "" or len(numero) > 2 or numero <= "0" or numero > str(cant)):
				return True
			else:
				return False