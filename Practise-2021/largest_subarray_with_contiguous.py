"""
Given an array of distinct integers, find length of the longest subarray 
which contains numbers that can be arranged in a continuous sequence. 
Examples: 

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

[1,2,5,6,7,8,9]
- Will the whole array is sorted ? No 
[1,2,9,7,8,5,6] - 5
- Is it only positive integer
- continuous mean a[i] = a[i-1] + 1 --> Is this correct
- Subarray : i,i+1, i=2 is a sub-array
- "Can be " - The array is not sorted

Can't offort to lose the order

Brute Force:
{
	1: 0
	2: 1
	9: 2
	7: 3
	8: 4
	5: 5
	6: 6
}

7,8,9 - 3,4,2
5,6,3,4,2 -> 2,3,4,5,6 -> Longest continuous sequence in this

Algorithm - 1: 
  - Put the elements in to a dictionary
  - pos = []
  - max_length = 0
  - for i in range(len(array)) - O(n2)
        element = array[i]
        part_pos = 0
        while element in dict:
			if element in calculated_result:
				part_pos = calculated_result[element]
				break
        	pos.append(dict[element])
        	element = element + 1
	
		if len(pos) + part_pos > max_length:
			 if (check_continuous(sorted(pos)) - O(nlogn) + O(n))
			     max_length = len(pos) + part_pos
				 calculate_result[element] = len(pos) + part_pos

"""

class Solution(object):
	def __init__(self):
		pass
	def get_longest_continuous_subarray(self, array):
		max_length = 0
		calculated_length = {}
		element_pos = self.add_elements_to_dict(array)
		for i in range(len(array)):
			element = array[i]
			positions = []
			part_pos = 0
			while element in element_pos:
				if element in calculated_length:
					part_pos = calculated_length[element]
					break
				positions.append(element_pos[element])
				element = element + 1
			if self.check_continuous(sorted(positions)):
				if len(positions) + part_pos > max_length:
					max_length = len(positions) + part_pos
				calculated_length[element] = len(positions) + part_pos
		return max_length

	def check_continuous(self, positions):
		result = True
		for i in range(1, len(positions)):
			if positions[i] - 1 != positions[i-1]:
				result = False
				break
		return result

	def add_elements_to_dict(self,array):
		result = {}
		for pos,element in enumerate(array):
			result[element] = pos
		return result

if __name__ == "__main__":
	solution = Solution()
	array = [1,2,9,7,8,5,6]
	array = [10, 12, 11]
	# array = [14, 12, 11, 20]
	array = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
	array = range(1,100000)
	# array = [0,4,8,10]
	result = solution.get_longest_continuous_subarray(array)
	print(result)
