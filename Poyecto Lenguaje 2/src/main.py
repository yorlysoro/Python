from menu import menu, mostrarRecibo, eliminarRecibo, mostrarNomina, totalDeducciones, totalCobrado, crearRecibo
from constantes import CLS
from os import system
__name__ = "main"


def main():
	CLS
	cant = 1
	op = ""
	while (op != "7" or cant == 1):
		system(CLS)
		op = menu(op)
		cant = cant + 1
		if(op == "1"):
			crearRecibo()
		elif(op == "2"):
			mostrarRecibo()
		elif(op == "3"):
			eliminarRecibo()
		elif(op == "4"):
			mostrarNomina()
		elif(op == "5"):
			totalCobrado()
		elif(op == "6"):
			totalDeducciones()
		elif(op == "7"):
			input("Hasta luego")
		else:
			input("Opcion Incorrecta!!")

if __name__ == "main":
	main()
