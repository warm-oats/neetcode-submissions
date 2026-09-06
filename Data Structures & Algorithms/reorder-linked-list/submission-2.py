# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_stack = []
        stack_size = 0
        i = 0

        cur = head
        while cur:
            node_stack.append(cur)
            cur = cur.next
            stack_size += 1

        while stack_size > 1 and head:
            if i % 2 == 0:
                next_node = node_stack.pop()
                next_next_node = head.next
                head.next = next_node
                next_node.next = next_next_node
            
            stack_size -= 1
            i += 1
            head = head.next

        head.next = None
        

        
