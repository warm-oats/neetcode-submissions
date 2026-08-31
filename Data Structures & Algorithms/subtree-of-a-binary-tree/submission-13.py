# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def same_tree(root: TreeNode, node: TreeNode):
            if not root and not node:
                return True

            if not root or not node or root.val != node.val:
                return False

            return same_tree(root.left, node.left) and same_tree(root.right, node.right)

        if same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

            