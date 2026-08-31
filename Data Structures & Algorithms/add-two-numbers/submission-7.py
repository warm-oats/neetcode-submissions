# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_list = ListNode()
        tail = head_list
        l1_curr = l1
        l2_curr = l2
        carry_arr = []

        while l1_curr and l2_curr:
            node_sum = l1_curr.val + l2_curr.val

            if carry_arr:
                node_sum += int(carry_arr.pop())

            carry_arr += list(str(node_sum))

            tail.next = ListNode(int(carry_arr.pop()))
            tail = tail.next

            l1_curr = l1_curr.next
            l2_curr = l2_curr.next

        while l1_curr:
            node_sum = l1_curr.val

            if carry_arr:
                node_sum = l1_curr.val + int(carry_arr.pop())

            carry_arr += list(str(node_sum))

            tail.next = ListNode(int(carry_arr.pop()))
            tail = tail.next

            l1_curr = l1_curr.next

        while l2_curr:
            node_sum = l2_curr.val 

            if carry_arr:
                node_sum = l2_curr.val + int(carry_arr.pop())

            carry_arr += list(str(node_sum))

            tail.next = ListNode(int(carry_arr.pop()))
            tail = tail.next

            l2_curr = l2_curr.next

        if carry_arr:
            tail.next = ListNode(int(carry_arr.pop()))

        return head_list.next



        