import time,os,re
from constantes import Meses, Cargo, NivelInst
__name__ = "archivos"
def existeArchivo(nArchivo):
	return os.path.exists(nArchivo)

def creaActualizaNomina(sueldoNeto, TotalDeducciones, mes):
	nNomina = "../txt/Nomina"+"-"+time.strftime("%Y")+".txt"
	modificado = False
	valores = None
	if existeArchivo(nNomina):
		with open(nNomina, "r") as Nomina:
			for linea in Nomina:
				if(re.search("%s" %(mes), linea)):
					valores = linea.split()
					modificado = True
					break
		nNomina.close()
		if(modificado):
			with open("../txt/Respaldo.txt", "w") as Respaldo:
				with open(nNomina, "r") as Nomina:
					for linea in Nomina:
						Respaldo.write(linea)
				Nomina.close()
			Respaldo.close()
			sueldoNeto = sueldoNeto + float(valores[0])
			TotalDeducciones = TotalDeducciones + float(valores[1])
			with open("../txt/Respaldo.txt", "r") as Respaldo:
				with open(nNomina, "w") as Nomina:
					for linea in Respaldo:
						if(re.search("%s" % mes, linea)):
							Respaldo.write(str(sueldoNeto)+"	"+str(TotalDeducciones)+"	"+mes+"\n")
						else:
							Respaldo.write(linea)
				Nomina.close()
			Respaldo.close()
		else:
			with open(nNomina, "a") as Nomina:
				Nomina.write(str(sueldoNeto)+"	"+str(TotalDeducciones)+"	"+mes+"\n")
			Nomina.close()
	else:
		with open(nNomina, "w") as Nomina:
			Nomina.write("					Nomina\n")
			Nomina.write("Asignaciones 		"+"Deducciones 		"+"MES"+"\n")
			Nomina.write(str(sueldoNeto)+"	"+str(TotalDeducciones)+"	"+mes+"\n")
		Nomina.close()

def creaActualizaRegistro(Direccion, nRegistro):
	Direccion = "../txt/"+Direccion+".txt"
	if(existeArchivo(Direccion)):
		with open(Direccion, "a") as Registro:
			Registro.write(nRegistro)
		Registro.close()
	else:
		with open(Direccion, "w") as Registro:
			Registro.write(nRegistro)
		Registro.close()


def existeTrabajador(Registro, Cedula):
	Registro = "../txt/"+Registro+".txt"
	if(existeArchivo(Registro)):
		with open(Registro, "r") as nRegistro:
			for linea in nRegistro:
				if(re.search("%s" %(Cedula), linea)):
					nRegistro.close()
					return True
		nRegistro.close()
	return False

def extraeRecibo(Cedula, nRecibo):
	Cedula = "../txt/"+Cedula+".txt"
	if(existeArchivo(Cedula)):
		with open(Cedula, "r") as nCedula:
			for linea in nCedula:
				if(re.search("%s"% (nRecibo), linea)):
					nCedula.close()
					return nRecibo
		nCedula.close()
	return ""

def creaActualizaTotalIVSS(Cedula, TotalDeducciones, mes):
	nIVSS = "../txt/IVSS.txt"
	if(existeArchivo(nIVSS)):
		with open(nIVSS, "a") as IVSS:
			IVSS.write(Cedula+"	"+str(TotalDeducciones)+"	"+mes+"\n")
		IVSS.close()
	else:
		with open(nIVSS, "w") as IVSS:
			IVSS.write("				Total Pagado al IVSS\n")
			IVSS.write("Trabajador 	"+"Total Pagado	"+"MES"+"\n")
			IVSS.write(Cedula+"	"+str(TotalDeducciones)+"	"+mes+"\n")
		IVSS.close()


def crearRecibo(Trabajador, PrimaP, PrimaH, PrimaHJ, PrimaAD, PrimaA, DescuentoCA, DescuentoSSO, DescuentoFAOV, DescuentoPIE, TotalAsignaciones, TotalDeducciones):
	datosTrabajador = Trabajador.get_Datos()
	nombreRecibo = "../txt/"+datosTrabajador['Cedula']+datosTrabajador['dia']+datosTrabajador['mes']+datosTrabajador['anio']+".txt"
	anioActual = strftime("%Y")

	with open(nombreRecibo, "w") as recibo:
		recibo.write("					Recibo del Trabajador: "+datosTrabajador['Cedula']+"					Fecha: "+datosTrabajador['dia']+"/"+datosTrabajador['mes']+datosTrabajador['anio']+"\n")
		recibo.write("Cedula: "+datosTrabajador['Cedula']+"\n")
		recibo.write("Cargo: "+Cargo[datosTrabajador['Cargo']-1]+"				Nivel de Instruccion: "+NivelInst[datosTrabajador['nInst']-1]+"\n")
		recibo.write("Afiliado a caja de ahorro: "+datosTrabajador['AfCajaH']+"								Año de Ingreso: "+datosTrabajador['anioIngreso']+"\n")
		recibo.write("Sueldo Base: "+str(datosTrabajador['sueldoBase'])+"\n")
		recibo.write("					Asignaciones\n")
		recibo.write("Prima por Profesionalizacion: "+str(PrimaP)+"\n")
		recibo.write("Prima por Hogar: "+str(PrimaH)+"\n")
		recibo.write("Prima por Hijos: "+str(PrimaHJ)+"\n")
		recibo.write("Prima por apoyo a la actividad docente: "+str(PrimaAD)+"\n")
		recibo.write("Prima de Antiguedad: "+str(PrimaA)+"\n")
		recibo.write("					Deducciones\n")
		recibo.write("Descuento por Caja De Ahorro:"+str(DescuentoCA)+"\n")
		recibo.write("Descuento por SSO: "+str(DescuentoSSO)+"\n")
		recibo.write("Descuento por FAOV: "+str(DescuentoFAOV)+"\n")
		recibo.write("Descuento por PIE: "+str(DescuentoPIE)+"\n")
		recibo.write("					Totales\n")
		recibo.write("Total de Asignaciones: "+str(TotalAsignaciones)+"\n")
		recibo.write("Total de Deducciones: "+str(TotalDeducciones)+"\n")
		recibo.write("Sueldo Neto: "+str(datosTrabajador['sueldoNeto'])+"\n")
	recibo.close()
	creaActualizaNomina(datosTrabajador['sueldoNeto'], TotalDeducciones, Meses[int(datosTrabajador['mes'])-1])
	creaActualizaRegistro("Registro",datosTrabajador['Cedula'])
	creaActualizaRegistro(datosTrabajador['Cedula'], datosTrabajador['Cedula']+datosTrabajador['dia']+datosTrabajador['mes']+datosTrabajador['anio'])
	creaActualizaRegistro(datosTrabajador['Cedula']+"2", datosTrabajador['Cedula']+Meses[int(datosTrabajador['mes'])-1]+anioActual)
	creaActualizaTotalIVSS(datosTrabajador['Cedula'], TotalDeducciones, Meses[int(datosTrabajador['mes'])-1])

def LeeArchivo(Direccion):
	try:
		with open(Direccion, "r") as Archivo:
			for linea in Archivo:
				print(linea, end='')
		Archivo.close()
	except Exception as e:
		print("El Archivo no existe: ", e)

def eliminarArchivo(Direccion):
	try:
		os.remove(Direccion)
	except Exception as e:
		print("El Archivo no existe:", e)

def borraRegistro(Archivo, nRecibo):
	nRespaldo = "../txt/Respaldo.txt"
	with open(nRespaldo, "w") as Respaldo:
		try:
			with open(Archivo, "r") as nArchivo:
				for linea in nArchivo:
					if(re.search("%s"%(nRecibo), linea)):
						continue
					else:
						Respaldo.write(linea)
			nArchivo.close()
		except Exception as e:
			print("El Archivo no existe:", e)
			try:
				os.remove(nRespaldo)
			except Exception as e:
				pass
			return
	Respaldo.close()
	with open(nRespaldo, "r") as Respaldo:
		with open(Archivo,"w") as nArchivo:
			for linea in Respaldo:
				nArchivo.write(linea)
		nArchivo.close()
	Respaldo.close()
	try:
		os.remove(nRespaldo)
	except Exception as e:
		pass
	