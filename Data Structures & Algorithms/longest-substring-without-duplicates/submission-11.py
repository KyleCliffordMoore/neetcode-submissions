class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}          # char -> last index
        left = 0
        best = 0

        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1    # slide window past duplicate

            last[c] = right
            best = max(best, right - left + 1)

        return best