class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0

        while j < len(s) and i < len(g):

            if s[j] >= g[i]:
                # Assigning the cookie
                i += 1
            j += 1
        return i