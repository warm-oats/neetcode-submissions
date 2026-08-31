# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        def dfs(node: TreeNode):
            if not node:
                return 0

            max_left = max(dfs(node.left), 0)
            max_right = max(dfs(node.right), 0)

            nonlocal res

            res = max(res, node.val + max_left + max_right)

            return node.val + max(max_left, max_right)

        dfs(root)

        return res