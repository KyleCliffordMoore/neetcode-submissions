# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        head = ListNode(-9999)
        curr3 = head
        carry = 0

        while curr1 and curr2:
            total = curr2.val + curr1.val + carry

            val = total % 10
            carry = total // 10

            curr3.next = ListNode(val)

            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next

        while curr1:
            total = curr1.val + carry
            val = total % 10
            carry = total // 10
            curr3.next = ListNode(val)
            curr1 = curr1.next
            curr3 = curr3.next

        while curr2:
            total = curr2.val + carry
            val = total % 10
            carry = total // 10
            curr3.next = ListNode(val)
            curr2 = curr2.next
            curr3 = curr3.next

        #deal with final carry
        if carry > 0:
            curr3.next = ListNode(carry)


        head = head.next
        return head