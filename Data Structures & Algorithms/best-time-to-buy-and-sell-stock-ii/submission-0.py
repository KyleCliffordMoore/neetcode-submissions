class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        total = 0

        for right in prices[1:]:
            if left < right:
                total += right - left
            left = right
        
        return total