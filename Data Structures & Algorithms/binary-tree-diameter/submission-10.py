# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: TreeNode):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left_sum + right_sum)

            return 1 + max(left_sum, right_sum)

        dfs(root)

        return diameter