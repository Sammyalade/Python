user_input = int(input("Enter a dog's age in Human years: "))

if user_input <= 2:
	calculation1 = (user_input) * 10.5
	print("The dog's age in dog's year is ", calculation1)
elif user_input > 2:
	calculation = ((user_input - 2) * 4) + 21
	print("The dog's age in dog's year is ", calculation)
elif user_input < 2:
	print('Invalid input, Enter ages from 2 and above: ')