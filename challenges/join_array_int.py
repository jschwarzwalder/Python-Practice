# Given an array of 16 bit unsigned integers, print the largest number you can
# form by “joining” the numbers.
# Input => [62, 0, 4] => output 6240 is the largest number that can be formed. (You cannot
# rearrange the digits, just the numbers themselves
# 65,535 is max 16 bit integer

def function (int_array):
	new_int_array = sorted(int_array, cmp = compare)
	print(new_int_array)
	
	
def compare (a, b):
	AB = int(str(a) + str(b))
	BA = int(str(b) + str(a))
	return AB - BA
		
		
function([2, 20, 4, 100])