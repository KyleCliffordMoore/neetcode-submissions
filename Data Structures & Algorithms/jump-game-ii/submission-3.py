class Solution:
    def jump(self, nums: List[int]) -> int:

        furthest = nums[0]
        end = 0
        count = 0

        for i, num in enumerate(nums):

            furthest = max(furthest, num + i)

            if i != len(nums) - 1 and i >= end:
                count += 1
                end = furthest


        return count