"""
 Inorder successor of a node
 In Binary Tree, Inorder successor of a node is the next node in Inorder traversal 
 of the Binary Tree. Inorder Successor is NULL for the last node in Inorder traversal. 
In Binary Search Tree, Inorder Successor of
 an input node can also be defined as the node with the smallest key greater 
 than the key of the input node. So, it is sometimes important to find next node in sorted order.

 inorder_successor(graph, key)
 Will the key always exists in the Graph - No
Smallest node greater than the given key :
	class Node: 
		value = None
		left = None
		right = None
 Solution(object):
    current_smaller = None
    if root is None:
    	return
	if root > key:
	   self.current_smaller = root
	   search_left(root.left, key)
	else root <= key:
	   search_right(root.right, key)        

	   7
    5       9 

  4   6         10

Key 2
current_smaller = None, 7, 5
root = 7,5,4
"""
class Node:
	value = None
	left = None
	right = None
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class Solution(object):
	def __init__(self):
		self.result = None
	def find_inorder_successor(self, root, key):
		if root is None:
			return
		elif root.value > key:
			self.result = root
			self.find_inorder_successor(root.left, key)
		else:
			self.find_inorder_successor(root.right, key)

if __name__ == "__main__":
	solution  = Solution()
	node4 = Node(4, left=None, right=None)
	node6 = Node(6, left=None, right=None)
	node5 = Node(5, left=node4, right=node6)
	node10 = Node(10, left=None, right=None)
	node9 = Node(9, left=None, right=node10)
	node7 = Node(7, left=node5, right=node9)
	key = 9
	solution.find_inorder_successor(node7, key)
	print solution.result.value


