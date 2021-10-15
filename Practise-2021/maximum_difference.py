"""
Given an array arr[] of integers, find out the maximum difference between any two elements 
such that larger element appears after the smaller number. 

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8

{1,2,3,4,6,8,10}

a[i+1] - a[i] < a[j] - a[j-1]
 - Move left

Sort:  O(nlogn)
pos_dict - Space: O(n)
i = 0 
j = len(array) - 1
while (i<=j): O(N)
	if (pos_dict(a[j]) > pos_dict[a[i]])
   		max_diff = a[j] = a[i]
   		break
   	if a[i+1] - a[i] < a[j] - a[j-1]:
   		i = i + 1
   	if a[i+1] - a[i] > a[j] - a[j-1]:
   		j = j - 1
   	else a[i+1] - a[i] == a[j] - a[j-1]:
   		if pos_dict[a[i++]] < pos_dict[a[j]]:
   			i ++ 
   		else:
   			j --
"""

class Solution(object):
	def __init__(self):
		pass
	"""
	def find_max_difference(self, array):
		pos_dict = self.add_elements_to_dict(array)
		sorted_array = sorted(array)
		i = 0
		j = len(array) - 1
		while(i<j):
			if (pos_dict[sorted_array[j]] > pos_dict[sorted_array[i]]):
				return sorted_array[j] - sorted_array[i]
			if sorted_array[i+1] - sorted_array[i] < sorted_array[j] - sorted_array[j-1]:
				i += 1
			elif sorted_array[i+1] - sorted_array[i] > sorted_array[j] - sorted_array[j-1]:
				j -= 1
			elif sorted_array[i+1] - sorted_array[i] == sorted_array[j] - sorted_array[j-1]:
				if pos_dict[sorted_array[i+1]] < pos_dict[sorted_array[j]]:
					i += 1
				else:
					j -= 1
		return None
	"""
	def find_max_difference(self, array):
		small = array[0]
		big = array[0]
		diff = 0
		max_diff = 0
		for i in range(1, len(array)):
			if big < array[i]:
				big = array[i]
				diff = big - small
				max_diff = max(diff, max_diff)
			elif array[i] < small:
				small = array[i]
				big = array[i]
		return max_diff



	def add_elements_to_dict(self,array):
		result = {}
		for pos,element in enumerate(array):
			result[element] = pos
		return result

if __name__ == "__main__":
	solution = Solution()
	array = [2, 3, 10, 6, 4, 8, 1] 
	# array = [2, 3, 10, 6, 4, 9, 1] 
	# array = [7, 9, 5, 6, 3, 2]
	array = [1, 2, 6, 80, 100]
	array = [1, 2, 90, 10, 110]
	array = [80, 2, 6, 3, 100]
	result = solution.find_max_difference(array)
	print result