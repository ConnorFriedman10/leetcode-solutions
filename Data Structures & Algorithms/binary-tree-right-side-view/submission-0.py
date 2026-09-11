# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #do dfs, but focus on the right side instead of the left, only append if nothing else is on level
        if not root:
            return []
        
        flist = []
        def traverse(root, level):
            if root:
                if len(flist) == level:
                    flist.append(root.val)
                traverse(root.right, level + 1)
                traverse(root.left, level + 1)

        traverse(root, 0)
        return flist