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
                return 'n'

            left_subtree = preorder(node.left)
            right_subtree = preorder(node.right)

            return str(node.val) + ',' + left_subtree + ',' + right_subtree

        return preorder(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_list = data.split(',')
        self.index = 0

        def buildTree():
            if node_list[self.index] == 'n':
                return None

            curr_node = TreeNode(int(node_list[self.index]))
            self.index += 1
            curr_node.left = buildTree()
            self.index += 1
            curr_node.right = buildTree()

            return curr_node

        return buildTree()

        

        
            
                

            



        






        

        







        




