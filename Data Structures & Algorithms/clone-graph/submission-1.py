"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = defaultdict(list)
        root = None

        if not node:
            return None

        def dfs(node: Node):
            if node in clone_map:
                return clone_map[node]

            clone = Node(node.val)
            clone_map[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

        