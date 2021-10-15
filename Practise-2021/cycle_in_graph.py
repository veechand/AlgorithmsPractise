# Detecting cycles in graph using disjoint set

from graph import Graph, GraphUtility
from disjoint_sets import DisjointSets

graph_utility = GraphUtility()
disjoint_sets = DisjointSets()

def find_cycle_using_disjoint_sets(graph):
	for node in graph.nodes:
		disjoint_sets.makeset(node.value)
	for node in graph.nodes:
		for c in node.children:
			set0 = disjoint_sets.find_set(node.value)
			set1 = disjoint_sets.find_set(c.value)
			if (set0.value == set1.value):
				print("There's cycle")
				return
			else:
				disjoint_sets.union(node.value, c.value)

find_cycle_using_disjoint_sets(graph_utility.create_graph())
# set0 = disjoint_sets.find_set(vertices[0].value)
# set1 = disjoint_sets.find_set(vertices[1].value)
# union_set = disjoint_sets.union(set0.value, set1.value)

# for v in vertices[2:]:
# 	set0 = disjoint_sets.find_set(union_set.value)
# 	set1 = disjoint_sets.find_set(v.value)
# 	if (set0.value == set1.value):
# 		print("There's cycle")
# 		break
# 	else:
# 		disjoint_sets.union(union_set.value, v.value)
