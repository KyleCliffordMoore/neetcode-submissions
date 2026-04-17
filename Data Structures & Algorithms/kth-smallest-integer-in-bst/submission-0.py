# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        curr = root
        while curr or stack:

            # Go left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Do stack logic
            k -= 1
            curr = stack.pop()

            if k == 0:
                return curr.val

            # Go right 1
            curr = curr.right

        return -1