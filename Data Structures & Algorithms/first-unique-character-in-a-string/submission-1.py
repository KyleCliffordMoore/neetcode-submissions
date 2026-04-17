class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = Counter(s)

        for i, char in enumerate(s):
            if freqs[char] == 1:
                return i
        
        return -1