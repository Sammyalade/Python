average = 0
count = 0
total = 0
user_input = 0
while user_input >= 0:
	user_input = int(input('Enter a number or 0 to cancel: '))
	if user_input == 0:
		break
	total += user_input
	count += 1

average = float(total / count)
print('Sum of all input equals ', total)
print('Average of all input equals ', average)