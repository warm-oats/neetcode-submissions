"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        node_map = {}

        prev, cur = dummy, head
        while cur:
            new_node = Node(cur.val)

            prev.next = new_node
            node_map[cur] = new_node

            prev = new_node
            cur = cur.next

        cur = dummy.next
        while head:

            if head.random:
                cur.random = node_map[head.random]

            head = head.next
            cur = cur.next
        
        return dummy.next


            







        