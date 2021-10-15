"""
Sliding window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""

class SegmentTree(object):
	def __init__(self, inputList):
		segmentTreeSize = self.getSegmentTreeSize(inputList)
		self.MIN = -(2**32)
		self.segmentTree = [self.MIN]*segmentTreeSize
		self.buildTree(inputList, 0 , len(inputList) - 1, 0)
		print self.segmentTree
	def buildTree(self, inputList, start, end, pos):
		if start == end:
			self.segmentTree[pos] = inputList[start]
			return
		mid = start + ((end-start)/2)
		self.buildTree(inputList, start, mid, 2*pos + 1)
		self.buildTree(inputList, mid + 1, end, 2*pos + 2)
		self.segmentTree[pos] = max(self.segmentTree[2*pos + 1], self.segmentTree[2*pos + 2])
	def queryTree(self, qStartPos, qEndPos, start,end,pos):
		# no overlap
		if qEndPos < start or qStartPos > end:
			return self.MIN
		# Full overlap
		if qStartPos <= start and qEndPos>=end:
			return self.segmentTree[pos]
		# Partial overlap
		else:
			mid = start + ((end-start)/2)
			return max(self.queryTree(qStartPos, qEndPos, start, mid, 2*pos + 1),
			self.queryTree(qStartPos, qEndPos, mid+1, end, 2*pos + 2))


	def getSegmentTreeSize(self, inputList):
		inputListLength = self.nextPowerOfTwo(len(inputList))
		return (2*inputListLength) - 1
	def nextPowerOfTwo(self, number):
		if number == 0:
			return number
		if number & (number - 1) == 0:
			return number
		while(number & (number - 1) != 0):
			number = number & (number - 1)
		return number << 1 

class Solution(object):
	def maxSlidingWindow(self, nums, k):
		segmentTree = SegmentTree(nums)
		result = []
		for i in range(0, len(nums)):
			if i + (k-1) < len(nums):
				result.append(segmentTree.queryTree(i, i+(k-1), 0, len(nums) -1 , 0))
		return result
if __name__ == "__main__":
	inputList = [1,3,-1,-3,5,3,6,7]
	segmentTree = SegmentTree(inputList)
	k = 3
	result = []
	for i in range(0, len(inputList)):
		if i + (k-1) < len(inputList):
			result.append(segmentTree.queryTree(i, i+(k-1), 0, len(inputList) -1 , 0))
	# result = segmentTree.queryTree(4, 6, 0, len(inputList) - 1, 0)
	print result
	print result
