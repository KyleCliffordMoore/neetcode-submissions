# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque([])
        queue.append((root, 1))

        maximums = []

        while queue:
            (node, depth) = queue.popleft()
            if not node:
                continue

            if depth > len(maximums):
                maximums.append(node.val)

            maximums[depth - 1] = node.val

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        
        return maximums