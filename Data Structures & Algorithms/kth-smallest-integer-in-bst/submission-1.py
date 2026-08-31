# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return []
            
            left_side = dfs(node.left)
            right_side = dfs(node.right)

            left_side.append(node.val)
            left_side += right_side

            return left_side

        res = dfs(root)
        return res[k - 1]
