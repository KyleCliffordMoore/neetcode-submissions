class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        maxProf = 0

        for right in range(len(prices)):

            if prices[right] - prices[left] <= 0:
                left = right

            maxProf = max(maxProf, prices[right] - prices[left])
        
        return maxProf