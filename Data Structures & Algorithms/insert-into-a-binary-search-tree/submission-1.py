# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def insert(parent_node: TreeNode, cur_node: TreeNode, new_node: TreeNode):
            if not cur_node:
                if new_node.val < parent_node.val:
                    parent_node.left = new_node
                else:
                    parent_node.right = new_node

                return

            if new_node.val < cur_node.val:
                insert(cur_node, cur_node.left, new_node)
            else:
                insert(cur_node, cur_node.right, new_node)

        insert(None, root, TreeNode(val))

        return root
