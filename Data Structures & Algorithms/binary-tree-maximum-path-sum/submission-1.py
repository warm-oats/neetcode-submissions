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

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            left_max = max(left_sum, 0)
            right_max = max(right_sum, 0)

            nonlocal res
            res = max(res, node.val + right_max + left_max)
            return node.val + max(left_max, right_max)

        dfs(root)

        return res


