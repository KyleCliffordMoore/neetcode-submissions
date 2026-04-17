class Solution:
    def check(self, nums: List[int]) -> bool:

        smallest = min(nums)

        for offset in range(len(nums)):
            if smallest == nums[offset % len(nums)]:
                break
        
        print(offset)

        for i in range(len(nums) - 1):
            if nums[(i + offset) % len(nums)] > nums[(i + 1 + offset) % len(nums)]:
                return False
        return True