"""
https://leetcode.com/problems/ambiguous-coordinates/submissions/
"""
class Solution(object):
    def __init__(self):
        self.outputFormat = "({}, {})"
        self.DOT = "."
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s[1:len(s)-1]
        commaPos = 1
        result = []
        while (commaPos <= len(s) - 1):
            xCordinate = s[:commaPos]
            yCordinate = s[commaPos:]
            # if isValid(xCordinate) and isValid(yCordinate):
            #     result.append(self.outputFormat.format(xCordinate, yCordinate))
            if True:
                possibleXCordinates = [xCordinate] + self.getPossibleDotValues(xCordinate)
                possibleYCordinates = [yCordinate] + self.getPossibleDotValues(yCordinate)
                for x in possibleXCordinates:
                    if not self.isValid(x):
                        continue
                    for y in possibleYCordinates:
                        if self.isValid(y):
                            result.append(self.outputFormat.format(x, y))
            commaPos += 1
        return result
                    
    def getPossibleDotValues(self, cordinate):
        result = []
        dotPosition = 1
        while dotPosition < len(cordinate):
            curCordinate = cordinate[:dotPosition]+self.DOT+cordinate[dotPosition:]
            if not self.isValid(curCordinate):
                return result
            result.append(curCordinate)
            dotPosition += 1
        return result
    def isValid(self, cordinate):
        if len(cordinate) == 0:
            return False
        if cordinate[0] == self.DOT: #This is redundant
            return False
        if cordinate[0] == "0" and len(cordinate) > 1 and cordinate[1] != self.DOT:
            return False
        endPos = cordinate.find(self.DOT) if cordinate.find(self.DOT) != -1 else len(cordinate)
        tempCordinate = cordinate[:endPos]
        if int(tempCordinate) == 0 and len(tempCordinate) != 1:
            return False
        tempCordinate = cordinate[endPos+1:]
        # if len(tempCordinate)>0 and tempCordinate.count("0") == len(tempCordinate):
        if len(tempCordinate) > 0 and int(tempCordinate) == 0:
            return False
        if tempCordinate.endswith("0"):
            return False
        return True
        
    