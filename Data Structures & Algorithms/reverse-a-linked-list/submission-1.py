# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        cur_head = ListNode(head.val)
        cur_node = head.next

        while cur_node:
            new_node = ListNode(cur_node.val)
            new_node.next = cur_head
            cur_head = new_node
            cur_node = cur_node.next
        
        return cur_head
