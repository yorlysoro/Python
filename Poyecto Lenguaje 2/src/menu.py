from validaciones import Validaciones
from archivos import crearRecibo, LeeArchivo, eliminarArchivo, borraRegistro, existeArchivo, existeTrabajador, extraeRecibo
from cola import Cola, encolar, crearFifo
from constantes import CLS, Trabajador, Meses, OB, ADMIN, DOCENTES
from asignaciones import calculaPrimaProf,calculaPrimaHog,calculaPrimaHij, calculaActiDocen, calculaPrimaAnti
from deducciones import calculaDescuentaA, calculaSSO, calculaFAOV, calculaPIE
from os import system
import re, time
__name__ = "menu"
def menu(op):
	print("""
						SISTEMA ADMINISTRATIVO UNEFA
		1).-CREAR RECIBO
		2).-MOSTRAR UN RECIBO
		3).-ELIMINAR UN RECIBO
		4).-MOSTRAR NOMINA
		5).-MOSTRAR TOTAL COBRADO POR TRABAJADOR
		6).-MOSTRAR TOTAL DEBITADO POR TRABAJADOR
		7).-SALIR
		""")
	op = input("Introduzca una opcion: ")
	return op

def mostrarRecibo():
	system(CLS)
	regs = []
	cant = 0
	validar = Validaciones()
	resp = "N"
	if(existeArchivo("../txt/Registro.txt")):
		while(resp == "N"):
			cedula = input("Introduzca la cedula del trabajador: ")
			system(CLS)
			while(validar.validarCedula(cedula) or not existeTrabajador(cedula)):
				print("No existe el trabajador!!!")
				cedula = input("Introduzca la cedula del trabajador: ")
				system(CLS)
			registro = "../txt/"+cedula+".txt"
			with open(registro, "r") as nRegistro:
				for linea in nRegistro:
					if(re.search("%s" %(cedula),linea)):
						regs.append(linea)
						cant = cant + 1
			nRegistro.close()
			regs.append("Salir\n")
			system(CLS)
			if(cant == 0):
				print("Este trabajador no tiene recibos: ")
			else:
				system(CLS)
				print("				RECIBOS DEL TRABAJADOR")
				i = 1
				for recibo in regs:
					print("		",i,".",recibo, end='')
					i = i + 1
				op = input("Introduzca una opcion: ")
				while(validar.validarOpcion(op, "menu", cant)):
					print("Opcion Incorrecta!!!")
					op = input("Introduzca una opcion: ")
				op = int(op)
				if(op-1 == cant):
					return
				for i in range(cant):
					if(i == op-1):
						break
				LeeArchivo("../txt/"+regs[op-1]+".txt")
				resp = input("VOLVER(S/N): ")
				resp = validar.Respuestas(resp)
				while (resp != "S" or resp != "N"):
					print("Error!")
					resp = input("VOLVER(S/N): ")
					resp = validar.Respuestas(resp)
			system(CLS)
	else:
		system(CLS)
		input("Aun no ha registrado recibos!!!")
		
def eliminarRecibo():
	regs = []
	cant = 0
	resp = "N"
	validar = Validaciones()
	reps == "N"
	if(existeArchivo("../txt/Registro.txt")):
		while (resp == "N"):
			cedula = input("Introduzca la cedula del trabajador: ")
			while (validar.validarCedula(cedula) or not existeTrabajador(cedula)):
				print("Error cedula Incorrecta!!!")
				cedula = input("Introduzca la cedula del trabajador: ")
			registro = "../txt/"+cedula+".txt"
			with open(registro, "r") as nRegistro:
				for linea in nRegistro:
					regs.append(linea)
					cant = cant + 1
			nRegistro.close()
			regs.append("Eliminar Todos\n")
			cant = cant + 1
			regs.append("Salir\n")
			system(CLS)
			if(cant == 1):
				input("El trabajador no tiene recibos guardados")
				return
			else:
				print("					RECIBOS DEL TRABAJADOR")
				i = 1
				for recibo in regs:
					print("		", i, ".-", recibo, end='')
					i = i+1
				op = input("Introduzca una opcion: ")
				while (validar.validarOpcion(op, "menu", cant)):
					print("Opcion Incorrecta!!!")
					op = input("Introduzca una opcion: ")
				op = int(op)
				if(op-1 == cant):
					return
				elif(op-1 == cant - 1):
					resp = "Desea realizar esta accion? (S/N): "
					resp = validar.Respuestas(resp)
					while (resp != "S" or resp != "N"):
						print("Error!!")
						resp = input("Solo (S/N): ")
						resp = validar.Respuestas(resp)
					if(resp == "S"):
						print("Eliminando todos los registros")
						for recibo in regs:
							if(recibo != regs[cant-1]):
								eliminarArchivo("../txt/"+recibo+".txt")
								borraRegistro("../txt/"+cedula+".txt", recibo)
						eliminarArchivo("../txt/"+cedula+"2"+".txt")
						system(CLS)
						input("Registros eliminados")
						return
					else:
						system(CLS)
						input("Accion cancelada!!")
						return
				else:
					for i in range(cant):
						if(i == op-1):
							resp = input("Desea realizar esta accion? (S/N): ")
							resp = validar.Respuestas(resp)
							while (resp != "S" or resp !="N"):
								print("Error!!!")
								resp = input("Desea realizar esta accion? (S/N): ")
								resp = validar.Respuestas(resp)
							if(resp == "S"):
								eliminarArchivo("../txt/"+regs[op-1]+".txt")
								borraRegistro("../txt/"+regs[op-1]+".txt")
								if(cant < 4):
									eliminarArchivo("../txt/"+cedula+"2"+".txt")
								input("Registro eliminado!!!")
								return
							else:
								input("Accion cancelada!!!")
								return
	else:
		system(CLS)
		input("Aun no ha registrado un recibo!!!")



def mostrarNomina():
	system(CLS)
	if(existeArchivo("../txt/Nomina.txt")):
		LeeArchivo("../txt/Nomina.txt")
		input()
	else:
		input("Aun no ha registrado un trabajador")
	system(CLS)

def totalDeducciones():
	system(CLS)
	if(existeArchivo("../txt/IVSS.txt")):
		LeeArchivo("../txt/IVSS.txt")
		input()
	else:
		input("Aun no ha registrado un trabajador")

def totalCobrado():
	system(CLS)
	if(existeArchivo("../txt/FIFO.txt")):
		LeeArchivo("../txt/FIFO.txt")
		input()
	else:
		input("Aun no ha registrado un trabajador")

def crearRecibo():
	anioActual = time.strftime("%Y")
	resp = "N"
	validar = Validaciones()
	cola = Cola()
	trabajador = Trabajador()
	resp = "S"
	system(CLS)
	while (resp == "S"):
		system(CLS)
		cedula = input("Introduzca la cedula del Trabajador: ")
		while (validar.validarCedula(cedula)):
			print("Cedula Incorrecta!!")
			cedula = input("Introduzca la cedula del trabajador: ")
		fecha = input("Introduzca la fecha de pago: ")
		while (validar.fecha(fecha)):
			print("Error!")
			fecha = input("Introduzca la fecha de pago: ")
		nRecibo = "../txt/"+cedula+"-"+fecha.split()[0]+fecha.split()[1]+fecha.split()[2]
		nRegistro = extraeRecibo("../txt/"+cedula+"2", cedula+Meses[int(fecha.split()[1])-1]+anioActual)
		if(existeArchivo(nRecibo)):
			input("Ya existe un recibo para el numero de cedula!!!")
			crearRecibo()
		elif(nRegistro == cedula+Meses[int(fecha.split()[1])-1]+anioActual):
			input("Ya el trabajador tiene un recibo en el mes de "+Meses[int(fecha.split()[1])-1]+anioActual)
			crearRecibo()
		system(CLS)
		nombre = input("Introduzca su nombre: ")
		while (validar.validarNombreApellido(nombre)):
			print("Error!")
			nombre = input("Introduzca su nombre: ")
		apellido = input("Introduzca su apellido: ")
		while (validar.validarNombreApellido(apellido)):
			print("Error!")
			apellido = input("Introduzca su apellido: ")
		system(CLS)
		nombre = nombre.title()
		apellido = apellido.title()
		print("""	INTRODUZCA SU CARGO
			1.-PERSONAL ADMINISTRATIVO
			2.-PERSONAL DOCENTE
			3.-PERSONAL OBRERO""")
		cargo = input("Introduzca una de las opciones: ")
		while (validar.validarOpcion(cargo, "cargo", None)):
			print("Error!!")
			cargo = input("Introduzca una de la opciones: ")
		print("""	INTRODUZCA SU NIVEL DE INSTRUCCION
			1.-BACHILLER
			2.-TSU
			3.-INGENIERO
			4.-MAGISTER
			5.-DOCTOR
			""")
		nivel = input("Introduzca una de las opciones: ")
		while (validar.validarOpcion(nivel, "nivel", None)):
			print("Error!")
			nivel = input("Introduzca una de las opciones: ")
		resp = input("Posee Hijos? (S/N): ")
		resp = validar.Respuestas(resp)
		while (resp != "S" or resp != "N"):
			resp = input("Solo (S/N): ")
			resp = validar.Respuestas(resp)
		edades = []
		cant = 0
		if(resp == "S"):
			cant = input("Introduzca la cantidad de Hijos: ")
			while (validar.validarNumero(cant)):
				cant = input("Solo numeros: ")
			for i in range(int(cant)):
				edad = input("Introduzca la edad del hijo N° %d: " % (i+1))
				while (validar.validarEdad(edad)):
					edad = input("Introduzca solo numeros: ")
				edades.append(edad)
		
		resp = input("Posee afiliacion a la caja de ahorro? (S/N): ")
		resp = validar.Respuestas(resp)
		while (resp != "S" or resp != "N"):
			resp = input("Solo (S/N): ")
			resp = validar.Respuestas(resp)
		AfCajaH = resp
		anioIngreso = input("Introduzca el año de ingreso a la institucion: ")
		while (validar.validarAnio(anioIngreso)):
			print("Error")
			anioIngreso = input("Introduzca el año de ingreso a la institucion: ")
		sueldoBase = input("Introduzca el sueldo base: ")
		sueldoBase = validar.validarSueldo(sueldoBase)
		if(cargo == "1" and sueldoBase < ADMIN):
			while (validar.validarSueldo(sueldoBase) == 0.00 or validar.validarSueldo(sueldoBase) < ADMIN):
				print("Error!")
				sueldoBase = input("Introduzca el sueldoBase: ")
		elif(cargo == "2" and sueldoBase < DOCENTES):
			while (validar.validarSueldo(sueldoBase) == 0.00 or validar.validarSueldo(sueldoBase)):
				print("Error!")
				sueldoBase = input("Introduzca el sueldoBase: ")
		elif(cargo == "3" and sueldoBase < OB):
			while (validar.validarSueldo(sueldoBase) == 0.00 or validar.validarSueldo(sueldoBase)):
				print("Error!")
				sueldoBase = input("Introduzca el sueldoBase: ")
		sueldoBase = validar.validarSueldo(sueldoBase)
		PrimaAD = 0
		if(cargo == "2"):
			PrimaAD = calculaActiDocen()

		PrimaHij = calculaPrimaHij(edades)
		PrimaProf = calculaPrimaProf(nivel,sueldoBase)
		PrimaA = calculaPrimaAnti(anioIngreso, sueldoBase)
		PrimaH = calculaPrimaHog()
		DescuentoCA = calculaDescuentaA(sueldoBase)
		DescuentoFAOV = calculaFAOV(sueldoBase)
		DescuentoSSO = calculaSSO(sueldoBase)
		DescuentoPIE = calculaPIE(sueldoBase)
		TotalAsignaciones = PrimaAD + PrimaH + PrimaHij + PrimaA + PrimaProf
		ToltaDeducciones = DescuentoCA + DescuentoFAOV + DescuentoSSO + DescuentoPIE
		sueldoNeto = sueldoBase + TotalAsignaciones - ToltaDeducciones
		trabajador.set_Datos(cedula, fecha, nombre, apellido, cargo, nivel, cant, edades, AfCajaH, anioIngreso, sueldoBase, sueldoNeto)
		crearRecibo(trabajador, PrimaProf, PrimaH, PrimaHij, PrimaAD, PrimaA, DescuentoCA, DescuentoSSO, DescuentoFAOV, DescuentoPIE, TotalAsignaciones, ToltaDeducciones)
		encolar(cola,sueldoNeto,Meses[int(fecha.split()[1])-1])
		resp = input("Desea crear otro recibo? (S/N): ")
		resp = validar.Respuestas(resp)
		while (resp != "S" or resp != "N"):
			resp = input("Error Solo (S/N): ")
			resp = validar.Respuestas(resp)
	crearFifo(cola)