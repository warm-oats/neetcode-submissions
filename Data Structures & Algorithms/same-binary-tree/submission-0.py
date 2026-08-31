# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.same_tree = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p,q)

        return self.same_tree

    def dfs(self, p, q):
        if not p or not q:
            if p != q:
                self.same_tree = False
                
            return

        if q.val != p.val:
            self.same_tree = False

        self.dfs(p.left,q.left)
        self.dfs(p.right,q.right)
