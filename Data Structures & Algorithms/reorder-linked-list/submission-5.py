# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printLinkedList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        print("Linked List:", arr)



    def reorderList(self, head: Optional[ListNode]) -> None:

        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        sec = slow_ptr.next
        slow_ptr.next = None

        def reverse(curr):

            last = None
            while curr:
                temp = curr.next
                curr.next = last
                last = curr
                curr = temp
            
            return last
        
        left = head
        right = reverse(sec)

        self.printLinkedList(left)
        self.printLinkedList(right)

        dummy = ListNode(-1)
        curr = dummy

        while right:

            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next

        head = dummy.next

        self.printLinkedList(head)



