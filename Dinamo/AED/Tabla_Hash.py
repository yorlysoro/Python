
def hashing(entrada):
	numero = float(len(entrada)) 
	indice = int(numero % 1024) 
	return indice

def mostrar_vector(vector):
	print(vector)


dato = ["Jose", "Daniel", "Pancho", "Mama", "La concha"]
vector = {}
for i in range(len(dato)):
	vector[hashing(dato[i])] = dato[i]

mostrar_vector(vector)

