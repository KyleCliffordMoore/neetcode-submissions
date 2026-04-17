class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, n in enumerate(nums):
            ans ^= i ^ n
        ans ^= len(nums)
        return ans