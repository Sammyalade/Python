number = (int(input("Enter a unit: ")))


if number > 0 and number <= 100:
	print("Unit charge is #0")
elif number > 100 and number <= 200:
	decider = (number - 100) * 10
	print("Unit charge is #", decider)
elif number > 200:
	decider = (number - 100)
	if decider > 100:
		decider1 = 1000
		decider2 = (decider - 100) * 20
		print("Unit charge is ", decider1 + decider2)