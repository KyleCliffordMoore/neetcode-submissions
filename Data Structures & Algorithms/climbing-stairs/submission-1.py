class Solution:
    
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        a = 1
        b = 2
        for i in range(2, n):
            b = a + b
            a = b - a
        
        return b