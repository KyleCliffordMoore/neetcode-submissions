class Solution:
    def minOperations(self, s: str) -> int:
        starting0Score = 0
        starting1Score = 0

        flip = 0
        for char in s:
            if flip == 0:
                if char == "1":
                    starting0Score += 1
                else:
                    starting1Score += 1
            else:
                if char == "0":
                    starting0Score += 1
                else:
                    starting1Score += 1
                    
            flip = (flip + 1) % 2
        
        print(starting0Score, starting1Score)        
        return min(starting0Score, starting1Score)