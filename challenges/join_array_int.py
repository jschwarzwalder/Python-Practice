# Given an array of 16 bit unsigned integers, print the largest number you can
# form by “joining” the numbers.
# Input => [62, 0, 4] => output 6240 is the largest number that can be formed. (You cannot
# rearrange the digits, just the numbers themselves
# 65,535 is max 16 bit integer

def function (int_array):
	print(int_array)
	int_array.sort(key = cmp_to_key(compare))
	joined_int = "".join(map(str, int_array))
	print(joined_int)
	print()
	
	
def compare (a, b):
	AB = int(str(a) + str(b))
	BA = int(str(b) + str(a))
	return BA - AB # Sort largest to the left

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K	
		

function([1, 2, 3, 4, 5, 6, 7,8, 9, 10])
function([])
function([0,0,0,0,0,0])
function([2, 20, 4, 100])
function([6, 60, 62, 66])
function([9899, 9879, 98])
function([1,20, 300, 4000, 50000])
function([53, 2, 4, 9, 127])
function([65, 360])