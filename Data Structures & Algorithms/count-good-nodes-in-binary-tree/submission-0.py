# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        
        def dfs(node, largest):
            nonlocal good

            if not node:
                return
            
            # Yay
            if node.val >= largest:
                good += 1
                largest = node.val
            
            dfs(node.left, largest)
            dfs(node.right, largest)

        dfs(root, -101) # min value that it can be is -100 thus -101
        return good