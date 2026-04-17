class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev2 = 0  # dp[0] conceptually
        prev1 = 0  # dp[1] conceptually

        for c in cost:
            cur = c + min(prev1, prev2)
            prev2, prev1 = prev1, cur

        # Top is one step past the last index
        return min(prev1, prev2)