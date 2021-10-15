"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example: n == 2
()()
(())

n = 3
((()))
()()()
(())()
()(())
(()())

Open - 0

for i in range(0,2**1):
    x=bin(i)
    x = str(x)[2:]
    if len(x) != 2:
    	x = "0"*(2-len(x)) + x
    if str(x).count("1") == str(x).count("0"):
    	happened = True
    	opening = 0
    	for c in x:
    		if i == 14:
 				print c,  opening
    		if c == "0":
    			opening += 1
    		if c == "1":
    			opening -= 1
    		if opening < 0:
    			happened = False
    			break
    	if happened:
        	print "happened",i,x

"""

class Solution(object):
	def __init__(self):
		self.ZERO = "0"
		self.ONE = "1"
	def find_paranthesis(self, N):
		result = []
		total_number_of_parenthesis = N * 2 # since N is a pair
		for i in range(2**total_number_of_parenthesis):
			binary_representation = bin(i)[2:]
			if len(binary_representation) != total_number_of_parenthesis:
				binary_representation = self.ZERO * (total_number_of_parenthesis - len(binary_representation)) + binary_representation
			if (self.is_proper_open_close(binary_representation)):
				result.append(self.convert_to_paranthesis(binary_representation))
		return result
	def is_proper_open_close(self, binary_repr):
		happened = True
		if binary_repr.count(self.ZERO) == binary_repr.count(self.ONE):
			open_braces_count = 0
			for c in binary_repr:
				if c == self.ZERO:
					open_braces_count += 1
				elif c == self.ONE:
					open_braces_count -= 1
				if open_braces_count < 0:
					happened = False
					break
		else:
			happened = False
		return happened

	def convert_to_paranthesis(self, binary_repr):
		return binary_repr.replace(self.ZERO,"(").replace(self.ONE,")")

if __name__ == "__main__":
	solution = Solution()
	result = solution.find_paranthesis(8)
	print result, len(result)


