count = 2
print(2, 3, 5, 7, end =' ')
for number in range(2, 100):
	if count % 2 > 0:
		if count % 3 > 0:
			if count % 4 > 0:
				if count % 5 > 0:
					if count % 6 > 0:
						if count  % 7 > 0:
							if count % 8 > 0:
								if count % 9 > 0:
									if count % 10 > 0:
										print(count, end =' ')
	count += 1  