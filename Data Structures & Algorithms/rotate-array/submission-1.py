class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def myRev(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums.reverse()
        k %= len(nums)
        myRev(0, k - 1)
        myRev(k, len(nums) - 1)


