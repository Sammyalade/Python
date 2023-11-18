number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

maximum = number1

if number2 > maximum:
	maximum = number2

if number3 > maximum:
	maximum = number3

print('Maximum value is', maximum)


minimum = number3

if number2 < minimum:
	minimum = number2

if number1 < minimum:
	minimum = number1

print('Minimum value is', minimum)

print(min(number1, number2, number3))

print(max(number1, number2, number3))