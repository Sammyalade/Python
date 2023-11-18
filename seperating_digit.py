number = int(input("Enter 5 digits: "))

digit_one = number // 10000

digit_one1 = number % 10000

digit_two = digit_one1 // 1000

digit_two1 = digit_one1 % 1000

digit_three = digit_two1 // 100

digit_three1 = digit_two1 % 100

digit_four = digit_three1 // 10

digit_four1 = digit_three1 % 10

digit_five = digit_four1 // 1


print(digit_one, digit_two, digit_three, digit_four, digit_five)