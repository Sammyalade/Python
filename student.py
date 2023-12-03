passes = 0
failures = 0
student = 1

while student <= 10:
	
	result = int(input('Enter result (1 = pass, 2 = fail): '))
	
	while result != 1 and result != 2:
		result = int(input('Invalid input. Please enter 1 or 2: '))
	
	if result == 1:
		passes += 1
	
	student += 1

failures = 10 - passes
	

print('Passed: ', passes)
print('Failure: ', failures)

if passes > 8:
	print('Bonus to instructor')