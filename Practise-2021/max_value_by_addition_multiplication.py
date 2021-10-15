"""
Your input is a double array, and you can use *, +, -, and () parenthesis anywhere to create and output the maximum possible value.

Ex:
input is {3,4,5,1} --> output: 72
input is {1,1,1,5} --> output: 15

Follow up, if there are numbers <0


For positive numbers:
  Take a pass and remove all 0 and add 1 to the neighboring small number
  Multiply all other numbers
For Negative numbers:
  Take a pass and remove all 0 and add 1 to the neighboring small number
  This gets tricky since multiplication of two negative numbers can give positive result

  -2 + -2 * -3 * 2 * 3
  -2 6 2 3

  When negative numbers come
     - Surronded by positive number  3 -8 2  - Add with surronding numbers 
     - Surronded by negative number  -3 -3 -8 -4- Multiply the two biggest and add with the smaller - -3 - -3 * -8
     - One side by negative number  -3 -3 8  - Muliply the number

-4 -3 -8

When a negative number is seen,  
   negative_number_count = get all the surronding negative number 
   if the len(negative_number_count) %2 == 0:
   	    multiply all
   else:
   	  min = remove the one lowest number
      multiply everything else and add to min
      return value, negative_number_count

	numbers = filter(numbers)
	numbers = addOne(numbers)
result = 0
for i in numbers:
	if i > 0:
		result = result if result == 0 else result * i
	if i<0:
		getValue(numbers, i)

def getValue(self, numbers, i):
	negativeNumbers = []
	while i<len(numbers) and numbers[i] < 0:
		 	negativeNumbers.append(i)
	if len(negativeNumbers) % 2  == 0:
		multiplyAll
"""
from functools import reduce

class Solution(object):
	def __init__(self):
		pass
	def findMaximumValue(self, numbers):
		numbers = filter(lambda x: x != 0, numbers)
		numbers = self.addOne( numbers)
		numbers = filter(lambda x: x != 0, numbers)
		result = 0
		index = 0
		while index < len(numbers):
			print "index, numbers[index], result", index, numbers[index], result	
			if numbers[index] > 0:
				result = numbers[index] if result == 0 else result * numbers[index]
				index += 1
			else:
				negativeNumberCount, value = self.getValue(index, numbers)
				if value > 0:
					result = result * value if result != 0 else value
				if value < 0:
					result += value
				index += negativeNumberCount
		return result

	def getValue(self, index, numbers):
		negativeNumbers = []
		result = None
		while index < len(numbers) and numbers[index] < 0:
			negativeNumbers.append(numbers[index])
			index += 1
		negativeNumberLength = len(negativeNumbers)
		if len(negativeNumbers) % 2 == 0:
			result = reduce((lambda x, y: x * y), negativeNumbers)
		else:
			minElement = max(negativeNumbers)
			negativeNumbers.remove(minElement)
			result = reduce((lambda x, y: x * y), negativeNumbers) if len(negativeNumbers) > 0 else 0
			result += minElement
		return (negativeNumberLength, result)

	def addOne(self, numbers):
		output = []
		index = 0
		while index < len(numbers):
			num = numbers[index]
			if num == 1:
				rightNumber = None
				leftNumber = None
				if (index-1)>=0:
					leftNumber = numbers[index-1]
				if index+1 < len(numbers):
					rightNumber = numbers[index+1]
				if leftNumber and rightNumber and leftNumber > 0 and rightNumber >0:
					minValue = min(leftNumber, rightNumber)
					if minValue == leftNumber:
						output[-1] = output[-1] + 1
					else:
						numbers[index+1] = rightNumber + 1
				elif leftNumber and leftNumber > 0:
					output[-1] = output[-1] + 1
				elif rightNumber and rightNumber > 0:
					numbers[index+1] = rightNumber + 1
				elif leftNumber and rightNumber and leftNumber < 0 and rightNumber < 0:
					if leftNumber == -1:
						output[-1] = output[-1] + 1
					elif rightNumber == -1:
						numbers[index+1] = rightNumber + 1
				elif leftNumber and leftNumber<0:
					output[-1] = output[-1] * 1
				elif rightNumber and rightNumber<0:
					numbers[index+1] = rightNumber * 1
			else:
				output.append(num)
			index += 1
		return output




if __name__ == "__main__":
	solution = Solution()
	numbers = [
		([-2, -2, -3, 2, 3],24),
		[-2, 0, -3, 2, 3],
		[3,4,5,1],
		[1,4,5,1],
		[-1,1,2,3], # Doesn't work
		[-2,1,5,2],
		[2,1,-5,2],
		[-2, 0, 1, 2, 3],

	]
	result = solution.findMaximumValue([-2, 0, 1, 2, 3])
	print result
	# for number in numbers:
	# 	result = solution.findMaximumValue(number)
	# 	print result