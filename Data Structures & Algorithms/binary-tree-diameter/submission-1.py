# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        best = 0

        def dfs(node):
            nonlocal best
            
            # Handle None Case
            if not node:
                return 0
            
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            
            currentDepth = max(leftDepth, rightDepth) + 1
            currentDist = leftDepth + rightDepth

            best = max(best, currentDepth - 1)
            best = max(best, currentDist)

            print(f"Val {node.val}:", leftDepth, rightDepth, currentDepth, currentDist, best)

            return currentDepth

        dfs(root)
        return best