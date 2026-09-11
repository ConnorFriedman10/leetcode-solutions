# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodedict = []

        def traverse(root, level):
            if root:
                if level + 1 > len(nodedict):
                    nodedict.append([root.val])
                else:
                    nodedict[level].append(root.val)
                
                traverse(root.left, level + 1)
                traverse(root.right, level + 1)
        
        traverse(root, 0)
        # return [nodedict[x] for x in range(len(nodedict))]
        return nodedict
        
                
