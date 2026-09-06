# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_node = dummy_head

        while list1 and list2:
            next_node = None

            if list1.val <= list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            
            cur_node.next = next_node
            cur_node = next_node
        
        cur_node.next = list1 or list2
        
        return dummy_head.next