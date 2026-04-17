# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxValue = root.val

        def dfs(node):
            nonlocal maxValue
            if not node:
                return 0
            
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)

            summation = node.val
            summation += max(leftVal, 0)
            summation += max(rightVal, 0)

            maxValue = max(maxValue, summation)

            return node.val + max(0, leftVal, rightVal)

        
        dfs(root)
        return maxValue