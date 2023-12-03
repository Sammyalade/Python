age = int(input("Enter your age in years(e.g 30): "))

heart_rate = 220 - age

lower_end = (int(0.5 * heart_rate))

upper_end = (int(0.85 * heart_rate))

print('Heart Rate equals ',heart_rate)

print(' Target Heartrate is from  ',lower_end, 'bpm', 'to ', upper_end, 'bpm')

