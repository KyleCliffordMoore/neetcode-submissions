# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pindex = 0

        def dfs(preorder, inorder):
            nonlocal pindex
            # print(f"args: {preorder}, {pindex}, {inorder}")

            if not inorder:
                return None

            # Root        
            rootVal = preorder[pindex]
            pindex += 1
            root = TreeNode(rootVal)

            # Left Side
            l = []
            i = 0
            for ix, v in enumerate(inorder):
                i = ix
                if v == rootVal:
                    break
                l.append(v)
            
            # Right Side
            r = []
            for idx in range(i + 1, len(inorder)):
                r.append(inorder[idx])
            
            if pindex >= len(preorder):
                return root
            nextVal = preorder[pindex]

            root.left = dfs(preorder, l)
            root.right = dfs(preorder, r)
            
            return root
        
        return dfs(preorder, inorder)