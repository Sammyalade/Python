number1 = 5
number2 = 7
count = 1500

for count in range(1500, 2700):
	if count % number1 == 0:
		if count % number2 == 0:
			print(count)
			count += 1
			