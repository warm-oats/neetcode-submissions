# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        if p and not q or q and not p or q.val != p.val:
            return False

        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)

        return left_check and right_check
