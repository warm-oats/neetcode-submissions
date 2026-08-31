# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)

        return root
    
    def invert(self, node: TreeNode):
        if not node:
            return
            
        left_node = node.left
        node.left = node.right
        node.right = left_node

        self.invert(node.left)
        self.invert(node.right)
