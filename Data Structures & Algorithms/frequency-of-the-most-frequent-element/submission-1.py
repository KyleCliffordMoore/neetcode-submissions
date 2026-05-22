class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        maxLen = 1
        left = 0
        currPoints = k
        for right in range(1, len(nums)):
            currPoints -= (nums[right] - nums[right - 1]) * (right - left)

            while currPoints < 0:
                currPoints += nums[right] - nums[left]
                left += 1

            maxLen = max(maxLen, right - left + 1)
        
        return maxLen