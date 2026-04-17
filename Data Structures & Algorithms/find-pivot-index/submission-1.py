class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            leftSum += num
            if leftSum == total - leftSum + num:
                return i
        
        return -1