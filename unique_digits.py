# Given an array of 1000 32 bit integers, find the largest number in the array that has unique digits
# Example [1,2,3,4,9,11] ==> 9 (11 does not have unique digits, so disqualified)

def find_largest_unique_digits(array_of_integers):
	if (len(array_of_integers) > 0):
		max_int = None
		for num in array_of_integers:
			if (is_unique_digits(num)):
				if max_int == None or (num > max_int):
					max_int = num
				
		return max_int;
		
def find_largest_unique_digits_in_sorted_array(array_of_integers):
	max_index = len(array_of_integers) - 1
	if (is_unique_digits(array_of_integers[max_index])):
		return array_of_integers[max_index]
	else:
		for index in range(max_index-1, -1, -1 ):
			number = array_of_integers[index]
			if(is_unique_digits(number)):
				return number
			
	

def is_unique_digits(int):
	if (int > -10 and int < 10):
		return True
	num = str(int)
	#print(num)
	digits = []
	for i in num:
		#print(i)
		for j in range(0, len(digits)):
			if (i == digits[j]):
				return False
			elif (i < digits[j]):
				digits.insert(j, i)
				break
			
		digits.append(i)
	return True	


print(find_largest_unique_digits_in_sorted_array([1,2,3,4,5,6,7,8,9])	)	
print(find_largest_unique_digits_in_sorted_array([1,2,3,4,5,6,7,8,9,11])	)	
print(find_largest_unique_digits_in_sorted_array([1,2,3,4,5,6,7,8,9,11,13])	)	
print(find_largest_unique_digits_in_sorted_array([11,22,33,44,55,66,77,88,99])	)	
	
print(find_largest_unique_digits([1, 11, 33])	)
print(find_largest_unique_digits([123456789, 13476567561, 567891234,123412344, 4567890123])	)
print(find_largest_unique_digits([])	)
print(find_largest_unique_digits([-1234, -98372, -382954, -5])	)
print(find_largest_unique_digits([11,22,33,44,55,66,77,88,99])	)
	
#print(is_unique_digits(123456789))
#print(is_unique_digits(11))	
#print(is_unique_digits(121))
#print(is_unique_digits(212))
#print(is_unique_digits(122))
#print(is_unique_digits(987654329))
#print(is_unique_digits(211))
#print(is_unique_digits(-121))
#print(is_unique_digits(-212))
#print(is_unique_digits(-122))
#print(is_unique_digits(-987654329))
#print(is_unique_digits(-211))
#print(is_unique_digits(213))
#print(is_unique_digits(928))
#print(is_unique_digits(436))
#print(is_unique_digits(962))
