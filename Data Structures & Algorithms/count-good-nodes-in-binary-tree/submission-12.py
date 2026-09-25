# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def bfs(node, cur_max, count):
            if not node:
                return 0

            if node.val >= cur_max:
                count += 1

            left = bfs(node.left, max(cur_max, node.val), 0)
            right = bfs(node.right, max(cur_max, node.val), 0)

            return count + left + right
        
        return bfs(root, root.val, 0)
