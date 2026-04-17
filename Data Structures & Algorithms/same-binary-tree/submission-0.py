# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def toList(node, l):
            
            if not node:
                l.append(None)
                return node

            l.append(node.val)

            toList(node.left, l)
            toList(node.right, l)
        
        lp = []
        toList(p, lp)
        lq = []
        toList(q, lq)

        return lp == lq