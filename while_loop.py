fixed = 3
number = 1
count = 1
while count <= 10:
	number = number * fixed
	count  += 1
	print(number, end = ' ')
	if count == 11:
		break