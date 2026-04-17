class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqs = [0] * 26
        def toIdx(char):
            return ord(char) - ord('a')

        def formBalloon():
            for c in "balloon":
                freqs[toIdx(c)] -= 1
                if freqs[toIdx(c)] < 0:
                    return False
            return True
        
        for c in text:
            freqs[toIdx(c)] += 1
        
        k = 0
        while formBalloon():
            k += 1

        return k 