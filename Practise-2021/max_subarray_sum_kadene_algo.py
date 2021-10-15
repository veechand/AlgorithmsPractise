class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Implementation of Kadane's Algorithm
        Refer https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        """
        max_so_far = -(sys.maxint) - 1
        max_ending_here = 0
        for i in range(0,len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here <=0:
                max_ending_here = 0
        return max_so_far
        
        