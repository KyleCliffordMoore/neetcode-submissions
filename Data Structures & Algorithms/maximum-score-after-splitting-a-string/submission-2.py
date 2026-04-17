class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        for char in s:
            if char == "1":
                right += 1
    
        largest = 0
        for char in s[:-1]:
            if char == "0":
                left += 1
            if char == "1":
                right -= 1
            largest = max(largest, left + right)

        return largest