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

    def lenLinkedList(self, head: Optional[ListNode]) -> int:
        count = 0

        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        return count

    def splitIthLinkedList(self, head: Optional[ListNode], index: int) -> Optional[ListNode]:
        count = 0

        curr = head
        last = None
        while curr:

            if count == index:
                if last:
                    last.next = None
                return curr

            count += 1
            last = curr
            curr = curr.next
        
        return None

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = last
            last = curr
            curr = temp
        return last

    def mergeTwoLinkedLists(self, headLeft, headRight):

        isLeft = False
        curr = headLeft
        head = curr
        currRight = headRight
        currLeft = headLeft.next

        while currLeft and currRight:
            if isLeft:
                curr.next = currLeft
                currLeft = currLeft.next
            else:
                curr.next = currRight
                currRight = currRight.next
            curr = curr.next
            isLeft = not isLeft

        if currRight:
            curr.next = currRight

        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.lenLinkedList(head)
        if length == 1:
            return
        firstHalfLen = length // 2
        
        mid = self.splitIthLinkedList(head, firstHalfLen)
        # self.printLinkedList(head)
        revList = self.reverseLinkedList(mid)
        # self.printLinkedList(revList)
        self.mergeTwoLinkedLists(head, revList)
        # self.printLinkedList()
