# Given an array of 16 bit unsigned integers, print the largest number you can
# form by “joining” the numbers.
# Input => [62, 0, 4] => output 6240 is the largest number that can be formed. (You cannot
# rearrange the digits, just the numbers themselves

def function (int_array):
	int_array.sort(reverse=True)
	return ''.join(int_array)
	
	
