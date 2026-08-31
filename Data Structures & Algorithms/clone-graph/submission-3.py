"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clone_map = defaultdict(list)

        clone_map[node] = Node(node.val)
        root = clone_map[node]
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in clone_map:
                    clone_neighbor = Node(neighbor.val)
                    clone_map[neighbor] = clone_neighbor
                    
                    queue.append(neighbor)

                clone_map[node].neighbors.append(clone_map[neighbor])

        return root