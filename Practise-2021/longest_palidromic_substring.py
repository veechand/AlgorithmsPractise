"""
Given a string s, return the longest palindromic substring in s.

Palindrome: Reverse should be same
S = [] : Return : []
S = [ab] : Return 0

What to do is to assume everypoint is middle of the palidrome. 
Try to expand each side, make sure to check the edges, 
Once the string is not same then (j-i) + 1 is the longest palindrom

For example given: abcbaa
2 
i = 0
j = 4

Complexity: N * N = N2 
abacdb
Expand around the center

Test cases:
 aba
 ab
 abba

max_length = 0
for index, str in enumerate(string):
	cur_length = expand_around_i(index, str)
	max_length = max(cur_length, cur_length)
def expand_around_i(index, str):
	i = index - 1
	j = index + 1
	ans1 = expand_around_i_j(i, j, 1 str)
	ans2 = expand_around_i_j(index-1, index, 0 str)
	max(ans1, ans2)

def expand_around_i_j(i, j, length, str):

	while (i>=0 and j<len(str)):
		if str[i] == str[j]:
			length += 2
			i --
			j ++
	return length


"""

class Solution(object):
	def __init__(self):
		pass
	def find_longest_palindrome(self, str_input):
		max_palindromic_string = ""
		for index in range(len(str_input)):
			cur_length = self.expand_around_index(index, str_input)
			max_palindromic_string = cur_length if len(cur_length) > len(max_palindromic_string) else max_palindromic_string
			# max_length = max(cur_length,max_length)
		return max_palindromic_string
	def expand_around_index(self, index, str_input):
		answer1 = self.expand_around_i_j(index-1, index+1, 1, str_input[index], str_input)
		answer2 = self.expand_around_i_j(index-1, index, 0, "", str_input)
		return answer1 if len(answer1) > len(answer2) else answer2
		# return max(len(answer1, answer2)

	def expand_around_i_j(self, i, j, initial_length, initial_string, str_input):
		result = initial_length
		result_string = initial_string
		while (i>=0 and j < len(str_input)):
			if str_input[i] == str_input[j]:
				result += 2
				result_string = str_input[i:j+1]
				i -= 1
				j += 1
			else:
				break
		return result_string

if __name__ == "__main__":
	solution = Solution()
	str_input = "aba"
	print("aba" == solution.find_longest_palindrome("aba"))
	print("abba" == solution.find_longest_palindrome("abba"))
	print("" == solution.find_longest_palindrome(""))
	print("a" == solution.find_longest_palindrome("ab") or "b" == solution.find_longest_palindrome("ab"))
	print("aba" == solution.find_longest_palindrome("babad") or "bab" == solution.find_longest_palindrome("babad"))
	print("bb" == solution.find_longest_palindrome("cbbd"))
	print(solution.find_longest_palindrome("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))


