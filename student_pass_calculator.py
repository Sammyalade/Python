user_input = 1

pass_mark = 0

fail = 0

while user_input != 101:
	user_input = float(input("Enter Student Score or 101 to cancel: "))
	
	if user_input < 0:
		user_input = int(input("I go soon slap you. Oga Enter Student Score or 101 to cancel: "))
	if user_input > 100:
		user_input = int(input("You dey mad??? Oga Enter Student Score or 101 to cancel: "))
	if user_input == 100:
		break
	if user_input >= 45 and user_input <= 100:
		pass_mark += 1
	elif user_input < 45 and user_input >= 0:
		fail += 1

print("Number of pass is ", pass_mark, "Number of fail", fail)