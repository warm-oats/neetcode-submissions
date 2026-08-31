# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur_node = root

        while cur_node:
            if cur_node.val < p.val and cur_node.val < q.val:
                cur_node = cur_node.right
            elif cur_node.val > p.val and cur_node.val > q.val:
                cur_node = cur_node.left
            else:
                return cur_node