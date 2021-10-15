"""
https://leetcode.com/problems/remove-duplicate-letters/
"""
from collections import defaultdict 

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        duplicateCountMap = self.getDuplicateCountMap(s)
        result = ""
        mustRemove = set()
        for index,c in enumerate(s):
            if c in mustRemove:
                continue
            if duplicateCountMap[c] > 1:
                nextNonDuplicateNumber = self.getNextNonDuplicateNumber(c,s,index,duplicateCountMap)
                if nextNonDuplicateNumber is not None:
                    if nextNonDuplicateNumber > c:
                        result += c
                        mustRemove.add(c)
                    else:
                        duplicateCountMap[c] -= 1 # Reducing the duplicate count a c is not added in result
                else:    # nextNonDuplicateNumber is None
                    print "ERROR: Not expected"
            else: # if the number is not duplicate
                result += c
        return result        
    
    def getNextNonDuplicateNumber(self, inputChar, inputString, startIndex, duplicateCountMap):
        inputString = inputString[startIndex+1:]
        for c in inputString:
            if duplicateCountMap[c] == 1:
                return c
        # Can this be zero, no because theorectically this will be called only when there's a duplicate, so atleast 
        # the inputChar should be there
        return inputString[0]
    
    def getDuplicateCountMap(self, s):
        result = defaultdict(int)
        for c in s:
            result[c] += 1
        return result
        