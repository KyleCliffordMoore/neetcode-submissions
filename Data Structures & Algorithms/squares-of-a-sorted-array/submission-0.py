class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        ans = [0] * len(nums)
        idx = len(nums) - 1

        while left <= right:

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                ans[idx] = left_square
                left += 1
            else:
                ans[idx] = right_square
                right -= 1
            
            idx -= 1
        
        return ans