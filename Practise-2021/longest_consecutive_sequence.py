class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbersAsSet = self.getNumbersAsSet(nums)
        longestConsecutiveNumber = {}
        maxCount = 0
        
        for num in nums:
            count = 1
            nextNumber = num + 1
            while (nextNumber in numbersAsSet):
                if nextNumber in longestConsecutiveNumber:
                    count += longestConsecutiveNumber[nextNumber]
                    break
                count += 1
                nextNumber += 1
            self.updateLongestConsecutiveNumber(longestConsecutiveNumber, num, nextNumber, count)
            # longestConsecutiveNumber[num] = count
            maxCount = max(count, maxCount)
        return maxCount
    
    def updateLongestConsecutiveNumber(self, longestConsecutiveNumber, num, nextNumber, count):
        for n in range(num, nextNumber + 1):
            longestConsecutiveNumber[n] = count
            count -= 1
    def getNumbersAsSet(self, nums):
        result = set()
        for num in nums:
            result.add(num)
        return result
if __name__ == "__main__":
    testCases = [
      ([100,4,200,1,3,2],4),
      (range(1,100),99)
    ]
    solution = Solution()
    for testCase in testCases:
        print(testCase[1] == solution.longestConsecutive(testCase[0]))