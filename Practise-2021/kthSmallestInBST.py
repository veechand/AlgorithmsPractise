# Definition for a binary tree node.

"""
Inorder  and inorder[k-1] <- O(n)
Number of elements in the tree
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.annotateTreeWithLeftAndRightNodes(root)
        self.printTree(root)
    def printTree(self, root):
        print root.val, root.leftNumberOfNodes, root.rightNumberOfNodes
        
    def annotateTreeWithLeftAndRightNodes(self,root):
        if root is None:
            return 0
        totalNodesOnLeft = self.annotateTreeWithLeftAndRightNodes(root.left)
        root.leftNumberOfNodes = totalNodesOnLeft
        totalNodesOnRight = self.annotateTreeWithLeftAndRightNodes(root.right)
        root.rightNumberOfNodes = totalNodesOnRight
        return root.leftNumberOfNodes + root.rightNumberOfNodes + 1
        