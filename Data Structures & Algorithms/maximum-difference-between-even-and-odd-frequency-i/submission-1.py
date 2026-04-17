class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = [0] * 26

        def toIdx(char):
            return ord(char) - ord('a')

        for char in s:
            freqs[toIdx(char)] += 1
        
        maxOdd = float('-inf')
        minEven = float('inf')
        for freq in freqs:
            if freq == 0:
                continue
            if freq % 2 == 0:
                minEven = min(minEven, freq)
            else:
                maxOdd = max(maxOdd, freq)
        
        return maxOdd - minEven