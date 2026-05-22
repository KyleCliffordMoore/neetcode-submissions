class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 0
        right = num

        while left < right:
            mid = (left + right + 1) // 2

            if mid**2 <= num:
                left = mid
            else:
                right = mid - 1
        
        return left**2 == num