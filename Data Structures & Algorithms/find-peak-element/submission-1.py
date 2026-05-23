class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        get = lambda idx: nums[idx] if 0 <= idx < len(nums) else -float('inf')

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = left + (right - left + 1) // 2

            l, m, r = get(mid - 1), get(mid), get(mid + 1)

            if l > m:
                right = mid - 1
            elif r > m:
                left = mid
            else:
                return mid
        
        return left