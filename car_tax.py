cost_of_car = (int(input("Enter the car amount: ")))

if cost_of_car < 1000000:
	tax1 = (float(cost_of_car * 0.10))
	print("Tax is ",tax1)
elif cost_of_car >= 1000000 and cost_of_car < 3000000:
	tax2 = (float(cost_of_car * 0.15))
	print("Tax is ",tax2)
elif cost_of_car >= 3000000 and cost_of_car < 5000000:
	tax3 = (float(cost_of_car * 0.20))
	print("Tax is ",tax3)
elif cost_of_car > 5000000:
	tax4 = (float(cost_of_car * 0.25))
	print("Tax is ",tax4)