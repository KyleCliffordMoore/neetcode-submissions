class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left, right = 0, 0
        ans = ""

        while left < len(word1) and right < len(word2):
            ans += word1[left] + word2[right]
            left += 1
            right += 1

        ans += word1[left:]  if left  < len(word1) else ""
        ans += word2[right:] if right < len(word2) else ""
        
        return ans