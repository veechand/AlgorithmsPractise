"""
 Segment Trees are used for Range queries
 Segment Trees are represented as Array, same like max heap
 leaf nodes are towards the end
 if there number of element in the array is power of 2 then number of 
 array elements in 2*n - 1
 if there number of element in the array is not power of 2 find the 
 the next power of 2 and array elements in 2*n + 1

 How to check is an element power of 2 
     4  2  1
     1  1  0  - 6
   1 0  0  0  - 8
   ==========
   1 0 0 0 -- AND gives 8

  1 0 0 0
1 0 0 0 0
==========

bin(number) - count number of 1 is == 1 then it's power of 2 

What's the mathematical property of Number = 2 ^ N

Sqrt Number is whole Number
11
10
1
"""

class SegmentTree:

	def __init__(self, inputArray):
		self.segmentTree = None
		self.MAX = 2**32
		powerOfTwo = self.getPowerOfTwo(len(inputArray))
		self.segmentTree = [self.MAX] * ((2 * powerOfTwo)-1)
		print self.segmentTree
		self.buildTree(inputArray, 0, len(inputArray)-1, 0)

	def getPowerOfTwo(self, number):
		if number == 0:
			return number
		if number & (number-1) == 0:
			return number
		while (number & (number-1) != 0):
			number = number & (number - 1)
		return number << 1


	def buildTree(self, inputArray, start, end, pos):
		if (start==end):
			self.segmentTree[pos] = inputArray[start]
			return
		mid = (start+end)/2
		self.buildTree(inputArray, start, mid, (2 * pos)+ 1)
		self.buildTree(inputArray, mid+1, end, (2 * pos)+ 2)
		self.segmentTree[pos] = min(self.segmentTree[2*pos+1], self.segmentTree[2*pos+2])

	def searchRange(self, qStart, qEnd, start, end, pos):
		# No overlap
		if qStart > end or qEnd < start:
			return self.MAX
		# Full overlap
		# What you are querying contains the current complete range
		elif qStart <= start and qEnd >=end:
			return self.segmentTree[pos]
		else:
			mid = (start+end)/2
			return min(self.searchRange(qStart, qEnd, start, mid, (2 * pos) +1),
				self.searchRange(qStart, qEnd, mid+1, end, (2*pos)+2)) 
		# Full Overlap
		# Partial overlap

if __name__ == "__main__":
	segmentTree = SegmentTree([1,2,3,4])
	print(segmentTree.searchRange(0,4,0,3,0))
	print(segmentTree.segmentTree)



