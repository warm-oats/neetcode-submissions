# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(node: TreeNode, depth: int):
            if not node:
                return

            if len(res) - 1 < depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)

            bfs(node.left, depth + 1)
            bfs(node.right, depth + 1)

        bfs(root, 0)

        return res