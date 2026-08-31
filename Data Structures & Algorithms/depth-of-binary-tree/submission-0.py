# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse_depth(root,0)

    def traverse_depth(self, node: TreeNode, curr_depth: int):
        if not node:
            return curr_depth

        left_depth = self.traverse_depth(node.left, curr_depth + 1)

        return max(left_depth, self.traverse_depth(node.right, curr_depth + 1))
        