# Given an array of 16 bit unsigned integers, print the largest number you can
# form by “joining” the numbers.
# Input => [62, 0, 4] => output 6240 is the largest number that can be formed. (You cannot
# rearrange the digits, just the numbers themselves
# 65,535 is max 16 bit integer

def function (int_array):
	ones = []
	tens = []
	hundres = []
	thousands = []
	ten_thousands = []
	for int in int_array:
		if int > 9999:
			
			if len(ten_thousands) == 0:
				ten_thousands.append(int)
			else:
				# insert in order to ten_thousands
		elif int > 999: 
			if len(thousands) == 0:
				thousands.append(int)
			else:
				# insert in order to thousands
	
	new_int_array = []
	ones_index
	tens_index
	hundreds_index
	thous_index
	ten_thous_index
	# compare arrays and add largest left most integer next
	new_int = one[ones_index]
	ones_index += 1
	if new_int < tens[tens_index] % 10:
		new_int = tens[tens_index]
		tens_index += 1
		ones_index -= 1
		
			
	for index in range(0,len(new_int_array)):
		end_num
	
	