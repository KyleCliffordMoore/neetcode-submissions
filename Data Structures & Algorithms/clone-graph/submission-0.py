"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_to_new = {}

        def bfs(first_pass=True):
            nonlocal old_to_new
            visited = set()
            old_queue = deque([ node ])

            while old_queue:

                old = old_queue.popleft()
                if not old or old in visited:
                    continue
                visited.add(old)

                new = None
                if first_pass:
                    old_to_new[old] = Node(old.val)
                else:
                    new = old_to_new[old]

                for neighbor in old.neighbors:

                    if not neighbor:
                        continue

                    if new:
                        new.neighbors.append(old_to_new[neighbor])
                    old_queue.append(neighbor)
    

        bfs()
        bfs(False)

        return old_to_new[node] if node else node