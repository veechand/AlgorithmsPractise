class DisjointSetNode:
	value = None
	rank = 0
	parent = None
	def __init__(self, value, parent = None, rank = 0):
		self.value = value
		self.rank = rank
		self.parent = parent

class DisjointSets:
	value_node_mapping = {}

	def union(self,node_value1, node_value2):
		if node_value1 not in self.value_node_mapping or node_value2 not in self.value_node_mapping:
			raise("makeset not yet called")
		node1 = self.find_set(node_value1)
		node2 = self.find_set(node_value2)
		if not node1 or not node2:
			raise ("Node doesn't exist")
		if (node1 == node2):
			print ("Already merged... ")
			return self.find_set(node1)
		if node1.rank < node2.rank:
			node1.parent = node2
			return node2
		elif node2.rank < node1.rank:
			node2.parent = node1
			return node1
		else:
			node1.rank +=1
			node2.parent = node1
			return node1


	def find_set(self,node_value):
		if node_value not in self.value_node_mapping:
			return None
		node = self.value_node_mapping[node_value]
		while (node.parent != node):
			node = node.parent
		return node

	def makeset(self,node_value):
		if node_value in self.value_node_mapping:
			return
		node = DisjointSetNode(node_value)
		node.parent = node
		self.value_node_mapping[node_value] = node
		return node

if __name__ == "__main__":
	disjointsets = DisjointSets()
	disjointsets.makeset(10)
	disjointsets.makeset(20)
	print(disjointsets.find_set(10).value)
	print(disjointsets.find_set(20).value)
	disjointsets.union(10,20)
	print(disjointsets.find_set(10).value)