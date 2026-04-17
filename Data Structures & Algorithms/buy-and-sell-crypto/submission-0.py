class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        least = prices[0]
        largestDiff = 0

        for price in prices:
            currDiff = price - least
            if currDiff > largestDiff:
                largestDiff = currDiff
            if price < least:
                least = price
        
        return largestDiff