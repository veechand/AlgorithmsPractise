"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

array = [1,3,4,-4]
result = 12

array = [1,3,-4,4,-5]
output: 240

Brute Force:
 - Think each number is the starting number
 - multiply with every other number
 - if the current_output is greater than last_product then store it

 [-2,0,-1]

 result = -10000
 max_till_now = [0 0 0 0 -5] 
 for index in range(len(array)-2, -1, -1):
	max_till_now[index] = max(array[index], array[index])

[-1 -2 -3]
[]
Algorithm 1:
  pos_p = 0
  neg_p = 0
  for elem in array:
  	if elem > 0:
  		pos_p = elem if pos_p == 0 else pos_p * elem
  	if elem < 0:
  		if neg_p >= 0 : # it can't be > 0
  			neg_p = elem
  			pos_p = 0
  		else:
  			pos_p = neg_p * pos_p
  			neg_p = 0
  	if elem == 0
  		pos_p = elem
  		neg_p = elem
"""

class Solution(object):
	def __init__(self):
		pass
	def maximum_product(self, array):
		pos_p, neg_p = 0, 0
		maximum_product = array[0]
		seen_one_zero_element = False
		for elem in array:
			if elem > 0:
				pos_p = elem if pos_p == 0 else pos_p * elem
				neg_p = elem * neg_p
			elif elem < 0:
				temp = pos_p
				if neg_p >= 0:
					neg_p = elem if pos_p == 0 else pos_p * elem
					pos_p = 0
				else:
					pos_p = neg_p * elem
					neg_p = elem if temp == 0 else temp * elem
			elif elem == 0:
				seen_one_zero_element = True
				pos_p = 0
				neg_p = 0
			maximum_product = max(pos_p, maximum_product)
		# print seen_one_non_zero_element, maximum_product
		if not seen_one_zero_element and maximum_product == 0:
			maximum_product = array[0]
		return maximum_product


if __name__ == "__main__":
	solution = Solution()
	# array = 
	print(6 == solution.maximum_product([2,3,-2,4]))
	print(24 == solution.maximum_product([2,-3,-4]))
	print(2 == solution.maximum_product([-2,2,0,-6]))
	print(-2 == solution.maximum_product([-2]))
	print(0 == solution.maximum_product([-2,0,-1]))
	print(24 == solution.maximum_product([2,-5,-2,-4,3]))
	print(108 == solution.maximum_product([-1,-2,-9,-6]))
	
	
	# result = solution.maximum_product(array)
	# print(result)