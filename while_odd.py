count = 1000
total = 0

while count <= 5000:
	if count % 2 > 0:
		total += count
	count += 1

print('Sum of odd numbers from 1000 to 5000 is ', total) 