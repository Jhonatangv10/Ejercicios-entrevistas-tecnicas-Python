def convertToBase13(num):
	first_number = num // 13
	second_number = round(num%13)
	conversion = str(first_number) + str(second_number)

	if first_number == 0 and second_number == 10:
		print("A")
	elif first_number == 0 and second_number == 11:
		print("B")
	elif first_number == 0 and second_number == 12:
		print("C")
	elif first_number == 0:
		print(str(second_number))
	elif second_number == 10:
		print(str(first_number) + "A")
	elif second_number == 11:
		print(str(first_number) + "B")
	elif second_number == 12:
		print(str(first_number) + "C")
	else:
		print(conversion)

convertToBase13(69)