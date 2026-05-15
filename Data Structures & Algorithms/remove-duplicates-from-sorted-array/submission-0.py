class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 0
        last = -1
        for right in range(len(nums)):
            if nums[right] == last:
                continue
            
            last = nums[right]
            nums[left] = nums[right]
            left += 1
        
        return left