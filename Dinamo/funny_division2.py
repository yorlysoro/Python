def funny_division2(anumber):
	try:
		if anumber == 13:
			raise ValueError("13 is a number unluckly number")
		return 100 / anumber
	except ZeroDivisionError:
		return "Enter a number other than zero"
	except TypeError:
		return "Enter a numerical value"
	except ValueError:
		print("No, No, not 13!")
		raise 
for val in (0, "hello", 50.0, 13):
	print("Testing {}: ", format(val), end=" ")
	print(funny_division2(val))
