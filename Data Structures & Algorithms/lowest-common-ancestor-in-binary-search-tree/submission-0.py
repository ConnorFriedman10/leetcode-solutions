# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #traverse tree until you reach nodes p and q
        #until then, for each node go left and right to see if either one contains p or q, if both do make that the new minimum
        #go over each side, if one side contains both stop it
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        if root.val <= p.val and root.val > q.val:
            return root
        
        if root.val > p.val and root.val <= q.val:
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return self.lowestCommonAncestor(root.left, p, q)

    def containsNode(self, root, node) -> Optional[TreeNode]:
        if not root:
            return False
        
        if root.val == node.val:
            return True
        
        return self.containsNode(root.left, node) or self.containsNode(root.right, node)
        

        
    # leftq = self.containsNode(root.left, q)
    # rightq = self.containsNode(root.right, q)
    # if root.val == p.val: #if the current root is an ancestor
    #     if (leftq or rightq):
    #         return root
    
    # # leftp = self.containsNode(root.left, p)
    # # rightp = self.containsNode(root.right, p)
    # if root.val == q.val: #if the current root is an ancestor
    #     if (leftp or rightp):
    #         return root
    
    # if root.val <= p.val and root.val <= q.val:
    #     return self.lowestCommonAncestor(root.right, p, q)
    
    # if root.val > p.val and root.val > q.val:
    #     return self.lowestCommonAncestor(root.left, p, q)
        