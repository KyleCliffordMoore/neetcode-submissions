class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        currLarge = 1
        currSmall = 1
        longest = 1

        for i in range(len(nums) - 1):
            left = nums[i]
            right = nums[i + 1]

            if left < right:
                currLarge += 1
                currSmall = 1
            elif left > right:
                currLarge = 1
                currSmall += 1
            else:
                currLarge = 1
                currSmall = 1
            
            longest = max(longest, currSmall, currLarge)
        
        return longest