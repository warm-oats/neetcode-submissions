# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root.val >= p.val and root.val <= q.val or root.val <= p.val and root.val >= q.val:
            return root

        left_check = self.lowestCommonAncestor(root.left, p, q)
        right_check = self.lowestCommonAncestor(root.right, p, q)

        if left_check:
            return left_check
        
        if right_check:
            return right_check