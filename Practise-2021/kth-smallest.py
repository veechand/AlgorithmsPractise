"""
Given an array arr[] and a number K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.
arr[] = 7 10 4 3 20 15
K = 3
output = 7

Arrays can contain positive and Negative: Yes
Elements within a range : No

Simplest: Sort a[k] - O(NlogN)
Heap: (Nlogk)
  10     7
       3  4  
  7 4
Algorithm:
  - With First K elements create a Max heap
  - 10
   7    ->  7  -> 4 --> 
                 3
           4
Quick Select:
   - Choose a pivot
   - find the positition of the element in the pivot
   - if position == K 
         return else continue
   - Position of the pivot in the array:
         pivot = last element
         Idea is to move all the element smaller than pivot to the pivitos left
           i = 0
           j = 0
           while (j<len(n))
           j < pivot:
             swap (i,j)
             i ++
           j++
           swap(i,pivot)
           return i
"""

class Solution(object):
	def __init__(self):
		pass
	def find_k_smallest_element(self, array, k, start, end):
		pivot = end 
		position = self.find_pivot_position_in_array(array, pivot, start, end)
		if position == k:
			return array[k]
		if position < k:
			return self.find_k_smallest_element(array, k, position + 1, end)
		else:
			return self.find_k_smallest_element(array, k, start, position - 1)

	def find_pivot_position_in_array(self, array, pivot, start, end):
		i=start
		j=start
		while(j<=end):
			if array[j]<array[pivot]:
				self.swap(i,j,array)
				i += 1
			j+=1
		self.swap(i,pivot,array)
		return i
	def swap(self, src, dst, array):
		array[src], array[dst] = array[dst], array[src]



if __name__ == "__main__":
	solution = Solution()
	array = [7,10,4,3,20,15]
	k = 3
	result = solution.find_k_smallest_element(array, k-1, 0, len(array)-1)
	print(result)