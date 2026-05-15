class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left = 0
        right = 0
        ans = ""

        while left < len(word1) and right < len(word2):
            ans += word1[left] + word2[right]
            left += 1
            right += 1

        # print(ans)
        if left < len(word1):
            # print("left:", word1[left:])
            ans += word1[left:]
        if right < len(word2):
            # print("right:", word2[right:])
            ans += word2[right:]
        
        return ans