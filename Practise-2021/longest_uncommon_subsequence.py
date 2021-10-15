class TrieNode(object):
    name = None
    endingStrings = []
    children = {}
    def __init__(self, name, endingStrings, children, pathOfStrings):
        self.name = name
        self.endingStrings = endingStrings
        self.pathOfStrings = pathOfStrings
        self.children = children
        
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        for s in strs:
            self.addToTrie(s)
        self.DFSTrie(self.root,0)
        return self.longestSequence
    def __init__(self):
        self.root = TrieNode("", [],{},[])
        self.longestSequence = -1
    def DFSTrie(self,root, length):
        if len(root.pathOfStrings) == 1:
            self.longestSequence = max(self.longestSequence, length)
        for key,child in root.children.items():
            self.DFSTrie(child, length + 1)
        
    def addToTrie(self, inputStr):
        curNode = self.root
        for w in inputStr:
            if w not in curNode.children:
                node = TrieNode(w, [],{},[])
                curNode.children[w] = node    
            curNode = curNode.children[w]
            curNode.pathOfStrings.append(w)
        curNode.endingStrings.append(inputStr)

if __name__ == "__main__":
    strs = ["aba","aba","aa"]
    solution = Solution()
    solution.findLUSlength(strs)