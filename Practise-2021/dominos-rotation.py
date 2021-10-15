"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

[1 4 6 ]
[3 3 3]

[ 2 2 5]
[ 1 1 6]

Maximum time occuring element - Try to replace everything other than that 

Minimum rotation to make all the elements in top array same

tops = [2,1,2,4,2,2],  
 Maximum Time occuring element: 2 
 Try replacing those that's != maximum time occuring element if we get all equal then that's the maximum rotation
bottoms = [5,2,6,2,3,2]
 Maximum Time occuring element: 2 

 get_maximum_rotation(src, dst):
     elem = get_maximum_occuring_element(src)
     number_of_rotations = -1
     for i,e in enumerate(src):
     	 if e!= elem:
     	 	if dst[i] == elem:
     	 		number_of_rotations += 1
     	 	else:
     	 		number_of_rotations = (2 * 10**5)
     	 		break 			
"""
from collections import defaultdict

class Solution(object):
	def __init__(self):
		self.MAX_VALUE = 2 * (10**5)
	def get_number_of_rotations(self, top, bottom):
		answer1 = self.get_maximum_rotations(top, bottom)
		answer2 = self.get_maximum_rotations(bottom, top)
		result =  min(answer1, answer2)
		return -1 if result == self.MAX_VALUE else result

	def get_maximum_rotations(self, src, dst):		
		element = self.get_maximum_occuring_element(src)
		number_of_rotations = 0
		for index, cur_element in enumerate(src):
			if cur_element != element:
				if dst[index] == element:
					number_of_rotations += 1
				else:
					number_of_rotations = self.MAX_VALUE
					break
		return number_of_rotations

	def get_maximum_occuring_element(self, array):
		occurences = defaultdict(int)
		for elem in array:
			occurences[elem] += 1
		return sorted(occurences.items(), key= lambda x: x[1], reverse=True)[0][0]
	


if __name__ == "__main__":
	solution = Solution()
	tops = [2,2,1]
	bottoms = [1,4,4]
	tops = [2,1,2,4,2,2]
	bottoms = [5,2,6,2,3,2]
	tops = [3,5,1,2,3]
	bottoms = [3,6,3,3,4]
	result = solution.get_number_of_rotations(tops, bottoms)
	print (result)