# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_length = 0
        
        def dfs(node: TreeNode):
            if not node:
                return 0

            left_length = dfs(node.left)
            right_length = dfs(node.right)

            nonlocal longest_length
            longest_length = max(longest_length, left_length + right_length)

            return max(left_length, right_length) + 1

        dfs(root)

        return longest_length