# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we'll use dfs to traverse the tree
        return self.traverse( root, root.val)
        
    def traverse(self, root, mx):
        if not root:
            return 0
        
        if root.val >= mx:
            mx = root.val
            return 1 + self.traverse(root.left, mx) + self.traverse(root.right, mx)
        
        return 0 + self.traverse(root.left, mx) + self.traverse(root.right, mx)