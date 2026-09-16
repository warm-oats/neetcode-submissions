# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        def checkSubroot(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            left = checkSubroot(root.left, subRoot.left)
            right = checkSubroot(root.right, subRoot.right)
            isEqual = root.val == subRoot.val

            return isEqual and left and right

        return checkSubroot(root, subRoot) or left or right
