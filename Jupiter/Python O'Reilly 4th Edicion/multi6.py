import os
from multiprocessing import Pool

def powers(x):
	return 2 ** x

workers = Pool(processes=5)

results = workers.map(powers, [2]*100)
print(results[:16])
print(results[-2:])

results = workers.map(powers, range(100))
print(results[:16])
print(results[-2:])


