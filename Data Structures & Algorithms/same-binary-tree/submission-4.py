# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)

    def dfs(self, p, q):
        if not p or not q:
            if p != q:
                return False

            return True

        if q.val != p.val:
            return False

        left_identical = self.dfs(p.left,q.left)
        right_identical = self.dfs(p.right,q.right)

        return left_identical and right_identical
