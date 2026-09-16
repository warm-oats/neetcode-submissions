# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(cur_node):
            nonlocal diameter

            if not cur_node:
                return 0

            left = dfs(cur_node.left)
            right = dfs(cur_node.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return diameter