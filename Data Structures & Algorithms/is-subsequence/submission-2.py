class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for schar in s:
            idx = t.find(schar, idx, len(t))
            if idx == -1:
                return False
            idx += 1
        return True