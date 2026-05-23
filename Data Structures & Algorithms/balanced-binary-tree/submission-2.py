# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True

        def getHeight(node):
            nonlocal isBalanced

            # Handle None Case
            if not node:
                return 0
            
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right) 

            print(leftHeight, rightHeight)

            if leftHeight == -1 or rightHeight == -1:
                # print("what?")
                return -1

            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
                return -1
                

            return max(leftHeight, rightHeight) + 1

        print(getHeight(root))

        
        return isBalanced
        