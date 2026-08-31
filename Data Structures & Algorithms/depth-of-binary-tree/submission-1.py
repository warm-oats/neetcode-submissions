# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_depth(root,0)
    
    def find_depth(self, node:TreeNode, depth):
        if not node:
            return depth

        left_depth = self.find_depth(node.left,depth + 1)
        right_depth = self.find_depth(node.right,depth + 1)

        return max(left_depth, right_depth)