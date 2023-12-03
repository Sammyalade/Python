count = 1
total = 0

while count <= 20:
	
	number = int(input('Enter numbers from 1 - 20: '))
	count += 1
	total = total + number
if total > 210:
	print('Invalid, number not in the range of 1 - 20')	
else:
	print('sum is ', total)
