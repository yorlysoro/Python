import re, string, time, sys
__name__="constantes"
class Trabajador(object):
	def __init__(self):
		self.__CI = None
		self.__nombre = None
		self.__apellido = None
		self.__dia = None
		self.__mes = None
		self.__anio = None
		self.__cargo = None
		self.__nInst = None
		self.__CantH = None
		self.__edadH = None
		self.__AfCajaH = None
		self.__anioIngreso = None
		self.__sueldoBase = None
		self.__sueldoNeto = None

	def set_Datos(self, CI=None, fecha=None, nombre=None, apellido=None, cargo=None, nInst=None, CantH=None, edadH=None, AfCajaH=None, anioIngreso=None, sueldoBase=None, sueldoNeto=None):
		self.__CI, self.__nombre, self.__apellido = CI, nombre, apellido
		self.__dia, self.__mes, self.__anio = fecha.split()
		self.__cargo, self.__nInst, self.__CantH = int(cargo), int(nInst), int(CantH)
		self.__edadH, self.__AfCajaH, self.__anioIngreso = edadH, AfCajaH, anioIngreso
		self.__sueldoBase, self.__sueldoNeto = float(sueldoBase), float(sueldoNeto)

	@property
	def get_Datos(self):
		datos = {'Cedula' : self.__CI,
		'Cargo': self.__cargo,
		'nInst': self.__nInst,
		'AfCajaH':self.__AfCajaH,
		'anioIngreso': self.__anioIngreso,
		'sueldoBase':self.__sueldoBase,
		'sueldoNeto': self.__sueldoNeto,
		'dia' : self.__dia,
		'mes': self.__mes,
		'anio': self.__anio}
		return datos
	


UT = 850.00 #Unidades Tributarias
SLM = 1000000.00 #Salario Minimo

#Asignaciones
TSU = 0.10 #TSU
ING = 0.14 #Ingeniero
MAG = 0.18 #Magister
DOC = 0.20 #Doctor

PH = 300*UT #Prima Hogar
PHJ = 15*UT #Prima por Hijos
PAD = 15*UT #Prima por apoyo a la actividad docente
PA = 0.015 #Prima Antiguedad

#Sueldo Base
OB = 2*SLM
ADMIN = 6*SLM
DOCENTES = 7*SLM

#Deducciones
CJA = 0.10 #Caja de ahorro
SSO = 0.04 #Seguro Social
FAOV = 0.01 #Fondo de ahorro obligatorio para la vivienda
PIE = 0.01 #Perdida Involuntaria del empleo

NivelInst = ["Bachiller", "TSU", "Ingeniero", "Magister", "Doctor"]
Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
Cargo = ["Administrativo", "Docente", "Obrero"]

if(sys.platform.startswith("linux")):
	CLS = "clear"
elif(sys.platform.startswith("win32")):
	CLS = "cls"