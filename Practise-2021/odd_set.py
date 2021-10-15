"""
Given an array of sets find the one that does not belong:
example: [[a,b,c,d], [a,b,f,g], [a,b,h,i], [j,k,l,m]]
output: [j,k,l,m]

We can see above that the first three sets have a subset [a,b,c] and the last one does not. Note: There may be a case where the outlier set does have elements contained in the input group. In this case we have the find the set that has the least in common with the other sets.

Clarifications:
 - If there are only two sets
      a. [1,2] [2,1] --> ??
      b. [1,2] [4,5] --> What's the answer
      c. [1,2,3,4] [5,6,7,8] [1,2,3,4] [5,6,7,8] 
 - Least in common 
 - Can I assume that the elements of the set is comparable Yes 
 - Can we sort the given arrary ? Yes
 - [a,b,c,d], [a,b,f,g], [a,b,h,i], [j,k,l,m]
 - Set all pointers to index 0
 - Insert the pointer position in to heap (value, array index)
 - Increment all the pointers
 - Have visited sets {} : Key - Min Value Value: (array_index, 1)
 while(heap is not empty)     
     - Pop the minimum from the heap
     - if it exists in the set, increment the result for array_index by 1 and set intersection as True
     - if it doesn't exist insert it into the visited set, with value as False for intersection
     - Pop the next position from the array_index and insert it in to Heap
 Traverse the vistited set
     - For all that has intersection has True increment the array index
 Get the minimum of the array_indices
 {1} - 2,2,0
 {2} - 2,2,0
 {3} - 2,2,0
 {4} - 0,0,0
"""
from heapq import heappush, heappop

class BruteForceSolution(object):
	pass
class Solution(object):
	def find_least_intersection(self, arrays):
		heap = []
		pointers = [0 for i in range(0,len(arrays))]
		result = [0 for i in range(0,len(arrays))]
		sorted_arrays = self.sort_arrays(arrays)
		visited_values = {}
		for array_pos, pos in enumerate(pointers):
			if pos < len(sorted_arrays[array_pos]):
				heappush(heap, (sorted_arrays[array_pos][pos],array_pos))
				pointers[array_pos]+= 1
		while(len(heap)>0):
			value,array_pos = heappop(heap)
			current_pointer_pos = pointers[array_pos]
			if current_pointer_pos < len(sorted_arrays[array_pos]):
				heappush(heap, (sorted_arrays[array_pos][current_pointer_pos], array_pos))
				pointers[array_pos]+= 1

			if value not in visited_values:
				visited_values[value] = (array_pos,False)
			else:
				result[array_pos] += 1
				temp = visited_values[value]
				visited_values[value] = (temp[0], True)

		for key, value in visited_values.items():
			if value[1]:
				result[value[0]] += 1
		return self.get_minimum_index(result)

	def get_minimum_index(self, result):
		minimum = 2**32
		minimum_index = -1
		print(result)
		for index, value in enumerate(result):
			if value < minimum:
				minimum = value
				minimum_index = index
		return minimum_index	
	def sort_arrays(self, arrays):
		result = []
		for array in arrays:
			result.append(sorted(array))
		return result


solution = Solution()
# values = [['a','b','c','d'], ['a','b','f','g'], ['a','b','h','i'], ['j','k','l','m']]
values = [[1,2,3,4],  [1,9,10,11,12], [3,4,6,7,8], [1,2,4,5,6]]
values = [[1,2,3,4],  [1,9,10,11,12], [3,4,6,7,8], []]
result = solution.find_least_intersection(values)
print(result)
print(values[result])