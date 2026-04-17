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
            if not node:
                return 0

            ld = dfs(node.left)
            rd = dfs(node.right)

            best = max(ld + rd, best)
            return max(ld, rd) + 1

        dfs(root)
        return best