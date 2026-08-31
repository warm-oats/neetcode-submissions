# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node: TreeNode):
            if not node:
                return 'N'

            left_subtree = preorder(node.left)
            right_subtree = preorder(node.right)

            return str(node.val) + ';' + left_subtree + ';' + right_subtree

        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals_arr = data.split(';')
        node_index = 0

        def buildTree():
            nonlocal node_index

            if vals_arr[node_index] == 'N':
                return None

            cur_node = TreeNode(int(vals_arr[node_index]))
            node_index += 1
            cur_node.left = buildTree()
            node_index += 1
            cur_node.right = buildTree()

            return cur_node

        return buildTree()
