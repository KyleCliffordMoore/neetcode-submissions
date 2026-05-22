class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        calc = lambda val: val * (val + 1) // 2

        left = 0
        right = n

        while left < right:
            mid = (left + right + 1) // 2

            num_stairs = calc(mid)
            
            if num_stairs <= n:
                left = mid
            else:
                right = mid - 1
        
        return left