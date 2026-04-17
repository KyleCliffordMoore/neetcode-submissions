# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node1, node2):
            if (not node1) and node2:
                return False
            if node1 and not node2:
                return False
            if (not node1) and (not node2):
                return True
            if node1.val != node2.val:
                return False
            
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        
        if (not root) and subRoot:
            return False
        if root and (not subRoot):
            return True
        if (not root) and (not subRoot):
            return True

        return True if isSame(root, subRoot) else self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
