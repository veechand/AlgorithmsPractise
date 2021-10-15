"""
https://leetcode.com/problems/wiggle-sort-ii/

Wiggle Sort of an integer Array
nums[0]<nums[1]>nums[2]<nums[3]
4 5 3

3 4 5
3 5 4

7 17 23 43 64

1 3 2 2 3 1
1 1 2 2 3 3

1 3 1 3 2 2

7 98 17 64 23 43

7 23 17 64 43 98

Can there be duplicates 
1 5 1 1 6 4
1 1 1 4 5 6
1 6 1 5 1 4
+ive and -ive numbers
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums)
        middle = len(nums) / 2 if len(nums) % 2 == 0 else (len(nums)/2) + 1
        i = 0 j = middle
        result = []
        while (i<middle and j<len(nums)):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        while i<middle:
            result.append(nums[i])
            i+=1
        nums=result
        