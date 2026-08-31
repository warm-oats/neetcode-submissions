# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        nodes_left = 0
        itr = head

        while itr:
            nodes_left += 1
            itr = itr.next
        
        chain_head = None
        new_head = None
        reverse_head = head
        count = 0
        prev,curr = None, reverse_head

        while count < k and reverse_head:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

            if count == k:
                if not new_head:
                    new_head = prev
                if not chain_head:
                    chain_head = reverse_head
                else:
                    chain_head.next = prev
                    chain_head = reverse_head
                reverse_head.next = curr
                reverse_head = curr

                prev = None
                nodes_left -= count
                count = 0
            
            if nodes_left < k:
                return new_head

        