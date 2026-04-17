class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def toIdx(s):
            return ord(s) - ord('a')
        
        if len(s1) > len(s2):
            return False
        
        S1ARR = [0] * 26
        for char in s1:
            S1ARR[toIdx(char)] += 1

        freqWindow = [0] * 26
        for char in s2[:len(s1)]:
            freqWindow[toIdx(char)] += 1

        if S1ARR == freqWindow:
            return True

        for i in range(len(s1), len(s2)):
            freqWindow[toIdx(s2[i])] += 1
            freqWindow[toIdx(s2[i - len(s1)])] -= 1

            if S1ARR == freqWindow:
                return True

        return False