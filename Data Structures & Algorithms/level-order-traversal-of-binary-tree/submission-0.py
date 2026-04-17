# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        queue.append((root, 0))

        ans = []
        height = -1
        while queue:
            (node, depth) = queue.popleft()
            
            if not node:
                continue

            if depth > height:
                ans.append([])
                height += 1
            
            ans[height].append(node.val)

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return ans