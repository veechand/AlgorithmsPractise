
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sortedWords = words
        wordsInBit = self.convertWordsToBit(sortedWords)
        maxProduct=0
        for i in range(len(sortedWords)):
            for j in range(i+1,len(sortedWords)):
                if (self.isDistinct(wordsInBit[i],wordsInBit[j])):
                    product = len(sortedWords[i]) * len(sortedWords[j])
                    maxProduct = max(maxProduct, product)
        return maxProduct
    
    def convertWordsToBit(self,sortedWords):
        result = [0 for i in range(len(sortedWords))]
        for index, word in enumerate(sortedWords):
            result[index] = self.convertWordToBit(word)
        return result
    def convertWordToBit(self, word):
        result = 0
        for w in word:
            number = ord(w) - ord('a')
            result |= (1 << number)
        return result
    def isDistinct(self, number1, number2):
        result = number1 & number2
        return True if result == 0 else False
            
    # def isDistinct(self, word1, word2):
    #     word1Chars = set()
    #     for w in word1:
    #         word1Chars.add(w)
    #     for w in word2:
    #         if w in word1Chars:
    #             return False
    #     return True
if __name__ == "__main__":
    solution = Solution()
    testCases = [
      (["abcw","baz","foo","bar","xtfn","abcdef"],16),
      (["a","ab","abc","d","cd","bcd","abcd"],4),   
      (["a","aa","aaa","aaaa"],0),
      ]
    for testCase in testCases:
        print(testCase[1] == solution.maxProduct(testCase[0]))