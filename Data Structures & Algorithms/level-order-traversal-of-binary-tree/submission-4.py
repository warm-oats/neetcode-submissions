# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(cur_node, depth):
            if not cur_node:
                return None

            if len(res) <= depth:
                res.append([])
            
            res[depth].append(cur_node.val)

            bfs(cur_node.left, depth + 1)
            bfs(cur_node.right, depth + 1)

        bfs(root, 0)

        return res