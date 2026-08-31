# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        right_nodes = []

        if not root:
            return not root and not subRoot

        while root or right_nodes:
            if root.val == subRoot.val and self.dfs(root, subRoot):
                return True

            if root.right:
                right_nodes.append(root.right)

            if not root.left and right_nodes:
                root = right_nodes.pop()
            else:
                root = root.left

        return False

    def dfs(self, node: TreeNode, sub_node: TreeNode):
        if not node and not sub_node:
            return True

        if node and not sub_node or sub_node and not node or node.val != sub_node.val:
            return False

        left_check = self.dfs(node.left, sub_node.left)
        right_check = self.dfs(node.right, sub_node.right)

        return left_check and right_check 