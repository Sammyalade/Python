count = 1
total = 0
for count in range(1, 21):
	number = int(input('Enter numbers from 1 - 20: '))
	total = total + number
	count += 1
	if count == 21:
		break

if total > 210:
	print('Invalid, number not in the range of 1 - 20')	
else:
	print('sum is ', total)