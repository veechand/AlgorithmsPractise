from collections import deque

"""
 DOESN"T WORK if the INPUT and OUTPUT of a operatio is 
 > 10
"""

class Solution(object):

	PRECEDENCE_LEVELS = [
	       ("*", "/"),
	       ("+", "-")
		]
	OPERATORS = ("*", "/", "+", "-")
	stack = deque()
	def calculate(self, s):
		value = self.strip_space(s)
		if len(value) <= 0:
			return -1
		for cur_precedence_level in self.PRECEDENCE_LEVELS:
			self.calculate_for_precedence(value, cur_precedence_level)
			value = self.calculate_string()
			print(value)
			if (len(value) == 1):
				break
		return value

	def strip_space(self, s):
		value = ""
		for i in range(0,len(s)):
			if s[i] == " ":
				continue
			else:
				value += s[i]
		return value

	def calculate_string(self):
		value = ""
		for i in range(len(self.stack)):
			value += self.stack.popleft()
		return value

	def operate(self, operator, value1, value2):
		print(operator, value1, value2)
		if (operator == "+"):
			return value1 + value2 
		if (operator == "-"):
			return value1 - value2 
		if (operator == "*"):
			return value1 * value2 
		if (operator == "/"):
			return value1 / value2 

	def calculate_for_precedence(self, s, cur_precedence_level):
		self.stack.append(s[0])
		for i in range(1, len(s)):
			if s[i] in self.OPERATORS:
				self.stack.append(s[i])
			else:
				if self.stack[-1] in cur_precedence_level:
					value = self.operate(self.stack.pop(),int(self.stack.pop()),int(s[i])) 
					self.stack.append(str(value))
				else:
					self.stack.append(s[i])


solution = Solution()
print(solution.calculate("2+3*4"))
# print(solution.calculate("2+3*2"))
# print(solution.calculate("3*2+2*2-2"))
