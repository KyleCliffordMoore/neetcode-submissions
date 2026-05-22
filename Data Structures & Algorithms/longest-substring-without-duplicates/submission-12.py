class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        maxLen = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maxLen = max(maxLen, len(chars))
        
        return maxLen