# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printLinkedList(self, head):
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        print('Linked List:', arr)

    def lenLinkedList(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def removeNodeFromLinkedList(self, head, index):
        count = 1
        curr = head
        newhead = head
        last = None
        while curr:

            if count == index:
                # print(curr.val)
                if last:
                    last.next = curr.next
                else:
                    newhead = curr.next
                return newhead

            count += 1
            last = curr
            curr = curr.next
        return newhead

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = self.lenLinkedList(head)
        if length == 1:
            return None
        index = length - n + 1

        h = self.removeNodeFromLinkedList(head, index)
        # self.printLinkedList(head)
        return h




