# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(left, right):
            if (not left) and (not right):
                return True
            if (not left) or (not right):
                return False
            if left.val != right.val:
                return False

            return isSame(left.left, right.left) and isSame(left.right, right.right)
        
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if isSame(curr, subRoot):
                return True

            if not curr:
                continue

            queue.append(curr.left)
            queue.append(curr.right)

        return False