# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        list_length = 1

        while fast and fast.next:
            if fast.next.next: # Odd number of elements
                list_length += 2
                fast = fast.next.next
                slow = slow.next
            else: # Even number of elements
                list_length += 1
                fast = fast.next
                slow = slow.next

        # Reverse the last portion of linked list
        prev,curr = None,slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        last_index = list_length - 1
        mid_index = math.floor(list_length / 2)
        head = head
        tail = prev

        while last_index > mid_index:
            head_nxt = head.next
            tail_nxt = tail.next

            head.next = tail
            tail.next = head_nxt

            head = head_nxt
            tail = tail_nxt

            last_index -= 1




        
        