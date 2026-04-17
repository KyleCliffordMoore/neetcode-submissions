class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target_idx = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):            
            if nums[idx] + idx >= target_idx:
                target_idx = idx

        return target_idx == 0