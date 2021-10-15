from collections import Counter as C

class Solution:
    def isPossible(self, nums):
        h = C(nums)
        one = two = three = 0
        print h
        for current in range(nums[0], nums[-1] + 1):
            x = h[current]
            x -= one + two
            if x < 0:
                return False
            c = min(x, three)
            one, two, three = x - c, one, two + c
            print c, one, two, three
        return one == two == 0

Solution().isPossible([1,2,3,3,4,5])