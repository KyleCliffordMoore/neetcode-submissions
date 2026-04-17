class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target_idx = len(nums) - 1

        for i in range(len(nums)):
            rev_i = len(nums) - 1 - i
            
            if nums[rev_i] + rev_i >= target_idx:
                target_idx = rev_i

        return target_idx == 0