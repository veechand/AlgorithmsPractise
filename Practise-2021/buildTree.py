from datetime import datetime
>/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.constructBinarySearchTree(preorder, inorder, 0, len(inorder)-1)

    def constructBinarySearchTree(self, preorder, inorder, start, end):
    	if (start > end):
    		return None

    	root =  TreeNode(preorder[0])
    	inorder_root_index = inorder.index(preorder[0])
    	preorder_index = 1 + (inorder_root_index - start)
    	root.left = self.constructBinarySearchTree(preorder[1:preorder_index], inorder, start, inorder_root_index-1)
    	root.right = self.constructBinarySearchTree(preorder[preorder_index:], inorder, inorder_root_index + 1, end)
    	return root

    def printInorder(self, root):
    	if not root:
    		return
    	self.printInorder(root.left)
    	print(root.val)
    	self.printInorder(root.right)


solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
inorder = [1,3,4,6,7,8,10,13,14]
preorder =[8,3,1,6,4,7,10,14,13]
root = solution.buildTree(preorder, inorder)
solution.printInorder(root)
