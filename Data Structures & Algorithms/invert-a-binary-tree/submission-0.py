# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, tree_node: TreeNode):
        if not tree_node:
            return

        node_left = tree_node.left
        tree_node.left = tree_node.right
        tree_node.right = node_left

        self.invert(tree_node.left)
        self.invert(tree_node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        curr_node = root

        self.invert(curr_node)

        return root

