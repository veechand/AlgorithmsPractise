from graph import GraphUtility
from collections import defaultdict

class TreeNode:
	value = None
	leftChild = None
	rightChild = None
	def __init__(self, value, leftChild = None, rightChild = None):
		self.value = value
		self.leftChild = leftChild
		self.rightChild = rightChild

class TreeUtility:
	def __init__(self):
		pass
	def createTree(self):
		node_a = TreeNode("A")
		node_b = TreeNode("B")
		node_c = TreeNode("C")
		node_d = TreeNode("D")
		node_e = TreeNode("E")
		node_f = TreeNode("F")
		node_g = TreeNode("G")

		node_a.leftChild = node_b
		node_a.rightChild = node_c
		node_b.leftChild = node_d
		node_c.rightChild = node_e
		node_d.leftChild = node_f
		node_d.rightChild = node_g

		return node_a

	def createExamTree(self):
		node_1 = TreeNode(1)
		node_2 = TreeNode(2)
		node_3 = TreeNode(3)
		node_4 = TreeNode(4)
		node_5 = TreeNode(5)
		node_6 = TreeNode(6)
		node_7 = TreeNode(7)
		node_1.leftChild = node_2
		node_1.rightChild = node_3
		node_2.leftChild = node_4
		node_2.rightChild = node_5
		node_3.leftChild = node_6
		node_3.rightChild = node_7
		return node_1

	def createBottomViewExamTree(self):
		node_20 = TreeNode(20)
		node_8 = TreeNode(8)
		node_22 = TreeNode(22)
		node_25 = TreeNode(25)
		node_5 = TreeNode(5)
		node_3 = TreeNode(3)
		node_10 = TreeNode(10)
		node_14 = TreeNode(14)
		node_20.leftChild = node_8
		node_20.rightChild = node_22
		node_8.leftChild = node_5
		node_8.rightChild = node_3
		node_3.rightChild = node_10
		node_3.leftChild = node_10
		node_3.rightChild = node_14
		node_22.rightChild = node_25
		return node_20

class Solution(object):
	
	def printTopView(self, tree):
		self.__printTopView__(tree, 0, set())

	def __printTopView__(self, node, depth, visitedDepths):
		if not node:
			return
		if depth not in visitedDepths:
			print node.value,
			visitedDepths.add(depth)

		self.__printTopView__(node.leftChild, depth - 1, visitedDepths)
		self.__printTopView__(node.rightChild, depth + 1, visitedDepths)

	def printBottomView(self, tree):
		result = defaultdict(list)
		self.__printBottomView__(tree, 0, result)
		for key, value in sorted(result.items(), key= lambda x: x[0], reverse=False):
			print value[0],

	def __printBottomView__(self, node, depth, output):
		if not node:
			return
		output[depth].append(node.value)
		self.__printBottomView__(node.leftChild, depth - 1, output)
		self.__printBottomView__(node.rightChild, depth + 1, output)

	def removePathsLessThanK(self, root, k):
		nodeLengths = {}
		self.__findLengthsOfNodes__(root, 0, nodeLengths)
		self.__printRemovableNodeNames__(nodeLengths)

	def __printRemovableNodeNames__(self, nodeLengths):
		for key,value in nodeLengths.items():
				if value < k:
					print key,
		print "======="
	
	def __findLengthsOfNodes__(self, root, curLength, nodeLengths):
		if not root:
			return 0
		leftTreeLength = self.__findLengthsOfNodes__(root.leftChild, curLength + 1, nodeLengths)
		rightTreeLength = self.__findLengthsOfNodes__(root.rightChild, curLength + 1, nodeLengths)
		thisNodeLength = max(leftTreeLength, rightTreeLength, curLength)
		nodeLengths[root.value] = thisNodeLength
		return thisNodeLength

if __name__ == "__main__":

	treeUtility = TreeUtility()
	tree = treeUtility.createBottomViewExamTree()
	solution = Solution()
	solution.printTopView(tree);
	print "======="
	solution.printBottomView(tree)
	tree = treeUtility.createTree()
	print "======="
	solution.removePathsLessThanK(tree, 3)
