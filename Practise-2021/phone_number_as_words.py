"""
 Phone number and words
 Given a Phone number and words, Return the list of words that are reprsented by that phone number

 For example:
  flowers: 3569377
Given a phone number (3569377) find all possible words.
Few clarification - The number should be of the same length as the word- Not necessarily because it can be contained in one of the possible word
For example: if word is possible word then or is contained in it

One is backtracking:
 356
 def jkl mno

 djm djn djo dkm dkn dko dlm dln dlo
 ejm ejn ejo ekm ekn eko elm eln elo
 fjm fjn fjo fkm fkn fko flm fln flo

These are possible words: Now for each word in the list iterate and find does 
any of these possible words contains that 
possible_words.contains(word) != -1
then add it to the list

Have a dictionary of letter to number mapping
For each word in the list: {
	form the number
	final_number.indexof(number)!= -1:
	    add that possible_words
}
if the list of words are smaller
a 2
b 2             3569377
c 2
d 3
e 3
f 3
g 3
h 4
i 4
j  4

Build a trie for the given number
covert each letters to numbers, find it falls in to any of the node in the trie
"""
import string

class TrieNode(object):
	value = None
	children = None
	endLabel = None
	possibleEndLabels = []
	def __init__(self, value, children = {}, kids = [], endLabel=[]):
		self.value = value
		self.children = children
		self.kids = kids
		self.endLabel = endLabel


class Solution(object):
	
	def __init__(self):
		self.root = self.getNode("")
		self.wordToNumberDict = self.getWordToNumberDict()
		self.wordToNumber = self.getWordToNumber()
		self.longestPalindrome = ""

	def getNode(self, value):
		return TrieNode(value, {},[None] * len(range(0,10)),[])

	def getWordToNumber(self):
		return ["2","2","2","3","3","3","4","4","4","5","5","5","6","6","6","7","7","7","7","8","8","8","9","9","9","9"]
	def getWordToNumberDict(self):
		result = {}
		result['a'] = "2"
		result['b'] = "2"
		# NOT COMPLETE
		return result

	def addToTrie(self, input_number, endLabel = ""):
		cur_node = self.root
		for number in input_number: # number as string
			# if cur_node.kids[int(number)] != None:
			if number in cur_node.children:
				cur_node = cur_node.children[number]
				# cur_node = cur_node.kids[int(number)]
			else:
				node = self.getNode(number)
				cur_node.children[number] = node
				# cur_node.kids[int(number)] = node
				cur_node = cur_node.children[number]
				# cur_node = cur_node.kids[int(number)]
		cur_node.endLabel.append(endLabel)
	def printTrie(self, root):
		for value, child in self.root.children["9"].items():
			print value
		# print root.value," CHildrens are "
		# for value,child in root.children.items():
		# 	self.printTrie(child)
		
	def convertWordToNumber(self, word):
		result = []
		for c in word:
			# result.append(self.wordToNumberDict[c])
			result.append(self.wordToNumber[ord(c.lower()) - ord('a')])
		return result

	def isNumberPartOfTrie(self, number, root):
		if root is None and len(number) != 0:
			return False
		if len(number) == 0:
			return True
		# nextRoot = root.children[number[0]] if number[0] in root.children else None
		nextRoot = root.kids[int(number[0])]
		return self.isNumberPartOfTrie(number[1:], nextRoot)

	def addSuffixesToTrie(self, userInput, endLabel=""):
		for i in range(len(userInput)-1, -1,-1):
			self.addToTrie(userInput[i:], endLabel)

	def getLongestPalindrome(self, root):
		self.updatePossibleEndLabels(self.root)
		self.findingLongestPalindrome(root, "")
		print self.longestPalindrome

	def findingLongestPalindrome(self, root, cur_output):
		if len(root.possibleEndLabels) == 2 and  len(cur_output) > len(self.longestPalindrome):
			self.longestPalindrome = cur_output
		for key, child in root.children.items():
			self.findingLongestPalindrome(child, cur_output+key)
		
	def updatePossibleEndLabels(self, root):
		possibleEndLabels = []
		for key, child in root.children.items():
			endLabel = self.updatePossibleEndLabels(child)
			possibleEndLabels.extend(endLabel)
		if len(root.endLabel) > 0:
			possibleEndLabels.extend(root.endLabel)
		root.possibleEndLabels = possibleEndLabels
		return possibleEndLabels

def checkPhoneNumberAsWord():
	solution = Solution()
	number = "3569377"
	words = ["flow","flowers","fuck"]

	solution.addSuffixesToTrie(number)

	# solution.printTrie(solution.root)
	wordNumbers = []
	for word in words:
		wordNumbers.append(solution.convertWordToNumber(word))
	output = []
	for i,wordNumber in enumerate(wordNumbers):
		if solution.isNumberPartOfTrie(wordNumber, solution.root):
			output.append(words[i])
	print output

def getLongestPalindrome():
	solution = Solution()
	inputString = "23"
	solution.addSuffixesToTrie(inputString, "straight")
	solution.addSuffixesToTrie(inputString[::-1], "reversed")
	solution.getLongestPalindrome(solution.root)
	# solution.getLongestPalindrome()

if __name__ == "__main__":

	# checkPhoneNumberAsWord()
	getLongestPalindrome()


	