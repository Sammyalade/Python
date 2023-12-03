number1 = input("Enter first value: ")
number2 = input("Enter second value: ")
number3 = input("Enter third value: ")


highest = number1

if number2 > highest:
	number2 = highest

if number3 > highest:
	number3 = highest

middle = number1

if number1 > number3 and number1 < number2:
	middle = number1
if number1 > number2 and number1 < number3:
	middle = number1

if number2 > number1 and number2 < number3:
	middle = number2
if number2 > number3 and number2 < number1:
	middle = number2

if number3 > number1 and number3 < number2:
	middle = number3
if number3 > number2 and number3 < number1:
	middle = number3

smallest = number1

if number2 < smallest:
	smallest = number2

if number3 < smallest:
	smallest = number3



print(smallest,middle,highest)

