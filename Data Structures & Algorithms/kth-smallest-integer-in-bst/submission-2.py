# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []

        def dfs(node: TreeNode):
            if not node:
                return

            heapq.heappush(min_heap, node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        res = 0

        for count in range(k):
            res = heapq.heappop(min_heap)

        return res