class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        def isEven(num):
            return num % 2 == 0

        def isSpecial(idx):
            if len(nums) <= 1:
                return True

            if idx == 0:
                return isEven(nums[idx]) != isEven(nums[idx + 1])
            if idx == len(nums) - 1:
                return isEven(nums[idx]) != isEven(nums[idx - 1])
            return (
                isEven(nums[idx]) != isEven(nums[idx - 1]) and
                isEven(nums[idx + 1]) == isEven(nums[idx - 1])
            )
        
        for i in range(len(nums)):
            if not isSpecial(i):
                return False
        return True