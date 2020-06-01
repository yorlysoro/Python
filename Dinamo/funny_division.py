def funny_division(anumber):
	try:
		if anumber == 13:
			raise ValueError("13 is an unluckly number")
		return 100 / anumber
	except (ZeroDivisionError, TypeError):
		return "Enter a number other than zero"
for val in (0, "hello", 50.0, 13):
	print("Testing {}: ", format(val), end=" ")
	print(funny_division(val))
