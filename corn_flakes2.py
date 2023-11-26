count = 1
even_count = 0
odd_count = 0

for number in range(100):
	if count % 2 == 0:
		even_count += 1
	elif count % 2 > 0:
		odd_count += 1
	count += 1
print('Number of Even numbers: ', even_count)
print('Number of Odd numbers: ', odd_count)