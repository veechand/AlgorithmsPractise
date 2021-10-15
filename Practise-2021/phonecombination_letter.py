class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        result_index = [1]*len(digits)
        current_letters = map(lambda x: letters_map[x], digits)
        if len(current_letters) == 0:
            return []
        if len(current_letters) == 1:
            return [l for l in current_letters[0]]
        else:
            while(len(current_letters) > 1):
                first, second, rem = current_letters[0], current_letters[1], current_letters[2:]
                result = self. merge_first_second(first, second)
                current_letters =  result + rem
            return current_letters[0]   
    
    def merge_first_second(self, first, second):
        result = []
        for i in first:
            for j in second:
                result.append(i+j)
        return [result]
