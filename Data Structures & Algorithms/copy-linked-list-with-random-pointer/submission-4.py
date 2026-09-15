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
        list_map = defaultdict(lambda: Node(0))

        prev, cur = dummy, head
        while cur:
            new_node = Node(cur.val)

            prev.next = new_node
            list_map[cur] = new_node
            
            prev = prev.next
            cur = cur.next

        cur = dummy.next
        while head:

            if not head.random:
                mapped_rand_node = None
            else:
                mapped_rand_node = list_map[head.random]

            cur.random = mapped_rand_node
                
            cur = cur.next
            head = head.next
        
        return dummy.next






        