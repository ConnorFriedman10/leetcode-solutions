# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                currnode = q.popleft()
                level.append(currnode.val)
                if currnode.left:
                    q.append(currnode.left)
                if currnode.right:
                    q.append(currnode.right)
            res.append(level)
        
        return res
