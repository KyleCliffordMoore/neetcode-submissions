class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxValue = nums[0]
        currValue = nums[0]

        for i in range(len(nums) - 1):
            left = nums[i]
            right = nums[i + 1]

            if left < right:
                currValue += right
            else:
                currValue = right
            
            maxValue = max(maxValue, currValue)
        
        return maxValue