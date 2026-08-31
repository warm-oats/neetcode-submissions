# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        num_arr = []
        dummy = ListNode()
        tail = dummy

        for head in lists:
            itr = head

            while itr:
                num_arr.append(itr.val)
                tail.next = itr
                tail = tail.next
                itr = itr.next

        num_arr.sort()

        itr = dummy.next

        for num in num_arr:
            itr.val = num
            itr = itr.next

        return dummy.next

        