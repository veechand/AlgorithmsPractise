"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Given string S 
Dictionary D
Return longest words from dictionary that can be formed using S
Longest word with Smallest Lexiographical order

Create a set out of S
Sort the String
For word in sortedWords:
  if len(result) > 0 and len(word) < len(result[0]):
  break
  if word in S:
     result.append(word)
    
 
"""
from collections import defaultdict 
import copy

class Solution(object):
    def findLongestWord(self, s, words):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        #O(S) - Storage O(S) - Runtime
        wordAsSet = self.getWordsAsSet(s)
        #O(Wlog(W)) W - is len(words)
        sortedWords = sorted(words, key=lambda x: len(x), reverse=True) #TODO: Can we have two condition for sorting
        result = []
        for word in sortedWords: 
            print word #O(W)
            if len(result) > 0:
                print len(word) < len(result[0])
            if len(result) > 0 and len(word) < len(result[0]):
                break   
            if (self.isPossibleToCreate(word,copy.deepcopy(wordAsSet))):
                print "word", word
                result.append(word)
            print wordAsSet
        print result, sorted(result)
        return sorted(result)[0] if len(result) > 0 else ""
                
    def isPossibleToCreate(self,word, wordSet):
        maxPositionSeenSoFar = -1
        for w in word:
            if w not in wordSet or len(wordSet[w]) <= 0:
                return False
            curPosition = wordSet[w].pop(0)
            while (len(wordSet[w]) != 0 and curPosition < maxPositionSeenSoFar):
                curPosition = wordSet[w].pop(0)
            if maxPositionSeenSoFar > curPosition:
                return False
            maxPositionSeenSoFar = curPosition
        return True
                
    def getWordsAsSet(self, s):
        result = defaultdict(list)
        for index,w in enumerate(s):
            result[w].append(index)
        return result

if __name__ == "__main__":
    solution = Solution()
    s = "abce"
    words = ["abe","abc"]
    result = solution.findLongestWord(s, words)
    print(result)
        