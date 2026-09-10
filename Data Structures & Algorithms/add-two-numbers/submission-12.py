# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = False

        cur = dummy
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry

            new_node = ListNode(int(str(cur_sum)[-1]))
            cur.next = new_node
            cur = cur.next

            carry = (cur_sum >= 10)
            l1 = l1.next
            l2 = l2.next

        cur_node = l1 or l2
        while carry:
            cur_sum = 1

            if cur_node:
                cur_sum += cur_node.val
                cur_node = cur_node.next
            
            new_node = ListNode(int(str(cur_sum)[-1]))
            cur.next = new_node
            cur = cur.next
            carry = (cur_sum >= 10)

        if carry:
            cur.next = ListNode(1)
        cur.next = cur_node
        
        return dummy.next




