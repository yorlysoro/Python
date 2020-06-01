epsilon = 1.0E-6
nmax = 100

def funcion(x, fx, dfx):
	fx = x * x - 2
	dfx = 2 * x
	return (fx, dfx)

x = 2.0
k = 1
fx = 0
dfx = 0.0
fx, dfx = funcion(x, fx, dfx)
while(abs(fx) >= epsilon) and (k < nmax):
	fx, dfx = funcion(x, fx, dfx)
	x = x - (fx / dfx)
	k = k + 1
#	print("fx = ",fx)
#	print("dfx = ",dfx)
#	print("x = ",x)
#	print("k = ",k)

if k < nmax:
	print(x)
else:
	print("No converge con ", nmax, " iterciones")
