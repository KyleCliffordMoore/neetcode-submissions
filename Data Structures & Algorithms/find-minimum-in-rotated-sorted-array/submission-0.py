class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            lval = nums[left]
            rval = nums[right]
            mval = nums[mid]

            print(lval, mval, rval)
            if lval > mval:
                right = mid
            elif mval > rval:
                left = mid + 1
            else:
                return lval
            
        return nums[mid]