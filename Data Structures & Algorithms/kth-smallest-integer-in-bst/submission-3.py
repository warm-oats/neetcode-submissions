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

            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            left_subtree.append(node.val)
            left_subtree += right_subtree

            return left_subtree

        return dfs(root)[k-1]