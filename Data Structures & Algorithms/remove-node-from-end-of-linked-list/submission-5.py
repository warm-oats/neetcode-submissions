# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0

        if not head.next:
            return None

        itr = head

        while itr:
            list_length += 1
            itr = itr.next

        index = list_length - n 
        curr = head
        curr_prev = head
        curr_nxt = head

        # If removed node is the head
        if n == list_length:
            nxt = head.next
            head.next = None
            return nxt

        for num in range(index):
            curr_prev = curr
            curr = curr.next
            curr_nxt = curr.next

        curr_prev.next = curr_nxt
        curr.next = None

        return head


        



        