# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(node, cur_max, cur_min):
            if not node:
                return True

            if node.val >= cur_max or node.val <= cur_min:
                return False

            left = bfs(node.left, node.val, cur_min)
            right = bfs(node.right, cur_max, node.val)

            return left and right

        return bfs(root, float('inf'), float('-inf'))