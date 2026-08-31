# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced_tree = True

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            nonlocal balanced_tree
            
            if abs(left_height - right_height) > 1:
                balanced_tree = False
            
            return 1 + max(left_height,right_height)

        dfs(root)

        return balanced_tree