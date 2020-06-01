from constantes import TSU, ING, MAG, DOC, PH, PHJ, PA, PAD
import time
__name__="asignaciones"
def calculaPrimaProf(nInst, sueldoBase):
	Prima = None
	if(nInst == "1"):
		Prima = 0.00
	elif(nInst == "2"):
		Prima = sueldoBase * TSU
	elif(nInst == "3"):
		Prima = sueldoBase * ING
	elif(nInst == "4"):
		Prima = sueldoBase * MAG
	elif(nInst == "5"):
		Prima == sueldoBase * DOC
	return Prima

def calculaPrimaHog():
	return PH

def calculaPrimaHij(edades):
	Prima = 0.00
	for edad in edades:
		if(edad < "18"):
			Prima = Prima + PHJ
	return Prima

def calculaActiDocen():
	return PAD

def calculaPrimaAnti(anioIngreso, sueldoBase):
	anioActual = time.strftime("%Y")
	Prima = 0.00
	cantAnios = int(anioActual) - int(anioIngreso)

	if(cantAnios > 0):
		Prima = sueldoBase * PA
		Prima = Prima * cantAnios
	return Prima