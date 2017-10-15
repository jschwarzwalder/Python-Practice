# Given two source strings, and a target string, identify if the
# target string can be formed by “merging” the two source strings?
# Example: SSLLS, deki ­> SdeSkiLLS ­ TRUE

def can_merge(string1, string2, target):
	string1_index = 0
	string2_index = 0
	for letter in target:
		if (string1_index < len(string1)) and (letter == string1[string1_index]):
			string1_index += 1
			continue
		elif (string2_index < len(string2)) and (letter == string2[string2_index]):
			string2_index += 1
			continue
		else:
			return False
	return True


print(can_merge("abc","123", "abc123"))	
print(can_merge("abc","123", "a1b2c3"))	
print(can_merge("abcd","123", "a1b2c3"))	
print(can_merge("abcd","1234", "a1b2c3"))
print(can_merge("toher","get", "together"))	
print(can_merge("cba","123", "abc123"))	
print(can_merge("a1b2c","123", "abc123"))
print(can_merge("pu","al", "paul"))	
print(can_merge("pu","al", ""))		
print(can_merge("pu","al", "u"))	