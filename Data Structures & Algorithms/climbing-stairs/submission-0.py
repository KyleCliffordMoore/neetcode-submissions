class Solution:
    
    

    def climbStairs(self, n: int) -> int:

        prev = {}
        def helper(n):
            if n <= 2:
                return n

            if n in prev:
                return prev[n]
            
            val = helper(n - 1) + helper(n - 2)

            prev[n] = val
            return val

        return helper(n)