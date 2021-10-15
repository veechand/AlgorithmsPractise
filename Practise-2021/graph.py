class Graph:
	nodes = []
	def __init__(self, nodes):
		self.nodes = nodes
class Node:
	value = None
	children = []
	def __init__(self, value, children):
		self.value = value
		self.children = children
	def add_child(self, child):
		self.children.append(child)

class GraphUtility:

	def create_graph(self):
		a_node = Node("A",[])
		b_node = Node("B",[])
		c_node = Node("C",[])
		d_node = Node("D",[])
		e_node = Node("E",[])
		f_node = Node("F",[])
		a_node.add_child(b_node)
		b_node.add_child(c_node)
		c_node.add_child(d_node)
		c_node.add_child(f_node)
		d_node.add_child(e_node)
		return Graph([a_node, b_node, c_node, d_node, e_node, f_node])

	def create_graph_with_cycle(self):
		a_node = Node("A",[])
		b_node = Node("B",[])
		c_node = Node("C",[])
		d_node = Node("D",[])
		e_node = Node("E",[])
		f_node = Node("F",[])
		a_node.add_child(b_node)
		b_node.add_child(c_node)
		c_node.add_child(d_node)
		c_node.add_child(f_node)
		d_node.add_child(e_node)
		f_node.add_child(a_node)
		return Graph([a_node, b_node, c_node, d_node, e_node, f_node])

	def create_complex_graph(self):
		node_1 = Node("1",[])
		node_2 = Node("2",[])
		node_3 = Node("3",[])
		node_4 = Node("4",[])
		node_5 = Node("5",[])
		node_6 = Node("6",[])
		node_8 = Node("8",[])
		node_11 = Node("11",[])
		node_1.add_child(node_3)
		node_1.add_child(node_2)
		node_3.add_child(node_4)
		node_3.add_child(node_8)
		node_6.add_child(node_3)
		node_5.add_child(node_6)
		node_8.add_child(node_11)
		return Graph([node_1, node_2, node_3, node_4, node_5, node_6, node_8, node_11])


	def dfs(self, graph):
		visited = []
		for node in graph.nodes:
			if node not in visited:
				self.__dfs__(node, visited) # Taking the first node as root and iterating with empty array

	def __dfs__(self, node, visited):
		if node.value in visited:
			return
		visited.append(node.value)
		for child in node.children:
			self.__dfs__(child, visited)
		print(node.value)

if __name__ =='__main__':
	graph_utility = GraphUtility()
	graph = graph_utility.create_complex_graph()
	graph_utility.dfs(graph)



