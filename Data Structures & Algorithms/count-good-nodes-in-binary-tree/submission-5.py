# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode, max_path_val: int):
            if not node:
                return None

            if node.val >= max_path_val:
                nonlocal res
                res += 1

            new_path_max = max(max_path_val, node.val)

            dfs(node.left, new_path_max)
            dfs(node.right, new_path_max)

        dfs(root, root.val)

        return res