# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def bfs(node, cur_max):
            nonlocal count 

            if not node:
                return

            if node.val >= cur_max:
                count += 1

            bfs(node.left, max(cur_max, node.val))
            bfs(node.right, max(cur_max, node.val))
        
        bfs(root, root.val)

        return count
