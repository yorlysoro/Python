a = [1,2,-1,-4,5,-2]

i = 0
while i < len(a):
	if a[i] < 0:
		del a[i]
	else:
		i += 1
print(a)
