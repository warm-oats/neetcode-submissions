# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def get_heights(cur_node):
            nonlocal balanced

            if not cur_node:
                return 0

            left_height = get_heights(cur_node.left)
            right_height = get_heights(cur_node.right)

            if abs(left_height - right_height) > 1:
                balanced = False

            return 1 + max(left_height, right_height)

        get_heights(root)
        
        return balanced
        