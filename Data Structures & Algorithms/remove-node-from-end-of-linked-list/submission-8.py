# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        list_len = 0

        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        prev = dummy
        while head:
            if list_len == n:
                prev.next = head.next
                break
            
            prev = head
            head = head.next
            list_len -= 1

        return dummy.next





