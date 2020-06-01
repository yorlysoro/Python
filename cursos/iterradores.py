def double(num):
	return num+2
	
def even(num):
	return (num%2) == 0
def operation(num1, num2):
	return num1*num2+1
	
l1 = range(10)

l2 = map(double, l1)
l3 = filter(even, l1)
l4 = reduce(operation,l1)


l5 = map(lambda num: num*2, l1)
l6 = filter(lambda num: num%2 == 0, l1)
l7 = reduce(lambda num1, num2: num1*num2 + 1, l1)

l8 = [num+2 for num in l1]

print l1
print l2,l5
print l3,l6
print l4,l7

print l8
