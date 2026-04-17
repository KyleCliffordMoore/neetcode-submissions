"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:    

    def updateMap(self, head, map_):

        curr = head
        while curr:
            map_[curr] = Node(curr.val)
            curr = curr.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        myMap = {}
        self.updateMap(head, myMap)
        
        curr = head
        while curr:
            
            newCurr = myMap[curr]

            if curr.next:
                newCurr.next = myMap[curr.next]
            else:
                 curr.next = None

            if curr.random:
                newCurr.random = myMap[curr.random]
            else:
                newCurr.random = None

            curr = curr.next
        
        return myMap[head]
