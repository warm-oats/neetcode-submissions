# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float('-inf')

        def dfs(node: TreeNode):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            max_sum = 1 + left_sum + right_sum 

            nonlocal diameter
            diameter = max(diameter, max_sum)

            return 1 + max(left_sum, right_sum)

        dfs(root)

        return diameter - 1