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
        node_hashmap = defaultdict(Node)

        if not head:
            return None

        index,itr = 0,head
        prev = None
        while itr:
            new_node = Node(itr.val,None,itr.random)

            if prev:
                prev.next = new_node

            node_hashmap[itr] = new_node
            prev = new_node
            itr = itr.next
            index += 1

        random_itr = head
        itr = node_hashmap.get(head)

        while itr:
            if random_itr.random:
                itr.random = node_hashmap[random_itr.random]
            
            random_itr = random_itr.next
            itr = itr.next

        return node_hashmap[head]

        
        
        


        

        