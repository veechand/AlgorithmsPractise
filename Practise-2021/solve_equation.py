from collections import defaultdict 

class Equation(object):
	"""
	 Stores the equation 5 = x + 3 as [5,=,x,+,3]
	"""
	representation = None
	number_of_variables = None
	resolved = False

	def __init__(self, equation_as_string):
		self.SYMBOLS = ['=', '+']
		self.form_equation(equation_as_string)
	def is_variable(self, value):
		 return not value.isdigit() and value not in self.SYMBOLS
	def form_equation(self, equation_as_string):
		number_of_variables = 0
		representation = []
		for i in equation_as_string:
			representation.append(i)
			if self.is_variable(i):
				number_of_variables += 1
		self.number_of_variables = number_of_variables
		self.representation = representation
	"""
	Equation is a single equation
	variable_values is a map of variables to values
	"""
	def solve_equation(self, variable_values={}):
		self.replace_equation_with_values(variable_values)
		if self.number_of_variables != 1:
			print "ERROR:Can't solve now"
			return {}
		else:
			variable = self.get_variable()
			total_sum = self.get_sum()
			if self.is_variable(self.representation[0]):
				return {self.representation[0]:total_sum}
			else:
				value = int(self.representation[0]) - total_sum
				return {variable:value}

	def get_sum(self):
		total_sum = 0
		seen = False
		for i in self.representation:
			if i == "=":
				seen = True
			if not seen:
				continue
			if not self.is_variable(i) and i not in self.SYMBOLS:
				total_sum += int(i)
		return total_sum

	def get_variable(self):
		for i in self.representation:
			if self.is_variable(i):
				return i

	def replace_equation_with_values(self, variable_values):
		for index in range(0, len(self.representation)):
			if self.is_variable(self.representation[index]) and self.representation[index] in variable_values:
				self.representation[index] = str(variable_values[self.representation[index]])
				self.number_of_variables -= 1



class EquationSolver(object):
	def solve_equation(self, equations):
		equation_objects = self.transform_to_equation_objects(equations)
		grouped_equation_objects  = self.group_equation(equation_objects)
		result = {}
		cur_result = self.solve_equation_at_each_level(grouped_equation_objects)
		while (cur_result is not None and len(cur_result) > 0):
			result.update(cur_result)
			cur_result = self.solve_equation_at_each_level(grouped_equation_objects)
		return result
	
	def solve_equation_at_each_level(self, grouped_equation_objects):
		sorted_keys = sorted(grouped_equation_objects)
		result = {}
		for key in sorted_keys:
			for equation in grouped_equation_objects[key]:
				if equation.resolved:
					continue
				cur_result = equation.solve_equation(result)
				if (cur_result is not None and len(cur_result) != 0):
					equation.resolved=True	
					result.update(cur_result)
		return result
	def group_equation(self, equation_objects):
		result = defaultdict(list)
		for equation in equation_objects:
			result[equation.number_of_variables].append(equation)
		return result
	def transform_to_equation_objects(self, equations):
		equation_objects = []
		for equation in equations:
			equation_objects.append(Equation(equation))
		return equation_objects
if __name__ == '__main__':
	# equation = Equation("5=x+3")
	# print equation.representation, equation.number_of_variables
	# equation = Equation("3=y+1")
	# print equation.number_of_variables
	# print(equation.solve_equation(equation, {'x':2}))
	# print equation.representation, equation.number_of_variables
	# print (equation.get_variable(equation))
	equation_solver = EquationSolver()
	result = equation_solver.solve_equation(["5=x+2", "y=x+2", "z=x+y+1"])
	print(result)
	print(equation_solver.solve_equation(["5=x+2", "y=x+2", "z=y+1", "a=z+z+z"]))
	print(equation_solver.solve_equation(["5=x+2", "y=x+2", "a=z+z+z"]))